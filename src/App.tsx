
import React, { useState, useEffect } from 'react';
import { Phone, Zap, Shield, Bomb, Activity, Terminal } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';

const API_BASE = '/api';

function App() {
  const [phone, setPhone] = useState('');
  const [count, setCount] = useState(50);
  const [bombId, setBombId] = useState<string | null>(null);
  const [status, setStatus] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let interval: any;
    if (bombId && status?.status !== 'completed') {
      interval = setInterval(async () => {
        try {
          const res = await axios.get(`${API_BASE}/status/${bombId}`);
          setStatus(res.data);
          if (res.data.status === 'completed') {
            clearInterval(interval);
            setLoading(false);
          }
        } catch (err) {
          console.error("Poll error", err);
        }
      }, 2000);
    }
    return () => clearInterval(interval);
  }, [bombId, status]);

  const handleBomb = async () => {
    if (!phone || phone.length < 10) return;
    setLoading(true);
    setBombId(null);
    setStatus(null);
    
    try {
      const res = await axios.post(`${API_BASE}/bomb`, {
        phone: phone,
        count: count
      });
      setBombId(res.data.bomb_id);
    } catch (err) {
      alert("Failed to connect to backend. Make sure it's running.");
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-xl glass-card"
      >
        <div className="text-center mb-8">
          <motion.div
            animate={{ rotate: [0, 10, -10, 0] }}
            transition={{ repeat: Infinity, duration: 4, ease: "easeInOut" }}
            className="inline-block p-4 rounded-2xl bg-cyan-500/10 mb-4"
          >
            <Bomb className="w-12 h-12 text-cyan-400" />
          </motion.div>
          <h1 className="text-4xl neon-text mb-2">SrV Bomber</h1>
          <p className="text-white/40 text-sm">Automated OTP verification stress testing tool</p>
        </div>

        <div className="space-y-6">
          <div>
            <label className="label">Target Phone Number</label>
            <div className="relative">
              <Phone className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-white/20" />
              <input 
                type="tel"
                placeholder="Enter 10-digit number"
                className="input-field pl-12"
                value={phone}
                onChange={(e) => setPhone(e.target.value.replace(/\D/g, '').slice(0, 10))}
              />
            </div>
          </div>

          <div>
            <label className="label">Batch Count: {count}</label>
            <input 
              type="range"
              min="10"
              max="200"
              step="10"
              className="w-full h-2 bg-white/10 rounded-lg appearance-none cursor-pointer accent-cyan-400"
              value={count}
              onChange={(e) => setCount(Number(e.target.value))}
            />
          </div>

          <button 
            onClick={handleBomb}
            disabled={loading || !phone || phone.length < 10}
            className="btn neon-button w-full"
          >
            {loading ? (
              <Activity className="w-5 h-5 animate-spin" />
            ) : (
              <Zap className="w-5 h-5 fill-current" />
            )}
            {loading ? 'INITIATING...' : 'START BOMBING'}
          </button>
        </div>

        <AnimatePresence>
          {status && (
            <motion.div 
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="mt-8 border-t border-white/10 pt-8"
            >
              <div className="flex justify-between items-center mb-4">
                <div className="flex items-center gap-2">
                  <Activity className="w-4 h-4 text-cyan-400" />
                  <span className="text-sm font-medium">Operation Status</span>
                </div>
                <span className={`status-badge ${status.status === 'running' ? 'status-running' : 'status-completed'}`}>
                  {status.status}
                </span>
              </div>

              <div className="flex justify-between text-xs text-white/40 mb-1">
                <span>Progress: {status.sent} / {status.total}</span>
                <span>{Math.round((status.sent / status.total) * 100)}%</span>
              </div>
              <div className="progress-container">
                <div 
                  className="progress-bar" 
                  style={{ width: `${(status.sent / status.total) * 100}%` }}
                />
              </div>

              {status.logs && status.logs.length > 0 && (
                <div className="log-container">
                  <div className="flex items-center gap-2 mb-2 text-cyan-400/50">
                    <Terminal className="w-3 h-3" />
                    <span className="text-[10px] uppercase tracking-wider font-bold">Live Proxy Logs</span>
                  </div>
                  {status.logs.slice(-5).reverse().map((log: string, i: number) => (
                    <div key={i} className="log-entry">
                      <span className="text-cyan-500/30 mr-2">{'>'}</span>
                      {log}
                    </div>
                  ))}
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        <div className="mt-8 grid grid-cols-3 gap-4">
          <div className="text-center p-3 rounded-xl bg-white/5 border border-white/5">
            <Shield className="w-4 h-4 mx-auto mb-2 text-cyan-400/50" />
            <div className="text-[10px] text-white/30 uppercase font-bold">Anonymized</div>
          </div>
          <div className="text-center p-3 rounded-xl bg-white/5 border border-white/5">
            <Zap className="w-4 h-4 mx-auto mb-2 text-cyan-100/50" />
            <div className="text-[10px] text-white/30 uppercase font-bold">Fast Lane</div>
          </div>
          <div className="text-center p-3 rounded-xl bg-white/5 border border-white/5">
            <Bomb className="w-4 h-4 mx-auto mb-2 text-purple-400/50" />
            <div className="text-[10px] text-white/30 uppercase font-bold">Multi-Source</div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default App;

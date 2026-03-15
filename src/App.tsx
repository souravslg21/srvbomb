
import React, { useState } from 'react';
import { Phone, Zap, Shield, Bomb, Activity, Terminal, BookOpen } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';

const API_BASE = '/api';

function App() {
  const [phone, setPhone] = useState('');
  const [count, setCount] = useState(50);
  const [status, setStatus] = useState<any>({
    status: 'idle',
    sent: 0,
    total: 0,
    logs: []
  });
  const [loading, setLoading] = useState(false);
  const [isStopping, setIsStopping] = useState(false);
  const [mode, setMode] = useState<'sms' | 'call'>('sms');
  const stopRef = React.useRef(false);

  const importFromPhonebook = async () => {
    try {
      // @ts-ignore
      if (!('contacts' in navigator && 'select' in navigator.contacts)) {
        alert("Phonebook access works best on Android Chrome via HTTPS.");
        return;
      }
      // @ts-ignore
      const picked = await navigator.contacts.select(['name', 'tel'], { multiple: false });
      if (picked.length > 0 && picked[0].tel?.length > 0) {
        const tenDigit = picked[0].tel[0].replace(/\D/g, '').slice(-10);
        if (tenDigit.length === 10) setPhone(tenDigit);
        else alert("Could not find a valid 10-digit number.");
      }
    } catch (err) {
      console.warn("Phonebook access failed:", err);
    }
  };

  const handleBomb = async () => {
    if (!phone || phone.length < 10) return;
    setLoading(true);
    setIsStopping(false);
    stopRef.current = false;
    setStatus({ status: 'running', sent: 0, total: count, logs: [`Initialising ${mode.toUpperCase()} system...`] });
    let currentSent = 0;
    for (let i = 0; i < count; i++) {
      if (stopRef.current) {
        setStatus((prev: any) => ({ ...prev, status: 'stopped', logs: [...prev.logs, 'Stopped by user.'] }));
        setLoading(false);
        return;
      }
      try {
        const res = await axios.post(`${API_BASE}/bomb/single`, { phone, mode, count: 1 });
        currentSent++;
        setStatus((prev: any) => ({ ...prev, sent: currentSent, logs: [...prev.logs, res.data.log].slice(-20) }));
      } catch {
        setStatus((prev: any) => ({ ...prev, logs: [...prev.logs, 'Network error.'].slice(-20) }));
      }
      if (i < count - 1) await new Promise(r => setTimeout(r, mode === 'call' ? 1500 : 800));
    }
    setStatus((prev: any) => ({ ...prev, status: 'completed' }));
    setLoading(false);
  };

  const handleStop = () => { setIsStopping(true); stopRef.current = true; };
  const progress = status.total > 0 ? Math.round((status.sent / status.total) * 100) : 0;

  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '1.5rem' }}>
      <motion.div
        className="card"
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: 'easeOut' }}
      >
        {/* ── HEADER ── */}
        <div className="header">
          <motion.div
            className="logo-wrap"
            animate={{ rotate: [0, 8, -8, 0] }}
            transition={{ repeat: Infinity, duration: 4, ease: 'easeInOut' }}
          >
            <Bomb className="logo-icon" />
          </motion.div>
          <h1 className="title">SrV Bomber</h1>
          <p className="subtitle">Automated verification stress testing tool</p>
        </div>

        {/* ── MODE TOGGLE ── */}
        <div className="mode-toggle">
          <button
            className={`mode-btn ${mode === 'sms' ? 'sms-active' : ''}`}
            onClick={() => setMode('sms')}
            disabled={loading}
          >
            <Zap width={15} height={15} />
            SMS MODE
          </button>
          <button
            className={`mode-btn ${mode === 'call' ? 'call-active' : ''}`}
            onClick={() => setMode('call')}
            disabled={loading}
          >
            <Activity width={15} height={15} />
            CALL MODE
          </button>
        </div>

        {/* ── FORM ── */}
        <div className="form-section">

          {/* Phone input */}
          <div>
            <label className="field-label">Target Number</label>
            <div className="phone-row">
              <div className="phone-input-wrap">
                <Phone className="phone-icon" />
                <input
                  type="tel"
                  className="phone-input"
                  placeholder="Enter 10-digit number"
                  value={phone}
                  onChange={e => setPhone(e.target.value.replace(/\D/g, '').slice(0, 10))}
                />
              </div>
              <button className="phonebook-btn" onClick={importFromPhonebook} title="Pick from Phonebook">
                <BookOpen />
              </button>
            </div>
          </div>

          {/* Batch slider */}
          <div>
            <div className="count-label-row">
              <label className="field-label" style={{ margin: 0 }}>Batch Count</label>
              <span className="count-value">{count}</span>
            </div>
            <input
              type="range" min="10" max="200" step="10"
              className="slider"
              value={count}
              onChange={e => setCount(Number(e.target.value))}
            />
          </div>

          {/* Action button */}
          <div>
            {!loading ? (
              <button
                className="bomb-btn"
                onClick={handleBomb}
                disabled={!phone || phone.length < 10}
              >
                <Zap width={18} height={18} />
                START BOMBING
              </button>
            ) : (
              <button
                className="stop-btn"
                onClick={handleStop}
                disabled={isStopping}
              >
                <Shield width={18} height={18} />
                {isStopping ? 'STOPPING...' : 'STOP BOMBING'}
              </button>
            )}
          </div>
        </div>

        {/* ── STATUS PANEL ── */}
        <AnimatePresence>
          {status.status !== 'idle' && (
            <motion.div
              className="status-panel"
              initial={{ opacity: 0, height: 0, marginTop: 0 }}
              animate={{ opacity: 1, height: 'auto', marginTop: '1.75rem' }}
              exit={{ opacity: 0, height: 0, marginTop: 0 }}
              transition={{ duration: 0.3 }}
            >
              <div className="status-header">
                <div className="status-title">
                  <Activity />
                  Operation Status
                </div>
                <span className={`badge ${
                  status.status === 'running' ? 'badge-running' :
                  status.status === 'completed' ? 'badge-completed' : 'badge-stopped'
                }`}>
                  {status.status}
                </span>
              </div>

              <div className="progress-meta">
                <span>Sent: {status.sent} / {status.total}</span>
                <span>{progress}%</span>
              </div>
              <div className="progress-track">
                <div className="progress-fill" style={{ width: `${progress}%` }} />
              </div>

              {status.logs?.length > 0 && (
                <div className="log-box">
                  <div className="log-header">
                    <Terminal /> Live Proxy Logs
                  </div>
                  {[...status.logs].reverse().slice(0, 8).map((log: string, i: number) => (
                    <div key={i} className="log-entry">{log}</div>
                  ))}
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        {/* ── FOOTER CHIPS ── */}
        <div className="chip-row">
          <div className="chip">
            <Shield />
            <span className="chip-label">Anonymized</span>
          </div>
          <div className="chip">
            <Zap />
            <span className="chip-label">Fast Lane</span>
          </div>
          <div className="chip">
            <Bomb />
            <span className="chip-label">Multi-Source</span>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default App;

import { useState, useCallback } from 'react';
import type { GenerateRequest } from '../types';
import { startGeneration, resetAll } from '../api';
import './ConfigPanel.css';

interface ConfigPanelProps {
  isRunning: boolean;
  onStart: () => void;
  onReset: () => void;
}

export default function ConfigPanel({ isRunning, onStart, onReset }: ConfigPanelProps) {
  const [prompt, setPrompt] = useState('');
  const [memoryFacts, setMemoryFacts] = useState('');
  const [datasetSize, setDatasetSize] = useState(100);
  const [customSize, setCustomSize] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handlePreset = useCallback((size: number) => {
    setDatasetSize(size);
    setCustomSize('');
  }, []);

  const handleCustomSize = useCallback((value: string) => {
    setCustomSize(value);
    const num = parseInt(value, 10);
    if (!isNaN(num) && num > 0) {
      setDatasetSize(num);
    }
  }, []);

  const handleSubmit = useCallback(async () => {
    setError(null);
    const facts = memoryFacts
      .split('\n')
      .map(f => f.trim())
      .filter(f => f.length > 0);

    const req: GenerateRequest = {
      prompt: prompt.trim(),
      memory_facts: facts,
      dataset_size: datasetSize,
    };

    if (!req.prompt) {
      setError('Please describe your persona or task.');
      return;
    }

    try {
      await startGeneration(req);
      onStart();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to start generation');
    }
  }, [prompt, memoryFacts, datasetSize, onStart]);

  const handleReset = useCallback(async () => {
    setError(null);
    try {
      await resetAll();
      setPrompt('');
      setMemoryFacts('');
      setDatasetSize(100);
      setCustomSize('');
      onReset();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to reset');
    }
  }, [onReset]);

  const presets = [
    { label: '100', value: 100 },
    { label: '1K', value: 1000 },
    { label: '10K', value: 10000 },
    { label: '100K', value: 100000 },
  ];

  return (
    <div className="config-panel">
      <h2 className="config-title">Configuration</h2>

      <div className="config-field">
        <label htmlFor="prompt-input">Describe your persona or task</label>
        <textarea
          id="prompt-input"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          placeholder="e.g. A friendly customer support agent for a SaaS company that helps users troubleshoot billing issues, reset passwords, and navigate product features..."
          rows={5}
          disabled={isRunning}
        />
      </div>

      <div className="config-field">
        <label htmlFor="memory-input">Memory facts (one per line)</label>
        <textarea
          id="memory-input"
          value={memoryFacts}
          onChange={e => setMemoryFacts(e.target.value)}
          placeholder={"Company name is Acme Corp\nSupport hours are 9am-5pm EST\nRefund policy is 30 days"}
          rows={3}
          disabled={isRunning}
        />
      </div>

      <div className="config-field">
        <label>Dataset size</label>
        <div className="size-controls">
          <div className="preset-buttons">
            {presets.map(p => (
              <button
                key={p.value}
                className={`preset-btn ${datasetSize === p.value && !customSize ? 'active' : ''}`}
                onClick={() => handlePreset(p.value)}
                disabled={isRunning}
              >
                {p.label}
              </button>
            ))}
          </div>
          <input
            type="number"
            className="custom-size-input"
            placeholder="Custom..."
            value={customSize}
            onChange={e => handleCustomSize(e.target.value)}
            min={1}
            disabled={isRunning}
          />
        </div>
        <span className="size-label">Target: {datasetSize.toLocaleString()} samples</span>
      </div>

      {error && <div className="config-error">{error}</div>}

      <div className="config-actions">
        <button
          className="btn-generate"
          onClick={handleSubmit}
          disabled={isRunning}
        >
          🚀 Generate Dataset
        </button>
        <button
          className="btn-reset"
          onClick={handleReset}
          disabled={isRunning}
        >
          🔄 Reset
        </button>
      </div>
    </div>
  );
}

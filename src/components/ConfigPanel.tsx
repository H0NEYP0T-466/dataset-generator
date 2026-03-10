import { useState, useCallback } from 'react';
import type { GenerateRequest } from '../types';
import { startGeneration, resetAll } from '../api';
import './ConfigPanel.css';

interface ConfigPanelProps {
  isRunning: boolean;
  onStart: () => void;
  onReset: () => void;
}

const THRESHOLD_PRESETS = [
  { label: '0.7', value: 0.7 },
  { label: '0.8', value: 0.8 },
  { label: '0.9', value: 0.9 },
];

export default function ConfigPanel({ isRunning, onStart, onReset }: ConfigPanelProps) {
  const [prompt, setPrompt] = useState('');
  const [memoryFacts, setMemoryFacts] = useState('');
  const [datasetSize, setDatasetSize] = useState(100);
  const [customSize, setCustomSize] = useState('');
  const [skipDedup, setSkipDedup] = useState(false);
  const [dedupThreshold, setDedupThreshold] = useState(0.85);
  const [customThreshold, setCustomThreshold] = useState('');
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

  const handleThresholdPreset = useCallback((value: number) => {
    setDedupThreshold(value);
    setCustomThreshold('');
  }, []);

  const handleCustomThreshold = useCallback((value: string) => {
    setCustomThreshold(value);
    const num = parseFloat(value);
    if (!isNaN(num) && num >= 0 && num <= 1) {
      setDedupThreshold(num);
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
      skip_dedup: skipDedup,
      dedup_threshold: dedupThreshold,
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
  }, [prompt, memoryFacts, datasetSize, skipDedup, dedupThreshold, onStart]);

  const handleReset = useCallback(async () => {
    setError(null);
    try {
      await resetAll();
      setPrompt('');
      setMemoryFacts('');
      setDatasetSize(100);
      setCustomSize('');
      setSkipDedup(false);
      setDedupThreshold(0.85);
      setCustomThreshold('');
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

  const isThresholdPresetActive = (value: number) =>
    dedupThreshold === value && !customThreshold;

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
          placeholder="Company name is Acme Corp&#10;Support hours are 9am-5pm EST&#10;Refund policy is 30 days"
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

      <div className="config-field">
        <div className="dedup-toggle-row">
          <label htmlFor="skip-dedup-toggle" className="dedup-toggle-label">
            Skip deduplication check
          </label>
          <button
            id="skip-dedup-toggle"
            role="switch"
            aria-checked={skipDedup}
            className={`toggle-btn ${skipDedup ? 'active' : ''}`}
            onClick={() => setSkipDedup(v => !v)}
            disabled={isRunning}
          >
            <span className="toggle-thumb" />
          </button>
        </div>
        {skipDedup && (
          <span className="dedup-hint">All generated samples will be saved without similarity filtering.</span>
        )}
      </div>

      {!skipDedup && (
        <div className="config-field">
          <label>Similarity threshold</label>
          <div className="size-controls">
            <div className="preset-buttons">
              {THRESHOLD_PRESETS.map(p => (
                <button
                  key={p.value}
                  className={`preset-btn ${isThresholdPresetActive(p.value) ? 'active' : ''}`}
                  onClick={() => handleThresholdPreset(p.value)}
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
              value={customThreshold}
              onChange={e => handleCustomThreshold(e.target.value)}
              min={0}
              max={1}
              step={0.01}
              disabled={isRunning}
            />
          </div>
          <span className="size-label">
            Threshold: {dedupThreshold} — samples with similarity ≥ {dedupThreshold} are considered duplicates
          </span>
        </div>
      )}

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

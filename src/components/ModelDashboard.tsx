import { useState, useEffect, useCallback } from 'react';
import type { ModelStatus } from '../types';
import { getModelStatus } from '../api';
import './ModelDashboard.css';

interface ModelDashboardProps {
  isRunning: boolean;
}

export default function ModelDashboard({ isRunning }: ModelDashboardProps) {
  const [models, setModels] = useState<ModelStatus[]>([]);
  const [collapsed, setCollapsed] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchModels = useCallback(async () => {
    try {
      const data = await getModelStatus();
      setModels(data);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch models');
    }
  }, []);

  useEffect(() => {
    fetchModels();
  }, [fetchModels]);

  useEffect(() => {
    if (!isRunning) return;
    const interval = setInterval(fetchModels, 10000);
    return () => clearInterval(interval);
  }, [isRunning, fetchModels]);

  const getStatusBadge = (model: ModelStatus) => {
    if (!model.available || model.blacklisted) {
      return <span className="status-badge exhausted">🔴 Exhausted</span>;
    }
    const usageRatio = model.daily_limit > 0 ? model.requests_used / model.daily_limit : 0;
    if (usageRatio >= 0.8) {
      return <span className="status-badge near-limit">🟡 Near Limit</span>;
    }
    return <span className="status-badge available">🟢 Available</span>;
  };

  return (
    <div className="model-dashboard">
      <button
        className="dashboard-toggle"
        onClick={() => setCollapsed(!collapsed)}
      >
        <span className="toggle-icon">{collapsed ? '▶' : '▼'}</span>
        <h2 className="dashboard-title">Model Dashboard</h2>
        <span className="model-count">{models.length} models</span>
      </button>

      {!collapsed && (
        <div className="dashboard-content">
          {error && <div className="dashboard-error">{error}</div>}
          {models.length === 0 && !error ? (
            <div className="dashboard-empty">No models available. Is the backend running?</div>
          ) : (
            <div className="table-wrapper">
              <table className="model-table">
                <thead>
                  <tr>
                    <th>Model Name</th>
                    <th>Provider</th>
                    <th>Daily Limit</th>
                    <th>Used</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {models.map(model => (
                    <tr key={`${model.provider}-${model.model}`}>
                      <td className="model-name">{model.model}</td>
                      <td>{model.provider}</td>
                      <td>{model.daily_limit.toLocaleString()}</td>
                      <td>{model.requests_used.toLocaleString()}</td>
                      <td>{getStatusBadge(model)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

import { useEffect, useRef } from 'react';
import type { PipelineState } from '../types';
import './PipelineProgress.css';

interface PipelineProgressProps {
  state: PipelineState;
}

const STAGE_LABELS = [
  'Prompt Expansion',
  'Manager Review',
  'Scenario Generation',
  'Dataset Generation',
  'Deduplication',
  'Assembly',
];

function getStatusIcon(status: string) {
  switch (status) {
    case 'running': return <span className="status-icon spinning">🔄</span>;
    case 'complete': return <span className="status-icon">✅</span>;
    case 'error': return <span className="status-icon">❌</span>;
    default: return <span className="status-icon">⏳</span>;
  }
}

export default function PipelineProgress({ state }: PipelineProgressProps) {
  const logEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [state.logs]);

  const stages = STAGE_LABELS.map((label, i) => {
    const stageInfo = state.stages.find(s => s.stage === i + 1);
    return {
      stage: i + 1,
      label,
      status: stageInfo?.status ?? 'pending',
    };
  });

  const totalCompleted = Array.from(state.progress.values()).reduce(
    (sum, p) => sum + p.completed, 0
  );
  const totalTarget = state.totalSamples || Array.from(state.progress.values()).reduce(
    (sum, p) => sum + p.target, 0
  );
  const progressPct = totalTarget > 0 ? Math.min((totalCompleted / totalTarget) * 100, 100) : 0;

  return (
    <div className="pipeline-progress">
      <h2 className="pipeline-title">Pipeline Progress</h2>

      <div className="stages-flow">
        {stages.map(s => (
          <div key={s.stage} className={`stage-card stage-${s.status}`}>
            <div className="stage-icon">{getStatusIcon(s.status)}</div>
            <div className="stage-number">Stage {s.stage}</div>
            <div className="stage-label">{s.label}</div>
          </div>
        ))}
      </div>

      {totalTarget > 0 && (
        <div className="progress-section">
          <div className="progress-header">
            <span>Overall Progress</span>
            <span>{totalCompleted.toLocaleString()} / {totalTarget.toLocaleString()} samples</span>
          </div>
          <div className="progress-bar-track">
            <div
              className="progress-bar-fill"
              style={{ width: `${progressPct}%` }}
            />
          </div>
          <div className="progress-pct">{progressPct.toFixed(1)}%</div>
        </div>
      )}

      {state.modelSwitches.length > 0 && (
        <div className="model-switches">
          <h3>Model Switches</h3>
          {state.modelSwitches.map((msg, i) => (
            <div key={i} className="switch-notification">⚡ {msg}</div>
          ))}
        </div>
      )}

      <div className="log-section">
        <h3>Live Logs</h3>
        <div className="log-container">
          {state.logs.length === 0 ? (
            <div className="log-empty">Waiting for logs...</div>
          ) : (
            state.logs.map((line, i) => (
              <div key={i} className="log-line">{line}</div>
            ))
          )}
          <div ref={logEndRef} />
        </div>
      </div>

      {state.error && (
        <div className="pipeline-error">
          ❌ {state.error}
        </div>
      )}
    </div>
  );
}

import { getDownloadUrl } from '../api';
import './DownloadSection.css';

interface DownloadSectionProps {
  totalSamples: number;
  elapsedTime: number;
  scenariosCount: number;
}

export default function DownloadSection({ totalSamples, elapsedTime, scenariosCount }: DownloadSectionProps) {
  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    if (m === 0) return `${s}s`;
    return `${m}m ${s}s`;
  };

  return (
    <div className="download-section">
      <h2 className="download-title">✨ Generation Complete</h2>

      <div className="download-meta">
        <div className="meta-item">
          <span className="meta-value">{totalSamples.toLocaleString()}</span>
          <span className="meta-label">Total Samples</span>
        </div>
        <div className="meta-item">
          <span className="meta-value">{formatTime(elapsedTime)}</span>
          <span className="meta-label">Elapsed Time</span>
        </div>
        <div className="meta-item">
          <span className="meta-value">{scenariosCount}</span>
          <span className="meta-label">Scenarios</span>
        </div>
      </div>

      <a
        href={getDownloadUrl()}
        className="btn-download"
        download
      >
        📥 Download dataset.jsonl
      </a>
    </div>
  );
}

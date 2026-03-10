import { useState, useCallback, useRef, useEffect } from 'react';
import type { PipelineState, StageInfo, ProgressInfo } from './types';
import { createSSEConnection } from './api';
import ConfigPanel from './components/ConfigPanel';
import ModelDashboard from './components/ModelDashboard';
import PipelineProgress from './components/PipelineProgress';
import DownloadSection from './components/DownloadSection';
import './App.css';

const initialPipelineState: PipelineState = {
  stages: [],
  progress: new Map(),
  logs: [],
  modelSwitches: [],
  totalSamples: 0,
  isComplete: false,
  error: null,
};

function App() {
  const [isRunning, setIsRunning] = useState(false);
  const [showPipeline, setShowPipeline] = useState(false);
  const [pipelineState, setPipelineState] = useState<PipelineState>(initialPipelineState);
  const [elapsedTime, setElapsedTime] = useState(0);
  const [scenariosCount, setScenariosCount] = useState(0);
  const sseRef = useRef<EventSource | null>(null);
  const startTimeRef = useRef<number>(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const cleanupSSE = useCallback(() => {
    if (sseRef.current) {
      sseRef.current.close();
      sseRef.current = null;
    }
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  }, []);

  useEffect(() => {
    return cleanupSSE;
  }, [cleanupSSE]);

  const connectSSE = useCallback(() => {
    cleanupSSE();

    const es = createSSEConnection();
    sseRef.current = es;

    es.addEventListener('stage_update', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as StageInfo;
        setPipelineState(prev => {
          const stages = [...prev.stages];
          const idx = stages.findIndex(s => s.stage === data.stage);
          if (idx >= 0) {
            stages[idx] = data;
          } else {
            stages.push(data);
          }
          return { ...prev, stages };
        });
      } catch { /* ignore parse errors */ }
    });

    es.addEventListener('progress', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as ProgressInfo;
        setPipelineState(prev => {
          const progress = new Map(prev.progress);
          progress.set(data.scenario_index, data);
          return { ...prev, progress };
        });
      } catch { /* ignore parse errors */ }
    });

    es.addEventListener('log', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as { stage: number; cycle: number; approved: boolean; confidence: number; feedback: string };
        const msg = `[Stage ${data.stage}] Cycle ${data.cycle}: ${data.approved ? '✅ Approved' : '⏳ Revising'} (confidence: ${data.confidence}) — ${data.feedback}`;
        setPipelineState(prev => ({
          ...prev,
          logs: [...prev.logs, msg],
        }));
      } catch {
        setPipelineState(prev => ({
          ...prev,
          logs: [...prev.logs, e.data],
        }));
      }
    });

    es.addEventListener('model_switch', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as { from: string; reason: string };
        const msg = `Switched from ${data.from}: ${data.reason}`;
        setPipelineState(prev => ({
          ...prev,
          modelSwitches: [...prev.modelSwitches, msg],
        }));
      } catch {
        setPipelineState(prev => ({
          ...prev,
          modelSwitches: [...prev.modelSwitches, e.data],
        }));
      }
    });

    es.addEventListener('complete', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as { total_samples: number; scenarios?: number; elapsed_seconds?: number };
        setPipelineState(prev => ({
          ...prev,
          totalSamples: data.total_samples,
          isComplete: true,
        }));
        setScenariosCount(data.scenarios ?? 0);
        if (data.elapsed_seconds !== undefined) {
          setElapsedTime(Math.round(data.elapsed_seconds));
        }
      } catch {
        setPipelineState(prev => ({
          ...prev,
          isComplete: true,
        }));
      }
      setIsRunning(false);
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
      es.close();
      sseRef.current = null;
    });

    es.addEventListener('error', (e: MessageEvent) => {
      try {
        const data = JSON.parse(e.data) as { message: string };
        setPipelineState(prev => ({
          ...prev,
          error: data.message,
        }));
      } catch {
        setPipelineState(prev => ({
          ...prev,
          error: e.data,
        }));
      }
      setIsRunning(false);
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
      es.close();
      sseRef.current = null;
    });

    es.onerror = () => {
      // EventSource will auto-reconnect; we don't treat this as fatal
    };
  }, [cleanupSSE]);

  const handleStart = useCallback(() => {
    setPipelineState(initialPipelineState);
    setElapsedTime(0);
    setScenariosCount(0);
    setIsRunning(true);
    setShowPipeline(true);
    startTimeRef.current = Date.now();

    timerRef.current = setInterval(() => {
      setElapsedTime(Math.floor((Date.now() - startTimeRef.current) / 1000));
    }, 1000);

    connectSSE();
  }, [connectSSE]);

  const handleReset = useCallback(() => {
    cleanupSSE();
    setIsRunning(false);
    setShowPipeline(false);
    setPipelineState(initialPipelineState);
    setElapsedTime(0);
    setScenariosCount(0);
  }, [cleanupSSE]);

  return (
    <div className="app">
      <header className="app-header">
        <h1 className="app-title">⚡ DataForge</h1>
        <p className="app-subtitle">LLM Fine-Tuning Dataset Generator</p>
      </header>

      <ConfigPanel
        isRunning={isRunning}
        onStart={handleStart}
        onReset={handleReset}
      />

      <ModelDashboard isRunning={isRunning} />

      {showPipeline && (
        <PipelineProgress state={pipelineState} />
      )}

      {pipelineState.isComplete && (
        <DownloadSection
          totalSamples={pipelineState.totalSamples}
          elapsedTime={elapsedTime}
          scenariosCount={scenariosCount}
        />
      )}
    </div>
  );
}

export default App;

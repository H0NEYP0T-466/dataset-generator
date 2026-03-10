export interface GenerateRequest {
  prompt: string;
  memory_facts: string[];
  dataset_size: number;
}

export interface ModelStatus {
  model: string;
  provider: string;
  available: boolean;
  requests_used: number;
  tokens_used: number;
  daily_limit: number;
  monthly_limit: number;
  blacklisted: boolean;
}

export interface StageInfo {
  stage: number;
  status: 'pending' | 'running' | 'complete' | 'error';
  label: string;
}

export interface ProgressInfo {
  stage: number;
  scenario_index: number;
  scenario: string;
  target: number;
  completed: number;
}

export interface PipelineState {
  stages: StageInfo[];
  progress: Map<number, ProgressInfo>;
  logs: string[];
  modelSwitches: string[];
  totalSamples: number;
  isComplete: boolean;
  error: string | null;
}

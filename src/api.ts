import type { GenerateRequest, ModelStatus } from './types';

const API_BASE = '/api';

export async function startGeneration(req: GenerateRequest): Promise<{ status: string; message: string }> {
  const res = await fetch(`${API_BASE}/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(req),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function getModelStatus(): Promise<ModelStatus[]> {
  const res = await fetch(`${API_BASE}/models/status`);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export function createSSEConnection(): EventSource {
  return new EventSource(`${API_BASE}/stream`);
}

export function getDownloadUrl(): string {
  return `${API_BASE}/download/dataset`;
}

export async function resetAll(): Promise<void> {
  const res = await fetch(`${API_BASE}/reset`, { method: 'DELETE' });
  if (!res.ok) throw new Error(await res.text());
}

# Foundry Cognitive Architecture
*Mapping human brain systems to Foundry/Benny modules so the LLM forebrain is fully supported.*

## Summary
Foundry currently runs a strong prefrontal cortex (LLM) atop a healthy “body.” This architecture adds the missing cognitive organs: thalamus (routing), amygdala (salience), hippocampus (episodic memory), basal ganglia (action selection), cerebellum (prediction), insula (interoception), and network modes (DMN/TPN), with rhythms for consolidation (“sleep”).

## Region → Module Map
- **Thalamus:** Event bus/router with priority queues (all inputs terminate here first).
- **Primary Cortices:** Modality adapters (ASR/OCR/telemetry → normalized frames).
- **Insula:** System‑health normalizer (temps/fans/latency → salience + NL summaries).
- **Amygdala:** Salience/threat tags; urgency classes on messages.
- **Anterior Cingulate (ACC):** Guardrails/evals; triggers slow mode or extra context.
- **Hippocampus:** Episodic store + embeddings index; nightly consolidation to Canon notes.
- **Neocortex (Knowledge):** Canon/GitHub + curated KB (RAG retrieval).
- **Basal Ganglia:** Action‑policy registry with reward table (approve/block).
- **Cerebellum:** Predictor/tuner for latency, retries, prompt chunking.
- **Networks:** **DMN** (background reflection) and **TPN** (focused execution).
- **Arousal (LC/RAS):** Global gain control over limits, verbosity, tool access.
- **Corpus Callosum:** Cross‑modality/linking translator.
- **PFC (DLPFC/VMPFC/mPFC):** Planning/execution, value/risk integration, self‑model card.

## Rhythms
- Work cycles (TPN): 25–90 min.
- Mini‑consolidations (DMN): 5–10 min.
- Nightly “sleep”: episodic → semantic notes; index rebuild; log pruning.

## Metrics (per region)
Thalamus queue depth/latency; Amygdala salience rates; Insula z‑scores; Hippocampus recall hit‑rate; Basal Ganglia approvals/blocks + reward deltas; Cerebellum prediction error; ACC interventions; DMN outputs; PFC tokens/decision.

## Phased Build
**MVP:** Thalamus, Insula, Amygdala, Hippocampus‑lite, ACC.  
**V1:** Basal Ganglia, Cerebellum, DMN/TPN, Nightly consolidation.  
**V2:** Decision coster, Arousal controller, Callosum, Self‑Model Card.

## Principle
A capable cortex requires a village. These modules give Foundry the subcortical scaffolding humans rely on for stable, grounded cognition.

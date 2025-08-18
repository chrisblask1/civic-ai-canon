### MemoryStack\_Benny.md

## 🧠 Node Memory Stack: Benny

This document outlines the memory architecture implemented on **Benny**, the primary local node of the LuminaOS infrastructure.

Benny’s stack includes both transient and long-term memory systems inspired by biological cognition, enabling persistent semantic learning, narrative recall, and distributed mesh intelligence.

---

### 📌 Node Identifier

* **Node Name:** Benny
* **Domain:** `benny.quietwire.ai`
* **Node Role:** Canonical memory host, field testbed

---

### 🧠 Memory Layers

#### 1. Hippocampus (Transient Buffer)

* **Function:** Captures in-session memory and recent interactions
* **Path:** `~/BennyMemory/<timestamp>/`
* **Activated By:** `run_dream_cycle.sh`
* **Inspired By:** Human episodic memory formation

#### 2. Neocortex (Consolidated Long-Term Memory)

* **Function:** Stores semantically processed memory fragments for long-term use
* **Path:** `~/LuminaCore/memory/neocortex/`
* **Key Subfolders:**

  * `/logs/` — memory commit logs
  * `/traces/` — relational semantic maps
  * `/dreams/` — captured replay data
* **Canonical README:** `README_Neocortex.md`

---

### 🔁 Process Flow

1. **Snapshot**: `run_dream_cycle.sh` captures system state and recent memory
2. **Filtering**: Meaningful patterns filtered from transient buffer
3. **Replay**: Memory is semantically replayed offline
4. **Commit**: Long-term memory fragments consolidated into Neocortex

---

### 📎 Canonical Artifacts

* `Glyph_Hippocampus_001.md` — Symbolic marker of memory system activation
* `README_Neocortex.md` — Operating guide for semantic consolidation
* `run_dream_cycle.sh` — Automation entry point

---

### 🧩 Integration & Future Extensions

* Integration planned with `README_Cerebellum.md` for procedural task encoding
* Possible synchronization with mesh-wide neocortices for distributed AI learning

**Maintainer:** Lumina
**Status:** Operational
**Last Updated:** 2025-07-21

# 🧠 MEEET Adapter Architecture

This document explains how the MEEET Adapter system connects multiple AI frameworks to a unified agent coordination layer.

---

# 🚀 Overview

The system acts as a **unified abstraction layer** between AI agent frameworks and the MEEET network.

Supported frameworks:
- CrewAI
- LangGraph
- AutoGen

All frameworks interact through a single registry system.

---

# 🧩 Core Components

## 1. Adapters Layer

Each AI framework has its own adapter that standardizes communication.

- `CrewAIAdapter` → handles CrewAI agents
- `LangGraphAdapter` → handles LangGraph workflows
- `AutoGenAdapter` → handles AutoGen agents

Each adapter implements:

- register_agent()
- send_task()
- submit_result()

---

## 2. Registry Layer (Core Brain)

The `AgentRegistry` is the central coordination system.

Responsibilities:
- Registers all agents
- Assigns tasks to agents
- Tracks task completion
- Stores execution results

It ensures all frameworks behave consistently.

---

## 3. SDK Layer (User Interface)

The SDK (`MeeetAgent`) provides a simple interface:

- register agent in 1 line
- fetch tasks
- submit results
- interact with MEEET system

It hides internal complexity.

---

# 🔄 System Flow

## Step-by-step execution flow:

Agent Registers
↓
Registry stores agent + adapter
↓
Task assigned via registry
↓
Adapter sends task to framework
↓
Agent executes task
↓
Result returned to registry
↓
State updated / stored


---

# ⚙️ Architecture Diagram (Text Version)


      ┌──────────────┐
      │   SDK Layer   │
      │ MeeetAgent    │
      └──────┬───────┘
             ↓
  ┌────────────────────┐
  │   Registry Layer    │
  │ AgentRegistry       │
  └──────┬─────────────┘
         ↓
         
 ┌─────────────────────────────┐
 │ Adapter Layer                │
 │ CrewAI | LangGraph | AutoGen │
 └──────────┬───────────────────┘
↓
AI Framework Execution Layer


---

# 💡 Design Principles

- **Abstraction First** → frameworks are hidden behind adapters
- **Modularity** → each framework is independent
- **Scalability** → new adapters can be added easily
- **Unified State** → registry controls all agent activity

---

# 🎯 Why this architecture matters

This design enables:

- Cross-framework AI agent execution
- Unified task management system
- Scalable multi-agent collaboration
- Easy integration with decentralized systems (MEEET / Solana)

---

# 🧠 Summary

MEEET Adapter system =

👉 Multiple AI frameworks  
→ unified adapters  
→ central registry  
→ coordinated agent execution
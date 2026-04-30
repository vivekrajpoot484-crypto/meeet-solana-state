# meeet_adapter/registry.py

from typing import Dict, Any


class AgentRegistry:
    """
    Central registry for all MEEET agents across frameworks.
    Handles lifecycle, routing, and state tracking.
    """

    def __init__(self):
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.tasks: Dict[str, Dict[str, Any]] = {}

    # ---------------------------
    # AGENT MANAGEMENT
    # ---------------------------

    def register_agent(self, agent_id: str, framework: str, adapter):
        """
        Register an agent from any framework (CrewAI, LangGraph, AutoGen)
        """
        self.agents[agent_id] = {
            "framework": framework,
            "adapter": adapter,
            "status": "active",
            "tasks_completed": 0
        }

        print(f"[Registry] Agent registered: {agent_id} ({framework})")

    def get_agent(self, agent_id: str):
        return self.agents.get(agent_id)

    # ---------------------------
    # TASK ROUTING
    # ---------------------------

    def assign_task(self, agent_id: str, task: str):
        """
        Send task to correct adapter based on agent framework
        """
        agent = self.get_agent(agent_id)

        if not agent:
            raise ValueError(f"Agent {agent_id} not found")

        adapter = agent["adapter"]

        task_id = f"task_{len(self.tasks) + 1}"

        self.tasks[task_id] = {
            "agent_id": agent_id,
            "task": task,
            "status": "assigned"
        }

        adapter.send_task(agent_id, task)

        print(f"[Registry] Task assigned: {task_id} → {agent_id}")

        return task_id

    # ---------------------------
    # RESULT HANDLING
    # ---------------------------

    def submit_result(self, agent_id: str, task_id: str, result: str):
        """
        Store and mark task completion
        """
        if task_id not in self.tasks:
            raise ValueError("Invalid task_id")

        self.tasks[task_id]["status"] = "completed"
        self.tasks[task_id]["result"] = result

        self.agents[agent_id]["tasks_completed"] += 1

        print(f"[Registry] Result submitted by {agent_id}")

    # ---------------------------
    # DEBUG / INSPECT
    # ---------------------------

    def status(self):
        return {
            "agents": len(self.agents),
            "tasks": len(self.tasks),
            "active_agents": [
                a for a, v in self.agents.items() if v["status"] == "active"
            ]
        }
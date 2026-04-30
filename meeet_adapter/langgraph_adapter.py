from .base_adapter import BaseAdapter


class LangGraphAdapter(BaseAdapter):
    def register_agent(self, agent):
        print(f"[LangGraph] Registered: {agent}")

    def send_task(self, agent_id, task):
        print(f"[LangGraph] Task → {agent_id}: {task}")

    def submit_result(self, agent_id, result):
        print(f"[LangGraph] Result from {agent_id}: {result}")
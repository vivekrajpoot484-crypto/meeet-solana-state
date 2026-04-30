from .base_adapter import BaseAdapter


class AutoGenAdapter(BaseAdapter):
    def register_agent(self, agent):
        print(f"[AutoGen] Registered: {agent}")

    def send_task(self, agent_id, task):
        print(f"[AutoGen] Task → {agent_id}: {task}")

    def submit_result(self, agent_id, result):
        print(f"[AutoGen] Result from {agent_id}: {result}")
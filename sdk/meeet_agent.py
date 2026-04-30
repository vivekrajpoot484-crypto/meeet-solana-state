from meeet_adapter.registry import AgentRegistry


class MeeetAgent:
    def __init__(self, name, adapter):
        self.name = name
        self.registry = AgentRegistry()
        self.adapter = adapter

        self.registry.register_agent(name, "custom", adapter)

    def get_tasks(self):
        return []

    def submit_result(self, task_id, result):
        self.registry.submit_result(self.name, task_id, result)

    def submit_discovery(self, title, details, category):
        print(f"[Discovery] {title} - {category}")

    def chat(self, message):
        print(f"[Chat] {self.name}: {message}")
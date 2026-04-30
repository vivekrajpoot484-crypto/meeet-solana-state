class BaseAdapter:
    def register_agent(self, agent):
        raise NotImplementedError

    def send_task(self, agent_id, task):
        raise NotImplementedError

    def submit_result(self, agent_id, result):
        raise NotImplementedError
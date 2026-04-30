from meeet_adapter.registry import AgentRegistry
from meeet_adapter.langgraph_adapter import LangGraphAdapter

print("\n🚀 LangGraph Demo Starting...\n")

registry = AgentRegistry()
adapter = LangGraphAdapter()

registry.register_agent("agent_2", "langgraph", adapter)

task_id = registry.assign_task(
    "agent_2",
    "Process workflow analysis"
)

registry.submit_result(
    "agent_2",
    task_id,
    "Workflow optimized"
)

print("\n✅ LangGraph Demo Complete\n")
print(registry.status())
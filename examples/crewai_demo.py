from meeet_adapter.registry import AgentRegistry
from meeet_adapter.crewai_adapter import CrewAIAdapter

print("\n🚀 CrewAI Demo Starting...\n")

registry = AgentRegistry()
adapter = CrewAIAdapter()

registry.register_agent("agent_1", "crewai", adapter)

task_id = registry.assign_task(
    "agent_1",
    "Analyze crypto market sentiment"
)

registry.submit_result(
    "agent_1",
    task_id,
    "Bullish trend detected"
)

print("\n✅ CrewAI Demo Complete\n")
print(registry.status())
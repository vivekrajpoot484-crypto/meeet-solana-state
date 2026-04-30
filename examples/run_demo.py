from meeet_adapter.registry import AgentRegistry
from meeet_adapter.crewai_adapter import CrewAIAdapter

print("\n🚀 MEEET SYSTEM STARTING...\n")

registry = AgentRegistry()
adapter = CrewAIAdapter()

# Register agent
registry.register_agent("agent_1", "crewai", adapter)

# Assign task
task_id = registry.assign_task(
    "agent_1",
    "Analyze crypto market sentiment"
)

# Submit result
registry.submit_result(
    "agent_1",
    task_id,
    "Market shows bullish momentum"
)

print("\n✅ SYSTEM EXECUTION COMPLETE\n")
print(registry.status())
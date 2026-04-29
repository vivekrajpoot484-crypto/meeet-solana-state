from meeet_agent.trust_tool import MEEETTrustTool

def test_basic():
    tool = MEEETTrustTool()
    assert tool.run("hello") is not None
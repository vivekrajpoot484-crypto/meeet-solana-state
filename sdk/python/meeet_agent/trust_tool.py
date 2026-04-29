from .trust_client import MEEETTrustClient

class MEEETTrustTool:
    def __init__(self, min_trust=0.7):
        self.min_trust = min_trust
        self.client = MEEETTrustClient()

    def run(self, text: str) -> str:
        score = self.client.check(text)

        if score >= self.min_trust:
            return f"Trusted (score: {score:.2f})"
        return f"Low trust (score: {score:.2f})"
class MEEETTrustClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def check(self, text: str) -> float:
        if not text:
            return 0.0
        return min(1.0, len(text) / 100)
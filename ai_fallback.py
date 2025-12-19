def ai_fallback_decision(text: str) -> str:
    t = text.lower()
    if "down" in t or "error" in t or "fail" in t:
        return "URGENT"
    return "NORMAL"

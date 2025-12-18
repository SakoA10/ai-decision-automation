from rules import load_rules

def ai_decision(text: str) -> bool:
    rules = load_rules()
    t = text.lower()
    return any(rule in t for rule in rules)
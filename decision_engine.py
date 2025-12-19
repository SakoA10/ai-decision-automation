from ai_decision import ai_decision as rule_decision
from ai_fallback import ai_fallback_decision

def decision(text: str) -> str:
    if rule_decision(text):
        return "URGENT"
    return ai_fallback_decision(text)

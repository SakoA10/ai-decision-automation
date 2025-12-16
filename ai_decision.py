def load_rules():
    with open("rules.txt", "r") as f:
        return [line.strip().lower() for line in f if line.strip()]


def ai_decision(text: str) -> bool:
    rules = load_rules()
    t = text.lower()
    return any(rule in t for rule in rules)



def main():
    messages = [
        "Please review this when you can",
        "URGENT: server is down",
        "Meeting notes from yesterday",
        "Critical bug found in production",
        "ASAP: send the report",
    ]

    important = [m for m in messages if ai_decision(m)]

    print("Important messages:")
    for m in important:
        print("-", m)


if __name__ == "__main__":
    main()

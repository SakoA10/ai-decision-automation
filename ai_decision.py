def ai_decision(text: str) -> bool:
    """
    Simple AI-style decision (rule-based for now):
    returns True if the message looks important.
    """
    keywords = ["urgent", "important", "asap", "critical"]
    t = text.lower()
    return any(k in t for k in keywords)


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

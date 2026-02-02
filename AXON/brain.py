from skills import run as time_skill


INTENTS = {
    "time": {
        "keywords": ["time", "what time", "current time"],
        "action": time_skill
    },
    "exit": {
        "keywords": ["exit", "quit", "bye"],
        "action": None
    }
}

def process_command(command):
    for intent, data in INTENTS.items():
        for keyword in data["keywords"]:
            if keyword in command:
                if data["action"]:
                    return intent, data["action"]()
                else:
                    return intent, "Shutting down. Goodbye."

    return "unknown", "I don't have that skill yet."

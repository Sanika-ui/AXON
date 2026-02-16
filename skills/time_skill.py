name = "time"

def can_handle(text: str) -> bool:
    keywords = ["time", "current time", "what time"]
    return any(word in text for word in keywords)

def handle(text: str) -> str:
    from datetime import datetime
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

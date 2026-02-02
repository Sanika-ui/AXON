print("AXON is online.")

import pyttsx3
# import speech_recognition as sr   # STT paused for now

engine = pyttsx3.init()  # Initialize the TTS Engine

voices = engine.getProperty('voices')  # Choose a voice

voice_options = {
    0: ("AXON PRIME", voices[0].id),
    1: ("AXON LUMINA", voices[1].id)
}

print("\n🎤 CHOOSE AXON'S VOICE")
print("=================================")

for index, (name, vid) in voice_options.items():
    print(f"{index}. {name}")

choice = int(input("\nEnter your choice (0 or 1): "))

engine.setProperty('voice', voice_options[choice][1])
engine.setProperty('rate', 120)      # speech speed
engine.setProperty('volume', 50.0)   # volume

print(f"\nVoice set to: {voice_options[choice][0]}\n")

engine.say(
    f"Hello Saana. How are you today? How can I help you? {voice_options[choice][0]}"
)
engine.runAndWait()


# TEXT INPUT (STT PAUSED)

def get_user_input():
    return input("\n🧑 You: ").lower()


# COMMAND HANDLING (BRAIN)

def command_handler(command):
    if "hello" in command or "hi" in command:
        return "Hello! How can I assist you today?"
    elif "play music" in command:
        return "Playing your favourite music now."
    else:
        return "I'm not sure how to help with that yet."
    
# MAIN LOOP

def main():
    print("AXON is online. Type 'exit' to quit.")

    while True:
        command = get_user_input()

        if command == "":
            continue

        if "exit" in command:
            response = "Shutting down. Goodbye."
            print("AXON:", response)
            engine.say(response)
            engine.runAndWait()
            break

        response = command_handler(command)

        print("AXON:", response)
        engine.say(response)
        engine.runAndWait()


if __name__ == "__main__":
    main()

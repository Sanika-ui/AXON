print("AXON is online.")

import pyttsx3
# import speech_recognition as sr   # STT paused for now

from brain import process_command   # 🧠 import brain

# -------------------------
# TTS SETUP
# -------------------------
engine = pyttsx3.init()

voices = engine.getProperty('voices')

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
engine.setProperty('rate', 120)
engine.setProperty('volume', 50.0)

print(f"\nVoice set to: {voice_options[choice][0]}\n")

engine.say(
    f"Hello Saana.How are you today?How can I help you? {voice_options[choice][0]}"
)
engine.runAndWait()


# -------------------------
# TEXT INPUT (STT PAUSED)
# -------------------------
def get_user_input():
    return input("\n🧑 You: ").lower()


# -------------------------
# MAIN LOOP
# -------------------------
def main():
    print("AXON is online. Type 'exit' to quit.")

    while True:
        command = get_user_input()

        if command == "":
            continue

        # 🧠 send command to brain
        intent, response = process_command(command)

        print("AXON:", response)
        engine.say(response)
        engine.runAndWait()

        if intent == "exit":
            break


if __name__ == "__main__":
    main()

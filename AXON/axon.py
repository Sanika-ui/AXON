print("AXON is online.")
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init() #Initialize the TTS Engine

voices = engine.getProperty('voices') #Choose a voice

voice_options = {
    0: ("AXON PRIME", voices[0].id),
    1: ("AXON LUMINA",voices[1].id)
}

print("\n🎤 CHOOSE AXON'S VOICE")
print("=================================")

for index, (name,vid) in voice_options.items():
    print(f"{index}.{name}")

choice = int(input("\nEnter your choice (0 or 1):"))

engine.setProperty('voice', voice_options[choice][1]) #0m1f
engine.setProperty('rate',120) #speed
engine.setProperty('volume',10.0)

print(f"\nVoice set to:{voice_options[choice][0]}\n")

engine.say(f"Hello Raaaj.How are you today? {voice_options[choice][0]}")
engine.runAndWait()

#STT
def listen_to_Saana():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎧AXON is listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text.lower()
    except Exception:
        print("❗Sorry Saana , I couldn't understand that")
        return ""
    
#Command Handling
    
def command_handler(command):
    if "hello" in command:
        return "Hello! How can I assist you today?"
    elif "play music" in command:
        return "Playing your favourite music now."
    else:
        return "I'm not sure how to help with that."
 

def main():
    print("AXON is online. Type 'exit' to quit")

    while True:
        command = listen_to_Saana()
        if command == "":
            continue

        if "exit" in command:
            print("Goodbye!")
            break

        response = command_handler(command)

        print("AXON:"+ response)
        engine.say(response)
        engine.runAndWait()

if __name__ == "__main__":
   main()



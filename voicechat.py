import speech_recognition as sr
import pyttsx3
import datetime


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio and return the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def execute_command(command):
    """Execute commands based on recognized speech."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "your name" in command:
        speak("I am your personal assistant.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I can't help with that.")
    return True

def main():
    """Main function to run the voice assistant."""
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if not execute_command(command):
            break

if __name__ == "__main__":
    main()
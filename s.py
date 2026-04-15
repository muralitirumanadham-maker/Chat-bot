import datetime
import webbrowser
import os

def chatbot():
    print("🤖 AI Assistant (Type 'exit' to stop)")
    print("Assistant: Hello Murali! How can I help you?\n")

    while True:
        command = input("You: ").lower()

        # TIME
        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            print(f"Assistant: The time is {time}")

        # DATE
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            print(f"Assistant: Today is {date}")

        # GREETINGS
        elif "hello" in command or "hi" in command:
            print("Assistant: Hello! 👋 How can I help you?")

        # OPEN YOUTUBE
        elif "open youtube" in command:
            print("Assistant: Opening YouTube...")
            webbrowser.open("https://youtube.com")

        # OPEN GOOGLE
        elif "open google" in command:
            print("Assistant: Opening Google...")
            webbrowser.open("https://google.com")

        # SEARCH
        elif "search" in command:
            query = command.replace("search", "").strip()
            print(f"Assistant: Searching for {query}...")
            webbrowser.open(f"https://google.com/search?q={query}")

        # OPEN NOTEPAD (Windows)
        elif "open notepad" in command:
            print("Assistant: Opening Notepad...")
            os.system("notepad")

        # SIMPLE RESPONSES
        elif "how are you" in command:
            print("Assistant: I'm just code, but I'm doing great 😄")

        elif "your name" in command:
            print("Assistant: I am your Python AI Assistant 🤖")

        # EXIT
        elif "exit" in command or "stop" in command:
            print("Assistant: Goodbye Murali! 👋")
            break

        # UNKNOWN
        else:
            print("Assistant: Sorry, I don't understand that yet.")

# Run chatbot
chatbot()
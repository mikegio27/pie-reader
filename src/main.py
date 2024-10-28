import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1


def text_input(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError as e:
        print(f"File {filename} not found: {e.with_traceback(None)}")
    
def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    user_file_input = input('Enter the file name: ')
    if not user_file_input:
        user_text_input = input('Enter the text: ')
        speak(user_text_input)
        return
    text = text_input(user_file_input)
    speak(text)

if __name__ == '__main__':
    main()
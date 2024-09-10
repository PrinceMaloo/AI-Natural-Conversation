import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

prompt="""You are a Natural Conversational AI: give natural response based on input in less than 100 words """
genai.configure(api_key="AIzaSyDFngW1i6lMFucchEDC6wEX29NX0o5XRuo")

def generate_gemini_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

recognizer = sr.Recognizer()
tts = pyttsx3.init()


start_trigger = "start"
end_trigger = "stop"

def speak(text):
    tts.say(text)
    tts.runAndWait()
    # voices = tts.getProperty('voices') 
    # tts.setProperty('voice', voices[1].id)

def listen():
    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Listening...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=10)
            recognized_text = recognizer.recognize_google(audio)
            # print(f"Recognized text: {recognized_text}")
            return recognized_text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        

def start_conversation():
    speak("Hello! How can I assist you today?")
    input = ""
    while True:
        user_input = listen()
        if user_input:
            # user_input = user_input.strip()  
            print(f"User said: {user_input}")  
            if end_trigger.lower() in user_input.lower():
                speak("Goodbye! Talk to you soon.")
                break
            try:
                response = generate_gemini_content(input + user_input,prompt)
                speak(response)
            except Exception as e:
                print(f"Error generating response: {e}")
        else:
            print("No valid input detected.")


if __name__ == "__main__":
    print("Say 'start' to start the conversation with AI.")
    while True:
        user_input = listen()
        # print(user_input)
        if(user_input is None):
            continue
        
        if start_trigger in user_input.lower():
            start_conversation()




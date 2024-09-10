# Natural Conversational AI Application

This project uses Speech Recognition, Text-to-Speech, and Google's Gemini API to create a conversational AI system. The user can initiate a conversation by saying "start," and the application will listen, process the input using AI, and respond. The conversation can be ended by saying "stop."

## Prerequisites

- Python 3.6 or higher
- An API key for Google Gemini (Generative AI) API
- A working microphone for speech input

## Installation

### 1. Create a Virtual Environment

To create a virtual environment (venv), use the following command:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 2. Install the Required Packages

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```


### 3. Run the Application

After installing the dependencies, run the application using:

```bash
python app.py
```

## Usage

Once the application is running, say "start" to begin a conversation and "stop" to end it. The system will listen to your input, generate a response using Google's Gemini AI, and reply to you using Text-to-Speech.

## Functions Explanation

### 1. `generate_gemini_content(transcript_text, prompt)`

This function generates conversational responses using Google's Gemini AI based on the user's input (transcript text) and the provided prompt.

- `transcript_text`: Text of the user's speech input.
- `prompt`: A predefined conversational prompt.
- **Returns**: AI-generated response text.

### 2. `speak(text)`

This function converts the given text into speech using the `pyttsx3` Text-to-Speech engine.

- `text`: The text to be spoken by the system.

### 3. `listen()`

This function captures audio input from the user's microphone and uses the `SpeechRecognition` library to convert it into text. It handles ambient noise, unknown words, and timeouts gracefully.

- **Returns**: The recognized text from the user’s speech.

### 4. `start_conversation()`

This is the main function to handle the conversational loop. It begins by greeting the user and listens for their input continuously. It generates AI responses and speaks them back to the user until the "stop" command is detected.

### 5. Main Loop

In the main loop, the program listens for the "start" command to initiate the conversation. If no valid input is detected, it continues waiting.


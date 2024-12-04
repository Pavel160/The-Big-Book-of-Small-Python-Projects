# Text-to-Speech (TTS) Project
**Author**: Al Sweigart (al@inventwithpython.com)

This project is designed to convert text into speech using Python. The application takes input text and produces an audio output that can be heard as speech.

## Requirements
Before running the project, you need to install the necessary dependencies:

- Python 3.x
- pyttsx3
- gTTS (Google Text-to-Speech)
- playsound (to play the generated audio)

You can install the required packages using pip:
- On Windows, open a Command Prompt and run:
```bash
pip install pyttsx3
pip install gTTS playsound
```
- On macOS and Linux, open a Terminal and run:
```bash
pip3 install pyttsx3
pip3 install gTTS playsound
```

## Features
- Convert any input text into speech.
- Save the generated speech to an audio file (e.g., .mp3 format).
- Option to play the speech directly from the program.

## How It Works
This project uses the gTTS (Google Text-to-Speech) library, which interfaces with Google's Text-to-Speech API. The program takes input text, converts it to speech, and allows you to either play the speech immediately or save it as an audio file.

## Usage
1. Convert Text to Speech and Play It:

   To convert text into speech and play it immediately, simply run the following code:

```python
from gtts import gTTS
from playsound import playsound

text = "Hello, welcome to the Text to Speech conversion example!"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
playsound("output.mp3")
```
- This will convert the provided text into speech and play it using the playsound module.

2. Save the Speech to a File:

   If you only want to save the speech to a file without playing it, you can use:

```python

tts.save("output.mp3")
```
   The audio file will be saved as output.mp3 in the current directory.

3. Customizing the Language:

   You can change the language of the speech by modifying the lang parameter in the gTTS constructor. For example:

```python

tts = gTTS(text=text, lang='ru')  # For Russian speech
```
   Supported languages include English (en), Russian (ru), Spanish (es), and many more. Check the gTTS documentation for a full list of supported languages.

## Example Input and Output
### Input:
```python

text = "Привет, как дела?"
```
### Output:
An MP3 file with the speech "Привет, как дела?" in Russian, played through the speakers.

## License
See the [LICENSE](LICENSE) file for details.

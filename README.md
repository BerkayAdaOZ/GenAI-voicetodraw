
# VoicetoDraw with GenAI

## Overview
VoicetoDraw is a Streamlit-based application that allows users to record their voice, transcribe it using OpenAI's Whisper, and generate images based on the transcribed text. The project leverages both OpenAI's DALL·E model for text-to-image generation and Google's Gemini model for multimodal image generation based on existing images.

## Features
- **Voice Recording**: Users can record audio directly in the app.
- **Speech-to-Text Transcription**: The recorded voice is transcribed into text using OpenAI's Whisper model.
- **Text-to-Image Generation**: Transcriptions are used to generate images through DALL·E and Gemini models.
- **Downloadable Image Output**: Generated images can be downloaded.
- **Chat UI**: Displays the transcription and generated image in a chat-style interface.


## Prerequisites
- Python 3.x
- A virtual environment (optional, but recommended)
- API keys for OpenAI and Google Gemini

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone 
   ```

2. Navigate into the project directory:

   ```bash
   cd 
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your `.env` file with the following environment variables (do not commit this file):

   ```
   openai_apikey=<your-openai-api-key>
   google_apikey=<your-google-api-key>
   ```

   Make sure you add this file to your `.gitignore` to keep your keys private.

6. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

## Usage

1. Once the app is running, you can record your voice by clicking the "Start" button and stop the recording by clicking the "Stop" button.
2. After the recording is completed, the app will transcribe the audio and display it in the chat window.
3. The app will generate an image based on the transcription. If you wish, you can also use the last generated image as the base for a new image using Google Gemini.
4. The generated images can be downloaded.

## Security

- Ensure that your `.env` file, which contains API keys, is not committed to version control. It should be listed in the `.gitignore` file by default.
- Do not share or expose your API keys publicly.

## Future Improvements

- Add more customization options for image generation (e.g., adjusting the model parameters).
- Implement additional language support for transcription and image generation prompts.
- Improve the UI/UX for a smoother user experience.

## License
This project is licensed under the MIT License.

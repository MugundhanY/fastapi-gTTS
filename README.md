# FastAPI Text-to-Speech Service

This is a FastAPI application that provides a text-to-speech (TTS) service. It uses the Google Text-to-Speech (gTTS) library to convert text into speech and serves the audio file via an API endpoint.

## Features

- Detects the language of the input text.
- Converts text to speech using gTTS.
- Provides the audio file as a downloadable MP3.

## Endpoints

### POST /tts

Converts text to speech.

**Request Body:**
```json
{
  "text": "Your text here"
}

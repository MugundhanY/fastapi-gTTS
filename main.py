from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gtts import gTTS
from langdetect import detect, DetectorFactory
from io import BytesIO
from fastapi.responses import StreamingResponse

# Ensure consistent language detection
DetectorFactory.seed = 0

app = FastAPI()

# Define a request model
class TextToSpeechRequest(BaseModel):
    text: str

@app.post("/tts")
async def generate_speech(request: TextToSpeechRequest):
    text = request.text

    try:
        # Detect the language of the text
        try:
            language = detect(text)
        except:
            language = "en"  # Default to English if detection fails
        
        # Generate speech using gTTS
        tts = gTTS(text=text, lang=language)
        
        # Save the audio to a BytesIO object
        audio_io = BytesIO()
        tts.write_to_fp(audio_io)
        audio_io.seek(0)
        
        # Return the audio file as a streaming response
        return StreamingResponse(
            audio_io,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=output.mp3"}
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Uvicorn server entry point - Uncomment if running locally
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

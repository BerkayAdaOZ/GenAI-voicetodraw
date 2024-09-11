from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

apiKeyOpenai = os.getenv("openai_apikey")

client = OpenAI(
    api_key=apiKeyOpenai
)

def transcribeWithWhisper(audioFileName):

    audioFile = open(audioFileName, "rb")

    AıGeneratedTranscript = client.audio.transcriptions.create(
        model="whisper-1",
        file= audioFile,
        language="tr"
    )

    return AıGeneratedTranscript.text

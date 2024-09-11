import pyaudio
import wave
import time

def record(recordActive, frames):
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100, #for high quality audio record hz
        input=True,
        frames_per_buffer=1024 # like chunk size
    )

    while recordActive.is_set():
       data = stream.read(1024, exception_on_overflow=False)
       frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()   

    soundFile = wave.open("voice_prompt.wav", "wb")
    soundFile.setnchannels(1)
    soundFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    soundFile.setframerate(44100)
    soundFile.writeframes(b''.join(frames))
    soundFile.close()

    time.sleep(1)
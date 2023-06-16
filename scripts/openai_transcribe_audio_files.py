import whisper

model = whisper.load_model("base")
result = model.transcribe("Insert_Audio_File_Here.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])
import whisper
import json

model = whisper.load_model("base")
result=model.transcribe(audio="audios/01_ String Methods.mp3",
                        language="hi",
                        task="translate")
# print(result["segments"])
# with open("result.json", "w") as f:
    # json.dump(result, f)  
chunks=[]
for segment in result["segments"]:
    chunks.append(f"start: {segment['start']} end: {segment['end']} text: {segment['text']}")
    print(chunks)

with open("result.json", "w") as f:
  json.dump(chunks, f)
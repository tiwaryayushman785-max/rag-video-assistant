# import whisper
# import json
# import os

# model=whisper.load_model("large-v2")
# audio=os.listdir("audio")

# for audios in audio:
#     if audio.endswith(".mp3"):
#          number=audios.split("-")[0]
#          title=audios.split(".")[1][:-4]
#          print(number,title)
#          result = model.transcribe(audio = f"audio/{audios}", 
#         # result = model.transcribe(audio = f"audios/sample.mp3", 
#                               language="hi",
#                               task="translate",
#                               word_timestamps=False )
        
#          chunks=[]
#          for segment in result["segments"]:
#               chunks.append({"number":number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
#               chunks_with_metadata={"chunks":chunks,"text":result["text"]}

#               with open(f"jsons/{audios}.json","w")as f:
#                    json.dump(chunks_with_metadata,f)


import whisper
import json
import os

model = whisper.load_model("large-v2")

audio_files = os.listdir("audio")

os.makedirs("jsons", exist_ok=True)

for filename in audio_files:

    if filename.endswith(".mp3"):

        print("Processing:", filename)

        audio_path = os.path.join("audio", filename)

        result = model.transcribe(
            audio=audio_path,
            language="hi",
            task="translate"
        )

        chunks = []

        for segment in result["segments"]:
            chunks.append({
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

        output_path = os.path.join("jsons", filename + ".json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({
                "chunks": chunks,
                "text": result["text"]
            }, f, ensure_ascii=False, indent=4)

        print("Saved:", output_path)

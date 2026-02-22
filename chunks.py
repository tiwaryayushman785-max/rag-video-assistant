

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


import os
import subprocess
import shutil

FFMPEG = r"C:\Users\user\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"

os.makedirs("segments", exist_ok=True)
os.makedirs("demo_video", exist_ok=True)

SCENES = [
    {
        "id": "seg_01",
        "bg": "screenshots/01_login_hero.png",
        "overlay": "video_assets/card_01.png",
        "audio": "audio/scene1_hook.mp3"
    },
    {
        "id": "seg_02",
        "bg": "screenshots/02_idea_constellation.png",
        "overlay": "video_assets/card_02.png",
        "audio": "audio/scene2_pitch.mp3"
    },
    {
        "id": "seg_03",
        "bg": "screenshots/02_idea_constellation.png",
        "overlay": "video_assets/card_03.png",
        "audio": "audio/scene3_ingestion.mp3"
    },
    {
        "id": "seg_04",
        "bg": "screenshots/03_source_linked_blueprint.png",
        "overlay": "video_assets/card_04.png",
        "audio": "audio/scene4_blueprint.mp3"
    },
    {
        "id": "seg_05",
        "bg": "screenshots/04_storm_simulation.png",
        "overlay": "video_assets/card_05.png",
        "audio": "audio/scene5_simulation.mp3"
    },
    {
        "id": "seg_06",
        "bg": "screenshots/06_revision_learning.png",
        "overlay": "video_assets/card_06.png",
        "audio": "audio/scene6_revision.mp3"
    },
    {
        "id": "seg_07",
        "bg": "video_assets/scene7_bg.png",
        "overlay": "video_assets/card_07.png",
        "audio": "audio/scene7_architecture.mp3"
    }
]

print("1. Rendering individual scene segments...", flush=True)

segment_files = []
for s in SCENES:
    out_mp4 = f"segments/{s['id']}.mp4"
    cmd = [
        FFMPEG, "-y",
        "-loop", "1", "-i", s["bg"],
        "-i", s["overlay"],
        "-i", s["audio"],
        "-filter_complex", "[0:v]scale=1920:1080[bg];[bg][1:v]overlay=0:0[v]",
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        out_mp4
    ]
    print(f"Rendering {s['id']}...", flush=True)
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    segment_files.append(out_mp4)

print("2. Concatenating all segments into the final 1080p demo video...", flush=True)

# Create ffmpeg concat file
concat_txt = "segments/concat_list.txt"
with open(concat_txt, "w") as f:
    for seg in segment_files:
        f.write(f"file '{os.path.abspath(seg).replace(os.sep, '/')}'\n")

final_output = "demo_video/ChatAtlas_Foundry_Demo_Video.mp4"

concat_cmd = [
    FFMPEG, "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_txt,
    "-c", "copy",
    final_output
]

subprocess.run(concat_cmd, check=True)

# Inspect final video
ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
res = subprocess.run(
    [ffprobe, "-v", "error", "-show_entries", "format=duration,size", "-of", "default=noprint_wrappers=1", final_output],
    capture_output=True, text=True
)
print("\nFinal Demo Video Details:\n" + res.stdout)
print(f"Location: {os.path.abspath(final_output)}")
print("ASSEMBLY_COMPLETE", flush=True)

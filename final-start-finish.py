from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import fadein
import os

# Set fixed resolution
w, h = 1280, 720
target_size = (w, h)

# Load intro and extro and resize to fixed resolution
intro_clip_raw = VideoFileClip("INTRO.mp4")
extro_clip_raw = VideoFileClip("EXTRO.mp4")

target_fps = intro_clip_raw.fps  # Use intro fps as standard

intro_clip = intro_clip_raw.resize(target_size).set_fps(target_fps)
extro_clip = extro_clip_raw.resize(target_size).set_fps(target_fps)

# Folder containing videos to be merged
video_folder = "."
output_folder = "merged_videos"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(video_folder):
    if filename.endswith(".mp4") and filename not in ["INTRO.mp4", "EXTRO.mp4"]:
        print(f"Processing: {filename}")
        try:
            main_clip_raw = VideoFileClip(os.path.join(video_folder, filename))
            main_clip = main_clip_raw.resize(target_size).set_fps(target_fps)

            # Fade-in effect
            main_clip = fadein(main_clip, duration=1.5)

            # Merge intro + main + extro
            final_clip = concatenate_videoclips([intro_clip, main_clip, extro_clip])
            output_path = os.path.join(output_folder, filename)

            final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

            # Cleanup
            final_clip.close()
            main_clip.close()
            main_clip_raw.close()

        except Exception as e:
            print(f"Error processing {filename}: {e}")

intro_clip.close()
extro_clip.close()

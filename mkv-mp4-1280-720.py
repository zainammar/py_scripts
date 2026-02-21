import os
import subprocess

# Define input and output folders
input_folder = "mkv"
output_folder = "mp4"

# Define target resolution
target_width = 1280
target_height = 720

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through MKV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mkv"):
        mkv_path = os.path.join(input_folder, filename)
        mp4_filename = os.path.splitext(filename)[0] + ".mp4"
        mp4_path = os.path.join(output_folder, mp4_filename)
        
        print(f"🔁 Converting and resizing: {filename} → {mp4_filename} to {target_width}x{target_height}")
        
        # ffmpeg command to convert with re-encoding and resizing
        cmd = [
            "ffmpeg",
            "-i", mkv_path,
            "-vf", f"scale={target_width}:{target_height}", # Video filter for scaling
            "-c:v", "libx264", # Video codec (H.264)
            "-preset", "medium", # Encoding preset for speed/quality balance
            "-crf", "23", # Constant Rate Factor for quality (lower is better, 23 is a good default)
            "-c:a", "aac", # Audio codec
            "-b:a", "128k", # Audio bitrate
            mp4_path
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Saved: {mp4_path}\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error converting: {filename}")
            print(f"Error details: {e}\n")
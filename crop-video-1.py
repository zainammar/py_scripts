from moviepy.editor import VideoFileClip

# === INPUT SETTINGS === Lecture 14-2025_11_10
input_video = "input.mp4"      # Input video file
output_video = "cut_video.mp4" # Output file
start_time =120         # Start time in seconds
end_time =900     # End time in seconds

# === LOAD VIDEO === 
video = VideoFileClip(input_video)

# === CUT VIDEO ===
cut_video = video.subclip(start_time, end_time)

# === EXPORT RESULT ===
cut_video.write_videofile(output_video, codec="libx264", audio_codec="aac")

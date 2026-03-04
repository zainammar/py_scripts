from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# === Config ===
bg_video = "background.mp4"  # Background video  Lecture 14-2025_11_10
logo_image = "logo.png"      # Logo file
output_file = "final_video.mp4"
video_duration =  1440     # Fixed duration in seconds 1440  
w, h = 1280, 720
# bg_box_color = (0, 0, 0,)  # RGBA: black with transparency (150 = semi-transparent)

# === Create Text Image with Background ===


# === Background Video ===
bg_clip = VideoFileClip(bg_video).resize((w, h)).subclip(0, video_duration)

# === Logo Clip ===
logo_clip = (ImageClip(logo_image)
             .set_duration(video_duration)
             .resize(height=30)
             .set_position(("right", "top"))
             .margin(left=20, top=20, opacity=0))



# === Final Composite ===
final_clip = CompositeVideoClip([bg_clip, logo_clip])
final_clip.write_videofile(output_file, fps=bg_clip.fps, codec="libx264", audio_codec="aac")

print("✅ Video created with two animated texts, background boxes, and logo.")

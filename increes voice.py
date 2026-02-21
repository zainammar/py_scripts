from moviepy.editor import VideoFileClip, AudioFileClip
import math # Import math for the power calculation

def increase_video_volume(input_video_path, output_video_path, volume_factor):
    """
    Increases the audio volume of an MP4 video file while keeping the video track.

    Args:
        input_video_path (str): The path to the input MP4 video file.
        output_video_path (str): The path where the volume-increased MP4 video will be saved.
        volume_factor (float): The factor by which to multiply the volume (e.g., 2.0 for double volume).
                                To increase by a decibel amount (like +10dB), you'd calculate: 10^(dB/20)
                                For +10dB, volume_factor = 10^(10/20) = 10^0.5 = 3.16
                                For +5dB, volume_factor = 10^(5/20) = 10^0.25 = 1.78
    """
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_video_path)

        # Get the audio from the video clip
        original_audio = video_clip.audio

        if original_audio is None:
            print(f"Warning: No audio track found in '{input_video_path}'. Copying video directly.")
            video_clip.write_videofile(output_video_path, codec="libx264")
            video_clip.close()
            return

        # Increase the volume of the audio
        louder_audio = original_audio.volumex(volume_factor)

        # Set the louder audio back to the video clip
        final_clip = video_clip.set_audio(louder_audio)

        # Write the new video file with the adjusted audio
        # Using "libx264" codec for video and "aac" for audio is generally a good choice for MP4
        final_clip.write_videofile(
            output_video_path,
            codec="libx264",
            audio_codec="aac"
        )

        print(f"Successfully increased volume for '{input_video_path}' by a factor of {volume_factor}.")
        print(f"Saved to '{output_video_path}'")

        # Close clips to free up resources
        video_clip.close()
        original_audio.close()
        louder_audio.close()
        final_clip.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have FFmpeg installed and in your system's PATH.")
        print("You can download FFmpeg from: https://ffmpeg.org/download.html")
        print("Also, ensure 'moviepy' is installed: pip install moviepy")

# --- How to use it ---
if __name__ == "__main__":
    input_file = "3. Control Flow Statements (if, for, while) - Urdu.mp4"  # <--- IMPORTANT: Replace with your video file name
    output_file = "updated 3. Control Flow Statements (if, for, while) - Urdu.mp4" # Name for the output file

    # You need to decide on a volume factor.
    # A factor of 1.0 means no change. 2.0 means double the volume.
    # If you want to increase by X decibels (dB), the formula is 10^(X/20).
    
    # Example: Increase by 10 dB
    db_increase = 10 # <--- Adjust this number for more or less volume increase
    volume_multiplier = math.pow(10, db_increase / 20) 
    print(f"Increasing volume by {db_increase} dB, which is a multiplier of {volume_multiplier:.2f}")

    increase_video_volume(input_file, output_file, volume_multiplier)

    # You can uncomment and modify this section to try another increase,
    # for example, increasing the already louder video even more.
    # # Example: Increase by another 5 dB from the already louder video
    # input_file_2 = "your_video_louder.mp4"
    # output_file_2 = "your_video_even_louder.mp4"
    # db_increase_2 = 5
    # volume_multiplier_2 = math.pow(10, db_increase_2 / 20)
    # print(f"\nFurther increasing volume by {db_increase_2} dB, which is a multiplier of {volume_multiplier_2:.2f}")
    # increase_video_volume(input_file_2, output_file_2, volume_multiplier_2)
from pydub import AudioSegment
from moviepy.editor import *

def create_video_preview(audio_file, video_file, start_time, output_video="output.mp4"):
    """
    Extracts a 10-second audio preview and overlays it onto a given video.

    Parameters:
    - audio_file (str): Path to the input .wav file
    - video_file (str): Path to the input video file
    - start_time (float): Start time (in seconds) for the audio preview
    - output_video (str): Path to save the final video (default: "output.mp4")
    
    Returns:
    - None (Saves the new video file)
    """
       # Determine audio format
    if audio_file.lower().endswith(".mp3"):
        audio = AudioSegment.from_mp3(audio_file)
        print("*************   MP3 file detected   *************")
    elif audio_file.lower().endswith(".wav"):
        audio = AudioSegment.from_wav(audio_file)
        print("*************   WAV file detected   *************")
    else:
        raise ValueError("Unsupported audio format. Please use MP3 or WAV.")


    # Load the audio and extract the segment
    start_ms = start_time * 1000
    end_ms = start_ms + 10 * 1000  # 10 seconds later
    preview_audio = audio[start_ms:end_ms]
    
    # Save the extracted preview as a temporary file
    preview_audio.export("temp_preview.wav", format="wav")

    # Load the video file
    video = VideoFileClip(video_file)

    # Ensure the video is at least 10 seconds long
    video = video.subclip(0, min(10, video.duration))

    # Load the extracted audio preview
    new_audio = AudioFileClip("temp_preview.wav")
    
    # Set the audio of the video to the extracted audio
    video = video.set_audio(new_audio)
    
    # Export the final video
    video.write_videofile(output_video, codec="libx264", audio_codec="aac")
    
    print(f"Video preview saved as {output_video}")

# Example usage:
audio_used=sys.argv[1]
time1_used=int(sys.argv[2])
time2_used=int(sys.argv[3])
time3_used=int(sys.argv[4])
create_video_preview(audio_used, "outputnoaudio.mp4", time1_used,"outputvid1.mp4")
create_video_preview(audio_used, "outputnoaudio.mp4", time2_used,"outputvid2.mp4")
create_video_preview(audio_used, "outputnoaudio.mp4", time3_used,"outputvid3.mp4")
create_video_preview(audio_used, "outputnoaudioIG.mp4", time1_used,"outputvidIG.mp4")
# Example prompt: python audiocut.py orbitpodcast1.wav 946 1200 1500
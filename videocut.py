from moviepy.editor import *

def overlay_image_on_video(video_file, image_file,ratio,output_video="outputnoaudio.mp4"):
    """
    Overlays an image on top of a video for the entire duration.

    Parameters:
    - video_file (str): Path to the input video file
    - image_file (str): Path to the input image file
    - output_video (str): Path to save the final video (default: "output.mp4")

    Returns:
    - None (Saves the new video file)
    """

    # Load the video
    video = VideoFileClip(video_file)

    # Load the image
    image = ImageClip(image_file)

    # Resize the image to % of its original size
    image = image.resize(ratio)

    # Center the image on the video
    img_x = (video.w - image.w) / 2
    img_y = (video.h - image.h) / 2
    image = image.set_position((img_x, img_y)).set_duration(video.duration)

    # Overlay the image on the video
    final_video = CompositeVideoClip([video, image])

    # Export the final video
    final_video.write_videofile(output_video, codec="libx264", audio_codec="aac")

    print(f"Video with image overlay saved as {output_video}")

# Example usage:
image_used=sys.argv[1]
overlay_image_on_video("orbitpodcastbackgroundcut.mp4",image_used,0.85,"outputnoaudio.mp4" )
overlay_image_on_video("orbitpodcastbackgroundcutIG.mp4",image_used,0.95,"outputnoaudioIG.mp4")
# Example prompt: python videocut.py intoorbit1.png
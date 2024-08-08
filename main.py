from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

print("####### Choose Download Type #######\n[1] MP4\n")

choosen_type = input("Type: ")

if choosen_type == "1":
    link = input("Link: ")

    print("Downloading...")

    yt = YouTube(link)

    video_stream = yt.streams.filter(res="1080p", mime_type="video/mp4").first()
    video_path = video_stream.download(filename='video.mp4')

    audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
    audio_path = audio_stream.download(filename='audio.mp4')

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    ideo_clip = video_clip.set_audio(audio_clip)

    output_path = 'output.mp4'
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    os.remove(video_path)
    os.remove(audio_path)

    print("Done!")
else:
    print("Invalid Type")
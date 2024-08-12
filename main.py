from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

print("\n\033[35m####### \033[0mChoose Download Type \033[35m#######\n\033[0mVideo:\n[\033[35m1\033[0m] MP4\n\nAudio:\n[\033[35m2\033[0m] MP3\n[\033[35m3\033[0m] WAV\n[\033[35m4\033[0m] OGG\n")

choosen_type = input("Type: ")

link = input("Link: ")

print("Downloading...")

yt = YouTube(link)

if choosen_type == "1":
    video_title = yt.title.replace(" ", "_")

    video_stream = yt.streams.filter(res="1080p", mime_type="video/mp4").first()
    video_path = video_stream.download(filename='video.mp4')

    audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
    audio_path = audio_stream.download(filename='audio.mp4')

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop_path, f'{video_title}.mp4')

    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    video_clip.close()
    audio_clip.close()
    final_clip.close()

    os.remove(video_path)
    os.remove(audio_path)

    print(f"Done! Video saved to {output_path}")
elif choosen_type == "2":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(filename=yt.title+'.mp3', output_path=desktop_path)
    print(f"Audio saved to {audio_path}")
elif choosen_type == "3":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(filename=yt.title+'.wav', output_path=desktop_path)
    print(f"Audio saved to {audio_path}")
elif choosen_type == "4":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(filename=yt.title+'.ogg', output_path=desktop_path)
    print(f"Audio saved to {audio_path}")
else:
    print("Invalid Type")

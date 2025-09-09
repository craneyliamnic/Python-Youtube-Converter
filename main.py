from pytubefix import YouTube
from moviepy import VideoFileClip, AudioFileClip
import os

class colors:
    NORMAL = '\033[0m'
    PURPLE = '\033[35m'
    RED = '\033[31m'

print(
        f"{colors.PURPLE}\n####### {colors.NORMAL}Choose Download Type {colors.PURPLE}#######\n"
        f"{colors.NORMAL}Video:\n[{colors.PURPLE}1{colors.NORMAL}] MP4\n\n"
        "Audio:\n"
        f"[{colors.PURPLE}2{colors.NORMAL}] MP3\n"
        f"[{colors.PURPLE}3{colors.NORMAL}] WAV\n"
        f"[{colors.PURPLE}4{colors.NORMAL}] OGG\n"
        f"[{colors.PURPLE}5{colors.NORMAL}] ACC\n"
)

choosen_type = input("Type: ")

def init():
    link = input("Link: ")
    global yt
    yt = YouTube(link)
    print("Downloading...")

def downloadVideo(file_type: str):
    init()

    video_title = yt.title.replace(" ", "_")

    video_stream = yt.streams.get_highest_resolution()
    video_path = video_stream.download(filename='video.' + file_type)

    audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
    audio_path = audio_stream.download(filename='audio.mp4')

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.with_audio(audio_clip)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop_path, f'{video_title}.' + file_type)

    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    video_clip.close()
    audio_clip.close()
    final_clip.close()

    os.remove(video_path)
    os.remove(audio_path)

    print(f"Done! Video saved to {output_path}")

def downloadAudio(file_type: str):
    init()

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(filename=yt.title + '.' + file_type, output_path=desktop_path)
    print(f"Audio saved to {audio_path}")

match choosen_type:
    case "1":
        downloadVideo('mp4')
    case "2":
        downloadAudio('mp3')
    case "3":
        downloadAudio('wav')
    case "4":
        downloadAudio('ogg')
    case "5":
        downloadAudio('aac')
    case _:
        print(f"[{colors.RED}ERROR{colors.NORMAL}] Invalid type")
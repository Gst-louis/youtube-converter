from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

link = str(input("Entrez le lien: "))
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

question = str(input("Mp3 ou Mp4 ? "))

if question.lower() == "mp3":
    video_file = yd.download(r"C:\Users\SURFACE\Downloads\PyConverter")

    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    mp3_file = os.path.splitext(video_file)[0] + ".mp3"
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    video_clip.close()

    os.remove(video_file)

    print(f"Conversion terminée. Fichier MP3 sauvegardé sous: {mp3_file}")

elif question.lower() == "mp4":
    yd.download(r"C:\Users\SURFACE\Downloads\PyConverter")
    print("Téléchargement MP4 terminé.")

else:
    print("Format non reconnu. Choisissez entre 'Mp3' ou 'Mp4'.")

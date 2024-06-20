from pytube import YouTube
from sys import argv

link = str(input("Entrez le lien: "))
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(r"C:\Users\SURFACE\Downloads\PyConverter")  

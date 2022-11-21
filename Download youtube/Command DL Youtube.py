
from pytube import YouTube
from pytube import Playlist

link = input("Enter Your URL: ")
youtube_dl = YouTube(link)

# print(youtube_dl.title) # لعرض عنوان الفديو

# print(youtube_dl.thumbnail_url) # لعرض صوره الفديو

# print(youtube_dl.streams.all()) # لعرض جميع محتويات الفديو

# video = youtube_dl.streams.filter(only_audio=True) # لتحويل الفديو لصوت
# vid = list(enumerate(video))
# for i in vid:
#     print(i)
# strm = int(input("Enter: "))
# video[strm].download()

print("Choose Number For Quilty Video: ")
qy = """  .....        .....
        1-720p
        2-480p
        3-360p
        4-144p
  .....        ....."""
print(qy)
quilty = int(input("> "))
def willd():
    if quilty == 1:
        print("Choosed Number 1 Quilty Downloader 720p")
    elif quilty == 2:
        print("Choosed Number 2 Quilty Downloader 480p")
    elif quilty == 3:
        print("Choosed Number 3 Quilty Downloader 360p")
    elif quilty == 4:
        print("Choosed Number 4 Quilty Downloader 144p")
    else:
        print("Wrong Number Try Again Letter")

willd()
print("Done...")

# @@ ##### Download Playlist ##### لتحميل playlist كامله
# py=Playlist(link)
# print(f"Downloading {py.title}")
# for video in py.videos:
#     video.streams.first().download() # type: ignore
from pytube import YouTube
from tkinter import filedialog
url_input = input('ENter URL: ')
all_streams = YouTube(url_input).streams.all()
v=-1
for i in all_streams:
    v=+1
    print(f"{v} : {i}")

stm_input= (int(input("Choose Quilty Video : ")))
print("Choose Path Download : ")
folder_name=filedialog.askdirectory()
choice = all_streams[stm_input].download(folder_name)
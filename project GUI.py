from tkinter import *
from pytube import YouTube
import threading

download_thread = None

def download_video(quality):
    global download_thread
    url = link_entry.get()
    yt = YouTube(url)
    if quality == 'high':
        video = yt.streams.get_highest_resolution()
    elif quality == 'low':
        video = yt.streams.get_lowest_resolution()
    else:
        video = yt.streams.filter(only_audio=True).first()
    def download():
        video.download()
        status_label.config(text="Download Complete!")
    download_thread = threading.Thread(target=download)
    download_thread.start()

def cancel_download():
    global download_thread
    if download_thread is not None:
        download_thread = None
        status_label.config(text="Download Canceled!")
root = Tk()
root.title("YouTube Downloader")
label = Label(root, text="Past link here", font=("Arial", 14, "bold"))
label.pack(pady=10)
link_entry = Entry(root, width=50)
link_entry.pack(pady=10)
button_frame = Frame(root)
button_frame.pack(pady=20)
button1 = Button(button_frame, text="High Quality", command=lambda: download_video('high'), bg="#FFFF99", font=("Arial", 10))
button1.grid(row=0, column=0, padx=10)
button2 = Button(button_frame, text="Low Quality", command=lambda: download_video('low'), bg="#FFFF99", font=("Arial", 10))
button2.grid(row=0, column=1, padx=10)
button3 = Button(root, text="Audio Only", command=lambda: download_video('audio'), bg="#FFFF99", font=("Arial", 10))
button3.pack(pady=10)
button4 = Button(root, text="Cancel Download", command=cancel_download, bg="#FF6347", font=("Arial", 10))
button4.pack(pady=10)
status_label = Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)
root.mainloop()

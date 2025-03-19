from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
from pygame import mixer
import os
root=tk.Tk()
root.title("Music player")

root.geometry("920x670+290+85")

root.configure(bg="#0f1a2b")
root.resizable(False,False)
mixer.init()
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
    #print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])
def play_next_song():
    index=playlist.index(pygame.mixer.music.get_buzy())
    if index+1>=len(playlist):
        index=0
    else:
        index+=1
        play_song(index)

    
    
#icon
Image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,Image_icon)
TOP=PhotoImage(file="top.png ")
Label(root,image=TOP,bg="#0f1a2b").pack()
#logo
logo=PhotoImage(file="logo.png")
Label(root,image=Image_icon,bg="#0f1a2b").place(x=65,y=115)
#button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0,command=play_song).place(x=100,y=400)
#stop
stop_button=PhotoImage(file="stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=30,y=500)
#resume
resume_button=PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=115,y=570)
#next
#next_button=PhotoImage(file="next.png")
#Button(root,image=next_button,bg="#0f1a2b",bd=0,command=mixer.music.next).place(x=100,y=500)
#pause
pause_button=PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=200,y=500)
#Label
music=Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=565,y=265,anchor="center")
#music
Menu=PhotoImage(file="menu.png")
Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)
#Musicframe
Music_frame=Frame(root,bd=2,relief=SUNKEN)
Music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="open_folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330,y=300)
scroll=Scrollbar(Music_frame)
playlist=Listbox(Music_frame,width=100,font=("arial",10),bg="#333333",fg="gray",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)







root.mainloop()

from pygame import *
from tkinter import filedialog
songlist = []
songIndex = -1

#C:\Users\rohit\Desktop\songs
def loadsingle():
    # print("loadSingle")
    global songIndex
    path = filedialog.askopenfilename()
    songlist.append(path)
    songIndex + 1
    mixer.init()
    mixer.music.load(songlist[songIndex])
    print(songIndex)
    print(songlist[songIndex])


def Play():
    # # print("play")
    # print(mixer.music.get_pos())
    # mixer.music.play()
    if mixer.music.get_pos()>0:
        mixer.music.unpause()
    else:
        mixer.music.play()


def Pause():
    # print("Pause")
    mixer.music.pause()

def Stop():
    # print("Stop")
    mixer.music.stop()

def loadPlaylist():
    # print("playlist")
    global songIndex
    songlist.clear()
    songIndex = 0
    filePath = filedialog.askopenfilenames()
    print(filePath)
    for fileName in filePath:
        songlist.append(fileName)
    mixer.init()
    mixer.music.load(songlist[songIndex])
    mixer.music.play()
    print(songlist)

def nextSong():
   global songIndex
   songIndex += 1
   if songIndex >= len(songlist):
       songIndex = 0
   mixer.music.load(songlist[songIndex])
   mixer.music.play()

def previousSong():
    # print("previous")
    global songIndex
    songIndex -= 1
    if songIndex <0:
        songIndex = len(songlist)-1
    mixer.music.load(songlist[songIndex])
    mixer.music.play()

# if __name__ == '__main__':
#     while True:
#         print(" 1. Load single  2. Play 3. Pause 4. Stop  5.Load Playlist 6. Next 7.Previous")
#         ch = int(input(" "))
#         if ch == 1:
#             loadsingle()
#         elif ch == 2:
#             Play()
#         elif ch == 3:
#             Pause()
#         elif ch == 4:
#             Stop()
#         elif ch == 5:
#             loadPlaylist()
#         elif ch == 6:
#             nextSong()
#         elif ch == 7:
#             previousSong()

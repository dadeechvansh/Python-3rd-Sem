from abc import ABC,abstractmethod

class Mediaplayer(ABC):
    def playaudio(self):
        print("Can play audio")

    @abstractmethod
    def playvideo(self):
        pass

class SoundRecorder(Mediaplayer):
    def playvideo(self):
        print("can't play video")

class Vlcplayer(Mediaplayer):
    def playvideo(self):
        print("can play video")


sr=SoundRecorder()
sr.playaudio()
sr.playvideo()

vlc=Vlcplayer()
vlc.playaudio()
vlc.playvideo()
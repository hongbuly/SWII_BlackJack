from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtMultimedia import *
import os


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()

    def volumeUp(self):
        currentVolume = self.player.volume()
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() #
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):
        full_file_path = os.path.join(os.getcwd(), './sounds/bgm.mp3')
        url = QtCore.QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()

    def volumeUp(self):
        current_volume = self.player.volume()
        # print(currentVolume)
        self.player.setVolume(current_volume + 10)

    def volumeDown(self):
        current_volume = self.player.volume()
        # print(currentVolume)
        self.player.setVolume(current_volume - 10)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):
        full_file_path = os.path.join(os.getcwd(), './sounds/bgm.mp3')
        url = QtCore.QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()
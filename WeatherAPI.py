# -*- coding:utf-8 -*-

import requests
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'How is the Weather Today ?'
        self.left = 250
        self.top = 150
        self.width = 640
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('C:/Users/ykpcn/Desktop/logo-turkkep-dikey-trans.png'))

        #create menu
        menuBar = QMenuBar(self)
        file = menuBar.addMenu('File')
        edit = menuBar.addMenu('Edit')
        view = menuBar.addMenu('View')
        search = menuBar.addMenu('Search')
        tools= menuBar.addMenu('Tools')
        settings = menuBar.addMenu('Settings')
        help = menuBar.addMenu('Help')
        menuBar.resize(640, 20)

        #Create Label
        Label = QLabel(self)
        Label.setText('City Name: ')
        Label.move(20,60)
        Label.resize(50,30)

        #Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(80,62.5)
        self.textbox.resize(200,25)


        #Create Button
        self.button = QPushButton('Show', self)
        self.button.move(80,100)
        self.button.resize(75,30)

        #Button onclick
        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()

    def on_click(self):
        api_url = "http://api.openweathermap.org/data/2.5/weather?APPID=d1cce1626b42b2d8c5ee5e71c5f687c4&q="
        city = self.textbox.text()
        URL = api_url + city
        json_data = requests.get(URL).json()
        CityName = json_data['name']
        Status = json_data['weather'][0]['main']
        Temperature = json_data['main']['temp']
        Humidity = json_data['main']['humidity']
        WindSpeed = json_data['wind']['speed']
        print("City: ",CityName ,"\nStatus: ", Status, "\nTemperature: ", Temperature, " F\nHumidity: ", Humidity, "%\nWind Speed: ", WindSpeed,"\n\n")



        LabelCity = QLabel(self)
        LabelCity.setText(CityName)
        LabelCity.move(400, 60)
        LabelCity.resize(50, 40)
        LabelCity.show()

        LabelStat = QLabel(self)
        LabelStat.setText(Status)
        LabelStat.move(400, 75)
        LabelStat.resize(50, 40)
        LabelStat.show()

        LabelTemp = QLabel(self)
        LabelTemp.setText(Temperature)
        LabelTemp.move(400, 90)
        LabelTemp.resize(50, 40)
        LabelTemp.show()

        LabelHumi = QLabel(self)
        LabelHumi.setText(Humidity)
        LabelHumi.move(400, 105)
        LabelHumi.resize(50, 40)
        LabelHumi.show()

        LabelWind = QLabel(self)
        LabelWind.setText(WindSpeed)
        LabelWind.move(400, 120)
        LabelWind.resize(50, 40)
        LabelWind.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

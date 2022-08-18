from select import select
import sys
import time
import random
import requests
import datetime as dt
from infor import Ui_infor
from PyQt5.uic import loadUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton, QMenu, QListWidget, QMainWindow
from PyQt5.QtCore import QTimer, QTime, QDateTime, QEvent 

qtCreatorFile = "postulante.ui" # Nombre del archivo aquí.
url1 = 'https://swapi.dev/api/people/'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
lista_pj = []
num_ra = []

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        time = QTimer(self)
        self.setWindowTitle("Postulante para ROBOTILSA S.A")
        time.timeout.connect(self.hour_date)
        time.start(1000)
        self.request_pj.clicked.connect(self.st)
        #self.list_pj.installEventFilter(self)
        
    def hour_date(self):
        ctime = QTime.currentTime()
        time_for = ctime.toString('hh:mm:ss')
        self.clocks.setText(time_for)

        cdate = QDateTime.currentDateTimeUtc()
        date_for = cdate.toString('dd/MM/yyyy') 
        self.date.setText(date_for)
    
    def st(self):
        self.list_pj.clear()
        global lista_pj
        global num_ra
        dic_it = 0
        for i in range (10):
            dic_it += 1
            cf = dic_it
            cff = num_ra.append(cf)
            num = random.randint(1,83)
            url = url1+str(num)
            star_wars = requests.get(url)
            response_js = star_wars.json()
            name = response_js.get('name')
            self.list_pj.addItems([name])
            self.list_pj.installEventFilter(self)
            ad = response_js
            ac = lista_pj.append(ad)     
        #print("*******\n", lista_pj)
        #print(num_ra)
        
    def eventFilter(self, source, event):
        global lista_pj
        if event.type() == QEvent.ContextMenu and source is self.list_pj:
            menu = QMenu()
            aps = menu.addAction('Información del personaje ')
            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                r = random.randint(1,10)
                self.window = QMainWindow()
                self.secui = Ui_infor()
                self.secui.setupUi(self.window)
                self.window.show()
                select = item.text()
                r1 = self.list_pj.currentRow()+1
                for n in lista_pj[:r1]:
                    st = n
                height =  st['height']
                mass = st['mass']
                hair_color = st['hair_color']
                skin_color = st['skin_color']
                eye_color = st['eye_color']
                birth_year = st['birth_year']
                gender = st['gender']
                self.secui.info_pj.addItem('height:         ' + height)
                self.secui.info_pj.addItem('mass:           ' + mass)
                self.secui.info_pj.addItem('hair_color:     ' + hair_color)
                self.secui.info_pj.addItem('skin_color:     ' + skin_color)
                self.secui.info_pj.addItem('eye_color:      ' + eye_color)
                self.secui.info_pj.addItem('birth_year:     ' + birth_year)
                self.secui.info_pj.addItem('gender:         ' + gender)
            return True   
        return super().eventFilter(source, event)
    
    def segunda(self): 
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_infor()
        self.ui.setupUi(self.ventana)
        self.ventana.show()    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
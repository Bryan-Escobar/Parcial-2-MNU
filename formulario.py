# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parcial2fMkYZr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, -1, 1161, 711))
        self.tabBasica = QWidget()
        self.tabBasica.setObjectName(u"tabBasica")
        self.tabWidget_2 = QTabWidget(self.tabBasica)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(-4, -1, 1131, 671))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 140, 51, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_5.setFont(font)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 170, 241, 221))
        self.widget.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.a00 = QLineEdit(self.widget)
        self.a00.setObjectName(u"a00")
        self.a00.setGeometry(QRect(20, 20, 41, 41))
        self.a01 = QLineEdit(self.widget)
        self.a01.setObjectName(u"a01")
        self.a01.setGeometry(QRect(100, 20, 41, 41))
        self.a02 = QLineEdit(self.widget)
        self.a02.setObjectName(u"a02")
        self.a02.setGeometry(QRect(180, 20, 41, 41))
        self.a11 = QLineEdit(self.widget)
        self.a11.setObjectName(u"a11")
        self.a11.setGeometry(QRect(100, 90, 41, 41))
        self.a10 = QLineEdit(self.widget)
        self.a10.setObjectName(u"a10")
        self.a10.setGeometry(QRect(20, 90, 41, 41))
        self.a12 = QLineEdit(self.widget)
        self.a12.setObjectName(u"a12")
        self.a12.setGeometry(QRect(180, 90, 41, 41))
        self.a21 = QLineEdit(self.widget)
        self.a21.setObjectName(u"a21")
        self.a21.setGeometry(QRect(100, 160, 41, 41))
        self.a22 = QLineEdit(self.widget)
        self.a22.setObjectName(u"a22")
        self.a22.setGeometry(QRect(180, 160, 41, 41))
        self.a20 = QLineEdit(self.widget)
        self.a20.setObjectName(u"a20")
        self.a20.setGeometry(QRect(20, 160, 41, 41))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 0, 361, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 140, 51, 31))
        self.label_4.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 440, 91, 31))
        self.label_6.setFont(font)
        self.cbxOperacionBasica = QComboBox(self.tab)
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.setObjectName(u"cbxOperacionBasica")
        self.cbxOperacionBasica.setGeometry(QRect(220, 470, 131, 31))
        self.widget_3 = QWidget(self.tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(490, 170, 241, 221))
        self.widget_3.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.b00 = QLineEdit(self.widget_3)
        self.b00.setObjectName(u"b00")
        self.b00.setGeometry(QRect(20, 20, 41, 41))
        self.b01 = QLineEdit(self.widget_3)
        self.b01.setObjectName(u"b01")
        self.b01.setGeometry(QRect(100, 20, 41, 41))
        self.b02 = QLineEdit(self.widget_3)
        self.b02.setObjectName(u"b02")
        self.b02.setGeometry(QRect(180, 20, 41, 41))
        self.b11 = QLineEdit(self.widget_3)
        self.b11.setObjectName(u"b11")
        self.b11.setGeometry(QRect(100, 90, 41, 41))
        self.b10 = QLineEdit(self.widget_3)
        self.b10.setObjectName(u"b10")
        self.b10.setGeometry(QRect(20, 90, 41, 41))
        self.b12 = QLineEdit(self.widget_3)
        self.b12.setObjectName(u"b12")
        self.b12.setGeometry(QRect(180, 90, 41, 41))
        self.b21 = QLineEdit(self.widget_3)
        self.b21.setObjectName(u"b21")
        self.b21.setGeometry(QRect(100, 160, 41, 41))
        self.b22 = QLineEdit(self.widget_3)
        self.b22.setObjectName(u"b22")
        self.b22.setGeometry(QRect(180, 160, 41, 41))
        self.b20 = QLineEdit(self.widget_3)
        self.b20.setObjectName(u"b20")
        self.b20.setGeometry(QRect(20, 160, 41, 41))
        self.btnCalcularBasica = QPushButton(self.tab)
        self.btnCalcularBasica.setObjectName(u"btnCalcularBasica")
        self.btnCalcularBasica.setGeometry(QRect(510, 450, 141, 81))
        self.btnCalcularBasica.setFlat(False)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 80, 351, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border: 2px solid black;")
        self.dockBasica = QDockWidget(self.tab)
        self.dockBasica.setObjectName(u"dockBasica")
        self.dockBasica.setGeometry(QRect(850, 140, 271, 261))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.widget_4 = QWidget(self.dockWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 241, 221))
        self.widget_4.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.r00 = QLineEdit(self.widget_4)
        self.r00.setObjectName(u"r00")
        self.r00.setGeometry(QRect(20, 20, 41, 41))
        self.r01 = QLineEdit(self.widget_4)
        self.r01.setObjectName(u"r01")
        self.r01.setGeometry(QRect(100, 20, 41, 41))
        self.r02 = QLineEdit(self.widget_4)
        self.r02.setObjectName(u"r02")
        self.r02.setGeometry(QRect(180, 20, 41, 41))
        self.r11 = QLineEdit(self.widget_4)
        self.r11.setObjectName(u"r11")
        self.r11.setGeometry(QRect(100, 90, 41, 41))
        self.r10 = QLineEdit(self.widget_4)
        self.r10.setObjectName(u"r10")
        self.r10.setGeometry(QRect(20, 90, 41, 41))
        self.r12 = QLineEdit(self.widget_4)
        self.r12.setObjectName(u"r12")
        self.r12.setGeometry(QRect(180, 90, 41, 41))
        self.r21 = QLineEdit(self.widget_4)
        self.r21.setObjectName(u"r21")
        self.r21.setGeometry(QRect(100, 160, 41, 41))
        self.r22 = QLineEdit(self.widget_4)
        self.r22.setObjectName(u"r22")
        self.r22.setGeometry(QRect(180, 160, 41, 41))
        self.r20 = QLineEdit(self.widget_4)
        self.r20.setObjectName(u"r20")
        self.r20.setGeometry(QRect(20, 160, 41, 41))
        self.dockBasica.setWidget(self.dockWidgetContents)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(780, 260, 21, 31))
        font2 = QFont()
        font2.setPointSize(45)
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.dockBasica_2 = QDockWidget(self.tab_3)
        self.dockBasica_2.setObjectName(u"dockBasica_2")
        self.dockBasica_2.setGeometry(QRect(600, 160, 271, 261))
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.widget_5 = QWidget(self.dockWidgetContents_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 10, 241, 221))
        self.widget_5.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.j00 = QLineEdit(self.widget_5)
        self.j00.setObjectName(u"j00")
        self.j00.setGeometry(QRect(20, 20, 41, 41))
        self.j01 = QLineEdit(self.widget_5)
        self.j01.setObjectName(u"j01")
        self.j01.setGeometry(QRect(100, 20, 41, 41))
        self.j02 = QLineEdit(self.widget_5)
        self.j02.setObjectName(u"j02")
        self.j02.setGeometry(QRect(180, 20, 41, 41))
        self.j11 = QLineEdit(self.widget_5)
        self.j11.setObjectName(u"j11")
        self.j11.setGeometry(QRect(100, 90, 41, 41))
        self.j10 = QLineEdit(self.widget_5)
        self.j10.setObjectName(u"j10")
        self.j10.setGeometry(QRect(20, 90, 41, 41))
        self.j12 = QLineEdit(self.widget_5)
        self.j12.setObjectName(u"j12")
        self.j12.setGeometry(QRect(180, 90, 41, 41))
        self.j21 = QLineEdit(self.widget_5)
        self.j21.setObjectName(u"j21")
        self.j21.setGeometry(QRect(100, 160, 41, 41))
        self.j22 = QLineEdit(self.widget_5)
        self.j22.setObjectName(u"j22")
        self.j22.setGeometry(QRect(180, 160, 41, 41))
        self.j20 = QLineEdit(self.widget_5)
        self.j20.setObjectName(u"j20")
        self.j20.setGeometry(QRect(20, 160, 41, 41))
        self.dockBasica_2.setWidget(self.dockWidgetContents_2)
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(530, 280, 21, 31))
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(380, 100, 351, 41))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border: 2px solid black;")
        self.btnCalcularInversa = QPushButton(self.tab_3)
        self.btnCalcularInversa.setObjectName(u"btnCalcularInversa")
        self.btnCalcularInversa.setGeometry(QRect(460, 450, 141, 51))
        self.btnCalcularInversa.setFlat(False)
        self.widget_2 = QWidget(self.tab_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(240, 190, 241, 221))
        self.widget_2.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.i00 = QLineEdit(self.widget_2)
        self.i00.setObjectName(u"i00")
        self.i00.setGeometry(QRect(20, 20, 41, 41))
        self.i01 = QLineEdit(self.widget_2)
        self.i01.setObjectName(u"i01")
        self.i01.setGeometry(QRect(100, 20, 41, 41))
        self.i02 = QLineEdit(self.widget_2)
        self.i02.setObjectName(u"i02")
        self.i02.setGeometry(QRect(180, 20, 41, 41))
        self.i11 = QLineEdit(self.widget_2)
        self.i11.setObjectName(u"i11")
        self.i11.setGeometry(QRect(100, 90, 41, 41))
        self.i10 = QLineEdit(self.widget_2)
        self.i10.setObjectName(u"i10")
        self.i10.setGeometry(QRect(20, 90, 41, 41))
        self.i12 = QLineEdit(self.widget_2)
        self.i12.setObjectName(u"i12")
        self.i12.setGeometry(QRect(180, 90, 41, 41))
        self.i21 = QLineEdit(self.widget_2)
        self.i21.setObjectName(u"i21")
        self.i21.setGeometry(QRect(100, 160, 41, 41))
        self.i22 = QLineEdit(self.widget_2)
        self.i22.setObjectName(u"i22")
        self.i22.setGeometry(QRect(180, 160, 41, 41))
        self.i20 = QLineEdit(self.widget_2)
        self.i20.setObjectName(u"i20")
        self.i20.setGeometry(QRect(20, 160, 41, 41))
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 20, 241, 61))
        self.label_2.setFont(font1)
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(340, 160, 51, 31))
        self.label_11.setFont(font)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tabBasica, "")
        self.tabAvanzada = QWidget()
        self.tabAvanzada.setObjectName(u"tabAvanzada")
        self.widget_6 = QWidget(self.tabAvanzada)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(290, 150, 71, 61))
        self.widget_6.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k00 = QLineEdit(self.widget_6)
        self.k00.setObjectName(u"k00")
        self.k00.setGeometry(QRect(10, 10, 51, 41))
        self.widget_7 = QWidget(self.tabAvanzada)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(440, 150, 71, 61))
        self.widget_7.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k01 = QLineEdit(self.widget_7)
        self.k01.setObjectName(u"k01")
        self.k01.setGeometry(QRect(10, 10, 51, 41))
        self.label_3 = QLabel(self.tabAvanzada)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 40, 501, 61))
        self.label_3.setFont(font1)
        self.label_12 = QLabel(self.tabAvanzada)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(370, 150, 61, 61))
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.tabAvanzada)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(520, 150, 61, 61))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.tabAvanzada)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(680, 150, 61, 61))
        self.label_14.setFont(font1)
        self.widget_10 = QWidget(self.tabAvanzada)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(750, 150, 71, 61))
        self.widget_10.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.l00 = QLineEdit(self.widget_10)
        self.l00.setObjectName(u"l00")
        self.l00.setGeometry(QRect(10, 10, 51, 41))
        self.label_15 = QLabel(self.tabAvanzada)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(370, 240, 61, 61))
        self.label_15.setFont(font1)
        self.widget_11 = QWidget(self.tabAvanzada)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(750, 240, 71, 61))
        self.widget_11.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.l10 = QLineEdit(self.widget_11)
        self.l10.setObjectName(u"l10")
        self.l10.setGeometry(QRect(10, 10, 51, 41))
        self.label_16 = QLabel(self.tabAvanzada)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(680, 240, 61, 61))
        self.label_16.setFont(font1)
        self.widget_12 = QWidget(self.tabAvanzada)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(440, 240, 71, 61))
        self.widget_12.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k11 = QLineEdit(self.widget_12)
        self.k11.setObjectName(u"k11")
        self.k11.setGeometry(QRect(10, 10, 51, 41))
        self.widget_13 = QWidget(self.tabAvanzada)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(290, 240, 71, 61))
        self.widget_13.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k10 = QLineEdit(self.widget_13)
        self.k10.setObjectName(u"k10")
        self.k10.setGeometry(QRect(10, 10, 51, 41))
        self.label_17 = QLabel(self.tabAvanzada)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(520, 240, 61, 61))
        self.label_17.setFont(font1)
        self.widget_14 = QWidget(self.tabAvanzada)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(590, 240, 71, 61))
        self.widget_14.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k12 = QLineEdit(self.widget_14)
        self.k12.setObjectName(u"k12")
        self.k12.setGeometry(QRect(10, 10, 51, 41))
        self.label_18 = QLabel(self.tabAvanzada)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(520, 330, 61, 61))
        self.label_18.setFont(font1)
        self.label_19 = QLabel(self.tabAvanzada)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(370, 330, 61, 61))
        self.label_19.setFont(font1)
        self.widget_15 = QWidget(self.tabAvanzada)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(590, 330, 71, 61))
        self.widget_15.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k22 = QLineEdit(self.widget_15)
        self.k22.setObjectName(u"k22")
        self.k22.setGeometry(QRect(10, 10, 51, 41))
        self.widget_16 = QWidget(self.tabAvanzada)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(440, 330, 71, 61))
        self.widget_16.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k21 = QLineEdit(self.widget_16)
        self.k21.setObjectName(u"k21")
        self.k21.setGeometry(QRect(10, 10, 51, 41))
        self.label_20 = QLabel(self.tabAvanzada)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(680, 330, 61, 61))
        self.label_20.setFont(font1)
        self.widget_17 = QWidget(self.tabAvanzada)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(290, 330, 71, 61))
        self.widget_17.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k20 = QLineEdit(self.widget_17)
        self.k20.setObjectName(u"k20")
        self.k20.setGeometry(QRect(10, 10, 51, 41))
        self.widget_18 = QWidget(self.tabAvanzada)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(750, 330, 71, 61))
        self.widget_18.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.l20 = QLineEdit(self.widget_18)
        self.l20.setObjectName(u"l20")
        self.l20.setGeometry(QRect(10, 10, 51, 41))
        self.widget_9 = QWidget(self.tabAvanzada)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(590, 150, 71, 61))
        self.widget_9.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.k02 = QLineEdit(self.widget_9)
        self.k02.setObjectName(u"k02")
        self.k02.setGeometry(QRect(10, 10, 51, 41))
        self.label_21 = QLabel(self.tabAvanzada)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 530, 61, 61))
        self.label_21.setFont(font1)
        self.label_22 = QLabel(self.tabAvanzada)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(630, 530, 61, 61))
        self.label_22.setFont(font1)
        self.widget_19 = QWidget(self.tabAvanzada)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(390, 530, 71, 61))
        self.widget_19.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.xRes = QLineEdit(self.widget_19)
        self.xRes.setObjectName(u"xRes")
        self.xRes.setGeometry(QRect(10, 10, 51, 41))
        self.widget_20 = QWidget(self.tabAvanzada)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(700, 530, 71, 61))
        self.widget_20.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.zRes = QLineEdit(self.widget_20)
        self.zRes.setObjectName(u"zRes")
        self.zRes.setGeometry(QRect(10, 10, 51, 41))
        self.label_23 = QLabel(self.tabAvanzada)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(470, 530, 61, 61))
        self.label_23.setFont(font1)
        self.widget_21 = QWidget(self.tabAvanzada)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setGeometry(QRect(540, 530, 71, 61))
        self.widget_21.setStyleSheet(u" border-radius: 10px;\n"
"    background-color: #E5E5E5;\n"
"    border: 2px solid black;\n"
"    font-weight: normal;\n"
"    color: black;\n"
"    padding: 5px;")
        self.yRes = QLineEdit(self.widget_21)
        self.yRes.setObjectName(u"yRes")
        self.yRes.setGeometry(QRect(10, 10, 51, 41))
        self.btnCalcularLineal = QPushButton(self.tabAvanzada)
        self.btnCalcularLineal.setObjectName(u"btnCalcularLineal")
        self.btnCalcularLineal.setGeometry(QRect(490, 430, 141, 51))
        self.btnCalcularLineal.setFlat(False)
        self.tabWidget.addTab(self.tabAvanzada, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.btnCalcularBasica.setDefault(False)
        self.btnCalcularInversa.setDefault(False)
        self.btnCalcularLineal.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Matriz B", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Operaciones Basicas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matriz A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tipo de operacion", None))
        self.cbxOperacionBasica.setItemText(0, QCoreApplication.translate("MainWindow", u"SUMA", None))
        self.cbxOperacionBasica.setItemText(1, QCoreApplication.translate("MainWindow", u"RESTA", None))
        self.cbxOperacionBasica.setItemText(2, QCoreApplication.translate("MainWindow", u"MULTIPLICACION", None))

        self.btnCalcularBasica.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor de cadaelementos de las matrices A y B\n"
"Las fracciones se deben ingresar como decimal", None))
        self.dockBasica.setWindowTitle(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Basicas", None))
        self.dockBasica_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor de cada elemento de la matrices A \n"
"Las fracciones se deben ingresar como decimal", None))
        self.btnCalcularInversa.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Matriz Inversa", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Matriz A", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Inversa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBasica), QCoreApplication.translate("MainWindow", u"Aritmeticas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Res. Eq Lineales por Matrices", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"X +", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Y +", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Z =", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"X +", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z =", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Y +", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Y +", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X +", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Z =", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X =", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Z =", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Y =", None))
        self.btnCalcularLineal.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAvanzada), QCoreApplication.translate("MainWindow", u"Operaciones Avanzadas", None))
    # retranslateUi


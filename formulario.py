# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parcial2 ui - copiaYnFBjQ.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

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
        self.tabWidget_2.setGeometry(QRect(-4, -1, 981, 671))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(630, 120, 81, 81))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_5.setFont(font)
        self.dockBasica = QDockWidget(self.tab)
        self.dockBasica.setObjectName(u"dockBasica")
        self.dockBasica.setGeometry(QRect(590, 410, 391, 271))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.widget_4 = QWidget(self.dockWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(90, 10, 241, 221))
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
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(160, 170, 241, 221))
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
        self.label.setGeometry(QRect(220, 10, 631, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 120, 81, 81))
        self.label_4.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 400, 131, 81))
        self.label_6.setFont(font)
        self.cbxOperacionBasica = QComboBox(self.tab)
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.addItem("")
        self.cbxOperacionBasica.setObjectName(u"cbxOperacionBasica")
        self.cbxOperacionBasica.setGeometry(QRect(200, 460, 191, 41))
        self.widget_3 = QWidget(self.tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(530, 170, 241, 221))
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
        self.btnCalcularBasica.setGeometry(QRect(450, 430, 141, 81))
        self.btnCalcularBasica.setFlat(False)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 90, 351, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border: 2px solid black;")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tabBasica, "")
        self.tabAvanzada = QWidget()
        self.tabAvanzada.setObjectName(u"tabAvanzada")
        self.tabWidget.addTab(self.tabAvanzada, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1158, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.btnCalcularBasica.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Matriz B", None))
        self.dockBasica.setWindowTitle(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Operaciones Basicas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matriz A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tipo de operacion", None))
        self.cbxOperacionBasica.setItemText(0, QCoreApplication.translate("MainWindow", u"SUMA", None))
        self.cbxOperacionBasica.setItemText(1, QCoreApplication.translate("MainWindow", u"RESTA", None))
        self.cbxOperacionBasica.setItemText(2, QCoreApplication.translate("MainWindow", u"MULTIPLICACION", None))

        self.btnCalcularBasica.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ingrese el valor de cadaelementos de las matrices A y B\n"
"Las fracciones se deben ingresar como decimal", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Basicas", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Inversa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBasica), QCoreApplication.translate("MainWindow", u"Aritmeticas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAvanzada), QCoreApplication.translate("MainWindow", u"Operaciones Avanzadas", None))
    # retranslateUi


from math import sqrt
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
import sys

from PySide6.QtWidgets import QWidget
from formulario import *
from PySide6 import *
from formulario import Ui_MainWindow
#Import para la tabla
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sympy as sp #libreria para derivadas
import math



class ClasePrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dockBasica.hide()
        self.ui.btnCalcularBasica.clicked.connect(self.CalcularBasica)
        
    def CalcularBasica(self):
        a=[]
        b=[]
        res=[]
        '''INICIALIZAR LAS MATRICES'''

        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
        '''Datos ingresado de a y b'''
        a[0][0]=float(self.ui.a00.text())
        a[0][1]=float(self.ui.a01.text())
        a[0][2]=float(self.ui.a02.text())
        
        a[1][0]=float(self.ui.a10.text())
        a[1][1]=float(self.ui.a11.text())
        a[1][2]=float(self.ui.a12.text())
        
        a[2][0]=float(self.ui.a20.text())
        a[2][1]=float(self.ui.a21.text())
        a[2][2]=float(self.ui.a22.text())
        
        self.ui.dockBasica.show()  
                
        tipoOperacion=self.ui.cbxOperacionBasica.currentText()
        if (tipoOperacion=="SUMA"):
            print("Escogió suma ")
            
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myApp=ClasePrincipal()
    myApp.show()
    sys.exit(app.exec())

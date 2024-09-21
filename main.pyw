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
                res.append([0]*3)
        '''Datos ingresado de a y b'''
        '''a[0][0]=float(self.ui.a00.text())
        a[0][1]=float(self.ui.a01.text())
        a[0][2]=float(self.ui.a02.text())
        
        a[1][0]=float(self.ui.a10.text())
        a[1][1]=float(self.ui.a11.text())
        a[1][2]=float(self.ui.a12.text())
        
        a[2][0]=float(self.ui.a20.text())
        a[2][1]=float(self.ui.a21.text())
        a[2][2]=float(self.ui.a22.text())'''
        #obtener valores ingresados
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui,  f'a{i}{j}' ).text())
                b[i][j] = float(getattr(self.ui,  f'b{i}{j}' ).text())
                seleccion=self.ui.cbxOperacionBasica.currentText()
                if seleccion=="SUMA":
                    print("suma")
                    res[i][j]=a[i][j]+b[i][j]
                elif (seleccion=="RESTA"):
                        res[i][j]=a[i][j]-b[i][j]
                        print("resta")
                elif (self.ui.cbxOperacionBasica.currentText=="MULTIPLICACION"):
                        print("multi")
                self.ui.dockBasica.show()  
                getattr(self.ui,f'r{i}{j}').setText(str(res[i][j]))
                #print(str(a[i][j]))

            
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myApp=ClasePrincipal()
    myApp.show()
    sys.exit(app.exec())

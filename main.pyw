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
        self.ui.dockBasica_2.hide()
        self.ui.btnCalcularBasica.clicked.connect(self.CalcularBasica)
        self.ui.btnCalcularInversa.clicked.connect(self.CalcularInversa)
        
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
        '''for i in range(3):
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
                #print(str(a[i][j]))'''
        #lectura de datos
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui,  f'a{i}{j}' ).text())
                b[i][j] = float(getattr(self.ui,  f'b{i}{j}' ).text())
        seleccion=self.ui.cbxOperacionBasica.currentText()
        
        if seleccion=="SUMA":
            print("suma")
            for i in range(3):
                for j in range(3):
                    res[i][j]=a[i][j]+b[i][j]
        elif (seleccion=="RESTA"):
            print("resta")
            for i in range(3):
                for j in range(3):
                    res[i][j]=a[i][j]-b[i][j]
        elif (seleccion=="MULTIPLICACION"):
            print()
            for i in range(3):
                for j in range(3):
                    res[i][j]=round(a[i][0]*b[0][j]+a[i][1]*b[1][j]+a[i][2]*b[2][j],2)
            
        #graficacion de resultados
        for i in range (3):
            for j in range (3):
                self.ui.dockBasica.show()  
                getattr(self.ui,f'r{i}{j}').setText(str(res[i][j]))
                #print(str(a[i][j]))
    
    def CalcularInversa(self):
        a = []
        aCof=[]
        aT = []
        invM = []
        
        #iniclaizar matrices
        for i in range(3):
            for j in range(3):
                aCof.append([0]*3)
                aT.append([0]*3)
                invM.append([0]*3)
                a.append([0]*3)
                
        #obtener valores ingresados
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui,  f'i{i}{j}' ).text())
        
        # #imprimir matriz
        # print('Matriz')
        # for i in range(3):
        #     print('[', end=' ')
        #     for j in range(3):
        #         print(a[i][j], end= '  ')
        #     print(']')
        #     print(' ')
                
        #calcular determinante
        dp=a[0][0]*a[1][1]*a[2][2]+a[1][0]*a[2][1]*a[0][2]+a[2][0]*a[0][1]*a[1][2]
        ds=a[0][2]*a[1][1]*a[2][0]+a[1][2]*a[2][1]*a[0][0]+a[2][2]*a[0][1]*a[1][0]
        det=dp-ds
        
        # print('El determinante es ', det)
        #Generar matriz cofactores = Matriz Menor * Matriz Signos

        aCof[0][0]=a[1][1]*a[2][2]-a[1][2]*a[2][1]
        aCof[0][1]=-(a[1][0]*a[2][2]-a[2][0]*a[1][2])
        aCof[0][2]=a[1][0]*a[2][1]-a[1][1]*a[2][0]

        aCof[1][0]=-(a[0][1]*a[2][2]-a[2][1]*a[0][2])
        aCof[1][1]=a[0][0]*a[2][2]-a[2][0]*a[0][2]
        aCof[1][2]=-(a[0][0]*a[2][1]-a[2][0]*a[0][1])

        aCof[2][0]=a[0][1]*a[1][2]-a[1][1]*a[0][2]
        aCof[2][1]=-(a[0][0]*a[1][2]-a[1][0]*a[0][2])
        aCof[2][2]=a[0][0]*a[1][1]-a[1][0]*a[0][1]
        
        # #Imprimir Matriz cofactores
        # print('Matriz Cofactores: ')
        # for i in range(3):
        #     print('[', end=' ')
        #     for j in range(3):
        #         print(aCof[i][j], end= '  ')
        #     print(']')
        #     print(' ')
        
        #Calcular adjunta transpuesta
        for i in range(3):
            for j in range(3):
                aT[i][j] = aCof[j][i]
                
        #Dividir Cofactores entre Determinante
        for i in range(3):
            for j in range(3):
                invM[i][j] = round(aT[i][j]/det,2)
                
        #graficacion de resultados
        for i in range (3):
            for j in range (3):
                self.ui.dockBasica_2.show()  
                getattr(self.ui,f'j{i}{j}').setText(str(invM[i][j]))
         
                
        # print('Matriz inversa: ')
        # for i in range(3):
        #     print('[', end=' ')
        #     for j in range(3):
        #         print(invM[i][j], end= '  ')
        #     print(']')
        #     print(' ')        
                       

            
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myApp=ClasePrincipal()
    myApp.show()
    sys.exit(app.exec())

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
        self.ui.btnCalcularLineal.clicked.connect(self.CalcularEqLineal)
        
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
                       
    def CalcularEqLineal(self):

        invM = []
        aCof = []
        aT = []
        l = []
        eqLineal = [0] * 3 
                    
        for i in range(3):
            invM.append([0] * 3)
            aCof.append([0] * 3)
            aT.append([0] * 3)
            

        for i in range(3):
            l.append([0] * 1)
                

        for i in range(3):
            for j in range(3):
                invM[i][j] = float(getattr(self.ui,  f'k{i}{j}' ).text())
                    

        for i in range(3):
            l[i][0] = float(getattr(self.ui,  f'l{i}{0}' ).text())
            
        # calcular el determinante
        dp = invM[0][0]*invM[1][1]*invM[2][2] + invM[1][0]*invM[2][1]*invM[0][2] + invM[2][0]*invM[0][1]*invM[1][2]
        ds = invM[0][2]*invM[1][1]*invM[2][0] + invM[1][2]*invM[2][1]*invM[0][0] + invM[2][2]*invM[0][1]*invM[1][0]
        det = dp - ds
            

        if det == 0:
            print("El determinante es cero, no se puede calcular la inversa")
            return

    
        aCof[0][0] = invM[1][1]*invM[2][2] - invM[1][2]*invM[2][1]
        aCof[0][1] = -(invM[1][0]*invM[2][2] - invM[2][0]*invM[1][2])
        aCof[0][2] = invM[1][0]*invM[2][1] - invM[1][1]*invM[2][0]

        aCof[1][0] = -(invM[0][1]*invM[2][2] - invM[2][1]*invM[0][2])
        aCof[1][1] = invM[0][0]*invM[2][2] - invM[2][0]*invM[0][2]
        aCof[1][2] = -(invM[0][0]*invM[2][1] - invM[2][0]*invM[0][1])

        aCof[2][0] = invM[0][1]*invM[1][2] - invM[1][1]*invM[0][2]
        aCof[2][1] = -(invM[0][0]*invM[1][2] - invM[1][0]*invM[0][2])
        aCof[2][2] = invM[0][0]*invM[1][1] - invM[1][0]*invM[0][1]
            
        # Calculate adjoint matrix (transpose of cofactor matrix)
        for i in range(3):
            for j in range(3):
                aT[i][j] = aCof[j][i]
                    
        # Divide adjoint matrix by determinant to get the inverse matrix
        for i in range(3):
            for j in range(3):
                invM[i][j] = round(aT[i][j] / det, 2)
                    
        # Display the inverse matrix in the UI
        for i in range(3):
            for j in range(3):
                self.ui.dockBasica_2.show()
                getattr(self.ui, f'j{i}{j}').setText(str(invM[i][j]))
            
        #impriir matriz inversa
        # print('Matriz inversa:')
        # for i in range(3):
        #     print('[', end=' ')
        #     for j in range(3):
        #         print(invM[i][j], end='  ')
        #     print(']')
        #     print(' ')
            
        #multiplicar la matriz inversa por el vector l
        for i in range(3):
            eqLineal[i] = round(invM[i][0] * l[0][0] + invM[i][1] * l[1][0] + invM[i][2] * l[2][0], 2)
                        

        for i in range(3):
            getattr(self.ui, f'Res{i}{0}').setText(str(eqLineal[i]))
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myApp=ClasePrincipal()
    myApp.show()
    sys.exit(app.exec())

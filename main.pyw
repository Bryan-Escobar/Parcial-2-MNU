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
import numpy as np
import matplotlib.pyplot as plt


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
        self.ui.btnAggPuntos.clicked.connect(self.actualizar_tabla)
        self.ui.btnCalcularRegresionLineal.clicked.connect(self.CalcularRegresionLineal)
        
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
    
    def CalcularRegresionLineal(self):
        # Crear las listas vacías para X e Y
        
        # Listas para almacenar los valores de x, y, x*y, y x^2
        x_values = []  # valores de x
        y_values = []  # valores de y
        xy = []  # valores de x*y
        x2 = []  # valores de x^2
        n = self.ui.tabPuntosRegresion.rowCount()
        
        # Recorrer las filas de la tabla
        for row in range(n):
            try:
                # Obtener los valores de las celdas de la columna 0 (X) y la columna 1 (Y)
                x_item = self.ui.tabPuntosRegresion.item(row, 0)  # Columna X
                y_item = self.ui.tabPuntosRegresion.item(row, 1)  # Columna Y

                if x_item is not None and y_item is not None:
                    # Convertir los textos a float y añadirlos a las listas
                    x = float(x_item.text())
                    y = float(y_item.text())
                    x_values.append(x)
                    y_values.append(y)
                    
            except ValueError:
                # Si alguna celda tiene un valor inválido, podemos ignorarlo o manejar el error
                print(f"Error en la fila {row}: Valores inválidos")

        # Verifica que se hayan ingresado puntos válidos
        if len(x_values) == 0 or len(y_values) == 0:
            print("No se ingresaron suficientes puntos válidos.")
            return
        
        #print(f"Lista X: {x_values}")
        #print(f"Lista Y: {y_values}")
        
        # Calcular los valores de x * y y x^2
        for i in range(len(x_values)):  # Usar la longitud de x_values, no n
            xy.append(x_values[i] * y_values[i])  # x * y
            x2.append(x_values[i] ** 2)    # x^2

        # Sumar las listas para los cálculos
        sumX = sum(x_values)  # Sumatoria de x
        sumY = sum(y_values)  # Sumatoria de y
        sumXY = sum(xy)  # Sumatoria de x * y
        sumX2 = sum(x2)  # Sumatoria de x^2

        
        # Obtener la cantidad de puntos válidos
        n_valid = len(x_values)
        
        # Evitar división por cero (caso en que todos los puntos tengan el mismo valor de X)
        if n_valid * sumX2 - (sumX) ** 2 == 0:
            print("Error: División por cero. Todos los puntos tienen el mismo valor de X.")
            return

        # Cálculo de la pendiente (a) y la intersección (b)
        a = round((n_valid * sumXY - (sumX * sumY)) / (n_valid * sumX2 - (sumX) ** 2), 2)
        #print("a: " + str(a))
        
        b = round(((sumY / n_valid) - a * (sumX / n_valid)), 2)
        #print("b: " + str(b))
        
        # Mostrar la ecuación en un campo de texto
        self.ui.txtFuncionRegresion.setText(f"y = {a}x + {b}")
        
        self.ui.tabPuntosRegresion.setColumnCount(4)
        self.ui.tabPuntosRegresion.setHorizontalHeaderLabels(["X", "Y", "X*Y", "X^2"])
        self.ui.tabPuntosRegresion.setRowCount(n)
        
        for i in range(n):
            self.ui.tabPuntosRegresion.setItem(i, 0, QTableWidgetItem(str(x_values[i])))
            self.ui.tabPuntosRegresion.setItem(i, 1, QTableWidgetItem(str(y_values[i])))
            self.ui.tabPuntosRegresion.setItem(i, 2, QTableWidgetItem(str(xy[i])))
            self.ui.tabPuntosRegresion.setItem(i, 3, QTableWidgetItem(str(x2[i])))      
        # Graficar los puntos y la recta de regresión
        plt.scatter(x_values, y_values, color='blue', label='Puntos ingresados')

        # Generar los valores de Y usando la ecuación de la recta y = ax + b
        x_recta = np.linspace(min(x_values), max(x_values), 100)
        y_recta = a * x_recta + b

        # Graficar la recta de regresión
        plt.plot(x_recta, y_recta, color='red', label=f'Recta de regresión: y = {a}x + {b}')

        # Configurar etiquetas y título
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Puntos y Recta de Regresión')
        plt.legend()

        # Mostrar el gráfico
        plt.show()  
        print("graficando")
            
    def actualizar_tabla(self):
        # Obtener el número de filas desde el QSpinBox
        num_rows = self.ui.sbPuntos.value()

        # Ajustar el número de filas en la tabla
        self.ui.tabPuntosRegresion.setRowCount(num_rows)

        # Opcional: Borrar los contenidos anteriores
        for row in range(num_rows):
            for col in range(2):  # Limpiar las columnas X y Y
                self.ui.tabPuntosRegresion.setItem(row, col, QTableWidgetItem(""))


    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myApp=ClasePrincipal()
    myApp.show()
    sys.exit(app.exec())

# -*- coding: cp1252 -*-
#Vidal Ramos 8-917-97
#Pailiber Smith 8-855-1845
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np # Importamos numpy como el alias np
import scipy as sp# Importamos scipy como el alias sp
from scipy.optimize import curve_fit # Importamos curve_fit de scipy.optimize
import scipy as sp # Importamos scipy como el alias sp
import matplotlib.pyplot as plt # Importamos matplotlib.pyplot como el alias plt.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(140, 0, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Engravers MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.titulo.setFont(font)
        self.titulo.setMouseTracking(False)
        self.titulo.setAutoFillBackground(False)
        self.titulo.setScaledContents(False)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(False)
        self.titulo.setIndent(-1)
        self.titulo.setOpenExternalLinks(False)
        self.titulo.setObjectName("titulo")
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(70, 40, 651, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.foto.setFont(font)
        self.foto.setText("")
        self.foto.setPixmap(QtGui.QPixmap("2.jpg"))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")
        self.pffinal = QtWidgets.QLabel(self.centralwidget)
        self.pffinal.setGeometry(QtCore.QRect(0, 0, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pffinal.setFont(font)
        self.pffinal.setObjectName("pffinal")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(30, 430, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boton1.setFont(font)
        self.boton1.setStyleSheet("background-color: rgb(0, 218, 218);")
        self.boton1.setObjectName("boton1")
        self.boton2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(30, 480, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boton2.setFont(font)
        self.boton2.setAutoFillBackground(False)
        self.boton2.setStyleSheet("background-color: rgb(0, 218, 218);")
        self.boton2.setAutoRepeat(False)
        self.boton2.setObjectName("boton2")
        self.lineEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(70, 350, 111, 21))
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(240, 350, 111, 21))
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditC = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditC.setGeometry(QtCore.QRect(410, 350, 111, 21))
        self.lineEditC.setObjectName("lineEditC")
        self.lineEditD = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditD.setGeometry(QtCore.QRect(590, 350, 113, 20))
        self.lineEditD.setObjectName("lineEditD")
        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setGeometry(QtCore.QRect(30, 350, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelA.setFont(font)
        self.labelA.setObjectName("labelA")
        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setGeometry(QtCore.QRect(200, 350, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelB.setFont(font)
        self.labelB.setMouseTracking(True)
        self.labelB.setObjectName("labelB")
        self.labelC = QtWidgets.QLabel(self.centralwidget)
        self.labelC.setGeometry(QtCore.QRect(370, 350, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelC.setFont(font)
        self.labelC.setObjectName("labelC")
        self.labelC_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelC_2.setGeometry(QtCore.QRect(550, 350, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelC_2.setFont(font)
        self.labelC_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelC_2.setObjectName("labelC_2")
        self.botoninstrucciones = QtWidgets.QPushButton(self.centralwidget)
        self.botoninstrucciones.setGeometry(QtCore.QRect(30, 390, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.botoninstrucciones.setFont(font)
        self.botoninstrucciones.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.botoninstrucciones.setObjectName("botoninstrucciones")
        self.formula = QtWidgets.QLabel(self.centralwidget)
        self.formula.setGeometry(QtCore.QRect(510, 390, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.formula.setFont(font)
        self.formula.setObjectName("formula")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 380, 181, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("formula.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.labelexplica = QtWidgets.QLabel(self.centralwidget)
        self.labelexplica.setGeometry(QtCore.QRect(30, 290, 751, 61))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        self.labelexplica.setFont(font)
        self.labelexplica.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelexplica.setObjectName("labelexplica")
        self.impresion = QtWidgets.QLabel(self.centralwidget)
        self.impresion.setGeometry(QtCore.QRect(290, 430, 511, 151))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.impresion.setFont(font)
        self.impresion.setStyleSheet("background-color: rgb(183, 187, 255);\n"
"gridline-color: rgb(148, 0, 74);\n"
"border-color: rgb(167, 0, 83);")
        self.impresion.setText("")
        self.impresion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.impresion.setObjectName("impresion")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #############
        self.boton1.clicked.connect(self.show_grafica1)
        self.boton2.clicked.connect(self.show_grafica2)
        self.botoninstrucciones.clicked.connect(self.show_popup)#instrucciones

    #
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Previsiones de ventas"))
        self.pffinal.setText(_translate("MainWindow", "Proyecto Final"))
        self.boton1.setText(_translate("MainWindow", "Grafica 1"))
        self.boton2.setText(_translate("MainWindow", "Grafica 2"))
        
        self.lineEditA.setText(_translate("MainWindow", " "))
        self.lineEditB.setText(_translate("MainWindow", " "))
        self.lineEditC.setText(_translate("MainWindow", " "))
        self.lineEditD.setText(_translate("MainWindow", " "))
        
        self.labelA.setText(_translate("MainWindow", "A :"))
        self.labelB.setText(_translate("MainWindow", "B :"))
        self.labelC.setText(_translate("MainWindow", "C :"))
        self.labelC_2.setText(_translate("MainWindow", "D :"))
        self.botoninstrucciones.setText(_translate("MainWindow", "Instrucciones"))
    
        self.formula.setText(_translate("MainWindow", "Ecuacion:"))
        self.labelexplica.setText(_translate("MainWindow", "El Justo y Bueno del Dorado tiene prevista la venta de jamones para el pueblo panameño durante las primeras 5 h desde\n"
"que abren el local la cual esta determinada por la ecuacion que puede observar en la parte inferior.\n"
"La meta es mejorar las venta usando los coeficientes desconocidos (A, B, C, D)"))



#Metodo para el msgbox **************************************************EDITAR AQUI ********************
    def show_popup(self):
        msg=QMessageBox()
        msg.setWindowTitle("Instrucciones")
        msg.setText("1.El cliente debe ingresar los valores de A,B,C,D dicho valores simulan las ventas posibles en esas 5 horas.\n"
        "2.la aplicacion mejorar esos coeficientes hasta tener una mayor productividad de las ventas de los jamones.\n"
        "3.la grafica 1 muestra la variazion estimada\n"
        "4.la grafica 2 muestra el estado fase\n"
        "Nota: los puntos rojos son los valores experimientales y la linea azul el ajuste")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()
        
        
#Metodo para grafica 1
    def show_grafica1(self):
        a1 = float(str(self.lineEditA.text()))
        b1 = float(str(self.lineEditB.text()))
        c1 = float(str(self.lineEditC.text()))
        d1 = float(str(self.lineEditD.text()))
        plt.close(1)
        def mi_funcion(x, a, b, c, d):
            return a*sp.exp(-b*x**2/(2*d**2)) + c * x

            # Añadimos ruido
        x = sp.linspace(0, 5,40)
        y = mi_funcion(x, a1, b1, c1, d1)

        def ruido(x,y,k):
            yn = y + k * sp.random.normal(size = len(x))
            return yn
        coeficientes_optimizados, covarianza_estimada = curve_fit(mi_funcion, x, y)
        self.impresion.setText("Coeficientes Optimizados\n"+str(coeficientes_optimizados)+"\n\nCovarianza estimada:\n"+str(covarianza_estimada))
        results=mi_funcion(x,coeficientes_optimizados[0],coeficientes_optimizados[1],coeficientes_optimizados[2], coeficientes_optimizados[3])
        plt.figure(1)
        plt.plot(x,y,'ro', label = 'Experimental')
        plt.plot(x,results,'b-', label = 'Ajuste')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Ventas del supermercado en pescado x100 ($)')
        plt.title('Grafica de estimacion')
        plt.show(1)


#Metodo para grafica 2
    def show_grafica2(self):
        a1 = float(str(self.lineEditA.text()))
        b1 = float(str(self.lineEditB.text()))
        c1 = float(str(self.lineEditC.text()))
        d1 = float(str(self.lineEditD.text()))
        plt.close(2)
        def mi_funcion(x, a, b, c, d):
            return a*sp.exp(-b*x**2/(2*d**2)) + c * x

            # Añadimos ruido
        x = sp.linspace(0, 5,40)
        y = mi_funcion(x, a1, b1, c1, d1)

        def ruido(x,y,k):
            yn = y + k * sp.random.normal(size = len(x))
            return yn
    
        coeficientes_optimizados, covarianza_estimada = curve_fit(mi_funcion, x, y)
        self.impresion.setText("Coeficientes Optimizados\n"+str(coeficientes_optimizados)+"\n\nCovarianza estimada:\n"+str(covarianza_estimada))
        results=mi_funcion(x,coeficientes_optimizados[0],coeficientes_optimizados[1],coeficientes_optimizados[2], coeficientes_optimizados[3])
        plt.figure(2)
        plt.plot(y,results,'ro')
        plt.xlabel('optimizacion')
        plt.ylabel('producto')
        plt.title('Diagrama de estado fase')
        plt.show(2)
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy, QToolTip, QLabel, QLineEdit
import PyQt5.QtWidgets

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,0,0)
        self.setFixedSize(363,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setWindowTitle('Calculadora')


        self.botao(1, 358, 90, 40, QPushButton('(',self))
        self.botao(90,358, 90, 40, QPushButton('0',self))
        self.botao(180, 358, 90, 40,QPushButton(')',self))
        self.botao(270, 358, 90, 40,QPushButton('=',self),self.igual)

        self.botao(1, 318, 90, 40, QPushButton('1',self))
        self.botao(90, 318, 90, 40, QPushButton('2',self))
        self.botao(180, 318, 90, 40,QPushButton('3',self))
        self.botao(270, 318, 90, 40, QPushButton('+',self))

        self.botao(1, 278, 90, 40, QPushButton('4',self))
        self.botao(90, 278, 90, 40, QPushButton('5',self))
        self.botao(180, 278, 90, 40, QPushButton('6',self))
        self.botao(270, 278, 90, 40, QPushButton('-',self))

        self.botao(1, 238, 90, 40, QPushButton('7',self))
        self.botao(90, 238, 90, 40, QPushButton('8',self))
        self.botao(180, 238, 90, 40, QPushButton('9',self))
        self.botao(270, 238, 90, 40, QPushButton('x',self))

        self.botao(1, 198, 90, 40, QPushButton('.',self))
        self.botao(90, 198, 90, 40, QPushButton('√',self))
        self.botao(180, 198, 90, 40, QPushButton('*²',self))
        self.botao(270, 198, 90, 40, QPushButton('÷',self))

        self.botao(1, 158, 90, 40, QPushButton('%',self))
        self.botao(90, 158, 90, 40, QPushButton('CE',self))
        self.botao(180, 158, 90, 40,QPushButton('C',self), self.limpar)
        self.botao(270, 158, 90, 40, QPushButton('◄',self),self.apagar)
        self.minha_display()
        self.show()
    def botao( self, mx, my, rzx, rzy, bt,func=None):

        bt.resize(rzx, rzy)
        bt.move(mx, my)
        if not func:
           bt.clicked.connect( lambda:self.dsp.setText(
              self.dsp.text() + bt.text()))
        else:
            bt.clicked.connect(func)


    def minha_display(self):
        self.dsp = QLineEdit(self)
        self.dsp.resize(325, 100)
        self.dsp.move(20, 50)
        self.dsp.setDisabled(True)
        self.dsp.setStyleSheet('QLineEdit {  font-size:25px;background:#fff; color:black;}')
    def limpar(self):
        self.dsp.setText('')

    def apagar(self):
        self.dsp.setText(self.dsp.text()[:-1])

    def igual(self):
        aux = str(self.dsp.text())
        cont = 0
        lista = list(aux)
        for i in lista:
            if i == 'x':
                lista[cont]='*'
            if i == '²':
                lista[cont]='*'
            if i == '÷':
                lista[cont]='/'
            if i == '√':
                lista[cont] = '**0.5'
            if i == '%':
                lista[cont] = '/100*'

            cont =  cont + 1
        aux = "".join(lista)

        print(aux)
        try:

            self.dsp.setText(
                str(eval(aux))
            )
        except Exception as e:
            self.dsp.setText('Conta inválida.')




app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())

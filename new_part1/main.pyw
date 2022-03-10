from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt

Form, Window = uic.loadUiType("form.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle(" ")
window.show()

form.lineEdit.setAlignment(Qt.AlignHCenter)
form.lineEdit.setAlignment(Qt.AlignVCenter)
form.lineEdit.setAlignment(Qt.AlignCenter)

reg_ex = QRegExp("[0-9][0-9][0-9]")
validator = QRegExpValidator(reg_ex)
form.lineEdit_2.setValidator(validator)
form.lineEdit_3.setValidator(validator)


form.widget_4.setVisible(True)
form.widget_2.setVisible(False)
form.formula_n.setVisible(False)

form.pushButton.setAutoDefault(True)

#Вычисляющие функции
#Функция для вычисления факториала числа(= количества перестановок без повторений)
def factorial(number):
    factorialNumber = 1
    for i in range(2, number + 1):
        factorialNumber *= i
    return factorialNumber

#Функция для вычисления количества сочетаний без повторений
def combinationNoRepeat(numberN, numberM):
    number = numberN - numberM

    numberN = factorial(numberN)
    numberM = factorial(numberM)
    number = factorial(number)

    numberM *= number
    result = numberN // numberM
    return result

#Функция для вычисления количества размещений с повторениями
def placementWithRepetition(numberN, numberM):
    return numberN**numberM


#Изменение видимости формул в соответствии с выбранным типом комбинаций
def type_changed():
    if (form.comboBox.currentText() == "Сочетания без повторений"):
        form.lineEdit_3.setEnabled(True)
        form.label_11.setEnabled(True)
        form.widget_4.setVisible(True)
        form.widget_2.setVisible(False)
        form.formula_n.setVisible(False)
    if (form.comboBox.currentText() == "Размещения с повторениями"):
        form.lineEdit_3.setEnabled(True)
        form.label_11.setEnabled(True)
        form.widget_2.setVisible(True)
        form.widget_4.setVisible(False)
        form.formula_n.setVisible(False)
    if (form.comboBox.currentText() == "Перестановки без повторений"):
        form.lineEdit_3.setEnabled(False)
        form.label_11.setEnabled(False)
        form.formula_n.setVisible(True)
        form.widget_4.setVisible(False)
        form.widget_2.setVisible(False)

form.comboBox.activated.connect(type_changed)


#Рассчет функции, соответствующей выбранному типу комбинации после нажатия кнопки "Рассчитать"
def on_click():

    if(form.comboBox.currentText() == "Сочетания без повторений" or form.comboBox.currentText() == "Размещения с повторениями"):

        if(form.lineEdit_2.text()=="" or form.lineEdit_3.text()==""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Некорректное значение n и/или m")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            n = int(form.lineEdit_2.text())
            m = int(form.lineEdit_3.text())

            if ( n<= 100 and m<=100 and n>0 and m>0):

                if (form.comboBox.currentText() == "Сочетания без повторений"):
                    form.lineEdit.setPlainText(str(combinationNoRepeat(n, m)))
                elif (form.comboBox.currentText() == "Размещения с повторениями"):
                    form.lineEdit.setPlainText(str(placementWithRepetition(n, m)))

            else:#Вывод сообщения об ошибке
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Некорректное значение n и/или m")
                msg.setWindowTitle("Ошибка")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    else:
        if (form.lineEdit_2.text()!=""):
            n = int(form.lineEdit_2.text())
            if(n>0 and n<=100):
                form.lineEdit.setPlainText(str(factorial(n)))
            else:#Вывод сообщения об ошибке
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Некорректное значение n")
                msg.setWindowTitle("Ошибка")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        else:  # Вывод сообщения об ошибке
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setText("Некорректное значение n")
             msg.setWindowTitle("Ошибка")
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec_()

    return

form.pushButton.clicked.connect(on_click)

app.exec_()

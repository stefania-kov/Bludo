from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from dul import *

app = QtWidgets.QApplication([])
win = uic.loadUi("Blyda.ui")
Gr = Menu()
print("Всего блюд:", len(Gr.menu_dict))  # Выводим количество блюд

def updateTable():
    win.tableWidget.setRowCount(len(Gr.menu_dict))
    row = 0
    for dish in Gr.menu_dict.values():
        win.tableWidget.setItem(row, 0, QTableWidgetItem(dish.name))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(dish.category))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(str(dish.price)))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(dish.weight)))
        # Выравниваем содержимое ячеек по центру
        for col in range(win.tableWidget.columnCount()):
            win.tableWidget.item(row, col).setTextAlignment(Qt.AlignCenter)
        row += 1

def btnLoadTable():
    updateTable()

def btnAppendTable():
    str = win.lineEdit.text()
    Gr.appendDish(str)
    updateTable()  # Обновляем таблицу после добавления
    win.lineEdit.clear()  # Очищаем поле ввода
    



win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendTable)



win.show()
sys.exit(app.exec())


"# Bludo" 

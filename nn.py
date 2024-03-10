from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os

def writeToFile():
    with open("nn.json","w") as file:
        json.dump(notes,file,sort_keys=True)
        
with open("nn.json", "r", encoding='utf8' ) as file:
     notes= json.load(file)
        
app = QApplication([])
window = QWidget()
main_width, main_height = 800,600
    
text_editor= QTextEdit()
text_editor.setStyleSheet('background-color: red')  
text_editor.setPlaceholderText("Введіть теуст ....")

list_widget_1 = QListWidget() 
list_widget_1.setStyleSheet('background-color: blue;')

list_widget_2 = QListWidget() 
list_widget_2.setStyleSheet('background-color: wight;')

text_searcher = QLineEdit
text_searcher.setStyleSheet('background-color: broun;') 
text_searcher.setText("dd")

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег .... ")
input_dialog.setStyleSheet('background-color: green;')

make_note= QPushButton()
make_note.setStyleSheet('background-color: green;')
make_note.setText("Створити замітку")

delete_note= QPushButton()
delete_note.setStyleSheet('background-color: green;')
delete_note.setText("Видалити замітку")

save_note= QPushButton()
save_note.setStyleSheet('background-color: green;')
save_note.setText("Зберегти замітку")

search_for_text =QPushButton()
search_for_text.setStyleSheet('background-color: green;')
search_for_text.setText("Шукати замітку по тексту")
    
add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: broun;')
add_to_note.setText("")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: broun;')
unpin_to_note.asetText("")

action_them_btn = QPushButton()
action_them_btn.setStyleSheet('background-color: bleack;')

export_as_text = QPushButton()
export_as_text.setText("")

row1 = QHBoxLayout()
row1.addWidget(add_to_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список питань"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addLayout(text_searcher)
col2.addWidget(row2)
col2.addWidget(search_for_text)
col2.addWidget(search_for_text)
col2.addWidget(export_as_text)
col2.addWidget(action_them_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)


    
window.setStyleSheet('background-color: yellow; font-size:20px')
window.resize(main_width,main_height)
window.setLayout(layout_note)
window.show
app.exec_()
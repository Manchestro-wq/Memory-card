from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import Qt

window = QWidget()

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')
rb_ans1 = QRadioButton('1')
rb_ans2 = QRadioButton('2')
rb_ans3 = QRadioButton('3')
rb_ans4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)
lb_question = QLabel('Запитання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('Відповідь')
sp_rest = QSpinBox()
qb_question = QGroupBox('Варіант відповідей')

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()
rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
qb_question.setLayout(rb_h1)

qb_answer = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
qb_answer.setLayout(v1)
h1_main = QHBoxLayout()
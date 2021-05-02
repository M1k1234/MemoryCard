#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QRadioButton,QGroupBox,QButtonGroup
from random import shuffle, randint



class Question():
    def __init__(self, question, right_ans, wrg1, wrg2, wrg3):
        self.question = question
        self.right_ans = right_ans
        self.wrg1 = wrg1
        self.wrg2 = wrg2
        self.wrg3 = wrg3

quest_list=[]
quest_list.append(Question('Самый знаменитый русский','Борис','Пушкин','Путин','Ельцин'))
quest_list.append(Question('Кто придумал кириллицу','КиМ','Мефодий','Украиний','Кирилл'))
quest_list.append(Question('Какого народа больше на планете?','толерантного','русского','китайского','беларского'))
quest_list.append(Question('Где находится Урал','Справа от Москвы','В центре России','В посёлке Упорово','В Сколково'))
#quest_list.append('','','','','')


app = QApplication([])
memory = QWidget()
memory.setWindowTitle('Memory Card')
memory.resize(400,200)

vopros1=QLabel('Победитель пришел каким?')
bt_otv=QPushButton('Ответить')

RGB=QGroupBox('Варианты:')

btr1 = QRadioButton('1-м')
btr2 = QRadioButton("2-м")
btr3 = QRadioButton("3-м")
btr4 = QRadioButton("4-м")

RDG=QButtonGroup()
RDG.addButton(btr1)
RDG.addButton(btr2)
RDG.addButton(btr3)
RDG.addButton(btr4)


tst_txt=QLabel("Победитель пришел каким?")
otv_txt=QLabel("у тебя правильно?")
res_txt=QLabel("ответ!")


RGBh_line=QHBoxLayout()

v_line1=QVBoxLayout()
v_line2=QVBoxLayout()

AGBv_line=QVBoxLayout()

v_line1.addWidget(btr1)
v_line1.addWidget(btr2)
v_line2.addWidget(btr3)
v_line2.addWidget(btr4)

RGBh_line.addLayout(v_line1)
RGBh_line.addLayout(v_line2)

RGB.setLayout(RGBh_line)


AGB=QGroupBox("Результат:")
AGB.setLayout(AGBv_line)

h_line1=QHBoxLayout()
h_line2=QHBoxLayout()
h_line3=QHBoxLayout()

h_line4=QHBoxLayout()
h_line5=QHBoxLayout()

h_line1.addWidget(vopros1, alignment=Qt.AlignHCenter)
h_line2.addWidget(RGB, alignment=Qt.AlignHCenter)
h_line2.addWidget(AGB, alignment=Qt.AlignHCenter)
h_line3.addWidget(bt_otv, alignment=Qt.AlignHCenter)

AGBv_line.addWidget(otv_txt,alignment=Qt.AlignLeft)
AGBv_line.addWidget(res_txt,alignment=Qt.AlignHCenter)


v_line3=QVBoxLayout()#главная

v_line3.addLayout(h_line1)
v_line3.addLayout(h_line2,stretch=8)
v_line3.addLayout(h_line3)

memory.setLayout(v_line3)

AGB.hide()


def sres():
    RGB.hide()
    AGB.show()
    bt_otv.setText("Следующий вопрос")

def quest():
    RGB.show()
    AGB.hide()
    bt_otv.setText("Ответить")
    RDG.setExclusive(False)
    btr1.setChecked(False)
    btr2.setChecked(False)
    btr3.setChecked(False)
    btr4.setChecked(False)
    RDG.setExclusive(True)

answs=[btr1, btr2 , btr3, btr4]

def ask(q:Question):
    shuffle(answs)
    answs[0].setText(q.right_ans)
    answs[1].setText(q.wrg1)
    answs[2].setText(q.wrg2)
    answs[3].setText(q.wrg3)
    vopros1.setText(q.question)
    res_txt.setText(q.right_ans)
    quest()


def show_correct(res):
    otv_txt.setText(res)
    sres()

def ch_ans():
    if answs[0].isChecked():
        show_correct("Правильно")
        memory.score += 1
        print('Рейтинг:',(memory.score/memory.total*100),'%')
    else:
        if answs[1].isChecked() or answs[2].isChecked() or answs[3].isChecked():
            show_correct("Неправильно")
            print('Рейтинг:',(memory.score/memory.total*100),'%')

def next_question():
    memory.total += 1
    cur_question=randint(0,len(quest_list)-1)
    q=quest_list[cur_question]
    ask(q)

def OK ():
    if bt_otv.text() == 'Ответить':
        ch_ans()
    else:
        next_question() 



memory.score=0
memory.total=0
bt_otv.clicked.connect(OK)
next_question()
memory.show()
app.exec()

import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        hbox1 = QHBoxLayout()
        nameLabel = QLabel('Name:')
        self.nameLine = QLineEdit('')

        ageLabel = QLabel('Age:')
        self.ageLine = QLineEdit('')

        scoreLabel = QLabel('Score:')
        self.scoreLine = QLineEdit('')

        amountLabel = QLabel('Amount')
        self.amountLine = QLineEdit('')

        keyLabel = QLabel('Key')
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItems(['Name', 'Age', 'Score'])

        hbox1.addWidget(nameLabel)
        hbox1.addWidget(self.nameLine)

        hbox1.addWidget(ageLabel)
        hbox1.addWidget(self.ageLine)

        hbox1.addWidget(scoreLabel)
        hbox1.addWidget(self.scoreLine)

        hbox1.addWidget(amountLabel)
        hbox1.addWidget(self.amountLine)

        hbox1.addWidget(keyLabel)
        hbox1.addWidget(self.keyComboBox)


        hbox2 = QHBoxLayout()
        addButton = QPushButton('Add')
        delButton = QPushButton('Del')
        findButton = QPushButton('Find')
        incButton = QPushButton('Inc')
        showButton = QPushButton('show')
        hbox2.addWidget(addButton)
        hbox2.addWidget(delButton)
        hbox2.addWidget(findButton)
        hbox2.addWidget(incButton)
        hbox2.addWidget(showButton)
        addButton.clicked.connect(self.addScoreDB)
        delButton.clicked.connect(self.delScoreDB)
        findButton.clicked.connect(self.findScoreDB)
        incButton.clicked.connect(self.incScoreDB)
        showButton.clicked.connect(self.showScoreDB)

        hbox3 = QHBoxLayout()
        resultLabel = QLabel('Result:')
        hbox3.addWidget(resultLabel)

        hbox4 = QHBoxLayout()
        self.resultText = QTextEdit('')
        self.resultText.setReadOnly(True)

        hbox4.addWidget(self.resultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)

        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)


        self.setLayout(vbox)
        self.setGeometry(200, 250, 800, 400)
        self.setWindowTitle('ScoreDB')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  pickle.load(fH)
        except:
            self.scoredb = []
            return
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.resultText.clear()
        for p in sorted(self.scoredb, key=lambda person: person[self.keyComboBox.currentText()]):
            temp = ''
            for attr in sorted(p):
                temp += str(attr) + '=' + str(p[attr]) + '\t' + '\t'
            self.resultText.append(temp)

    def addScoreDB(self):
        try:
            record = {'Name':self.nameLine.text(), 'Age':int(self.ageLine.text()), 'Score':int(self.scoreLine.text())}
        except ValueError as e:
            self.resultText.clear()
            self.resultText.append('점수와 나이는 정수만 입력가능!')
            return
        self.scoredb += [record]
        self.showScoreDB()

    def delScoreDB(self):
        temp = True
        while temp:
            temp = False
            for p in self.scoredb:
                if self.nameLine.text() == p['Name']:
                    self.scoredb.remove(p)
                    temp = True
        self.showScoreDB()

    def findScoreDB(self):
        self.resultText.clear()
        for p in self.scoredb:
            if p['Name'] == self.nameLine.text():
                temp = ''
                for attr in sorted(p):
                    temp += str(attr) + '=' + str(p[attr]) + '\t'
                self.resultText.append(temp)

    def incScoreDB(self):
        try:
            int(self.amountLine.text())
        except ValueError as e:
            self.resultText.clear()
            self.resultText.append('숫자만 입력하시오!')
            return
        for p in self.scoredb:
            if p['Name'] == self.nameLine.text():
                p['Score'] += int(self.amountLine.text())
        self.showScoreDB()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = ScoreDB()
    sys.exit(app.exec_())
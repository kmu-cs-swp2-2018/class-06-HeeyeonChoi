from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

# 버튼(버튼이름)으로 하는 생성자 만들기 - 버튼(1) 하면 1을 이름으로 하는 버튼이 생성된다. 
class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons (버튼의 모양과 무늬만, 즉 버튼의 이름과 모양만 생성한 것이다. 기능은 아직 없음 )
        self.digitButton = [x for x in range(0, 10)]
        for i in self.digitButton :
            self.digitButton[i] = Button(str(i), self.buttonClicked)


        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=',self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*',self.buttonClicked)
        self.divButton = Button('/',self.buttonClicked)
        self.addButton = Button('+',self.buttonClicked)
        self.subButton = Button('-',self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(',self.buttonClicked)
        self.rparButton = Button(')',self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C',self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        for i in range(10):
            if i > 0:
                numLayout.addWidget(self.digitButton[i], 2 - ((i - 1) // 3), (i - 1) % 3)

            else:
                numLayout.addWidget(self.digitButton[0], 3, 0)


        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            # 디스플레이 위젯 안에 입력된 값을 실제로 계산하게 해준뒤(eval) 그것을 문자화(str)
            result = str(eval(self.display.text() ))
            # result 변수 스트링 값을 화면안에 나타내줌
            self.display.setText(result)
        elif key == 'C':
            # 지운다는 것은 결국 빈 화면, '' 이걸로 나타낸다는 것.
            self.display.setText('')
        else:
            # 숫자버튼이 눌릴 때 해당숫자를 덧붙여 표시함
            self.display.setText(self.display.text()+key)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


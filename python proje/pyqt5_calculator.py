import sys
from PyQt5 import QtWidgets, QtCore

class CalculatorUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 240, 360)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Ekran (Label)
        self.label = QtWidgets.QLabel("0", self.centralwidget)
        self.label.setGeometry(0, 0, 241, 61)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label.setStyleSheet("font: 16pt Arial; background-color: lightgray; color: black; padding: 10px;")

        # GridLayout
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 60, 240, 300))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını kaldır
        self.gridLayout.setSpacing(1)  # Butonlar arasındaki boşluğu azalt

        # Tuşlar ve stilleri
        buttons = [
            ('C', 0, 0), ('/', 0, 1), ('x', 0, 2), ('Del', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('=', 3, 3, 2, 1),  # '=' butonu 2 satır (row_span=2)
            ('%', 4, 0), ('0', 4, 1), ('.', 4, 2)
        ]

        self.buttons = {}
        for button in buttons:
            text, row, col = button[:3]
            row_span = button[3] if len(button) > 3 else 1
            col_span = button[4] if len(button) > 4 else 1

            btn = QtWidgets.QPushButton(text)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # Butonların esnek olmasını sağla
            btn.setStyleSheet("""
                background-color: rgb(108, 108, 108);
                color: white;
                font: 75 11pt 'Arial';
            """)

            if text == "=":
                btn.setStyleSheet("background-color: rgb(0, 170, 255); font: 75 11pt 'Arial';")

            # Tuşları basıldığında butona_basildi işlevini çağıracak şekilde bağla
            btn.clicked.connect(lambda checked, t=text: self.butona_basildi(t))
            self.gridLayout.addWidget(btn, row, col, row_span, col_span)
            self.buttons[text] = btn

    def butona_basildi(self, deger):
        # Mevcut ekrandaki değeri alın
        mevcut_text = self.label.text()

        # 'C' tuşuna basılırsa ekranı sıfırla
        if deger == 'C':
            self.label.setText("0")
        # 'Del' tuşuna basılırsa son karakteri sil
        elif deger == 'Del':
            self.label.setText(mevcut_text[:-1] or "0")
        # '=' tuşuna basılırsa işlemi değerlendir
        elif deger == '=':
            try:
                if '%' in mevcut_text:
                    parts = mevcut_text.split('%')
                    result = str(float(parts[0]) * float(parts[1]) / 100)
                else:
                    # 'x' yerine '*' ve '÷' yerine '/' koyarak hesaplama yap
                    result = str(eval(mevcut_text.replace('x', '*').replace('÷', '/')))
                self.label.setText(result)
            except Exception as e:
                self.label.setText("Error")
        # '.' tuşuna basılırsa ve ekranda zaten '.' yoksa ekle
        elif deger == '.':
            if '.' not in mevcut_text.split()[-1]:  # Son sayıdaki '.' kontrol et
                self.label.setText(mevcut_text + deger)
        # '%' tuşuna basılırsa ekrana yüzde işaretini ekle
        elif deger == '%':
            self.label.setText(mevcut_text + deger)
        # Herhangi bir diğer tuş basılırsa ekrana ekle
        else:
            if mevcut_text == "0":
                self.label.setText(deger)
            else:
                self.label.setText(mevcut_text + deger)

    def merkezde_yerlestir(self):
        ekran = QtWidgets.QDesktopWidget().screenGeometry()
        pencere = self.geometry()
        x = (ekran.width() - pencere.width()) // 2
        y = (ekran.height() - pencere.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorUI()
    window.merkezde_yerlestir()  
    window.show()
    sys.exit(app.exec_())

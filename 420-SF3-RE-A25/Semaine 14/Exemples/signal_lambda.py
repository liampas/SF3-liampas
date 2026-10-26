from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout


class SignalLambda(QFrame):

    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.bouton = QPushButton("Pesez-moi")
        self.bouton.pressed.connect(lambda: print("bouton pesé"))
        self.bouton.released.connect(self.bouton_released)
        self.bouton.clicked.connect(self.bouton_clicked())
        self.disposition.addWidget(self.bouton)

    def bouton_released(self):
        print("Bouton relâché")

    def bouton_clicked(self):
        return lambda: print("Bouton cliqué")


app = QApplication()
sl = SignalLambda()
sl.show()
app.exec()

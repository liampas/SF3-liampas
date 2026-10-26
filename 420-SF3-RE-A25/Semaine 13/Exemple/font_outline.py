from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QTextEdit, QComboBox, QLabel
from PySide6.QtGui import QFont, QFontDatabase


class FontOutline(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple police avec outline")
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.texte_edit = QTextEdit()
        self.disposition.addWidget(self.texte_edit)

        self.info_police = QLabel()
        self.disposition.addWidget(self.info_police)

        self.combo_polices = QComboBox()
        self.combo_polices.currentIndexChanged.connect(self.mise_a_jour_police)
        self.disposition.addWidget(self.combo_polices)

        # Ajout de polices à partir de fichiers de définition de police
        QFontDatabase.addApplicationFont("./polices/Klarissa.ttf")
        QFontDatabase.addApplicationFont("./polices/KlarissaShadow.ttf")
        QFontDatabase.addApplicationFont("./polices/KlarissaContour.ttf")

        # Ajouter toutes les familles de polices disponibles sur l'appareil
        familles_polices = QFontDatabase.families()
        for i, famille in enumerate(familles_polices):
            police = QFont()
            police.setStyleStrategy(QFont.StyleStrategy.ForceOutline)
            police.setFamily(famille)
            police.setPointSize(16)
            self.combo_polices.addItem(famille, police)
            if self.combo_polices.font().family() == famille:
                self.combo_polices.setCurrentIndex(i)

    def mise_a_jour_police(self, index):
        police: QFont = self.combo_polices.currentData()
        self.texte_edit.setFont(police)



app = QApplication()
fo = FontOutline()
fo.show()
app.exec()

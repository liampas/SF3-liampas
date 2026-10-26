from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu
from PySide6.QtGui import QAction, QIcon


class AboutEx(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple À propos")
        # Si on set un icône pour l'application, la fenêtre à propos va le réutiliser automatiquement
        self.setWindowIcon(QIcon("./images/app.png"))
        self.barre_menu = self.menuBar()
        self.menu_aide = QMenu("Aide")
        self.barre_menu.addMenu(self.menu_aide)
        self.action_a_propos = QAction("À propos")
        self.action_a_propos.triggered.connect(self.ouvrir_a_propos)
        self.menu_aide.addAction(self.action_a_propos)

    def ouvrir_a_propos(self):
        QMessageBox.about(self, "À propos", """
        Mon application
        
        Pier Luc Ducharme
        2025
        """)


app = QApplication()
ae = AboutEx()
ae.show()
app.exec()

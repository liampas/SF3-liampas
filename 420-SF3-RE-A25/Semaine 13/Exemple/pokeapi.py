from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout
import requests


class PokeApi(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon API")

        self.disposition = QVBoxLayout()
        self.textedit_output = QTextEdit()
        self.textedit_output.setReadOnly(True)
        self.disposition.addWidget(self.textedit_output)
        self.setLayout(self.disposition)

        self.disposition_controles = QHBoxLayout()
        self.numero_pokemon_edit = QLineEdit()
        self.disposition_controles.addWidget(self.numero_pokemon_edit)
        self.bouton_submit = QPushButton("Go")
        self.bouton_submit.clicked.connect(self.chercher_pokemon)
        self.disposition_controles.addWidget(self.bouton_submit)
        self.disposition.addLayout(self.disposition_controles)

    def chercher_pokemon(self):
        no_poke = self.numero_pokemon_edit.text()

        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{no_poke}").json()
        self.textedit_output.append(f"Information pour le pokémon no {no_poke}")
        self.textedit_output.append(f"Nom: {data["name"]}")
        slots = data["types"]
        for slot in slots:
            self.textedit_output.append(f"Type: {slot["type"]["name"]}")


app = QApplication()
pa = PokeApi()
pa.show()
app.exec()

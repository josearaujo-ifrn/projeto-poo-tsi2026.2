import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

teste = QLabel("Olá, PySide6!")
teste.show()

app.exec()
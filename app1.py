import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PySide6 no Codespaces")
window.resize(300, 150)

layout = QVBoxLayout()
label = QLabel("Olá do GitHub Codespaces!")
button = QPushButton("Clique Aqui")
button.clicked.connect(lambda: label.setText("PySide6 funcionando!"))

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
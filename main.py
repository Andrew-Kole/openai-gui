from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ChatBot")
        self.setMinimumSize(700, 500)

        # Messages field
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 30)

        # Button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 90, 30)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

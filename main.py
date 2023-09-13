from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
import sys
from ChatbotProcessing import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setWindowTitle("ChatBot")
        self.setMinimumSize(700, 500)

        # Messages field
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 30)
        self.input_field.returnPressed.connect(self.send_message)

        # Button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 90, 30)
        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#33333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background:#E9E9E9'>Bot: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

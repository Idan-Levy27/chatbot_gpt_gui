# Import required modules
import sys
import threading
from PyQt6.QtGui import QIcon
from backend import Chatbot
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication, QMessageBox


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of Chatbot
        self.chatbot = Chatbot()

        # Window settings
        self.setFixedSize(700, 500)
        self.setWindowTitle("Talking With Peter")
        self.setWindowIcon(QIcon("icons/ai.png"))

        # Add chat area field widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 320)
        self.chat_area.setStyleSheet("border-radius : 200; border: 2px solid black")
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 580, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(600, 340, 90, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        # Get the user input
        user_input = self.input_field.text().strip().capitalize()

        # Check if user input is valid
        self.valid_message(user_input)

        # Create a new thread to get the bot response
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        # Generate a response from the Chatbot instance
        response = self.chatbot.get_response(user_input)

        # Update the chat area with the response
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'> Peter: {response}</p>")

    def valid_message(self, user_input):
        # Check if the user input is empty
        if not user_input:
            QMessageBox.information(self, 'Error', 'Please enter a message.')
        else:
            # Update the chat area with the user input
            self.chat_area.append(f"<p style='color:#333333'> Me: {user_input}</p>")

            # Clear the input field
            self.input_field.clear()


# Create the application
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

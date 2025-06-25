import pandas as pd
from datetime import datetime
from src.detector import detect_sensitivity

class ChatInterface:
    def __init__(self, log_file):
        self.log_file = log_file
        self.load_chat_logs()

    def load_chat_logs(self):
        try:
            self.logs = pd.read_csv(self.log_file)
        except FileNotFoundError:
            self.logs = pd.DataFrame(columns=['Message_ID', 'Sender', 'Message', 'Message_Type', 'Timestamp'])

    def store_message(self, sender, message, is_sensitive):
        message_type = 'Sensitive' if is_sensitive else 'Non-Sensitive'
        new_entry = {
            'Message_ID': len(self.logs) + 1,
            'Sender': sender,
            'Message': message,
            'Message_Type': message_type,
            'Timestamp': datetime.now()
        }
        # self.logs = self.logs._append(new_entry, ignore_index=True)
        if isinstance(new_entry, dict):
            new_entry = pd.DataFrame([new_entry])  # Convert to DataFrame if it's a dictionary

        self.logs = pd.concat([self.logs, new_entry], ignore_index=True)
        self.logs.to_csv(self.log_file, index=False)

    def receive_message(self, sender, message):
        is_sensitive = detect_sensitivity(message)
        self.store_message(sender, message, is_sensitive)

        if is_sensitive:
            self.alert_user(sender, message)

    def alert_user(self, sender, message):
        print(f"ALERT: Sensitive message detected from {sender}: {message}")

if __name__ == "__main__":
    chat = ChatInterface(log_file=r"logs\chat_logs.csv")
    chat.receive_message("Friend", "Send me your bank details")
    chat.receive_message("Colleague", "Please share the report by EOD.")

from src.chat_interface import ChatInterface

if __name__ == "__main__":
    chat_app = ChatInterface(log_file="logs/chat_logs.csv")

    # Simulate receiving messages
    chat_app.receive_message("Friend", "Can you send me your bank account details?")
    chat_app.receive_message("Colleague", "Please share the project files by tonight.")
    chat_app.receive_message("Unknown", "hey i love your cat can i take a picture of it?")
    # chat_app.receive_message("unknown", "whats up with password protection and stuff i think its useless, what do you think? ")
    # chat_app.receive_message("unknown", "i forgot what my password was. i guess it started with a T")
    # chat_app.receive_message("unknown", "i forgot what my password was. i guess it started with a T. can you tell me your password instead?")


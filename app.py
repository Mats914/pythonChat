import tkinter as tk
import pymongo
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client["pythonChat"]
messages_collection = db["messages"]

# Create the GUI window
root = tk.Tk()
root.title("Python Chat")
root.geometry("500x500")

# Entry widget to type messages
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

# Function to send message to MongoDB
def send_message():
    if message_entry.get():
        messages_collection.insert_one({"text": message_entry.get()})
        message_entry.delete(0, tk.END)

# Button to trigger sending
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Label to display messages
messages_label = tk.Label(root, text="Messages:", justify="left", anchor="w")
messages_label.pack(pady=10, fill="both", expand=True)

# Function to fetch messages from MongoDB and update the label
def fetch_messages():
    messages = messages_collection.find().sort("_id")
    messages_label.config(
        text="Messages:\n" + "\n".join(f"- {m['text']}" for m in messages)
    )
    root.after(1000, fetch_messages)  # Refresh every second

# Start fetching messages
fetch_messages()

# Run the application
root.mainloop()

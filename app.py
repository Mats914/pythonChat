import tkinter as tk
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pythonChat"]
messages_col = db["messages"]


# GUI
root = tk.Tk()
root.title("pythonChat")
root.geometry("500x500") 

entry=tk.Entry(root, width=50)
entry.pack(pady=10)


def send_message():
    if entry.get():
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)


sen_button = tk.Button(root, text="Send", command=send_message)
sen_button.pack(pady=10)

root.mainloop()
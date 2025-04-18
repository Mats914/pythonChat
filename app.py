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



sen_button = tk.Button(root, text="Send")
sen_button.pack(pady=10)

root.mainloop()
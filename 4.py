 #4. Клиентская часть
#### main.py
import asyncio
import json
import websockets
from gui import start_gui

async def listen(websocket):
    while True:
        message = await websocket.recv()
        data = json.loads(message)
        print(f"Received: {data}")

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await listen(websocket)

if __name__ == "__main__":
    start_gui()
    asyncio.run(main())

#### gui.py
import tkinter as tk

def start_gui():
    root = tk.Tk()
    root.title("Чат")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Введите сообщение:")
    label.pack()

    entry = tk.Entry(frame, width=50)
    entry.pack(pady=5)

    send_button = tk.Button(frame, text="Отправить")
    send_button.pack()

    messages_box = tk.Text(frame, width=50, height=10)
    messages_box.pack(pady=5)

    root.mainloop()
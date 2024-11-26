import tkinter as tk
window = tk.Tk()
window.title("实例")
button = tk.Button(window,text="点击我")
button.pack()
window.geometry("800x600+100+100")
window.mainloop()
import tkinter as tk


class TkinterWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("placeholder")
        self.root.geometry("400x300") # default dimensions

    def run(self):
        self.root.mainloop()

    @staticmethod
    def initAndShowSampleWindow():
        root = tk.Tk()
        sampleWindow = TkinterWindow(root)
        sampleWindow.run()

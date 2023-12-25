import tkinter as tk
import TkinterWindow as TkinterWindowFile

class PHConfigurationAddWindow(TkinterWindowFile.TkinterWindow):
    def __init__(self, root):
        super().__init__(root)

        # changing title name
        self.root.title("pH Add Window")

        # label widget for name
        self.nameLabel = tk.Label(root, text="Name")
        self.nameLabel.pack()
        # entry widget for name
        self.nameEntry = tk.Entry(root, width=30)
        self.nameEntry.pack()
        # label widget for pH Level
        self.pHLevelLabel = tk.Label(root, text="pH Level")
        self.pHLevelLabel.pack()
        # entry widget for pH level
        self.pHLevelEntry = tk.Entry(root, width=30)
        self.pHLevelEntry.pack()
        # button to commit addition
        self.buttonCommit = tk.Button(root, text="Commit", command=lambda: print("Add Configuration"))
        self.buttonCommit.pack()
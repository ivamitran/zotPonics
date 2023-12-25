import TkinterWindow as TkinterWindowFile
import PHConfiguration as PHConfigurationFile
import PHConfigurationAddWindow as PHConfigurationAddWindowFile
import json
import tkinter as tk


def openSecondWindow():
    root2 = tk.Tk()
    pHConfigurationAddWindowInst = PHConfigurationAddWindowFile.PHConfigurationAddWindow(root2)
    pHConfigurationAddWindowInst.run()


class PHConfigurationWindow(TkinterWindowFile.TkinterWindow):
    def __init__(self, root):
        super().__init__(root)
        self.listbox = None
        self.pHConfigurationArrayList = []
        self.pHConfigurationWidgetsArrayList = []

    def parseConfigurationsFromJSONFile(self, filePath):
        with open(filePath, 'r') as file:
            jsonData = json.load(file) # expecting an array of dictionaries
            for dictionary in jsonData:
                currentPHConfiguration = PHConfigurationFile.PHConfiguration(dictionary["name"], dictionary["pHLevel"], 0) # listboxIndex is set to 0 initially when not in listbox yet
                self.pHConfigurationArrayList.append(currentPHConfiguration)

    # packs to the provided root, not necessarily the overall root
    def initListboxForPHConfigurations(self, root):
        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        # init the individual Listbox entries
        listBoxPHConfigurationEntryArrayList = []
        index = 0
        for pHConfiguration in self.pHConfigurationArrayList:
            pHConfiguration.listboxIndex = index
            tmpStrVar = f"name: {pHConfiguration.name} | pH: {pHConfiguration.pHLevel}"
            listBoxPHConfigurationEntryArrayList.append(tmpStrVar)
            index += 1

        for listBoxPHConfigurationEntry in listBoxPHConfigurationEntryArrayList:
            self.listbox.insert(tk.END, listBoxPHConfigurationEntry)

    def setActiveButtonCallback(self):
        # returns tuple of indexes but there should ever be only one index
        curSelectionTuple = self.listbox.curselection()
        curSelection = curSelectionTuple[0]
        for pHConfiguration in self.pHConfigurationArrayList:
            if curSelection == pHConfiguration.listboxIndex:
                print(
                    f"Selected Configuration Name: {pHConfiguration.name}, Selected Configuration pH Level: {pHConfiguration.pHLevel}")
                break

    # the three buttons are add, set, and remove
    def initThreeButtonsHFrameWidget(self, root):
        hFrame = tk.Frame(root)
        hFrame.pack()

        buttonAdd = tk.Button(hFrame, text="Add", command=lambda: openSecondWindow())
        buttonAdd.pack(side=tk.RIGHT)

        buttonSetActive = tk.Button(hFrame, text="Set Active", command=lambda: self.setActiveButtonCallback())
        buttonSetActive.pack(side=tk.RIGHT)

        buttonRemove = tk.Button(hFrame, text="Remove", command=lambda: print("placeholder"))
        buttonRemove.pack(side=tk.RIGHT)

    def initListboxForPHConfigurationsAsRootWidget(self):
        # init the Listbox first
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

        # init the individual Listbox entries
        listBoxPHConfigurationEntryArrayList = []
        index = 0
        for pHConfiguration in self.pHConfigurationArrayList:
            pHConfiguration.listboxIndex = index
            tmpStrVar = f"name: {pHConfiguration.name} | pH: {pHConfiguration.pHLevel}"
            listBoxPHConfigurationEntryArrayList.append(tmpStrVar)
            index += 1

        for listBoxPHConfigurationEntry in listBoxPHConfigurationEntryArrayList:
            self.listbox.insert(tk.END, listBoxPHConfigurationEntry)

    def settingUpDoubleClickFunctionalityForListbox(self):
        self.listbox.bind('<Double-1>', self.handleListboxDoubleClick)

    def handleListboxDoubleClick(self, event):
        # get the cursor selection, returns tuple of indexes but there should ever be only one index
        curSelectionTuple = self.listbox.curselection()
        curSelection = curSelectionTuple[0]
        for pHConfiguration in self.pHConfigurationArrayList:
            if curSelection == pHConfiguration.listboxIndex:
                print(f"Selected Configuration Name: {pHConfiguration.name}, Selected Configuration pH Level: {pHConfiguration.pHLevel}")
                break


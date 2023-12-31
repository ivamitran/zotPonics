import tkinter as tk
import TkinterWindow as TkinterWindowFile
import PHConfigurationWindow as PHConfigurationWindowFile

root = tk.Tk()
instPHConfigurationWindow = PHConfigurationWindowFile.PHConfigurationWindow(root)
instPHConfigurationWindow.parseConfigurationsFromJSONFile("./pHConfigurations.json")
instPHConfigurationWindow.initListboxForPHConfigurations(instPHConfigurationWindow.root)
# instPHConfigurationWindow.settingUpDoubleClickFunctionalityForListbox()
instPHConfigurationWindow.initThreeButtonsHFrameWidget(instPHConfigurationWindow.root)
instPHConfigurationWindow.run()

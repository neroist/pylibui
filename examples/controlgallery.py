"""
 Control Gallery.

"""

from pylibui.core import App
from pylibui.controls import (
    Window, 
    Button, 
    Checkbox,
    Group,
    Entry, 
    Label,
    Form,
    MultilineEntry,
    NonWrappingMultilineEntry,
    SearchEntry,
    PasswordEntry,
    Spinbox,
    Slider,
    ProgressBar, 
    # EditableCombobox
    Combobox,
    RadioButtons,
    DateTimePicker,
    DatePicker,
    TimePicker,
    # FontButton,
    # ColorButton,
    uiAlign, 
    Grid,
    HorizontalSeparator,
    VerticalSeparator,
    HorizontalBox,
    VerticalBox,
    Tab
)

def build_basic_controls_page(self: VerticalBox):
    self.setPadded(True)

    box1 = HorizontalBox()
    box1.setPadded(True)

    box1.append(Button("Button"))
    box1.append(Checkbox("Checkbox"))

    entriesGroup = Group("Entries")
    entriesGroup.setMargined(True)
    
    form = Form()
    form.setPadded(True)

    form.append("Entry", Entry())
    form.append("Search Entry", SearchEntry())
    form.append("Password Entry", PasswordEntry())
    form.append("Multiline Entry", MultilineEntry(), True)
    form.append("Multiline Entry No Wrap", NonWrappingMultilineEntry(), True)
    entriesGroup.setChild(form)

    self.append(box1)
    self.append(Label("This is a label.\nLabels can span multiple lines"))
    self.append(HorizontalSeparator())
    self.append(entriesGroup, True)

def build_numbers_and_lists_page(self: HorizontalBox):
    self.setPadded(True)

    numbersGroup = Group("Numbers")
    numbersGroup.setMargined(True)
    box1 = VerticalBox()
    box1.setPadded(True)

    spinbox = Spinbox(0, 100)
    slider = Slider(0, 100)
    progressBar = ProgressBar()

    def update(_):
        slider.setValue(spinbox.getValue())
        spinbox.setValue(slider.getValue())
        progressBar.setValue(spinbox.getValue())

    spinbox.onChanged = update
    slider.onChanged = update

    indeterminateProgressBar = ProgressBar()
    indeterminateProgressBar.setValue(-1)

    box1.append(spinbox)
    box1.append(slider)
    box1.append(progressBar)
    box1.append(indeterminateProgressBar)

    numbersGroup.setChild(box1)

    # --- lists ---

    listsGroup = Group("Lists")
    listsGroup.setMargined(True)
    box2 = VerticalBox()

    box2.append(
        Combobox([
            "Combobox Item 1", 
            "Combobox Item 2", 
            "Combobox Item 3"
        ])
    )

    # To be wrapped...
    #box2.append(
    #    EditableCombobox([
    #        "Editable Item 1", 
    #        "Editable Item 2", 
    #        "Editable Item 3"
    #    ])
    #)

    box2.append(
        RadioButtons([
            "Radio Button 1",
            "Radio Button 2",
            "Radio Button 3"
        ])
    )

    listsGroup.setChild(box2)

    self.append(numbersGroup, True)
    self.append(listsGroup, True)

def build_data_choosers_page(self: HorizontalBox):
    self.setPadded(True)

    box1 = VerticalBox()
    box1.setPadded(True)
    box1.append(DatePicker())
    box1.append(TimePicker())
    box1.append(DateTimePicker())
    #box1.append(FontButton())
    #box1.append(ColorButton())

    grid1 = Grid()
    grid1.setPadded(True)

    openFileButton = Button("Open File")
    #openFolderButton = Button("Open Folder")
    saveFileButton = Button("Save File")

    openFileEntry = Entry()
    #openFolderEntry = Entry()
    saveFileEntry = Entry()

    openFileEntry.setReadOnly(True)
    #openFolderEntry.setReadOnly(True)
    saveFileEntry.setReadOnly(True)

    openFileButton.onClick = lambda _: openFileEntry.setText(window.openFile())
    #openFolderButton.onClick = lambda _: openFolderEntry.setText(window.openFolder())
    saveFileButton.onClick = lambda _: saveFileEntry.setText(window.saveFile())
    
    grid1.append(openFileButton, 0, 0, 1, 1, False, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)
    grid1.append(openFileEntry, 1, 0, 1, 1, True, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)
    #grid1.append(openFolderButton, 0, 1, 1, 1, False, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)
    #grid1.append(openFolderEntry, 1, 1, 1, 1, True, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)
    grid1.append(saveFileButton, 0, 1, 1, 1, False, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)
    grid1.append(saveFileEntry, 1, 1, 1, 1, True, uiAlign.uiAlignFill, False, uiAlign.uiAlignFill)

    box2 = HorizontalBox()
    box2.setPadded(True)

    msgBoxButton = Button("Message Box")
    msgBoxButton.onClick = lambda _: window.showMessage(
        "This is a normal message box.",
        "More detailed information can be shown here."
    )

    errorBoxButton = Button("Error Box")
    errorBoxButton.onClick = lambda _: window.showError(
        "This message box describes an error.",
        "More detailed information can be shown here."
    )

    box2.append(msgBoxButton, True)
    box2.append(errorBoxButton, True)

    grid1.append(box2, 0, 3, 2, 1, False, uiAlign.uiAlignCenter, False, uiAlign.uiAlignStart)

    self.append(box1)
    self.append(VerticalSeparator())
    self.append(grid1, True)

class MainWindow(Window):
    def __init__(self):
        super().__init__("libui Control Gallery", 640, 480, False)
        self.setMargined(True)

        basic_controls = VerticalBox()
        numbers_and_lists = HorizontalBox()
        data_choosers = HorizontalBox()

        build_basic_controls_page(basic_controls)
        build_numbers_and_lists_page(numbers_and_lists)
        build_data_choosers_page(data_choosers)

        tab = Tab()
        tab.append("Basic Controls", basic_controls)
        tab.append("Numbers and Lists", numbers_and_lists)
        tab.append("Data Choosers", data_choosers)

        tab.setMargined(0, True)
        tab.setMargined(1, True)
        tab.setMargined(2, True)
        
        self.setChild(tab)

    def onClose(self, data):
        super().onClose(data)
        app.stop()

if __name__ == "__main__":
    app = App()

    window = MainWindow()
    window.show()

    app.start()
    app.close()

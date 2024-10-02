import tkinter, os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialfile="/", title='Choose file',
                                          filetypes=(('Text file', '.txt'),
                                                     ('All files', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Provodnik')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='File', height=5, width=20, background='silver')
text.place(x=105, y=80)
button_select = tkinter.Button(window, width=20, height=3,
                               text='Choose file', command=file_select)
button_select.place(x=103, y=170)
window.mainloop()
from tkinter import Tk, Button, Frame

def toggle_button(button):
    if button == yes_button:
        yes_button.config(state='disabled')
        no_button.config(state='normal')
    elif button == no_button:
        no_button.config(state='disabled')
        yes_button.config(state='normal')

root = Tk()
root.title('버튼 윈도우')
root.geometry('300x200')

frame = Frame(root)

yes_button = Button(frame, text='YES', width=10, height=2, command=lambda: toggle_button(yes_button))
yes_button.grid(row=0, column=0)

no_button = Button(frame, text='NO', width=10, height=2, command=lambda: toggle_button(no_button))
no_button.grid(row=0, column=1)
no_button.config(state='disabled')

frame.pack()
root.mainloop()

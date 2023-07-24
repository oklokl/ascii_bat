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
root.geometry('1000x500')  # 창 크기 수정

frame = Frame(root)

yes_button = Button(frame, text='YES', width=70, height=30, command=lambda: toggle_button(yes_button))  # 버튼 크기 수정
yes_button.grid(row=0, column=0)

no_button = Button(frame, text='NO', width=70, height=30, command=lambda: toggle_button(no_button))  # 버튼 크기 수정
no_button.grid(row=0, column=1)
no_button.config(state='disabled')

frame.pack()
root.mainloop()

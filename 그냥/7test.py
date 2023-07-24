import pygame
from tkinter import Tk, Button, Frame, font

def toggle_button(button):
    pygame.mixer.Sound.play(sound)  # 스위치 음 재생
    if button == yes_button:
        yes_button.config(state='disabled', fg='black')
        no_button.config(state='normal', fg='red')
    elif button == no_button:
        no_button.config(state='disabled', fg='black')
        yes_button.config(state='normal', fg='red')

# pygame 초기화 및 음향 효과 파일 로드
pygame.mixer.init()
sound = pygame.mixer.Sound('light-switch-156813.mp3')  # 음향 효과 파일 경로

root = Tk()
root.title('버튼 윈도우')
root.geometry('1000x300')  # 창 크기 변경

frame = Frame(root)

# 폰트 설정 및 텍스트 크기를 변경하려면 font 옵션을 사용합니다.
button_font = font.Font(size=24)

yes_button = Button(frame, text='YES', width=15, height=3, font=button_font, fg='red',
                    command=lambda: toggle_button(yes_button))  # 버튼 크기 수정, 색상 초기값은 빨간색
yes_button.grid(row=0, column=0, padx=(100, 0), pady=(50, 50))  # 패딩 추가

no_button = Button(frame, text='NO', width=15, height=3, font=button_font, fg='black',
                   command=lambda: toggle_button(no_button))  # 버튼 크기 수정, 색상 초기값은 검은색
no_button.grid(row=0, column=1, padx=(100, 0), pady=(50, 50))  # 패딩 추가
no_button.config(state='disabled')

frame.pack()
root.mainloop()

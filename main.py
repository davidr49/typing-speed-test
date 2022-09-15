import tkinter

from text import text_list
from tkinter import *

FONT = 'Courier'
BACKGROUND = '#7FB77E'
FONT_COLOR = '#F7F6DC'
MINUTE = 60

window = Tk()
window.title('Typing Speed Test')
window.config(padx=30, pady=30, bg=BACKGROUND, height=2000, width=650)

sample_text = (" ".join(text_list))

title = Label(window, text='Test How Fast You Can Type!', font=(FONT, 25, 'bold'), bg=BACKGROUND, pady=10)
title.grid(column=0, row=0, columnspan=2)

subtitle_1 = Label(window, text="Click the Start Button When You're Ready", font=(FONT, 20, 'bold'), bg=BACKGROUND,
                   foreground=FONT_COLOR, pady=10)
subtitle_1.grid(row=1, column=0, columnspan=2)
subtitle_2 = Label(window, text=" You Have 60 seconds to Type as Much of the Text as You Can", font=(FONT, 20, 'bold'),
                   bg=BACKGROUND, pady=10)
subtitle_2.grid(row=2, column=0, columnspan=2)
text_window = Text(window, height=12, width=60, wrap=WORD, pady=20, bg=BACKGROUND, highlightthickness=0, borderwidth=0, font=(FONT,10, 'bold'))
text_window.insert(INSERT, sample_text)
text_window.configure(state=DISABLED)
text_window.grid(row=3, column=1, rowspan=4)

type_input = Entry(window, width=30, font=(FONT, 15))
type_input.insert(END, 'Write Text Here')
type_input.grid(column=0, row=4)


def submit():
    type_input.delete(0, tkinter.END)
    type_input.focus_set()
    start_game()
    countdown(MINUTE)
    window.after(1000 * MINUTE, end_game)


def start_game():
    user_type = type_input.get()
    users_input = user_type.split(' ')
    for words in users_input:
        if words in text_list:
            countVar = StringVar()
            pos = text_window.search(words, "1.0", stopindex="end", count=countVar)
            end_point = pos + f"+{countVar.get()}c"
            text_window.tag_configure("search", background="green")
            text_window.tag_add("search", pos, end_point)
        else:
            continue
    window.after(500, start_game)


def countdown(time_left):
    countdown_clock['text'] = time_left
    if time_left > 0:
        window.after(1000, countdown, time_left - 1)
    if time_left < 10:
        countdown_clock.config(foreground='red')
        countdown_clock['text'] = f'0{time_left}'
    if time_left < 1:
        countdown_clock['text'] = "Time's up!"


def end_game():
    type_input.configure(state=DISABLED)
    user_type = type_input.get()
    users_input = user_type.split(' ')
    WPM = 0
    errors = 0
    for words in users_input:
        if words in text_list:
            WPM += 1
        else:
            errors += 1
    show_results(WPM, errors)


def show_results(result, mistakes):
    final_wpm = Label(window, text=f"Typing Speed: {result} Words per Minute", background=BACKGROUND,
                      font=(FONT, 15, 'bold'), foreground=FONT_COLOR, pady=30)
    if result <= 1:
        final_wpm.config(text=f'Typing Speed: {result} Word per Minute')
    final_wpm.grid(column=0, row=7)
    final_errors = Label(window, text=f'Total Errors Made: {mistakes}', background=BACKGROUND, font=(FONT, 15, 'bold'),
                         foreground=FONT_COLOR)
    final_errors.grid(column=1, row=7)


start_button = Button(window, text='Start Game', command=submit)
start_button.grid(column=0, row=5)

countdown_clock = Label(window, bg=BACKGROUND, anchor='center', foreground=FONT_COLOR, font=(FONT, 40, 'bold'))
countdown_clock.grid(column=0, row=6)

window.mainloop()


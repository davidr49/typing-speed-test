from text import text_list, sample_text
from tkinter import *

# user_text = input('Please type the following paragraph').split(' ')
window = Tk()

# def calculate_wpm():
#     global user_text
#     WPM = 0
#     errors = 0
#     for words in user_text:
#         if words in text_list:
#             WPM += 1
#         elif words not in text_list:
#             errors += 1

better_sample = (" ".join(text_list))

text_window = Text(window, height=10, width=99, wrap=WORD)
text_window.insert(INSERT, better_sample)
text_window.configure(state=DISABLED)
text_window.pack()

# countVar = StringVar()
# pos = text_window.search("calculates", "1.0", stopindex="end", count=countVar)
# end_point = pos + f"+{countVar.get()}c"
# text_window.tag_configure("search", background="green")
# text_window.tag_add("search", pos, end_point)

type_input = Entry(window, width=99)
type_input.pack()

game_on = False
type_list = []


# def start_game():
#     global game_on
#     game_on = True
#     while game_on:
#         user_type = type_input.get()
#         type_list.append(user_type.split())


errors = []
def submit():
    global text_list
    user_type = type_input.get()
    type_list.append(user_type.split())
    for words in type_list:
        try:
            countVar = StringVar()
            pos = text_window.search(words, "1.0", stopindex="end", count=countVar)
            end_point = pos + f"+{countVar.get()}c"
            text_window.tag_configure("search", background="green")
            text_window.tag_add("search", pos, end_point)
        except:
            errors.append(words)
            continue



# start_button = Button(window, text='Start Game', command=start_game)
# start_button.pack()

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack()

# print(f'Your words-per-minute = {WPM}')
# print(f'Number of errors = {errors}')

# implement timing device from looking at pomadoro technique code
# another for loop to cover the words as they're typed and matched.
# after the timer is over, use python to hit the enter button
# create a while game on loop that's constantly 'getting' the text being inputted into the text box, and every time it
# matches it creates a new number in wpm
# when the match happens highlight the word in green and maybe delete?
# use the timer as the game_on boolean

window.mainloop()

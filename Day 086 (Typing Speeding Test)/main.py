from tkinter import *
import random
import time
from stopwatch import Stopwatch


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = '#013220'
YELLOW = '#ffd32c'

window = Tk()



def clear_screen():
    #this will remove all widgets from the window
    for widget in window.winfo_children():
        widget.grid_forget()



def timer():
    # Import list of sentences
    from sentences import easy_mode_sentences

    stopwatch = Stopwatch()
    stopwatch.start()

    text_label = Label(text=random.choice(easy_mode_sentences), font=('Arial', 14), bg=GREEN)
    text_label.grid(row=3, column=1, pady=20, padx=20, sticky='ew')

    def stop_timer():
        stopwatch.stop()
        total_time = stopwatch.elapsed
        # Display elapsed time on the screen
        time_label = Label(text=f"Time: {total_time:.2f} seconds", font=('Arial', 14), bg=GREEN)
        time_label.grid(row=4, column=1, pady=20, padx=20, sticky='ew')

    stop_button = Button(text=' STOP ', highlightthickness=0, bg=GREEN, command=stop_timer)
    stop_button.grid(row=0, column=1, pady=20, padx=20)






def easy_clicked():
    clear_screen()

    window.config(bg=GREEN)

    start_button = Button(text='START', highlightthickness=0, bg=GREEN, command=timer)
    start_button.grid(row=0, column=1, pady=20, padx=20)

    text_entry = Entry(width=35)
    text_entry.grid(row=1, column=1, columnspan=2, pady=20, padx=20)



    exit_button = Button(text='EXIT',highlightthickness=0,bg=GREEN,command=mainwindow)
    exit_button.grid(row=2,column=1,pady=20,padx=20,)

    text_label = Label(text="Click the START button to start. "
                            "Type in the word and hit Enter. "
                            "You'll have 90 seconds.",
                       font=('Arial', 14), bg=GREEN)
    text_label.grid(row=3,column=1,pady=20,padx=20,sticky='ew')






def medium_clicked():
    pass


def hard_clicked():
    pass



def mainwindow():
    clear_screen()
    window.title("Typing Speed Test")
    window.minsize(width=500, height=300)
    window.config(padx=50, pady=50, bg=PINK)

    header_label = Label(text='TYPING SPEED TEST', font=('Arial', 18), bg=PINK)
    header_label.grid(column=1, row=0, sticky='ew', padx=20, pady=20)

    select_difficulty_label = Label(text='Select your level to play:', font=('Arial', 14), bg=PINK)
    select_difficulty_label.grid(column=1, row=1, sticky='ew', padx=20, pady=20)

    #buttons
    easy_button = Button(text='Easy', command=easy_clicked, bg=PINK, highlightthickness=0)
    easy_button.grid(column=0, row=2, sticky='ew', padx=20, pady=20)

    medium_button = Button(text='Medium', command=medium_clicked)
    medium_button.grid(column=1, row=2, sticky='ew', padx=20, pady=20)

    hard_button = Button(text='Hard', command=hard_clicked)
    hard_button.grid(column=2, row=2, sticky='ew', padx=20, pady=20)

mainwindow()

window.mainloop()

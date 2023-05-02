import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import webbrowser
from tkcalendar import DateEntry



# phrases to display during the countdown
phrases = [    "Stay focused!",    "You can do it!",    "If not now then when!",    "I love you so much!",    "I'm proud of you bb!",    "Don't give up!",    "You can do it!",    "Time is precious but you are even more precious!",    "Stay motivated!",    "You got this!", "you the most precious!"]

# variable to keep track of whether phrases are on or off
show_phrases = True

# variable to keep track of the timer
timer_id = None

#songs 
youtube_links =["https://www.youtube.com/watch?v=BMuknRb7woc" , "https://www.youtube.com/watch?v=CvFH_6DNRCY" , "https://www.youtube.com/watch?v=y7kvGqiJC4g",
      "https://www.youtube.com/watch?v=dQw4w9WgXcQ" , "https://www.youtube.com/watch?v=jgpJVI3tDbY" , "https://www.youtube.com/watch?v=VB6SIKl8Md0",
      "https://www.youtube.com/watch?v=vwIUJbIU57s", "https://www.youtube.com/watch?v=yBet3jC7Kss", "https://www.youtube.com/watch?v=y1dbbrfekAM"       
]


####################

# function to start the countdown timer
def start_timer():
    global timer_id
    selected_date = datetime.combine(date_entry.get_date(), datetime.min.time())
    if selected_date:
        remaining_time = selected_date - datetime.now()
        if remaining_time.total_seconds() > 0:
            hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            countdown_label.configure(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            timer_id = countdown_label.after(1000, start_timer) # call this function again after 1 second
            # Display a random phrase every 3 seconds
            if show_phrases:
                if int(remaining_time.total_seconds()) % 3 == 0:
                    random_phrase = random.choice(phrases)
                    phrase_label.configure(text=random_phrase)
            else:
                phrase_label.configure(text="")
        else:
            countdown_label.configure(text="Time's up!")
            messagebox.showinfo("Timer", "Time's up!")
    else:
        messagebox.showerror("Error", "Please enter a date")

# function to toggle the phrases on or off
def toggle_phrases():
    global show_phrases
    show_phrases = not show_phrases
    if show_phrases:
        toggle_button.configure(text="I DONT NEED DISTRACTIONS", foreground="red")
    else:
        toggle_button.configure(text="I NEED LOVE AND KISSES", foreground="pink")

# function to stop the timer
def stop_timer():
    global timer_id
    if timer_id is not None:
        countdown_label.after_cancel(timer_id)
        timer_id = None
        countdown_label.configure(text="00:00:00")
        phrase_label.configure(text="")

#takes you to a calm song
def open_youtube():
    random_link = random.choice(youtube_links)
    webbrowser.open(random_link)




####################

# create the GUI
root = tk.Tk()
root.title("Timer")
root.configure(bg='#A2CD5A')

youtube_button = tk.Button(root, text="A song for a princess", command=open_youtube, relief="solid", bg="#6E8B3D", fg="pink")
youtube_button.pack(pady=5)

date_label = tk.Label(root, text="Select a date:", bg="#A2CD5A", fg="#006400")
date_label.pack()

date_entry = DateEntry(root, width=12, background="#006400", foreground="#006400",
                       borderwidth=2, year=datetime.now().year, month=datetime.now().month, 
                       day=datetime.now().day)
date_entry.pack(pady=5)

#start and stop
start_button = tk.Button(root, text="Start", command=start_timer, relief="solid", bg="#6E8B3D", fg="black")
start_button.pack(pady=10, anchor="center")
stop_button = tk.Button(root, text="Stop", command=stop_timer,relief="solid", bg="#6E8B3D", fg="black")
stop_button.pack(pady=0, anchor="center")

countdown_label = tk.Label(root, text="00:00", font=("Helvetica", 20), bg="#556B2F")
countdown_label.pack(pady=10)

phrase_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#556B2F")
phrase_label.pack(pady=5, anchor="center", fill="x")

toggle_button = tk.Button(root, text="I DONT NEED DISTRACTIONS", foreground="black", bg="#6E8B3D",command=toggle_phrases)
toggle_button.pack(pady=5)


root.mainloop()

from tkinter import *

# --- Real Pomodoro Settings ---
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

pomodoro_count = 0  # Kaç Pomodoro tamamlandı

# --- Functions ---
def show_main_menu():
    main_menu_frame.pack(pady=50)
    timer_frame.pack_forget()
    log_frame.pack_forget()

def start_pomodoro():
    global pomodoro_count
    main_menu_frame.pack_forget()
    timer_frame.pack(pady=20)
    log_frame.pack(pady=10)
    start_button.config(state="disabled")
    pomodoro_count = 0
    start_work_session()

def start_work_session():
    global pomodoro_count
    pomodoro_count += 1
    timer_frame.config(bg="#000000")
    timer_label.config(bg="#000000", fg="#ffffff", font=("Arial", 48, "bold"))
    count_down(WORK_MIN * 60, "Work")

def start_break():
    if pomodoro_count % 4 == 0:
        # Long break
        timer_frame.config(bg="#000000")
        timer_label.config(bg="#000000", fg="#ffffff")
        count_down(LONG_BREAK_MIN * 60, "Long Break")
        log_text.insert(END, "⭐ Long break time!\n")
    else:
        # Short break
        timer_frame.config(bg="#000000")
        timer_label.config(bg="#000000", fg="#ffffff")
        count_down(SHORT_BREAK_MIN * 60, "Short Break")
        log_text.insert(END, "☕ Short break time!\n")

def count_down(count, mode):
    minutes = count // 60
    seconds = count % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        root.after(1000, count_down, count-1, mode)
    else:
        if mode == "Work":
            log_text.insert(END, "✅ Work session complete!\n")
            start_break()
        else:
            log_text.insert(END, f"✅ {mode} complete!\n")
            start_work_session()

# --- UI ---
root = Tk()
root.title("Minimal Pomodoro")
root.geometry("500x600")
root.configure(bg="#000000")

# --- Main Menu ---
main_menu_frame = Frame(root, bg="#000000")
Label(main_menu_frame, text="Minimal Pomodoro", font=("Arial", 40, "bold"), fg="#ffffff", bg="#000000").pack(pady=10)
Button(main_menu_frame, text="Start", width=20, bg="#333333", fg="#ffffff", font=("Arial", 16, "bold"), relief="flat", bd=3, pady=10, command=start_pomodoro).pack(pady=5)
Button(main_menu_frame, text="Exit", width=20, bg="#333333", fg="#ffffff", font=("Arial", 16, "bold"), relief="flat", bd=3, pady=10, command=root.destroy).pack(pady=5)

# --- Timer Frame ---
timer_frame = Frame(root, bg="#000000")
timer_label = Label(timer_frame, text=f"{WORK_MIN:02d}:00", font=("Arial", 48, "bold"), bg="#000000", fg="#ffffff")
timer_label.pack(pady=60)

# Start Pomodoro button
start_button = Button(timer_frame, text="Start Pomodoro", bg="#333333", fg="#ffffff", font=("Arial", 16, "bold"), relief="flat", bd=3, pady=10, command=start_pomodoro)
start_button.pack(pady=20)

# --- Log Frame ---
log_frame = Frame(root, bg="#000000")
log_text = Text(log_frame, width=50, height=12, font=("Arial", 12), bg="#000000", fg="#ffffff", insertbackground="white")
log_text.pack(padx=10, pady=10)

# Show main menu initially
show_main_menu()

root.mainloop()

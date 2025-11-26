Minimal Pomodoro Timer  
A clean, minimalist Pomodoro timer built with Python and Tkinter.

This app uses the classic Pomodoro technique:  
- 25-minute focused work sessions  
- 5-minute short breaks  
- A long 30-minute break after every 4 Pomodoros  

The interface is intentionally simple and distraction-free — perfect for studying, coding, or deep-focus work.

---

Features

- 25-minute work sessions  
- Automatically triggered short (5 min) and long (30 min) breaks  
- Breaks scheduled every 4 Pomodoros  
- Activity log showing completed sessions  
- Simple black-and-white minimalist UI  
- Fully automatic cycle: Work → Break → Work → …  
- No external files required  

---

How It Works

- start_pomodoro() begins the full Pomodoro cycle  
- start_work_session() starts a 25-minute focus session  
- start_break() decides whether the break is short or long  
- count_down() updates the timer every second and triggers the next stage  
- A log window records:
  - Work sessions completed  
  - Short breaks  
  - Long breaks  

The cycle loops forever until the app is closed.

---

Code Structure

- WORK_MIN = 25 — work duration  
- SHORT_BREAK_MIN = 5 — short break duration  
- LONG_BREAK_MIN = 30 — long break duration  
- pomodoro_count tracks how many work sessions have been completed  
- All UI elements are created using Tkinter:
  - Main menu frame  
  - Timer frame  
  - Log frame  

---

How to Run

1. Install Python 3  
2. Save the script as minimal_pomodoro.py
3. Run the program:

bash
python minimal_pomodoro.py

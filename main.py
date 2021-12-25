import tkinter as tk
from playsound import playsound

class Application(tk.Frame):

    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.dumplings_on = False
        self.update_time = ''
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.stopwatch_label = tk.Label(self, text='00:00:00', font=('Arial', 80))
        self.stopwatch_label.pack()
        self.start_button = tk.Button(self, text='start', height=5, width=10, font=('Arial', 20), command=self.start)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self, text='pause', height=5, width=10, font=('Arial', 20), command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self, text='reset', height=5, width=10, font=('Arial', 20), command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        self.start_button = tk.Button(self, text='dumplings', height=5, width=10, font=('Arial', 20), command=self.dumplings)
        self.start_button.pack(side=tk.LEFT)
        self.quit_button = tk.Button(self, text='quit', height=5, width=10, font=('Arial', 20), command=self.window.quit)
        self.quit_button.pack(side=tk.LEFT)
        self.window.title('Пельменный таймер')

    def start(self):
        if not self.running and not self.dumplings_on:
            self.stopwatch_label.after(1000)
            self.update()
            self.running = True
        if not self.running and self.dumplings_on:
            self.stopwatch_label.after(1000)
            self.dumplings_update()
            self.dumplings_on = True
            self.running = True


    def pause(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False

    def reset(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
            self.dumplings_on = False
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.stopwatch_label.config(text='00:00:00')

    def dumplings(self):
        self.running = False
        self.dumplings_on = True
        self.hours, self.minutes, self.seconds = 0, 6, 0
        self.stopwatch_label.config(text='00:06:00')

    def update(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        self.output_time()
        self.update_time = self.stopwatch_label.after(1000, self.update)

    def dumplings_update(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.minutes -= 1
            self.seconds = 59
        if self.minutes == -1:
            self.hours -= 1
            self.minutes = 59
        self.output_time()
        if self.minutes == 0 and self.seconds == 0 and self.hours == 0:
            playsound("ringtone.mp3")
        self.update_time = self.stopwatch_label.after(1000, self.dumplings_update)

    def output_time(self):
        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        self.stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)


root = tk.Tk()
app = Application(window=root)
app.mainloop()

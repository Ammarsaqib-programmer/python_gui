import tkinter as tk
import math
import time
import os


class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analog Clock")
        self.geometry("400x450")
        self.resizable(True, True)
        self.center_x = 200
        self.center_y = 200
        self.radius = 180

        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack(expand=True, fill="both")

        self.digital_label = tk.Label(
            self, font=("Arial", 18, "bold"), bg="black", fg="cyan"
        )
        self.digital_label.pack(pady=10)

        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        self.canvas.delete("face")
        # Draw outer circle
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            outline="white",
            width=4,
            tags="face",
        )
        # Draw hour marks and numbers
        for i in range(12):
            angle = math.radians(i * 30 - 60)
            x1 = self.center_x + (self.radius - 20) * math.cos(angle)
            y1 = self.center_y + (self.radius - 20) * math.sin(angle)
            x2 = self.center_x + (self.radius - 5) * math.cos(angle)
            y2 = self.center_y + (self.radius - 5) * math.sin(angle)
            self.canvas.create_line(
                x1, y1, x2, y2, fill="white", width=3, tags="face"
            )
            # Draw numbers
            num_x = self.center_x + (self.radius - 40) * math.cos(angle)
            num_y = self.center_y + (self.radius - 40) * math.sin(angle)
            self.canvas.create_text(
                num_x,
                num_y,
                text=str(i if i != 0 else 12),
                fill="white",
                font=("Arial", 14, "bold"),
                tags="face",
            )

        # Draw minute marks
        for i in range(60):
            if i % 5 != 0:
                angle = math.radians(i * 6 - 60)
                x1 = self.center_x + (self.radius - 15) * math.cos(angle)
                y1 = self.center_y + (self.radius - 15) * math.sin(angle)
                x2 = self.center_x + (self.radius - 5) * math.cos(angle)
                y2 = self.center_y + (self.radius - 5) * math.sin(angle)
                self.canvas.create_line(
                    x1, y1, x2, y2, fill="gray", width=1, tags="face"
                )

    def update_clock(self):
        self.canvas.delete("hands")
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec

        # Calculate angles
        hour_angle = math.radians((hour + minute / 60) * 30 - 90)
        minute_angle = math.radians((minute + second / 60) * 6 - 90)
        second_angle = math.radians(second * 6 - 90)

        # Draw hour hand
        self.draw_hand(hour_angle, self.radius * 0.5, 8, "white")
        # Draw minute hand
        self.draw_hand(minute_angle, self.radius * 0.75, 5, "cyan")
        # Draw second hand
        self.draw_hand(second_angle, self.radius * 0.85, 2, "red")

        # Draw center
        self.canvas.create_oval(
            self.center_x - 8,
            self.center_y - 8,
            self.center_x + 8,
            self.center_y + 8,
            fill="yellow",
            outline="",
            tags="hands",
        )

        # Digital time
        digital_time = time.strftime("%I:%M:%S %p")
        self.digital_label.config(text=digital_time)

        # Redraw face if window resized
        self.after(1000, self.update_clock)

    def draw_hand(self, angle, length, width, color):
        x2 = self.center_x + length * math.cos(angle)
        y2 = self.center_y + length * math.sin(angle)
        self.canvas.create_line(
            self.center_x,
            self.center_y,
            x2,
            y2,
            fill=color,
            width=width,
            capstyle=tk.ROUND,
            tags="hands",
        )


if __name__ == "__main__":
    clock = AnalogClock()
    clock.mainloop()

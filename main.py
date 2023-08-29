from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Calibri"
BURNTUMBER = "#8A3324"
FRENCH_FONT = (FONT_NAME, 40, "italic")
ENGLISH_FONT = (FONT_NAME, 60, "bold")

# ------------------------- UI Set Up -------------------------------------#

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
card_text = canvas.create_text(400, 150, text="test", fill=BURNTUMBER, font=FRENCH_FONT)
canvas.grid(column=0, row=0)



window.mainloop()
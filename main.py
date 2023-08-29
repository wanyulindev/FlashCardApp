from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Calibri"
# BURNTUMBER = "#8A3324"
# CHOCOLATE4 = "#8B4513"
CADETBLUE4 = "#53868B"
# CYAN4 = "#008B8B"
BROWN4 = "#8B2323"
FRENCH_FONT = (FONT_NAME, 50, "italic")
ENGLISH_FONT = (FONT_NAME, 70, "bold")


# ------------------------------------------------------------------------------------------------#




# -----------------------------------------------------------------------------------------------#




# ------------------------- UI Set Up -----------------------------------------------------------#

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
card_french_text = canvas.create_text(400, 150, text="test", fill=CADETBLUE4, font=FRENCH_FONT)
card_english_text = canvas.create_text(400, 263, text="test", fill=BROWN4, font=ENGLISH_FONT)
canvas.grid(column=0, row=0, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR)
wrong = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR)
correct.grid(column=1, row=1)
wrong.grid(column=0, row=1)

window.mainloop()
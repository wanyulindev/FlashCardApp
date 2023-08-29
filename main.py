import random
from tkinter import *
from random import choice
import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Calibri"
# BURNTUMBER = "#8A3324"
# CHOCOLATE4 = "#8B4513"
CADETBLUE4 = "#53868B"
# CYAN4 = "#008B8B"
BROWN4 = "#8B2323"
LANGUAGE_FONT = (FONT_NAME, 50, "italic")
RESULT_FONT = (FONT_NAME, 70, "bold")

FRENCH_FLASH_CARD = ""


# ------------------------- Flash Card Generator --------------------------------------------------------------#

def flash_card_generator():

    global FRENCH_FLASH_CARD
    french = pandas.read_csv("data/french_words.csv")
    # print(french)
    # french_json = french.to_json()
    # print(french_json)
    french_dicts = french.to_dict()
    # print(french_dicts)

    # print(random.choice(french_dicts["French"]))
    FRENCH_FLASH_CARD = random.choice(french_dicts["French"])
    canvas.itemconfig(card_french_text, text=FRENCH_FLASH_CARD)
    # print(FRENCH_FLASH_CARD)


# -----------------------------------------------------------------------------------------------#




# ------------------------- UI Set Up -----------------------------------------------------------#

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
card_french = canvas.create_text(400, 150, text="French", fill=CADETBLUE4, font=LANGUAGE_FONT)
card_french_text = canvas.create_text(400, 263, text="test", fill=BROWN4, font=RESULT_FONT)
canvas.grid(column=0, row=0, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, command=flash_card_generator)
wrong = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=flash_card_generator)
correct.grid(column=1, row=1)
wrong.grid(column=0, row=1)

window.mainloop()
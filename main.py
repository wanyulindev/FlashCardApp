from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Calibri"
# BURNTUMBER = "#8A3324"
# CHOCOLATE4 = "#8B4513"
LIGHTBLUE3 = "#9AC0CD"
# CYAN4 = "#008B8B"
BROWN4 = "#8B2323"
EGGSHELL = "#FCE6C9"
LAVENDERBLUSH2 = "#EEE0E5"

LANGUAGE_FONT = (FONT_NAME, 50, "italic")
RESULT_FONT = (FONT_NAME, 70, "bold")


DATA = pandas.read_csv("data/french_words.csv")

# print(french)
# french_json = french.to_json()
# print(french_json)
# data_dicts = DATA.to_dict()

data_dicts = DATA.to_dict(orient="records")
# print(data_dicts)
#  orient="records" option is used to convert each row in the DataFrame into a dictionary,
#  where the keys of the dictionary are the column names and the values are the corresponding
#  values from the DataFrame row.

# FLASH_CARD = random.choice(data_dicts)
# FRENCH_FLASH_CARD = ""

current_card = {}
current_title_color = ""
current_phrase_color = ""


# ------------------------- Flash Card Generator --------------------------------------------------------------#

def flash_card_generator():

    # global FRENCH_FLASH_CARD
    # print(random.choice(french_dicts["French"]))
    # FRENCH_FLASH_CARD = random.choice(data_dicts["French"])

    global current_card, current_title_color, current_phrase_color
    current_card = random.choice(data_dicts)
    card_french = current_card["French"]

    current_title_color = LIGHTBLUE3
    current_phrase_color = BROWN4
    canvas.itemconfig(card_background, image=card_image)

    # data_dicts -= data_dicts["French"][FRENCH_FLASH_CARD]
    # FRENCH_FLASH_CARD

    # random_french, random_english = data_dicts.popitem()

    canvas.itemconfig(card_french_text, text=card_french, fill=current_phrase_color)
    canvas.itemconfig(card_language, text="French", fill= current_title_color)
    # print(FLASH_CARD)
    # print(data_dicts)
    # print(card_french)

    # timer(3)

    # canvas.itemconfig(card_language, text="English")
    # canvas.itemconfig(FRENCH_FLASH_CARD, text=FRENCH_FLASH_CARD[])

    timer()


# ------------------------------Set Timer ------------------------------------------------------#

def timer():

    window.after(3000, func=flip_cards)

# ------------------------------ Flip Cards ---------------------------------------------------#

def flip_cards():

    global current_phrase_color, current_title_color

    current_title_color = LAVENDERBLUSH2
    current_phrase_color = EGGSHELL
    canvas.itemconfig(card_background, image=flip_image)

    card_english = current_card["English"]
    canvas.itemconfig(card_language, text="English", fill=current_title_color)
    # canvas.itemconfig(current_card["French"], text=current_card["English"])
    canvas.itemconfig(card_french_text, text=card_english, fill=current_phrase_color)


    # print(card_english)


# ------------------------- UI Set Up -----------------------------------------------------------#

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer()

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
flip_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_image)
card_language = canvas.create_text(400, 150, text="", fill=LIGHTBLUE3, font=LANGUAGE_FONT)
card_french_text = canvas.create_text(400, 263, text="", fill=BROWN4, font=RESULT_FONT)
canvas.grid(column=0, row=0, columnspan=2)


correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, command=flash_card_generator)
wrong = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=flash_card_generator)
correct.grid(column=1, row=1)
wrong.grid(column=0, row=1)


flash_card_generator()

window.mainloop()
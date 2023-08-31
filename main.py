from tkinter import *
from tkinter import messagebox
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

# new_data = DATA

# print(french)
# french_json = french.to_json()
# print(french_json)
# data_dicts = DATA.to_dict()

# new_data = DATA.to_dict(orient="list")
# new_data = DATA.to_dict()
# print(data_dicts)
#  orient="records" option is used to convert each row in the DataFrame into a dictionary,
#  where the keys of the dictionary are the column names and the values are the corresponding
#  values from the DataFrame row.

# FLASH_CARD = random.choice(data_dicts)
# FRENCH_FLASH_CARD = ""

# csv_data = pandas.read_csv("data/french_words.csv")

data_dicts = {}

current_card = {}
current_title_color = ""
current_phrase_color = ""
#-------------------------- Resume game or not ----------------------------------------#
def load_data(file_path):
    return pandas.read_csv(file_path)

def resume_checkbox():
    # My code: have "reloading data_dicts" when resuming:
    global data_dicts
    resume_game = messagebox.askyesno(title="Hi there! ", message="Do you want to resume game? ")

    if resume_game:
        try:
            current_data = load_data("data/current_french_words.csv")
            data_dicts = current_data.to_dict(orient="records")
            # print(len(data_dicts))
        except pandas.errors.EmptyDataError:
            messagebox.showinfo(title="Good Job!", message="You have overcome all phrases. "
                                                           "Let's renew game!")
            default_data = load_data("data/french_words.csv")
            data_dicts = default_data.to_dict(orient="records")

    else:
        default_data = load_data("data/french_words.csv")
        data_dicts = default_data.to_dict(orient="records")

# # GPT:
# # import pandas as pd
# #
# # Global variable to hold data_dicts
# data_dicts = []
#
# # Function to load data from a CSV file and convert it to a list of dictionaries
# def load_data(file_path):
#     try:
#         data = pd.read_csv(file_path)
#         return data.to_dict(orient="records")
#     except pd.errors.EmptyDataError:
#         # Handle empty data scenario
#         return []
#     except Exception as e:
#         # Handle other exceptions
#         print("Error:", e)
#         return []
#
# # Initial loading of data during setup
# data_dicts = load_data("data/french_words.csv")
#
# # Function to resume game
# def resume_game():
#     global data_dicts
#     result = messagebox.askyesno(title="Hi there!", message="Do you want to resume the game?")
#
#     if result:
#         if not data_dicts:
#             data_dicts = load_data("data/current_french_words.csv")
#     else:
#         data_dicts = load_data("data/french_words.csv")


#-------------------------- DATA USE from -------------------------------------------------#
# def data_use_from():
#
#         global csv_data
#         csv_data = pandas.read_csv("data/current_french_words.csv")

# ------------------------- Flash Card Generator --------------------------------------------------------------#
def flash_card_generator():

    # global FRENCH_FLASH_CARD
    # print(random.choice(french_dicts["French"]))
    # FRENCH_FLASH_CARD = random.choice(data_dicts["French"])

    global current_card, current_title_color, current_phrase_color, flip_timer
    window.after_cancel(flip_timer)
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

    flip_timer = window.after(3000, func=flip_cards)


# ------------------------------Set Timer ------------------------------------------------------#
# def timer():
#
#    flip_timer = window.after(3000, func=flip_cards)
#
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
#-------------------------- Delete known words from .csv file ----------------------------------#
def known_words():

    # Take off the random generated data out of the .csv file:

    # print(type(data_dicts))
    # Output: List
    data_dicts.remove(current_card)
    # print(len(data_dicts))

    current_data_dicts = pandas.DataFrame(data_dicts)
    # print(current_data_dicts)
    current_data_dicts.to_csv("data/current_french_words.csv", index=False)

    flash_card_generator()



    # print(new_data)
    # # new_data = (new_data[card_french]).remove(card_french)
    # new_data = new_data[["French"][card_french] != card_french]
    # print(new_data)
    # print(f"{card_french}\n{current_card}")

    # data_dicts = data_dicts.remove(current_card)
    # print(data_dicts, current_card)

    # new_data_list = new_data.to_dict()
    # print(new_data_list)
    # new_data = new_data[["French"][card_french] != card_french]
    # new_data.to_csv("new_data.csv", index=False)
    # print(new_data)

# ------------------------- UI Set Up -----------------------------------------------------------#

resume_checkbox()
# resume_game()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#  Instead announce the timer as a function,
#  we set it as a global variable that we could use in other functions.
flip_timer = window.after(3000, func=flip_cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
flip_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_image)
card_language = canvas.create_text(400, 150, text="", fill=LIGHTBLUE3, font=LANGUAGE_FONT)
card_french_text = canvas.create_text(400, 263, text="", fill=BROWN4, font=RESULT_FONT)
canvas.grid(column=0, row=0, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, command=known_words)
wrong = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=flash_card_generator)
correct.grid(column=1, row=1)
wrong.grid(column=0, row=1)

flash_card_generator()

window.mainloop()
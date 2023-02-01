import pytesseract
import pyautogui

with open('pokedex.pickle', 'rb') as file2:
    record = pickle.load(file2)
def read() -> str:
    im1 = pyautogui.screenshot()
    return pytesseract.image_to_string(im1)

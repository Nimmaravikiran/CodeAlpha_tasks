from PIL import Image
from gtts import gTTS
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_sound(path_to_image):
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        return True
    except Exception as bug:
        print("A bug thrown while executing the code\n", bug)
        return

if __name__ == "__main__":
    image_to_sound(r"C:\Users\Ravikiran\Desktop\project\codealpha\image1.jpg")
    input()
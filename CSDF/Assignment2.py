#                               Assignment No. A2
# Implement a program to generate and verify CAPTCHA image.
import random
from captcha.image import ImageCaptcha
import cv2


def checkCaptcha(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False


def generateCaptcha(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    image = ImageCaptcha(width=280, height=90)
    captcha = ""
    while (n):
        captcha += chrs[random.randint(1, 1000) % 62]
        n -= 1
    captcha_image = image.generate(captcha)
    image.write(captcha, 'CAPTCHA.png')
    display_image = cv2.imread("CAPTCHA.png")
    cv2.imshow("", display_image)
    cv2.waitKey(20)
    return captcha


while True:
    captcha = generateCaptcha(4)

    print("Enter the shown above CAPTCHA:")
    usr_captcha = input()

    if (checkCaptcha(captcha, usr_captcha)):
        print("CAPTCHA Matched")
        break
    else:
        print("CAPTCHA Not Matched. Try Again!")
    cv2.destroyAllWindows()

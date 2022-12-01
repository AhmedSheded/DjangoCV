import cv2 as cv


def get_filterd_img(img, action):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    if action == 'NO_FILTER':
        filtered = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    elif action == 'COLORIZED':
        filtered = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    elif action == 'GRAYSCALE':
        filtered = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif action == 'BLURRED':
        width, height = img.shape[:2]
        n = int(0.05 * width)
        k = (n, n)
        blur = cv.blur(img, k)
        filtered = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
    elif action == 'BINARY':
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        _, filtered = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

    elif action == 'INVERT':
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        _, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
        filtered = cv.bitwise_not(binary)

    return filtered
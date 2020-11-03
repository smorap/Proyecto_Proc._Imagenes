import cv2
import numpy as np
import pyautogui
import pytesseract

SCREEN_SIZE = (1360, 768)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 30.0, (SCREEN_SIZE))

if __name__ == '__main__':
    while True:

        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img=out.write(frame)
        image_draw=frame.copy()
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret2, thresh1 = cv2.threshold(img_gray, 200, 250, cv2.THRESH_BINARY)
        edged = cv2.Canny(thresh1, 100, 200)

        contours, hierachy= cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for idx,cont in enumerate(contours):
            area = cv2.contourArea(contours[idx])
            if area > 4000:
                if area < 5050:
                    color = (0, 0, 255)
                    cv2.drawContours(image_draw, contours, idx, color, 1)

        output1 = cv2.resize(image_draw, (900,580))
        cv2.imshow("final", output1)
        output1 = cv2.resize(edged, (900,580))
        cv2.imshow("Contornos", output1)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    out.release()
import cv2
import numpy as np
import pyautogui

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
        edged = cv2.Canny(img_gray, 210, 250)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for idx, cont in enumerate(contours):
            area = cv2.contourArea(contours[idx])
            if area > 25:
                if area < 200:
                    color = (200, 0, 255)
                    cv2.drawContours(image_draw, contours, idx, color, 1)

        output1 = cv2.resize(image_draw, (900,580))
        cv2.imshow("Contornos", output1)

        output2 = cv2.resize(thresh1, (900, 580))
        output3 = cv2.resize(edged, (900, 580))
        cv2.imshow("grises", output3)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    out.release()
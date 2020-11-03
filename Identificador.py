import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

if __name__ == '__main__':
    path = "D:/Datos/sergio/UNIVERSIDAD/2020/Proc_ Imagens/Poryecto/Imagenes_fuente/Foto_5.PNG"


    img = cv2.imread(path)
    image_draw=img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale
    filename1 = 'identificador_grises.jpg'
    cv2.imwrite(filename1, img_gray)
    ret2, thresh1 = cv2.threshold(img_gray, 200, 230, cv2.THRESH_BINARY)
    filename2 = 'identificador_umbral.jpg'
    cv2.imwrite(filename2, thresh1)
    #edged = cv2.Canny(thresh1,100, 150)  # Perform Edge detection
    cv2.imshow('bordes_1',img)
    cv2.waitKey(0)
    cv2.imshow('bordes_1',thresh1)
    cv2.waitKey(0)


    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for idx, i in enumerate(contours):
        area = cv2.contourArea(contours[idx])
        if area > 25:
            if area < 200:
                color = (200, 0, 255)
                cv2.drawContours(image_draw, contours, idx, color, 1)

    custom_config = r'--oem 3 --psm 6'
    final=pytesseract.image_to_string(thresh1 , config=custom_config)

    print(final)
    cv2.imshow('final',image_draw)
    filename3 = 'identificador_contornos.jpg'
    cv2.imwrite(filename3, image_draw)
    cv2.waitKey(0)


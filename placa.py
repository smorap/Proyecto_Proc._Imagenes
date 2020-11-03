import cv2

if __name__ == '__main__':
    path = "D:/Datos/sergio/UNIVERSIDAD/2020/Proc_ Imagens/Poryecto/Imagenes_fuente/Foto_2.PNG"

    img = cv2.imread(path)
    image_draw=img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filename1 = 'placa_grises.jpg'
    cv2.imwrite(filename1, img_gray)

    ret2, thresh1 = cv2.threshold(img_gray, 150, 200, cv2.THRESH_BINARY)
    filename2 = 'placa_umbral.jpg'
    cv2.imwrite(filename2, thresh1)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for idx, cont in enumerate(contours):
        area = cv2.contourArea(contours[idx])
        if area > 4000:
            if area < 5050:
                color = (200, 0, 255)
                cv2.drawContours(image_draw, contours, idx, color, 1)

    cv2.imshow("Image", image_draw)
    filename3 = 'placa_contorno.jpg'
    cv2.imwrite(filename3, image_draw)
    cv2.waitKey(0)
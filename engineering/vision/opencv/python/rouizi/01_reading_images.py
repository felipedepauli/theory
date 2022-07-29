import cv2
import os

path = "engineering/vision/opencv/python/rouizi/"

image = cv2.imread(os.path.join(path, "images/sample.jpg"))

cv2.imshow("Minha Imagem", image)
cv2.imwrite(os.path.join(path, "images/minha_nova_imagem.jpg"), image)

cv2.waitKey(0)


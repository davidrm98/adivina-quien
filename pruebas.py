#mostrar imagen en pantalla cv2 y nampy 
import cv2
import numpy as np

def imprimir_image(path,num):
    img=cv2.imread(path,cv2.IMREAD_UNCHANGED)
    scale_porcent=num
    height=int(img.shape[0]*scale_porcent/100)
    width=int(img.shape[1]*scale_porcent/100)
    dim=(width,height)
    resized=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)

    cv2.imshow('imagen',resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






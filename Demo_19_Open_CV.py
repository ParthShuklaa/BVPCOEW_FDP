import cv2
#Step1: Import

#Step2: Reading an image
My_img = cv2.imread("MyImage.jpeg",cv2.IMREAD_GRAYSCALE)

#Step3 : Rendering Image
cv2.imshow('image',My_img,)
k = cv2.waitKey(0) & 0xFF

#Pressing Esc for closing windows
if k == 27:
    cv2.destroyAllWindows()
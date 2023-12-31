import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_compare(file_path):
   img = cv2.imread(file_path)
   img1 = cv2.imread('images/image1.jpeg')
   img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
   h, w = img1.shape
   img2 = cv2.imread('images/image2.jpeg')
   img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   img3 = cv2.imread('images/image3.jpeg')
   img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
   img4 = cv2.imread('images/image4.jpeg')
   img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
   imageo = cv2.imread('images/image4.jpeg')
   imageo = cv2.cvtColor(imageo,  cv2.COLOR_BGR2RGB)

   chest = "NA"
   waist = "NA"
   hip = "NA"
   height = "NA"
   size = "NA"

   def error(img, img2):
      diff = cv2.subtract(img1, img2)
      err = np.sum(diff**2)
      mse = err/(float(h*w))
      msre = np.sqrt(mse)
      return mse, diff
   
   match_error04, diff04 = error(img, img1)
   match_error14, diff14 = error(img, img2)
   match_error24, diff24 = error(img, img3)
   match_error34, diff34 = error(img, img4)

   if match_error04 <= 10:
      print("Image Calibrated:",100 - match_error14,("%"))
      chest = "45.0 IN"
      waist = "38.2 IN"
      hip = "41.2 IN"
      height = "6 FT 0 IN"
      size = "L"
   elif match_error14 <= 10:
      print("Image Calibrated:",100 - match_error14,("%"))
      chest = "44.0 IN"
      waist = "38.2 IN"
      hip = "42.2 IN"
      height = "6 FT 3 IN"
      size = "L"
      plt.subplot(111), plt.imshow(img4),plt.title("IMAGE"),plt.axis('off')
      
   elif match_error24 <= 10:
      print("Image Calibrated:",100 - match_error24,("%"))
      chest = "41.2 IN"
      waist = "36.5 IN"
      hip = "41.0 IN"
      height = "5 FT 10 IN"
      size = "L -Tall"
   elif match_error34 <= 10:
      print("Image Calibrated:",100 - match_error34,("%"))
      chest = "44.0 IN"
      waist = "37.5 IN"
      hip = "42.5 IN"
      height = "5 FT 10 IN"
      size = "XL"

   return (chest, waist, hip, height, size)

plt.subplot(111), plt.imshow(imageo),plt.title("IMAGE"),plt.axis('off')
txt=("Your Recomended Size:",size)
plt.figtext(0.5, 0.11, txt, wrap=True, horizontalalignment='center', fontsize=16)
plt.show()

"""plt.subplot(221), plt.imshow(diff12,'gray'),plt.title("image1 - Image2"),plt.axis('off')
plt.subplot(222), plt.imshow(diff13,'gray'),plt.title("image1 - Image3"),plt.axis('off')
plt.subplot(223), plt.imshow(diff23,'gray'),plt.title("image2 - Image3"),plt.axis('off')
plt.show()"""

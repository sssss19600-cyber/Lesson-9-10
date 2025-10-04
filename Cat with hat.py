import cv2
from PIL import Image

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image_path = 'cathat.jpg'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat_faces = cat_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

cat = Image.open(image_path).convert("RGBA")
hat = Image.open('hat.png').convert("RGBA")

for (x, y, w, h) in cat_faces:
    new_w = int(w * 1.5)
    new_h = int(h * 1.5)
    resized_hat = hat.resize((new_w, new_h))
    x_offset = x - int((new_w - w) / 2)
    y_offset = int(y + h * -1.3)

    cat.paste(resized_hat, (x_offset, y_offset), resized_hat)

cat.save("cat_with_hat.png")

cat_with_hat = cv2.imread("cat_with_hat.png")
cv2.imshow("Cat with hat", cat_with_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
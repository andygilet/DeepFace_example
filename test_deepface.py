import cv2
from deepface import DeepFace

img = cv2.imread("filepath")
results = DeepFace.analyze(img, actions=("gender", "age", "race", "emotion))

print(results)

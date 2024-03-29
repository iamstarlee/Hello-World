import face_recognition
from PIL import Image
import os

unknown_faces = os.listdir("./data/unknown/")

for image in unknown_faces:
    image_of_people = face_recognition.load_image_file(f"./data/unknown/FeifeiLi.png")
    unknown_face_locations = face_recognition.face_locations(image_of_people)

    for face_location in unknown_face_locations:
        top, right, bottom, left = face_location

        face_image = image_of_people[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(f"./data/extract/{image}_{top}.jpg")
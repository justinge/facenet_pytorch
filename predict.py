from PIL import Image

from facenet import Facenet

if __name__ == "__main__":
    model = Facenet()
    # image_1 = "img/1_001.jpg"
    # image_1 = Image.open(image_1)
    # image_2 = "img/1_002.jpg"
    # image_2 = Image.open(image_2)
    # probability = model.detect_image(image_1,image_2)
    # probability = model.save_to_tensor()
    probability = model.get_from_face_collection()
    print(probability)

    

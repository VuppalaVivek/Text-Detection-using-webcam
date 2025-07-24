import cv2
from PIL import Image
from pytesseract import pytesseract

def capture_image():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        cv2.imshow('Text detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            image_path = r"C:\Users\yendl\Pictures\Letter-of-Appointment.jpg"
            cv2.imwrite(image_path, frame)
            break
    camera.release()
    cv2.destroyAllWindows()
    return image_path

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    processed_image_path = r"C:\Users\yendl\Pictures\Processed-Letter-of-Appointment.jpg"
    cv2.imwrite(processed_image_path, binary_image)
    return processed_image_path

def tesseract(image_path):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)

# Capture the image from the webcam
image_path = capture_image()

# Preprocess the captured image
processed_image_path = preprocess_image(image_path)

# Perform OCR on the preprocessed image
tesseract(processed_image_path)

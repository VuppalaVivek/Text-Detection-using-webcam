# Text-Detection-using-webcam
Text Detection using OpenCV and Tesseract OCR
Text Detection using OpenCV and Tesseract OCR

This project demonstrates a simple *OCR (Optical Character Recognition)* pipeline using a webcam. The system captures a real-time image, processes it to enhance readability, and extracts the text content using the Tesseract OCR engine.

 Project Aim

To detect and extract text from images captured using a webcam by applying image preprocessing techniques and performing OCR using the Tesseract engine

 Features

- Real-time image capture from webcam.
- Automatic conversion of image to grayscale and binary.
- Integration with Tesseract OCR for text extraction.
- Keyboard-based control (s to save & OCR, q to quit).

 Technologies Used

- Python
- OpenCV (cv2)
- Pillow (PIL)
- Tesseract OCR (pytesseract)

 How It Works

1. Capture Image
   The webcam feed opens and displays live video.  
   Press s to capture the image and proceed.

2. Preprocess Image 
   The captured image is converted to grayscale and then binarized to improve OCR performance.

3. Extract Text
   The preprocessed image is passed to Tesseract, and the extracted text is printed to the console.

 Setup Instructions

1. Install Python libraries:
   bash
   pip install opencv-python pillow pytesseract

from PIL import Image, ImageEnhance
import pytesseract


new_width = 5000
new_height = 450


def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((new_width, new_height))
    img = img.convert("L")  # Convert to grayscale

    # Apply contrast enhancement (optional)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)

    return img


def extract_text_from_image(image_path):
    # Preprocess the image
    preprocessed_img = preprocess_image(image_path)

    # Use pytesseract to extract text from the ROI
    extracted_text = pytesseract.image_to_string(preprocessed_img, lang="eng")

    return extracted_text

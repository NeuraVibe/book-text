import os
import fitz  # PyMuPDF
from googletrans import Translator
import re

# Function to clean up text (remove extra lines and spaces)
def clean_text(text):
    """
    This function removes extra spaces, handles paragraph breaks, and cleans up unwanted line breaks.
    It also ensures that code, URLs, and other special blocks are handled correctly.
    """
    # 1. Remove multiple spaces between words
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 2. Add newlines after sentences (periods, exclamation points, question marks)
    text = re.sub(r'([.!?])\s*(?=[A-Za-z])', r'\1\n', text)
    
    # 3. Handle specific cases like code blocks or paths that should not have paragraph breaks
    text = re.sub(r'(http[s]?://\S+|www\.\S+|file://\S+)', r'\1', text)
    
    # Prevent adding newlines in code-like sections (detected by starting with "<" or something similar)
    text = re.sub(r'(<.*?>)', r'\1', text)  # Handle HTML-like tags
    
    # 4. Separate blocks of text with an extra newline
    text = re.sub(r'([a-zA-Z0-9])([A-Z])', r'\1\n\2', text)  # Adding newline before capital letters
    
    return text

# Function to save text to a file
def save_text(page_num, text, folder_path):
    """
    Save the cleaned text to a file within a folder corresponding to the page number.
    """
    page_folder = os.path.join(folder_path, f"Page_{page_num}")
    os.makedirs(page_folder, exist_ok=True)
    with open(os.path.join(page_folder, "page_text.txt"), 'w', encoding='utf-8') as file:
        file.write(text)

# Function to extract and process page
def process_page(page, page_num, translate=False, translator=None, folder_path=None, doc=None):
    """
    Extract and process the content of a single page, including extracting text, cleaning it, 
    translating it (if necessary), and saving any images on the page.
    """
    # Extract text from the page
    text = page.get_text("text")
    cleaned_text = clean_text(text)

    # Check for images
    image_paths = []
    for img in page.get_images(full=True):
        xref = img[0]
        base_image = fitz.Pixmap(doc, xref)
        
        # Ensure the folder for saving the image exists
        page_folder = os.path.join(folder_path, f"Page_{page_num}")
        os.makedirs(page_folder, exist_ok=True)

        image_path = os.path.join(page_folder, f"image_{xref}.png")
        
        # Save the image using save method
        if base_image.n < 5:  # if the image is RGB or grayscale
            base_image.save(image_path)
        else:  # if the image is CMYK or other color space, convert it to RGB first
            rgb_image = fitz.Pixmap(fitz.csRGB, base_image)
            rgb_image.save(image_path)
            rgb_image = None  # Free memory

        image_paths.append(image_path)

    # Translate text if needed
    if translate:
        try:
            translated_text = translator.translate(cleaned_text, src='en', dest='fa').text
            cleaned_text = clean_text(translated_text)
        except Exception as e:
            print(f"Error during translation: {e}")
            cleaned_text = cleaned_text  # Fallback to original text in case of error

    # Save text and images in the folder
    save_text(page_num, cleaned_text, folder_path)

    # If there are images, add them as "IMAGE" in the text file
    for image_path in image_paths:
        with open(os.path.join(folder_path, f"Page_{page_num}", "page_text.txt"), 'a', encoding='utf-8') as file:
            file.write(f"\nIMAGE: {image_path}")

# Main program function
def main():
    """
    Main function to handle the PDF processing, including user inputs for file paths, translation, 
    and saving the processed content to folders.
    """
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Colored print statements for better readability and user interaction
    print("\033[1;32mInitializing PDF processing tool...\033[0m")
    print("\033[1;34mPlease provide the path to your PDF book file.\033[0m")
    
    # Get the path to the PDF file
    pdf_path = input("\033[1;33mEnter the path of the PDF file: \033[0m").strip()
    doc = fitz.open(pdf_path)

    # Get information from the user
    folder_name = input("\033[1;33mEnter the main folder name: \033[0m").strip()
    folder_path = input("\033[1;33mEnter the path where the folder should be saved: \033[0m").strip()

    # Create the main folder
    main_folder = os.path.join(folder_path, folder_name)
    os.makedirs(main_folder, exist_ok=True)

    # Ask the user if translation is needed
    translate = input("\033[1;33mDo you want the pages to be translated to Persian? (y/n): \033[0m").strip().lower() == 'y'

    # Initialize translator if needed
    if translate:
        translator = Translator()

    # Process each page
    for page_num in range(len(doc)):
        print(f"\033[1;36mProcessing page {page_num + 1} of {len(doc)}...\033[0m")
        page = doc.load_page(page_num)
        process_page(page, page_num + 1, translate=translate, translator=translator, folder_path=main_folder, doc=doc)

    print("\033[1;32mOperation completed successfully!\033[0m")

if __name__ == "__main__":
    main()

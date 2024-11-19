
# 📘 PDF Processing Tool

This Python tool allows you to extract text and images from PDF files, clean the extracted text, and optionally translate it into Persian. It's a versatile and user-friendly solution for organizing and processing PDF documents efficiently. 🚀

---

## ⚡ Features
- **Text Extraction**: Extracts text from PDF pages and cleans it for better readability.
- **Image Extraction**: Identifies and saves images from each PDF page in structured folders.
- **Translation Support**: Translates text to Persian using Google Translate.
- **Organized Output**: Creates a folder for each page containing its text and images.
- **Smart Cleaning**: Handles special cases like URLs, code blocks, and file paths to avoid formatting issues.

---

## 🛠 Installation

### Prerequisites
Ensure you have **Python 3.7** or later installed.

### Install Required Libraries
Use the following command to install the required Python libraries:

```bash
pip install pymupdf googletrans==4.0.0-rc1
```

---

## 🚀 How to Use

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/NeuraVibe/book-text
   ```

2. Run the tool:
   ```bash
   cd book-text
   ```
   
3. Run the tool:
   ```bash
   cd source
   ```
   
4. Run the tool:
   ```bash
   python3 main.py
   ```

5. Follow the on-screen prompts:
   - Enter the path to your PDF file.
   - Provide a name for the main output folder.
   - Specify the location where the folder should be saved.
   - Choose whether to translate text into Persian (`y` for Yes, `n` for No).

---

## 📂 Output Structure

After processing, the tool organizes the output into structured folders. Each page of the PDF gets its folder, containing the extracted text and any images found on the page. Here's an example:

```
Output_Folder/
├── Page_1/
│   ├── page_text.txt
│   └── image_1.png
├── Page_2/
│   ├── page_text.txt
│   ├── image_2.png
│   └── image_3.png
...
```

### Description:
- **`page_text.txt`**: Contains the cleaned and optionally translated text for that page.
- **`image_x.png`**: Images extracted from the respective PDF page.

---

## 🤲 Support Me

This project was created with love and effort. If you want to support me personally, you can:

- Share this repository with others who may find it useful.
- Provide feedback or suggest improvements.
- Contact me for collaboration or projects.

Thank you for your kindness and support! ❤️

---

## 🔗 Connect with Me
- **GitHub**: [@NeuraVibe](https://github.com/NeuraVibe)
- **Twitter**: [@DrNeuraVibe](https://twitter.com/DrNeuraVibe)
- **Email**: DrNeuraVibe@gmail.com

---

Enjoy using the **PDF Processing Tool**! 🎉

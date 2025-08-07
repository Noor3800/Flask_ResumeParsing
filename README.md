# 📄 Flask Resume Parser

A simple web app built with Flask that allows users to upload a PDF resume and automatically extracts structured information like name, email, phone number, address, education, experience, and skills using python and basic NLP techniques.

---

## 📁 Project Structure

```
├── app.py           # Main Flask server
├── cv_parser.py     # Resume text parser and extractor
├── index.html       # HTML frontend for upload and output
├── uploads/         # Stores uploaded resumes
├── cv_data.json     # Parsed output stored as JSON
└── noor.pdf         # Sample PDF resume

```

## ▶ How to Run

1. Make sure **Python 3.x** is installed.

2. Install the required packages:
   ```bash
   pip install flask
   pip install PyPDF2

   ```
3. Run the Flask app:
  - first run this on command prompt: \Flask\env\Scripts\Activate.ps1
  - then run the app as follows:

    ```bash
    python app.py
    
    ```
4. Open your browser and visit:
   
   ```bash
    http://127.0.0.1:5000/
    
    ```
5. Upload a PDF resume and view the extracted details.

---

## 📷 Screenshots

![GUI Screenshot](screenshot.png)

**GUI Example:**

→ Upload PDF → Parse → View Information

---

## 🧠 Skills Practiced

- Web development using Flask  
- File handling & upload  
- Text extraction from PDFs  
- Regex for pattern matching  
- JSON parsing  
- Building user-friendly interfaces with HTML & Jinja2

---

## 📌 Technologies Used

- Python  
- Flask  
- PyPDF2  
- HTML / Jinja2  
- Regex  
- JSON

---

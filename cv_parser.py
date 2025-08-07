import PyPDF2
import re
import json

# Step 1: Read PDF Text
def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else ""


def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-\(\)]{9,}', text)
    return match.group() if match else ""


def extract_name(text):
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line:  # skip empty lines
            return line   #returning first non-empty line as name
    return ""


def extract_section(text, keywords):
    lines = text.split('\n')
    return [line.strip() for line in lines if any(k.lower() in line.lower() for k in keywords)]




def extract_address(text):
    cities = ['lahore', 'karachi', 'islamabad', 'rawalpindi', 'multan', 'pakistan']
    for city in cities:
        if city in text.lower():
            return city.title()
    return "Address not found"



# Step 3: Save as JSON
def parse_resume_to_json(pdf_path, json_path):
    text = extract_text(pdf_path)
    data = {
        "personal_info": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "address": extract_address(text) 
        },
        "education": extract_section(text, ["bachelor", "intermediate", "matric", "university", "school", "cgpa"]),
        "experience": extract_section(text, ["experience", "tutored", "collaboration", "worked"]),
        "skills": extract_section(text, ["skills", "programming", "tools", "soft skills"])
    }

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

# Run the function
#parse_resume_to_json("Flask/noor.pdf", "cv_data.json")


with open("cv_data.json", "r") as f:
    data = json.load(f)

print(json.dumps(data, indent=4))



# import PyPDF2
# import json
# import re

# a = PyPDF2.PdfReader(r"PDF Parsing\CV.pdf")

# print(a.metadata) #gives info about the pdf file
# print(a.pages[0].extract_text()) #extracts text from the first page of the pdf

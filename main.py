import pikepdf
from pathlib import Path

def unlock_pdfs(pdf_pass, given_path):
    files = list(Path(given_path).rglob("*.[pP][dD][fF]"))
    # iterate over all the files in the directory and over all the subdirectories and unlock the passwords
    for file in files:
        try:
            pdf = pikepdf.open(file, password=pdf_pass, allow_overwriting_input=True)
            pdf.save(file)
            print(f"File {file} unlocked successfully")
        except pikepdf._qpdf.PasswordError:
            print(f"File {file} couldnjson't be unlocked with the password provided")
        
def main():
    pdf_pass = input("PDF password: ")
    given_path = input("Enter the path: ")
    unlock_pdfs(pdf_pass, given_path)

if __name__ == "__main__":
    main()
    
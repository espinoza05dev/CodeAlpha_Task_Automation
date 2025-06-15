import os.path
import re

def extract_emails(path_in, path_OUT):
    with open(path_in, "r", encoding="utf-8") as f:
        texto = f.read()
        patron = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(patron, texto)

    with open(path_OUT, "w", encoding="utf-8") as f:
        for correo in emails:
            f.write(correo + "\n")

    if os.path.exists(path_OUT):
        print("Emails extracted successfully")

if __name__ == "__main__":
    path_origin = r"EMAILS"
    path_out = r"EMAILS2"

    extract_emails(path_origin, path_out)

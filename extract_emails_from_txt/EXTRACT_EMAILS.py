import re

path_origin = r"EMAILS"
path_out = r"EMAILS2"
patron = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'


def extract_emails(path_in, path_OUT):
    with open(path_in, "r", encoding="utf-8") as f:
        texto = f.read()
        emails = re.findall(patron, texto)

    with open(path_OUT, "w", encoding="utf-8") as f:
        for correo in emails:
            f.write(correo + "\n")

extract_emails(path_origin, path_out)
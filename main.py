import pdfplumber
import pandas as pd
import re               #Mintakereséshez
import os
import unicodedata      #Ez a karakterek javítására szolgál

def clean_text(text):
    #A szétesett ékezetes karakterek javítására szolgál
    if not text: return ""

    #1. Unicode normalizálás
    text = unicodedata.normalize('NFC',text)

    #2. Manuális javítás
    replacements = {
        "´a": "á", "´A": "Á",
        "´e": "é", "´E": "É",
        "´i": "í", "´I": "Í",
        "´o": "ó", "´O": "Ó",
        "´u": "ú", "´U": "Ú",
        "˝o": "ő", "˝O": "Ő",
        "˝u": "ű", "˝U": "Ű",
        "´ı": "í", "¨o": "ö",
        # Egyéb szemetek takarítása
        "(cid:114)": "",
        "õ": "ő", "û": "ű"  # Gyakori kódolási hiba régi számláknál
    }

    for bad,good in replacements.items():
        text = text.replace(bad, good)
    replacements_reverse = {
        "a´": "á", "e´": "é", "o˝": "ő", "A´": "Á"
    }
    for bad,good in replacements_reverse.items():
        text = text.replace(bad, good)

    return text


def extract_data(pdf_path):
    print(f"Analyzing {pdf_path}\n")
    data = {}    #ide gyűjtjük az adatokat

    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        raw_text = first_page.extract_text()
        text = clean_text(raw_text)
        # print(text)

        #A számlaszám keresése
        invoice_num_match = re.search(r'Számlaszám:\s*([A-Z]+-\d{4}-\d{1})',text)
        if invoice_num_match:
            data["Számlaszám"] = invoice_num_match.group(1)
        else:
            data["Számlaszám"] = "Nem található"

        #Végösszeg keresése
        total_match = re.search(r"Fizetendő:\s*([\d\s]+)",text)
        if total_match:
            raw_amount = total_match.group(1).replace(" ", "")
            data["Fizetendő"] = int(raw_amount)
        else:
            data["Fizetendő"] = 0

        #Dátum
        date_match = re.search(r'Telj.:\s*(\d{4}\.\d{2}\.\d{2}\.)', text)
        if date_match:
            data["Dátum"] = date_match.group(1)
        else:
            data["Dátum"] = "Nincs adat"

    return data



#Main program
if __name__ == "__main__":
    pdf_file = os.path.join("data","szamla.pdf")

    if os.path.exists(pdf_file):
        #Számla adatai
        invoice_data = extract_data(pdf_file)
        print(f"Kinyert adatok: {invoice_data}")

        #Excel készítése
        df = pd.DataFrame([invoice_data])

        output_file = "szamla_adatok.xlsx"
        df.to_excel(output_file)
        print(f"\n✅ SIKER! Az Excel fájl elkészült: {output_file}")

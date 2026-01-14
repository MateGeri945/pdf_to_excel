import pdfplumber
import os

def analyze_pdf(file_path: str) -> None:

    #Elemzi a pdf fájlt és kiírja a tartalmát
    print(f"--- Elemzés kezdete: {file_path} ---")

    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]

        #1. A szöveg kinyerése
        text_content = first_page.extract_text()
        print("\n:")
        print(text_content)
        print('-'*30)

        #2. Táblázatok keresése
        tables = first_page.extract_table()

        print("\n:")
        if tables:
            for row in tables:
                print(row)
        else:
            print("Nem találtam táblázatot ezen az oldalon.")

#Futtatás
if __name__ == "__main__":
    #A számla helye
    pdf_path = os.path.join("data","szamla.pdf")

    #Ellenőrizzük a fájl létezését
    if os.path.exists(pdf_path):
        analyze_pdf(pdf_path)
    else:
        print(f"HIBA: Nem találom a fájlt itt: {pdf_path}")
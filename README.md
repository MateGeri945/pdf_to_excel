PDF számla feldolgozó
Ez a python alapú automatizációs eszköz képes strukturálatlan PDF számlákból kinyerni a kulcsfontosságú adatokat (Dátum, Számlaszám, Végösszeg) és azokat egy Excel táblázatba exportálja.
A projekt fő erőssége egy egyedi karakter helyreállító algoritmus, amely képes a kezelni és javítani a PDF-ből beolvasott szöveg szétesett ékezetes karaktereit.


Probléma:
A cégek gyakran kapnak olyan PDF számlákat amelyekből az adatok kimásolása nehézkes és a kézi adatbevitel lassú.

Megoldás:
A program automatizálja a folyamatot.
1. Beolvassa a PDF fájlt. (pdfplumber)
2. Javítja a szétesett karaktereket.
3. Kinyeri a szükséges adatokat. (RegEx-vel mintakeresés)
4. Exportálja az adatokat egy Excel táblázatba.

Használt technológiák:
- Python 3.x
- pdfplumber (PDF )
- pandas (Dataframe kezelés és Excel export)
- openpyxl (Excel motor)
- unicodedata & regex (Adattisztítás és mintakeresés)


Telepítés és Futtatás:
1. Klónozd a repót:  git clone https://github.com/MateGeri945/pdf_to_excel.git
2. Telepítsd a szükséges csomagokat:  pip install -r requirements.txt
3. Helyezd a feldolgozandó számlát a data mappába szamla.pdf néven.
4. Futtasd a programot:  python main.py

Kimenet:
A program létrehoz egy szamla_adatok.xlsx fájlt a gyökérkönyvtárban a kinyert adatokkal.
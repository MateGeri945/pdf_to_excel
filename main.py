import pandas as pd
import os

# 1. Készítünk egy kis minta adatot (mintha ezt olvastuk volna ki egy PDF-ből)
data = {
    'Dátum': ['2025-01-13', '2025-01-14'],
    'Tétel': ['Laptop javítás', 'Monitor vásárlás'],
    'Összeg': ['12500 Ft', '50000 Ft']
}

# 2. Átalakítjuk DataFrame-mé (ez a Pandas táblázat formátuma)
df = pd.DataFrame(data)

# 3. Kiírjuk a konzolra, hogy lássuk
print("Ez kerül az Excelbe:")
print(df)

# 4. Kimentjük Excelbe
output_file = "teszt_szamla.xlsx"
df.to_excel(output_file, index=False)

print(f"\nSiker! A fájl létrejött itt: {os.getcwd()}\\{output_file}")

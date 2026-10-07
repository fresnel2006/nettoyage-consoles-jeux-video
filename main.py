from pathlib import Path

import pandas as pd
from tabulate import tabulate

DOSSIER = Path(__file__).parent
SORTIE = DOSSIER / "output"
SORTIE.mkdir(exist_ok=True)

consoles = pd.read_csv(DOSSIER / "Console Generation data.csv")

# Les noms de colonnes ont des espaces en trop
consoles.columns = consoles.columns.str.strip()

# Time period : "1972?present" -> "1972-2026"
consoles["Time period"] = (
    consoles["Time period"]
    .str.lower()
    .str.strip()
    .str.replace("present", "2026", regex=False)
    .str.replace("?", "-", regex=False)
)

# Texte
for colonne in ["Primary consoles", "Game media"]:
    consoles[colonne] = consoles[colonne].str.lower().str.strip()

consoles["Year of release"] = consoles["Year of release"].astype(int)

# Prix : " $611.21 " -> 611.21
for colonne in ["Original Price", "2022 Price (Adjusted for inflation)"]:
    consoles[colonne] = (
        consoles[colonne]
        .str.strip()
        .str.extract(r"\$([\d,.]+)", expand=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

# Ventes : " 1,000,000 " -> 1000000
consoles["Total Systems Sold"] = (
    consoles["Total Systems Sold"].str.replace(r"[,\s]", "", regex=True).astype("Int64")
)

consoles = consoles.drop(columns=["Generation"])

# Separation par constructeur
playstation = consoles[consoles["Primary consoles"].str.contains("playstation", na=False)]
xbox = consoles[consoles["Primary consoles"].str.contains("xbox", na=False)]
nintendo = consoles[consoles["Primary consoles"].str.contains("nintendo", na=False)]

playstation.to_csv(SORTIE / "playstation.csv", index=False)
xbox.to_csv(SORTIE / "xbox.csv", index=False)
nintendo.to_csv(SORTIE / "nintendo.csv", index=False)

for nom, table in [("PlayStation", playstation), ("Xbox", xbox), ("Nintendo", nintendo)]:
    print(f"\n{nom} ({len(table)} consoles)")
    print(tabulate(table, tablefmt="psql", headers="keys", showindex=False))

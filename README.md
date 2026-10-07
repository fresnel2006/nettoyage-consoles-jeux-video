# Nettoyage des données des consoles de jeux vidéo

Nettoyage d'un dataset sur les générations de consoles (prix d'origine, prix ajusté à l'inflation 2022, ventes totales) puis séparation par constructeur.

## Ce que fait le script
- Renommage des colonnes mal formatées (espaces en trop)
- Nettoyage de `Time period` (`present` remplacé par 2026, caractères parasites)
- Extraction des montants en dollars et conversion en nombres
- Conversion des ventes totales (`Total Systems Sold`) en nombres
- Séparation du dataset en trois fichiers : **PlayStation**, **Xbox**, **Nintendo**
- Affichage des trois tableaux dans la console

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Stack
Python, pandas, numpy, tabulate

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan

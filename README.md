# Nettoyage des données des consoles de jeux vidéo

Nettoyage d'un dataset sur les générations de consoles (prix d'origine, prix ajusté à l'inflation 2022, ventes totales), puis séparation par constructeur.

## Ce que fait le script
- Nettoyage des noms de colonnes (espaces en trop)
- Nettoyage de `Time period` : `"2020?present"` devient `"2020-2026"`
- Extraction des montants en dollars et conversion en nombres
- Conversion des ventes totales en entiers (`" 1,000,000 "` devient `1000000`)
- Séparation en trois fichiers dans `output/` : **PlayStation**, **Xbox**, **Nintendo**

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Les fichiers nettoyés sont enregistrés dans le dossier `output/` (créé automatiquement).

## Stack
Python, pandas, tabulate

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan

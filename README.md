# 📊 Pandas Revenue Challenge

Practice basic stats with **Pandas** and **Matplotlib**: parse and sort dates, compute the **average sales**, and create clean **bar** & **line** charts by month.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="pandas" src="https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white">
  <img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-3.x-11557C">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-green">
</p>

## ✨ What you’ll build
- Parse and sort reference dates  
- Compute the **average sales**  
- Plot a **bar chart** (month × value)  
- Plot a **line chart** (month × value)

## 🧰 Requirements
```
pandas>=2.0
matplotlib>=3.7
```

## 🚀 Quickstart
```
# (optional) create a virtual env
python -m venv .venv

# activate
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# install deps
pip install -r requirements.txt  # or install the packages above

# run
python src/main.py
```

## 🧩 Starter code (src/main.py)
```
import pandas as pd
import matplotlib.pyplot as plt

# Base Data
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
    ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
    ]
}
```

## 🖼 Outputs (add to repo)
-  bar_chart.png
-  line_chart.png

## ✅ Checklist
-  Convert data_ref to datetime and sort
-  Create month_ref (YYYY-MM)
-  Compute average sales
-  Save and commit bar_chart.png & line_chart.png
-  Push to GitHub and submit the repo URL

## 📄 License
MIT — feel free to use and adapt.

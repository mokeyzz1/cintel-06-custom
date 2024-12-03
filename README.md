# cintel-06-custom

# Stock Market Insights Dashboard 📈

An interactive and dynamic PyShiny application to explore and analyze the stock market landscape.

## 🌟 Features

- **Interactive Filters:** Easily filter data by market category, listing exchange, and financial status.
- **Dynamic Visualizations:** View the market category distribution in real-time with updated bar charts.
- **Actionable Insights:** Gain insights into the number of stocks, unique exchanges, and market categories.
- **Data Table:** Explore the filtered stock data in a concise and structured table format.

---

## 🗂 Dataset

- **Source:** [Stock Market Dataset on Kaggle](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset)  
- **File Used:** `symbols_valid_meta.csv`

---

## 🔧 Technologies Used

- **Python**: Backend processing
- **PyShiny**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Dynamic and interactive visualizations
- **Faicons**: Icons for aesthetic dashboards

---

## 🚀 Installation Instructions

### 1. Clone the Repository
```bash

git clone https://github.com/mokeyzz1/cintel-06-custom.git
cd cintel-06-custom

### 2. Set up Virtual Environment
``` bash 
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

### 3. Run the Application
bash
Copy code
shiny run --reload --launch-browser dashboard/app.py

# 📊 Interactive Analytics Features
- Filters: Filter stocks based on:
- Market Category
- Listing Exchange
- Financial Status
Outputs:
- Bar chart showing Market Category Distribution
- DataGrid displaying filtered stock details
- Summary metrics for total stocks, unique exchanges, and market categories
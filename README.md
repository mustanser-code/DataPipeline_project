# Product Data Cleaning & Visualization Pipeline

A robust Python pipeline designed to fetch raw product data from a remote server using python "requests" module, execute structural data cleaning using `pandas`, and generate visual insights using `matplotlib` and `seaborn`.

## 🚀 Features
- **Live Data Ingestion**: Dynamically fetches the latest product data from a server API via the `requests` library.
- **Data Integrity Auditing**: Automatically inspects datasets for null/missing entries and structural duplicates.
- **Data Standardization**: Parses nested JSON objects (dimensions, metadata) and normalizes columns for downstream analysis.
- **Statistical Visualization**: Generates clear distribution heatmaps and correlation plots.

## 🛠️ Tech Stack
- **Language**: Python 3.12.3
- **Data Libraries**: Pandas
- **Networking**: Requests
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Jupyter Lab

## 📁 Repository Structure
```text
├── apicalling.py        # Script handling server requests and data fetching
├── product_data.csv     # Cached raw data fetched from the server
├── cleaning.ipynb       # Jupyter notebook executing the Pandas cleaning pipeline
├── plot.ipynb           # Notebook dedicated to Matplotlib/Seaborn visualizations
└── README.md            # Project documentation
```

## 💻 Quick Start

### 1. Prerequisites
Install the required dependencies using pip:
```bash
pip install pandas requests matplotlib seaborn
```

### 2. Execution Order
1. Run `apicalling.py` to pull fresh data from the server and save it locally as a CSV.
2. Open `cleaning.ipynb` to process missing data, verify structural duplicates, and normalize data types.
3. Open `plot.ipynb` to render the visualization dashboards.

## 📊 Summary of Cleaning Steps
- Checked missing entries using `df.isnull().sum()`.
- Verified and dropped duplicate records using `df.duplicated()`.
- Handled complex structured types within `dimensions`, `reviews`, and `meta` fields.
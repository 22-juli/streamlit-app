# Streamlit - Professional Ranking Demo

This is a beginner-friendly Streamlit web application built with Python. It fetches publication data from PubMed using Biopython, processes the data with Pandas, and displays the results in a clean table format and NumPy. The app demonstrates basic data enrichment and web app development.

The app identifies, enriches, and ranks professionals in the domain of **3D in-vitro models for drug discovery and safety assessment**. The app fetches real publication data from **PubMed** using the NCBI Entrez API and combines it with simulated LinkedIn/conference data. It computes probability scores and displays a **sortable, filterable table** with the option to **export results to CSV**.

## 🚀 Features

- Fetches real-time PubMed publication data
- Combines publications with simulated professional profiles
- Computes probability scores for ranking
- Displays data in a sortable and filterable table
- Export results to CSV for offline analysis
- Interactive Streamlit UI

## 🧰 Tech Stack

- Python 3.11.x
- Streamlit
- Biopython (for PubMed data)
- Pandas (data processing)
- NumPy

💻 Installation & Run Locally

1. Clone the repository:

git clone https://github.com/22-juli/streamlit-app.git
cd streamlit-app

2. Install dependencies:

pip install -r requirements.txt

3. Run locally:

streamlit run app.py

🌐 Live Demo:

You can access the live deployed app here: https://27eqk3w77hudznoukq8efn.streamlit.app/


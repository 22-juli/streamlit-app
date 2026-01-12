# Professional Ranking Demo

This **Streamlit app** identifies, enriches, and ranks professionals in the domain of **3D in-vitro models for drug discovery and safety assessment**.

The app fetches real publication data from **PubMed** using the NCBI Entrez API and combines it with simulated LinkedIn/conference data. It computes probability scores and displays a **sortable, filterable table** with the option to **export results to CSV**.

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

## 💻 Installation & Run Locally

1. **Clone the repository:**

git clone https://github.com/22-juli/streamlit-app.git
cd streamlit

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py

⚠️ Note: Ensure you have an internet connection for PubMed API calls. The Entrez.email in the code is a placeholder; for production, set a valid email.

🌐 Live Demo
Click here to view the app online

📂 Project Structure

streamlit-app/
├─ app.py              # Main Streamlit app (UI and interaction)
├─ data_enrichment.py  # Functions to enrich PubMed data with additional info
├─ pubmed_fetcher.py   # fetched pubmed data or CSV exports
├─ README.md           # Project description
├─ requirements.txt    # Python dependencies
├─ scoring.py          # Computes probability scores for ranking professionals
├─ tests.py            # Test scripts for checking functionality

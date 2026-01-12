import streamlit as st
import pandas as pd
from data_enrichment import get_enriched_data
from scoring import compute_score

st.set_page_config(page_title="Professional Ranking", layout="wide")

data = get_enriched_data()
for person in data:
    person["score"] = compute_score(person)

df = pd.DataFrame(data)
df["rank"] = df["score"].rank(ascending=False, method="dense").astype(int)
df = df.sort_values("score", ascending=False)

st.title("Professional Ranking for 3D In-Vitro Models")

search = st.text_input("Search by name, title, or company")

if search:
    mask = df.apply(lambda row: search.lower() in str(row.values).lower(), axis=1)
    df = df[mask]

st.dataframe(df[["rank", "score", "name", "title", "company", "person_location", "company_hq", "email", "linkedin", "source"]])

csv = df.to_csv(index=False)
st.download_button("Download CSV", csv, "professionals.csv", "text/csv")
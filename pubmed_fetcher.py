from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "demo@example.com"  # Placeholder email for NCBI API

def fetch_pubmed_authors():
    # For demo purposes, return mock data to ensure the app runs
    # In production, uncomment the real fetch code
    mock_authors = {
        "John Doe": True,
        "Jane Smith": True,
        "Alice Johnson": True,
        "Bob Wilson": True,
    }
    return mock_authors

    # Uncomment below for real data
    """
    try:
        # Query for papers in last 24 months (Jan 2024 to Jan 2026)
        query = '("Drug-Induced Liver Injury" OR "Liver Toxicity" OR "3D cell culture" OR "Organ-on-chip") AND ("2024/01/01"[PDAT] : "2026/01/01"[PDAT])'

        # Search for paper IDs
        handle = Entrez.esearch(db="pubmed", term=query, retmax=10)  # Limit to 10 for demo
        record = Entrez.read(handle)
        handle.close()

        ids = record["IdList"]  # type: ignore
        if not ids:
            return {}

        # Fetch details
        handle = Entrez.efetch(db="pubmed", id=ids, rettype="xml")
        xml_data = handle.read()
        handle.close()

        root = ET.fromstring(xml_data)
        authors_set = set()

        for article in root.findall(".//PubmedArticle"):
            pub_date = article.find(".//PubDate")
            year = "Unknown"
            if pub_date is not None:
                year_elem = pub_date.find("Year")
                if year_elem is not None and year_elem.text:
                    year = year_elem.text

            title_elem = article.find(".//ArticleTitle")
            title = "Unknown"
            if title_elem is not None and title_elem.text:
                title = title_elem.text

            authors = article.findall(".//Author")
            for author in authors:
                last_name = author.find("LastName")
                fore_name = author.find("ForeName")
                if last_name is not None and fore_name is not None and last_name.text and fore_name.text:
                    full_name = f"{fore_name.text} {last_name.text}"
                    authors_set.add(full_name)

        # Return dict with published_dili = True
        return {author: True for author in authors_set}
    except Exception as e:
        print(f"Error fetching PubMed data: {e}")
        return {}
  """

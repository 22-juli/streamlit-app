import random
from pubmed_fetcher import fetch_pubmed_authors

# Simulated profiles
simulated_profiles = [
    {"name": "Alice Johnson", "title": "Director of Toxicology", "company": "PharmaCorp", "linkedin": "https://linkedin.com/in/alicejohnson", "source": "LinkedIn"},
    {"name": "Bob Smith", "title": "Head of Preclinical Safety", "company": "BioTech Inc", "linkedin": "https://linkedin.com/in/bobsmith", "source": "SOT Conference"},
    {"name": "Carol Lee", "title": "Safety Assessment Lead", "company": "ToxSolutions", "linkedin": "https://linkedin.com/in/carollee", "source": "AACR Conference"},
    {"name": "David Kim", "title": "Investigative Toxicology Manager", "company": "DrugSafe Ltd", "linkedin": "https://linkedin.com/in/davidkim", "source": "ISSX Conference"},
    {"name": "Eva Martinez", "title": "Director of Toxicology", "company": "InnovateBio", "linkedin": "https://linkedin.com/in/evamartinez", "source": "LinkedIn"},
]

# Company metadata
company_metadata = {
    "PharmaCorp": {"funding": "Series B", "industry": "Pharmaceuticals", "tech": ["in-vitro"], "hq": "Basel, Switzerland", "nam": True},
    "BioTech Inc": {"funding": "Series A", "industry": "Biotechnology", "tech": ["organ-on-chip", "NAMs"], "hq": "Cambridge, MA", "nam": True},
    "ToxSolutions": {"funding": "Public", "industry": "Toxicology Services", "tech": ["in-vitro"], "hq": "Bay Area, CA", "nam": False},
    "DrugSafe Ltd": {"funding": "Seed", "industry": "Drug Safety", "tech": ["3D cell culture"], "hq": "London, UK", "nam": True},
    "InnovateBio": {"funding": "Series B", "industry": "Biotech", "tech": ["organ-on-chip"], "hq": "Boston, MA", "nam": True},
}

def get_identified_persons():
    pubmed_authors = fetch_pubmed_authors()
    persons = []
    
    # Add simulated profiles
    for profile in simulated_profiles:
        person = profile.copy()
        person["published_dili"] = False  # type: ignore
        persons.append(person)
    
    # Add PubMed authors
    for author, published in pubmed_authors.items():
        person = {
            "name": author,
            "title": None,  # Will be assigned in enrichment
            "company": None,
            "linkedin": None,
            "source": "PubMed",
            "published_dili": published
        }
        persons.append(person)
    
    return persons

def enrich_person(person):
    name = person["name"]
    first, last = name.split()[:2] if len(name.split()) >= 2 else (name, "")
    company = person.get("company")
    
    if not company:
        # For PubMed authors, assign random company
        company = random.choice(list(company_metadata.keys()))
        person["company"] = company
    
    # Email
    email = f"{first.lower()}.{last.lower()}@{company.replace(' ', '').lower()}.com"
    person["email"] = email
    
    # Phone
    person["phone"] = "N/A"
    
    # Person location
    person["person_location"] = random.choice(["Remote", "Boston", "San Francisco", "Basel", "London"])
    
    # Company HQ
    person["company_hq"] = company_metadata[company]["hq"]
    
    # Company metadata
    person["funding_stage"] = company_metadata[company]["funding"]
    person["industry_focus"] = company_metadata[company]["industry"]
    person["technologies"] = company_metadata[company]["tech"]
    person["nam"] = company_metadata[company]["nam"]
    
    # For PubMed authors, assign random title if None
    if not person.get("title"):
        target_roles = ["Director of Toxicology", "Head of Preclinical Safety", "Safety Assessment Lead", "Investigative Toxicology Manager"]
        person["title"] = random.choice(target_roles)
    
    # LinkedIn for PubMed, mock
    if not person.get("linkedin"):
        person["linkedin"] = f"https://linkedin.com/in/{first.lower()}{last.lower()}"
    
    return person

def get_enriched_data():
    persons = get_identified_persons()
    enriched = [enrich_person(p) for p in persons]
    return enriched
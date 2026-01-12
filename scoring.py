def compute_score(person):
    score = 0
    
    title = person.get("title", "").lower()
    if any(word in title for word in ["toxicology", "safety", "hepatic", "3d"]):
        score += 30
    
    funding = person.get("funding_stage", "")
    if funding in ["Series A", "Series B"]:
        score += 20
    
    tech = person.get("technologies", [])
    if "in-vitro" in tech or "organ-on-chip" in tech:
        score += 15
    
    if person.get("nam", False):
        score += 10
    
    hq = person.get("company_hq", "")
    if any(hub in hq for hub in ["Boston", "Cambridge", "Bay Area", "Basel", "London"]):  # Assuming UK Golden Triangle includes London
        score += 10
    
    if person.get("published_dili", False):
        score += 40
    
    return min(score, 100)
from data_enrichment import get_enriched_data
from scoring import compute_score

try:
    data = get_enriched_data()
    for p in data:
        p["score"] = compute_score(p)
    print("Data processed successfully:", len(data))
    print("Sample:", data[0] if data else "No data")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
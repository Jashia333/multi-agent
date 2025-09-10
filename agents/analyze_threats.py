import re

def analyze_threats(news_list):
    cve_pattern = r"CVE-\d{4}-\d{4,7}"
    threat_keywords = ["vulnerability", "exploit", "malware", "ransomware", "data breach", "cyberattack"]

    analysis = []
    for item in news_list:
        cves = re.findall(cve_pattern, item)
        threats = [kw for kw in threat_keywords if kw in item.lower()]
        analysis.append({"text": item, "cves": cves, "keywords": threats})
    return analysis

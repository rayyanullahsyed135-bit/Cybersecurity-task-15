# Simple CVSS-based risk calculation


def calculate_risk(cvss_score, asset_value=5, exploitability=5):
return cvss_score * asset_value * exploitability


# Example
risk_score = calculate_risk(9.8)
print("Calculated Risk Score:", risk_score)

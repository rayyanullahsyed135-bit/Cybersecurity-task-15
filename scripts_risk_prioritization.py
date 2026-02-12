import csv


with open('nessus_scan_results.csv', 'r') as file:
reader = csv.DictReader(file)
for row in reader:
cvss = float(row['CVSS'])
if cvss >= 9.0:
print(f"CRITICAL: {row['Plugin Name']}")

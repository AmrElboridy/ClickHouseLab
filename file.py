# Script Name: generate_data.py
# Author: Amr (for lab practice)
# Date of Creation: 28-Sep-2025
# Description: Generate random sales data for MySQL vs ClickHouse performance lab.

import csv, random, datetime

with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for i in range(1, 1000001):  # 1 مليون صف
        product_id = random.randint(1, 500)
        customer_id = random.randint(1, 100000)
        amount = round(random.uniform(5, 500), 2)
        sale_date = datetime.date(2022, 1, 1) + datetime.timedelta(days=random.randint(0, 365))
        writer.writerow([i, product_id, customer_id, amount, sale_date])

report = "     Total Sales = 250000 PKR      "

clean = report.strip()
clean = clean.replace("Total Sales = ", "")
parts = clean.split()

amount = int(parts[0])

print("Amount:", amount)
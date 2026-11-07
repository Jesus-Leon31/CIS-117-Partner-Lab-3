with open(r"C:\Users\Hallo\OneDrive\Documents\GitHub\CIS-117-Partner-Lab-3\country_full.csv") as f:
    for line in f:
        print(line.split(",")[0] + ", " + line.split(",")[5] + "\n")


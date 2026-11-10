#Read a CSV file and prints the country name and region for each country.

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / "country_full.csv"


with open(file_path, "r") as f:
    next(f)
    for line in f:
        print(line.split(",")[0] + ", " + line.split(",")[5])
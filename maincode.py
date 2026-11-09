
# CIS-117 Partner Lab3
# Description: Read a CSV file containing country information
# and create separate CSV files for each region.
# Name: Mitchell Hadeed
# Partner: Jesus Leon

import csv
from pathlib import Path


def read_countries(filename):
    regions = {}

    with open(filename, "r", newline="", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)

        if not reader.fieldnames or not {"name", "region"}.issubset(reader.fieldnames):
            raise ValueError("The CSV file must have 'name' and 'region' columns.")

        for row in reader:
            country = (row.get("name") or "").strip()
            region = (row.get("region") or "").strip() or "Unclassified"

            if country:
                if region not in regions:
                    regions[region] = []
                regions[region].append([country, region])

    return regions


def write_region_files(regions, output_folder):
    output_folder.mkdir(exist_ok=True)

    for region, countries in regions.items():
        filename = output_folder / f"{region}.csv"

        with open(filename, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["name", "region"])
            writer.writerows(countries)

        print(f"Created {filename.name}: {len(countries)} countries")


def main():
    folder = Path(__file__).resolve().parent
    input_file = folder / "country_full.csv"
    output_folder = folder / "region_files"

    try:
        regions = read_countries(input_file)
        write_region_files(regions, output_folder)
        print("Finished splitting countries by region.")

    except FileNotFoundError:
        print("Error: country_full.csv was not found. Place it beside this script.")

    except PermissionError:
        print("Error: Permission denied while reading or writing a file.")

    except (OSError, csv.Error, ValueError) as error:
        print(f"Error processing the CSV file: {error}")


if __name__ == "__main__":
    main()

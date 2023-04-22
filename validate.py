import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

filename = "schools.csv"

# Count the number of rows in the CSV file (excluding the header row)
num_rows = sum(1 for line in open(filename)) - 1

# Open the CSV file and read the rows
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in tqdm(csvreader, total=num_rows):
        url = row[1]  # assuming URL is in the second column
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            if response.status_code == 200 and "404" not in soup.get_text():
                print(f"{url} is valid.")
            else:
                print(f"{url} returned a 404 error.")
        except requests.exceptions.RequestException as e:
            print(f"{url} raised an exception: {e}")

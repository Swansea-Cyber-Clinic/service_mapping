from datetime import datetime
import json
from pathlib import Path
import sqlite3 as sql
import pandas as pd
import os
import logging
import argparse
import sys

# Logging setup
parser = argparse.ArgumentParser()
parser.add_argument(
  '-v', '--verbose',
  help="Provides verbose output useful for finding errors in the CSV file",
  action="store_const", dest="loglevel", const=logging.DEBUG,
  default=logging.INFO
)

parser.add_argument(
  '-i', '--input',
  metavar='/path/to/file',
  help="The path to the input CSV file",
  type=Path,
  required=True
)

args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format='%(levelname)s: %(message)s')

errors_extant = False

# Check that specified CSV file is actually a file
csv_file = args.input
if not csv_file.is_file():
  logging.critical("Specified CSV file does not exist, quitting now.")
  sys.exit()

# Initial database set-up
if os.path.exists('service_mapping.db'):
  os.remove('service_mapping.db')
con = sql.connect('service_mapping.db')
sql_script = open('create_database.sql').read()

cursor = con.cursor()
cursor.executescript(sql_script)

# Commiting pre-defined information to database
countries_file = open('data/country.json')
countries = json.load(countries_file)

for index, item in enumerate(countries):
  cursor.execute("INSERT INTO coverage VALUES (?, ?)", (index, item))
  logging.debug(f"Inserted country {item} into database")
con.commit()
logging.info("Created country definitions")

for category_type in ('category', 'police_force'):
  file = open(f"data/{category_type}.json")
  file_dict = json.load(file)
  file.close()

  for index, item in enumerate(file_dict):
    cursor.execute(f"INSERT INTO {category_type} VALUES (?, ?, ?)", (index, item['name'], item['description']))
    logging.debug(f"Inserted {category_type} {item['name']} ({item['description']}) into database")
  con.commit()
  logging.info(f"Created {category_type} definitions")

# Organisations
## Apologies in advance to any pandas experts, I am going to be iterating through rows of a dataframe in a completely non-vibe adjacent way, I just wanted to make you aware of that fact ahead of time. (Performance wise it's not good in O(n)-esque terms, but because of the size of the dataset, it doesn't really matter, it's not like we have thousands upon thousands of records - let's be pragmatic about this!)

df = pd.read_csv(csv_file, sep=',')
df = df[df['Forces'].notna()].replace(to_replace='NA', value='')

cat_counter = 0
forces_counter = 0
cov_counter = 0
for i, r in df.iterrows():
  cursor.execute(
    "INSERT INTO organisation VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (i, r['Organisation'], r['Description'], r['Address_1'], r['Address_2'], r['City'], r['Postcode'], r['Email_office'], r['Tel_office'], r['Email_help'], r['Tel_help'], r['Web'], datetime.now().strftime('%d/%m/%Y'), datetime.now().strftime('%d/%m/%Y'))
    )
  con.commit()
  logging.debug(f"Inserted organisation {r['Organisation']} into database with id {i}")
  
  categories = r['Service_cat'].split(',')
  logging.debug(f"The following categories are associated with organisation {i}: {categories}")
  categories = [x.strip() for x in categories]
  for c in categories:
    try:
      cat_id = cursor.execute("SELECT cat_id FROM category WHERE category.cat_name=?", (c,)).fetchone()[0]
      cursor.execute("INSERT INTO category_mapping VALUES (?, ?, ?)", (cat_counter, i, cat_id))
      con.commit()
      logging.debug(f"Created association between category {c} (id: {cat_id}) and organisation {r['Organisation']} (id: {i})")
      cat_counter += 1
    except TypeError as e:
      logging.error(f"Category '{c}' listed for organisation {i} does not correspond to any known category, check line {i+2} of the CSV file.")
      errors_extant = True

  forces = r['Forces'].split(',')
  forces = [x.strip() for x in forces]
  for f in forces:
    try:
      force_id = cursor.execute("SELECT force_id FROM police_force WHERE police_force.force_code=?", (f,)).fetchone()[0]
      cursor.execute("INSERT INTO police_force_mapping VALUES (?, ?, ?)", (forces_counter, i, force_id))
      con.commit()
      logging.debug(f"Created association between Police force {f} (id: {force_id}) and organisation {r['Organisation']} (id: {i})")
      forces_counter += 1
    except TypeError as e:
      logging.error(f"Police force '{f}' listed for organisation {i} does not correspond to any known Police force, check line {i+2} of the CSV file.")
      errors_extant = True
  
  countries_list = r['Coverage'].split(',')
  countries_list = [x.strip() for x in countries_list]
  for cn in countries_list:
    try:
      country_id = cursor.execute("SELECT cov_id FROM coverage WHERE coverage.cov_nation=?", (cn,)).fetchone()[0]
      cursor.execute("INSERT INTO coverage_mapping VALUES (?, ?, ?)", (cov_counter, i, country_id))
      con.commit()
      logging.debug(f"Created association between country {cn} (id: {country_id}) and organisation {r['Organisation']} (id: {i})")
      cov_counter += 1
    except TypeError as e:
      logging.error(f"Country '{cn}' listed for organisation {i} does not correspond to any known country, check line {i+2} of the CSV file.")
      errors_extant = True

num_orgs = cursor.execute("SELECT COUNT(*) FROM organisation").fetchone()[0]
con.close()
if errors_extant:
  logging.warning("There are errors in the CSV file from which this database was generated. See previous output for details, in any case, you should not use the output of this tool until you have rectified this.")
logging.info(f"Database generated, added {num_orgs} organisation(s).")
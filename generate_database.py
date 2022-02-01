from datetime import datetime
import sqlite3 as sql
import pandas as pd
import os

# Initial database set-up
if os.path.exists('service_mapping.db'):
  os.remove('service_mapping.db')
con = sql.connect('service_mapping.db')
sql_script = open('create_database.sql').read()

cursor = con.cursor()
cursor.executescript(sql_script)

# Commiting pre-defined information to database

## Coverage
countries = [
  'Wales', 'England', 'NI', 'Scotland'
]

coverage_list = []
for i in range(4):
  coverage_list.append((i, countries[i]))

cursor.executemany("INSERT INTO coverage VALUES (?, ?)", coverage_list)
con.commit()

## Police Forces
force_short = ['DPP', 'GP', 'NWP', 'SWP']
force_long = ['Dyfed Powys Police', 'Gwent Police', 'North Wales Police', 'South Wales Police']

forces_list = []
for i in range(4):
  forces_list.append((i, force_short[i], force_long[i]))

cursor.executemany("INSERT INTO police_force VALUES (?, ?, ?)", forces_list)
con.commit()

## Categories
name = ['BAME', 'Cyber', 'DA', 'DS', 'DV', 'FFI', 'Housing', 'LGBTQ', 'MH', 'OP', 'PFS', 'SP', 'SV', 'VS', 'WS', 'Women', 'YP', 'FP', 'SOB']
desc = [
  'Support services for Black, Asian, and Minority Ethnic people',
  'Cyber security expert support and advice',
  'Drug and alcohol support',
  'Disability support services',
  'Domestic violence support services',
  'Financial, debt, fraud, and identity protection services and advice',
  'Housing, housing benefits, and homelessness support',
  'Support services for LGBTQ+ people',
  'Mental health support services',
  'Support services for older people',
  'Support for families and parents',
  'Suicide prevention',
  'Sexual violence support services',
  'General support for crime victims',
  'Welfare support services',
  'Support services for women',
  'Support services for children and young people',
  'Support services to alleviate fuel poverty',
  'Support for victims of stalking and online abuse'
]

category_list = []
for i in range(len(name)):
  category_list.append((i, name[i], desc[i]))

cursor.executemany("INSERT INTO category VALUES (?, ?, ?)", category_list)
con.commit()


# Organisations
## Apologies in advance to any pandas experts, I am going to be iterating through rows of a dataframe in a completely non-vibe adjacent way, I just wanted to make you aware of that fact ahead of time. (Performance wise it's not good in O(n)-esque terms, but because of the size of the dataset, it doesn't really matter, it's not like we have thousands upon thousands of records - let's be pragmatic about this!)

df = pd.read_csv('service_database_v1.txt', sep='\t', encoding='latin-1')
df = df[df['Forces'].notna()].replace(to_replace='NA', value='')

cat_counter = 0
forces_counter = 0
cov_counter = 0
for i, r in df.iterrows():
  print(r['Organisation'])
  cursor.execute(
    "INSERT INTO organisation VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (i, r['Organisation'], r['Description'], r['Address_1'], r['Address_2'], r['City'], r['Postcode'], r['Email_office'], r['Tel_office'], r['Email_help'], r['Tel_help'], r['Web'], datetime.now().strftime('%d/%m/%Y'), datetime.now().strftime('%d/%m/%Y'))
    )

  con.commit()
  
  categories = r['Service_cat'].split(',')
  print(categories)
  categories = [x.strip() for x in categories]
  for c in categories:
    cat_id = cursor.execute("SELECT cat_id FROM category WHERE category.cat_name=?", (c,)).fetchone()[0]
    cursor.execute("INSERT INTO category_mapping VALUES (?, ?, ?)", (cat_counter, i, cat_id))
    con.commit()
    cat_counter += 1

  forces = r['Forces'].split(',')
  forces = [x.strip() for x in forces]
  for f in forces:
    force_id = cursor.execute("SELECT force_id FROM police_force WHERE police_force.force_code=?", (f,)).fetchone()[0]
    cursor.execute("INSERT INTO police_force_mapping VALUES (?, ?, ?)", (forces_counter, i, force_id))
    con.commit()
    forces_counter += 1
  
  countries_list = r['Coverage'].split(',')
  print(countries_list)
  countries_list = [x.strip() for x in countries_list]
  for cn in countries_list:
    country_id = cursor.execute("SELECT cov_id FROM coverage WHERE coverage.cov_nation=?", (cn,)).fetchone()[0]
    cursor.execute("INSERT INTO coverage_mapping VALUES (?, ?, ?)", (cov_counter, i, country_id))
    con.commit()
    cov_counter += 1

con.close()
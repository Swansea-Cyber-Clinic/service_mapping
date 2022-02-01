# Service mapping
The scripts and data contained within this repository are used to generate a SQLite database used in Swansea Cyber Clinic's service mapping tool.

This repository does not contain the SQLite database itself, you'll have to generate that yourself, fortunately this is pretty simple.

## Generating `service_mapping.db`
You'll need:
- Git
- Python 3
- pandas

Generating the file is (well, should be) as simple as:
```zsh
git clone https://github.com/Swansea-Cyber-Clinic/service_mapping.git
cd service_mapping
python3 generate_database.py
```

## Database schema
The most recent version of the database schema is available [here](schema_design.md).

## To do
- Fix weird character encoding when exporting Excel file to TSV
- Ensure that all entries in the underlying Excel file have all fields (then change schema to have `NOT NULL` flags for all fields in `organisations`)

## Contributing
If you'd like to contribute anything to the dataset or contribute code, drop us an email at [cyberclinic@swansea.ac.uk](mailto:cyberclinic@swansea.ac.uk)!
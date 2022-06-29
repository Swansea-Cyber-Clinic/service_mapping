# Service mapping
The scripts and data contained within this repository are used to generate a SQLite database used in Swansea Cyber Clinic's service mapping tool.

This repository does not contain the SQLite database itself, you'll have to generate that yourself, fortunately this is pretty simple.

## Generating `service_mapping.db`
You'll need:
- Git
- Python 3
- pandas

For your convenience, a Pipfile has been created which can be used with [Pipenv](https://pipenv.pypa.io/en/latest/).

Generating the file is (well, should be) as simple as:
```zsh
git clone https://github.com/Swansea-Cyber-Clinic/service_mapping.git
cd service_mapping
python3 generate_database.py
```

If you'd like more output (i.e. more verbose), add the `-v` flag to the above.

## Database schema
The most recent version of the database schema is available [here](schema_design.md).

## To do


## Contributing
If you'd like to contribute anything to the dataset or contribute code, drop us an email at [cyberclinic@swansea.ac.uk](mailto:cyberclinic@swansea.ac.uk)!
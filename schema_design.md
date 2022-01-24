---
type: database_schema
author: Genevieve Clifford
version: InDev
---

# Database Schema

## Notes

This database schema design accounts for the data design created by Sara. It is an attempt to "SQL-ise" the data by transforming it from an Excel spreadsheet into a SQLite DB in third normal format.

## Overview

There are seven tables, four containing raw data, and three as two-way tables.

## Design

### `organisation`

While the database is being created, it will be possible for some fields to be `NOT NULL`, this is temporary and will be addressed in a later revision.

|Field|id|name|description|address_1|address_2|city|postcode|email_office|tel_office|email_help|tel_help|web|last_update|creation|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Type|int|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|datetime|datetime|
|Flags|pk|not null|not null||||||||||not null default CURRENT_TIMESTAMP|not null default CURRENT_TIMESTAMP|

#### Example

|id|name|description|address_1|address_2|city|postcode|email_office|tel_office|email_help|tel_help|web|last_update|creation|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Amethyst - RASASC|Amethyst is the Rape & Sexual Abuse Support Centre (RASASC) in North Wales...|11 Ash Court|Parc Menai|Bangor|LL57 4DF|info@rasacymru.org.uk|+44(0)1248670628|info@livefearfreehelpline.wales|+44(0)8088010800|https://www.rasawales.org.uk/|2022-01-24T16:14:00|2022-01-24T16:14:00|
|10|Gorwel - Grwp Cynefin|Gorwel is a Business Unit within Grŵp Cynefin (a Housing Association which operates in North Wales and North Powys)...|||||post@grwpcynefin.org|+44(0)3001112122|gorwel@gorwel.org|+44(0)3001112122|https://www.grwpcynefin.org/en/eich-cymuned/gorwel/|2022-01-24T16:14:00|2022-01-24T16:14:00|
...

### `police_force`

|Field|id|name|last_update|creation|
|---|---|---|---|---|
|Type|int|varchar|datetime|datetime|
|Flags|pk|not null|not null default CURRENT_TIMESTAMP|not null default CURRENT_TIMESTAMP|

#### Example

|id|name|last_update|creation|
|---|---|---|---|
|1|Dyfed-Powys Police|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|Gwent Police|2022-01-24T16:14:00|2022-01-24T16:14:00|
|3|North Wales Police|2022-01-24T16:14:00|2022-01-24T16:14:00|
|4|South Wales Police|2022-01-24T16:14:00|2022-01-24T16:14:00|

### `coverage`

|Field|id|nation|last_update|creation|
|---|---|---|---|---|
|Type|int|varchar|datetime|datetime|
|Flags|pk|not null|not null default CURRENT_TIMESTAMP|not null default CURRENT_TIMESTAMP|

#### Example

|id|nation|last_update|creation|
|---|---|---|---|
|1|Wales|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|England|2022-01-24T16:14:00|2022-01-24T16:14:00|
|3|Northern Ireland|2022-01-24T16:14:00|2022-01-24T16:14:00|
|4|Scotland|2022-01-24T16:14:00|2022-01-24T16:14:00|

### `category`

|Field|id|name|description|last_update|creation|
|---|---|---|---|---|---|
|Type|int|varchar|varchar|datetime|datetime|
|Flags|pk|not null|not null|not null default CURRENT_TIMESTAMP|not null default CURRENT_TIMESTAMP|

#### Example

|id|name|description|last_update|creation|
|---|---|---|---|---|
|1|BAME|Support services for Black, Asian, and Minority Ethnic people|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|Cyber|Cyber security expert support and advice|2022-01-24T16:14:00|2022-01-24T16:14:00|
|3|DA|Drug and alcohol support|2022-01-24T16:14:00|2022-01-24T16:14:00|
|4|DV|Disability support services|2022-01-24T16:14:00|2022-01-24T16:14:00|
|5|FFI|Financial, debt, fraud, and identity protection services and advice|2022-01-24T16:14:00|2022-01-24T16:14:00|
|6|Housing|Housing, housing benefits, and homelessness support|2022-01-24T16:14:00|2022-01-24T16:14:00|
|7|LGBTQ|Support services for LGBTQ+ people|2022-01-24T16:14:00|2022-01-24T16:14:00|
|8|MH|Mental health support services|2022-01-24T16:14:00|2022-01-24T16:14:00|
|9|OP|Support services for older people|2022-01-24T16:14:00|2022-01-24T16:14:00|
|10|PFS|Support for families and parents|2022-01-24T16:14:00|2022-01-24T16:14:00|
|11|SP|Suicide prevention|2022-01-24T16:14:00|2022-01-24T16:14:00|
|12|SV|Sexual violence support services|2022-01-24T16:14:00|2022-01-24T16:14:00|
|13|VS|General support for crime victims|2022-01-24T16:14:00|2022-01-24T16:14:00|
|14|WS|Welfare support services|2022-01-24T16:14:00|2022-01-24T16:14:00|
|15|Women|Support services for women|2022-01-24T16:14:00|2022-01-24T16:14:00|
|16|YP|Support services for children and young people|2022-01-24T16:14:00|2022-01-24T16:14:00|

### `category_mapping`

|Field|id|org_id|cat_id|
|---|---|---|---|
|Type|id|id|id|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

`FOREIGN KEY (org_id) REFERENCES organisation(id)`

`FOREIGN KEY (cat_id) REFERENCES category(id)`

#### Example

|id|org_id|cat_id|last_update|creation|
|---|---|---|---|---|
|1|1|13|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|10|4|2022-01-24T16:14:00|2022-01-24T16:14:00|
|3|10|12|2022-01-24T16:14:00|2022-01-24T16:14:00|
|4|10|6|2022-01-24T16:14:00|2022-01-24T16:14:00|
|5|10|3|2022-01-24T16:14:00|2022-01-24T16:14:00|
|6|10|8|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|10|10|2022-01-24T16:14:00|2022-01-24T16:14:00|

### `police_force_mapping`

|Field|id|org_id|force_id|
|---|---|---|---|
|Type|id|id|id|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

`FOREIGN KEY (org_id) REFERENCES organisation(id)`

`FOREIGN KEY (force_id) REFERENCES police_force(id)`

#### Example

|id|org_id|force_id|last_update|creation|
|---|---|---|---|---|
|1|1|3|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|10|3|2022-01-24T16:14:00|2022-01-24T16:14:00|

### `coverage_mapping`

|Field|id|org_id|cov_id|
|---|---|---|---|
|Type|id|id|id|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

`FOREIGN KEY (org_id) REFERENCES organisation(id)`

`FOREIGN KEY (cov_id) REFERENCES coverage(id)`

#### Example

|id|org_id|cov_id|last_update|creation|
|---|---|---|---|---|
|1|1|1|2022-01-24T16:14:00|2022-01-24T16:14:00|
|2|10|1|2022-01-24T16:14:00|2022-01-24T16:14:00|

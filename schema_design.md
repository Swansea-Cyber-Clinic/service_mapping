---
type: database_schema
author: Genevieve Clifford
version: 1.0
---

# Database Schema

## Notes

This database schema design accounts for the data design created by Sara. It "SQL-ises" the data by transforming it from an Excel spreadsheet into a SQLite DB in third normal format.

## Overview

There are seven tables, four containing raw data, and three as two-way tables.

## Design

### `organisation`

|Field|org_id|org_name|org_description|org_address_1|org_address_2|org_city|org_postcode|org_email_office|org_tel_office|org_email_help|org_tel_help|org_web|org_last_update|org_creation|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Type|int|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|varchar|datetime|datetime|
|Flags|pk|not null|not null||||||||||not null default CURRENT_TIMESTAMP|not null default CURRENT_TIMESTAMP|

#### Example

|org_id|org_name|org_description|org_address_1|org_address_2|org_city|org_postcode|org_email_office|org_tel_office|org_email_help|org_tel_help|org_web|org_last_update|org_creation|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Amethyst - RASASC|Amethyst is the Rape & Sexual Abuse Support Centre (RASASC) in North Wales...|11 Ash Court|Parc Menai|Bangor|LL57 4DF|info@rasacymru.org.uk|+44(0)1248670628|info@livefearfreehelpline.wales|+44(0)8088010800|https://www.rasawales.org.uk/|2022-01-24T16:14:00|2022-01-24T16:14:00|
|10|Gorwel - Grwp Cynefin|Gorwel is a Business Unit within Grŵp Cynefin (a Housing Association which operates in North Wales and North Powys)...|||||post@grwpcynefin.org|+44(0)3001112122|gorwel@gorwel.org|+44(0)3001112122|https://www.grwpcynefin.org/en/eich-cymuned/gorwel/|2022-01-24T16:14:00|2022-01-24T16:14:00|


### `category`

|Field|cat_id|cat_name|cat_description|
|---|---|---|---|
|Type|int|varchar|varchar|
|Flags|pk|not null|not null|

#### Example

|cat_id|cat_name|cat_description|
|---|---|---|
|1|BAME|Support services for Black, Asian, and Minority Ethnic people|
|2|Cyber|Cyber security expert support and advice|
|3|DA|Drug and alcohol support|
|4|DV|Disability support services|
|5|FFI|Financial, debt, fraud, and identity protection services and advice|
|6|Housing|Housing, housing benefits, and homelessness support|
|7|LGBTQ|Support services for LGBTQ+ people|
|8|MH|Mental health support services|
|9|OP|Support services for older people|
|10|PFS|Support for families and parents|
|11|SP|Suicide prevention|
|12|SV|Sexual violence support services|
|13|VS|General support for crime victims|
|14|WS|Welfare support services|
|15|Women|Support services for women|
|16|YP|Support services for children and young people|
|17|FP|Support services for children and young people|
|18|SOB|Support services for children and young people|

### `category_mapping`

|Field|cam_id|cam_org_id|cam_cat_id|
|---|---|---|---|
|Type|int|int|int|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

1. `FOREIGN KEY (org_id) REFERENCES organisation(id)`
2. `FOREIGN KEY (cat_id) REFERENCES category(id)`

#### Example

|id|cam_org_id|cam_cat_id|
|---|---|---|
|1|1|13|
|2|10|4|
|3|10|12|
|4|10|6|
|5|10|3|
|6|10|8|
|2|10|10|

### `coverage`

|Field|cov_id|cov_nation|
|---|---|---|
|Type|int|varchar|
|Flags|pk|not null|

#### Example

|cov_id|cov_nation|
|---|---|
|1|Wales|
|2|England|
|3|Scotland|
|4|NI|

### `coverage_mapping`

|Field|com_id|com_org_id|com_cov_id|
|---|---|---|---|
|Type|int|int|int|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

1. `FOREIGN KEY (org_id) REFERENCES organisation(id)`
2. `FOREIGN KEY (cov_id) REFERENCES coverage(id)`

#### Example

|com_id|com_org_id|com_cov_id|
|---|---|---|
|1|1|1|
|2|10|1|

### `police_force`

|Field|force_id|force_name|
|---|---|---|
|Type|int|varchar|
|Flags|pk|not null|

#### Example

|force_id|force_name|
|---|---|
|1|Dyfed-Powys Police|
|2|Gwent Police|
|3|North Wales Police|
|4|South Wales Police|

### `police_force_mapping`

|Field|fom_id|fom_org_id|fom_force_id|
|---|---|---|---|
|Type|int|int|int|
|Flags|pk|fk(1)|fk(2)|

#### Foreign key references

1. `FOREIGN KEY (org_id) REFERENCES organisation(id)`
2. `FOREIGN KEY (force_id) REFERENCES police_force(id)`

#### Example

|fom_id|fom_org_id|fom_force_id|
|---|---|---|
|1|1|3|
|2|10|3|

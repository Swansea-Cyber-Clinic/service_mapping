DROP DATABASE IF EXISTS service_mapping;
CREATE DATABASE service_mapping;

USE service_mapping;

CREATE TABLE organisation (
  id           INT           PRIMARY KEY,
  name         VARCHAR(50)   NOT NULL UNIQUE,
  description  VARCHAR(500)  NOT NULL,
  address_1    VARCHAR(50),
  address_2    VARCHAR(50),
  city         VARCHAR(50),
  postcode     VARCHAR(7),
  email_office VARCHAR(300)  NOT NULL,
  tel_office   VARCHAR(20),
  email_help   VARCHAR(300),
  tel_help     VARCHAR(20),
  web          VARCHAR(500),
  last_update  TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE police_force (
  id           INT         PRIMARY KEY,
  name         VARCHAR(50) UNIQUE NOT NULL,
  last_update  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE coverage (
  id           INT         PRIMARY KEY,
  nation       VARCHAR(50) UNIQUE NOT NULL,
  last_update  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE category (
  id           INT          PRIMARY KEY,
  name         VARCHAR(50)  UNIQUE NOT NULL,
  description  VARCHAR(500) NOT NULL,
  last_update  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created      TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE police_force_mapping (
  id       INT PRIMARY KEY,
  org_id   INT NOT NULL,
  force_id INT NOT NULL,
  FOREIGN KEY(org_id) REFERENCES organisation(id),
  FOREIGN KEY(force_id) REFERENCES police_force(id)
);

CREATE TABLE coverage_mapping (
  id       INT PRIMARY KEY,
  org_id   INT NOT NULL,
  cov_id   INT NOT NULL,
  FOREIGN KEY(org_id) REFERENCES organisation(id),
  FOREIGN KEY(cov_id) REFERENCES coverage(id)
);

CREATE TABLE category_mapping (
  id       INT PRIMARY KEY,
  org_id   INT NOT NULL,
  cat_id   INT NOT NULL,
  FOREIGN KEY(org_id) REFERENCES organisation(id),
  FOREIGN KEY(cat_id) REFERENCES category(id)
);
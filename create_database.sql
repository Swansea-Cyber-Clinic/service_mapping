CREATE TABLE organisation (
  org_id           INT           PRIMARY KEY,
  org_name         VARCHAR(50)   NOT NULL UNIQUE,
  org_description  VARCHAR(500)  NOT NULL,
  org_address_1    VARCHAR(50),
  org_address_2    VARCHAR(50),
  org_city         VARCHAR(50),
  org_postcode     VARCHAR(7),
  org_email_office VARCHAR(300),
  org_tel_office   VARCHAR(20),
  org_email_help   VARCHAR(300),
  org_tel_help     VARCHAR(20),
  org_web          VARCHAR(500),
  org_last_update  TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  org_created      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE police_force (
  force_id           INT          PRIMARY KEY,
  force_code         VARCHAR(50)  UNIQUE NOT NULL,
  force_name         VARCHAR(50)  NOT NULL
);

CREATE TABLE coverage (
  cov_id           INT         PRIMARY KEY,
  cov_nation       VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE category (
  cat_id           INTEGER NOT NULL PRIMARY KEY,
  cat_name         VARCHAR(50)  UNIQUE NOT NULL,
  cat_description  VARCHAR(500) NOT NULL
);

CREATE TABLE police_force_mapping (
  fom_id       INT PRIMARY KEY,
  fom_org_id   INT NOT NULL,
  fom_force_id INT NOT NULL,
  FOREIGN KEY(fom_org_id) REFERENCES organisation(org_id),
  FOREIGN KEY(fom_force_id) REFERENCES police_force(force_id)
);

CREATE TABLE coverage_mapping (
  com_id       INT PRIMARY KEY,
  com_org_id   INT NOT NULL,
  com_cov_id   INT NOT NULL,
  FOREIGN KEY(com_org_id) REFERENCES organisation(org_id),
  FOREIGN KEY(com_cov_id) REFERENCES coverage(cov_id)
);

CREATE TABLE category_mapping (
  cam_id       INT PRIMARY KEY,
  cam_org_id   INT NOT NULL,
  cam_cat_id   INT NOT NULL,
  FOREIGN KEY(cam_org_id) REFERENCES organisation(org_id),
  FOREIGN KEY(cam_cat_id) REFERENCES category(cat_id)
);
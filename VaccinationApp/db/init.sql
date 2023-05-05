CREATE DATABASE IF NOT EXISTS covid_vaccine_db;

USE covid_vaccine_db;

CREATE TABLE IF NOT EXISTS students (
    reg_no INT(11) NOT NULL,
    name VARCHAR(255) NOT NULL,
    vaccination_status ENUM('Yes', 'No') NOT NULL,
    PRIMARY KEY (reg_no)
);

INSERT INTO students (reg_no, name, vaccination_status) VALUES
(123, 'John Doe', 'Yes'),
(456, 'Jane Smith', 'No'),
(789, 'Bob Johnson', 'Yes');

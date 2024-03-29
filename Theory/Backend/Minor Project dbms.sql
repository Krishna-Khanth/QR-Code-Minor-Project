CREATE DATABASE minor_DB;

SHOW DATABASES;

USE minor_DB;

DROP DATABASE minor_DB;

CREATE TABLE `minor_db`.`user` (
  `User_id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `Email_id` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(15) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  `Permission` INT NOT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE INDEX `Email_id_UNIQUE` (`Email_id` ASC),
  UNIQUE INDEX `User_id_UNIQUE` (`User_id` ASC));

-- DROP TABLE user;
-- DROP TABLE registration;
-- DROP TABLE participants;
-- DROP TABLE events;
SHOW TABLES;

SELECT * FROM user;
SELECT * FROM participants;
SELECT * FROM events;
SELECT * FROM registration;

SELECT present FROM registration WHERE p_id = "dummy8-8222222222" AND event_id = "2";

SELECT * FROM participants WHERE p_id = "dummy7-7111111111";

SELECT `minor_db`.`participants`.*, GROUP_CONCAT(`minor_db`.`events`.name, `minor_db`.`registration`.present) as "events"
FROM ((`minor_db`.`participants`
INNER JOIN `minor_db`.`registration` ON `minor_db`.`participants`.p_id = `minor_db`.`registration`.p_id)
INNER JOIN `minor_db`.`events` ON `minor_db`.`events`.event_id = `minor_db`.`registration`.event_id)
group by p_id;


CREATE TABLE `minor_db`.`participants` (
  `p_id` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `Email_id` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC),
  UNIQUE INDEX `idparticipants_UNIQUE` (`p_id` ASC));

CREATE TABLE `minor_db`.`events` (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  PRIMARY KEY (`event_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `event_id_UNIQUE` (`event_id` ASC));

CREATE TABLE `minor_db`.`registration` (
  `r_id` INT NOT NULL AUTO_INCREMENT,
  `p_id` VARCHAR(50) NOT NULL,
  `event_id` INT NOT NULL,
  `present` INT NOT NULL,
  PRIMARY KEY (`r_id`),
  UNIQUE INDEX `r_id_UNIQUE` (`r_id` ASC),
  INDEX `p_id_idx` (`p_id` ASC),
  INDEX `event_id_idx` (`event_id` ASC),
  CONSTRAINT `p_id`
    FOREIGN KEY (`p_id`)
    REFERENCES `minor_db`.`participants` (`p_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `event_id`
    FOREIGN KEY (`event_id`)
    REFERENCES `minor_db`.`events` (`event_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  

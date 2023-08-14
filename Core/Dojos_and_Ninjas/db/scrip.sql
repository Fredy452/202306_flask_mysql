-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_y_ninjas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_y_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_y_ninjas` ;
USE `dojos_y_ninjas` ;

-- -----------------------------------------------------
-- Table `dojos_y_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_y_ninjas`.`dojos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_y_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_y_ninjas`.`ninjas` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `edad` INT NULL,
  `dojo_id` INT UNSIGNED NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_y_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

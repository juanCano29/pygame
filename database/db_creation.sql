-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.6-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para ahorcado
DROP DATABASE IF EXISTS `ahorcado`;
CREATE DATABASE IF NOT EXISTS `ahorcado` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `ahorcado`;

-- Volcando estructura para tabla ahorcado.jugadores
DROP TABLE IF EXISTS `jugadores`;
CREATE TABLE IF NOT EXISTS `jugadores` (
  `nickname` varchar(20) NOT NULL,
  PRIMARY KEY (`nickname`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla ahorcado.palabras
DROP TABLE IF EXISTS `palabras`;
CREATE TABLE IF NOT EXISTS `palabras` (
  `palabra` varchar(30) NOT NULL,
  PRIMARY KEY (`palabra`),
  UNIQUE KEY `palabra` (`palabra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Palabras por defecto*/
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('AUTOMOVIL');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('FRIJOLES');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('SUPERMAN');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('UNIVERSIDAD');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('PERRO');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('PAPANICOLAOU');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('OTORRINOLARINTOLOGO');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('TORREON');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('INGENIERIA');
INSERT INTO `ahorcado`.`palabras` (`palabra`) VALUES ('TECNOLOGIA');

-- Volcando estructura para tabla ahorcado.partidas
DROP TABLE IF EXISTS `partidas`;
CREATE TABLE IF NOT EXISTS `partidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jugador_id` varchar(20) NOT NULL,
  `puntos` int(11) DEFAULT 0,
  `status` varchar(10) NOT NULL DEFAULT 'EN PROCESO',
  PRIMARY KEY (`id`),
  KEY `fk_jugador_partidas` (`jugador_id`),
  CONSTRAINT `fk_jugador_partidas` FOREIGN KEY (`jugador_id`) REFERENCES `jugadores` (`nickname`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Table `ahorcado`.`partidas_gato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ahorcado`.`partidas_gato` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `jugador_id` VARCHAR(20) NULL DEFAULT NULL,
  `partidas_ganadas` INT(11) NULL DEFAULT '0',
  `partidas_perdidas` INT(11) NULL DEFAULT '0',
  `partidas_jugadas` INT(11) NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  CONSTRAINT `partidas_gato_jugadores_nickname_fk`
    FOREIGN KEY (`jugador_id`)
    REFERENCES `ahorcado`.`jugadores` (`nickname`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;



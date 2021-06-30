create database establecimientos;
use establecimientos;
CREATE TABLE `regiones` (
  `id_region` int NOT NULL AUTO_INCREMENT,
  `nombre_region` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_region`),
  UNIQUE KEY `idregiones_UNIQUE` (`id_region`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `comunas` (
  `id_comuna` int NOT NULL AUTO_INCREMENT,
  `nombre_comuna` varchar(100) DEFAULT NULL,
  `codigo_region` varchar(45) DEFAULT NULL,
  `region_comuna` varchar(45) DEFAULT NULL,
  `fase_comuna` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_comuna`),
  UNIQUE KEY `idcomunas_UNIQUE` (`id_comuna`),
  KEY `idregion_idx` (`region_comuna`)
) ENGINE=InnoDB AUTO_INCREMENT=16306 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `negocios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `comuna` varchar(60) DEFAULT NULL,
  `horario` varchar(100) DEFAULT NULL,
  `latitud` varchar(100) DEFAULT NULL,
  `longitud` varchar(100) DEFAULT NULL,
  `fasecomuna` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `idcomuna_idx` (`comuna`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



use establecimientos;
SELECT * FROM comunas where codigo_region = 13;
SELECT nombre_comuna, fase_comuna FROM comunas where codigo_region = 13;

select * from regiones;
select * from comunas;
select * from negocios;


DELETE  FROM `establecimientos`.`comunas`
WHERE id_comuna >=1;
rollback;
DELETE  FROM `establecimientos`.`regiones`
WHERE id_region >=1;


UPDATE `establecimientos`.`comunas`
SET
`fase_comuna` = '2'
WHERE `id_comuna` = 13103;

UPDATE `establecimientos`.`comunas`
SET
`fase_comuna` = '2'
WHERE `id_comuna` = 13105;

CREATE DATABASE `establecimientos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;



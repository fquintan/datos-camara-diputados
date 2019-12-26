
--
-- Table structure for table `Diputade`
--

DROP TABLE IF EXISTS `Diputade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Diputade` (
  `id` int(11) NOT NULL,
  `nombre` varchar(80) NOT NULL,
  `apellido1` varchar(80) NOT NULL,
  `apellido2` varchar(80) DEFAULT NULL,
  `sexo` enum('Femenino','Masculino') DEFAULT NULL,
  `datos` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Militancia`
--

DROP TABLE IF EXISTS `Militancia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Militancia` (
  `partido_id` varchar(30) NOT NULL,
  `diputade_id` int(11) NOT NULL,
  `fecha_desde` datetime NOT NULL,
  `fecha_hasta` datetime NOT NULL,
  PRIMARY KEY (`partido_id`,`diputade_id`,`fecha_desde`,`fecha_hasta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Partido`
--

DROP TABLE IF EXISTS `Partido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Partido` (
  `id` varchar(30) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Votacion`
--

DROP TABLE IF EXISTS `Votacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Votacion` (
  `id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `tipo_votacion` varchar(255) DEFAULT NULL,
  `tipo_quorum` varchar(255) DEFAULT NULL,
  `resultado` varchar(255) DEFAULT NULL,
  `totales` text,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Voto`
--

DROP TABLE IF EXISTS `Voto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Voto` (
  `votacion_id` int(11) NOT NULL,
  `diputade_id` int(11) NOT NULL,
  `voto` enum('En Contra','Afirmativo','Abstención', 'Dispensado') NOT NULL,
  PRIMARY KEY (`votacion_id`,`diputade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


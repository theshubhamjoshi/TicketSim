-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: tc
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booked`
--

DROP TABLE IF EXISTS `booked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booked` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `trainid` varchar(255) DEFAULT NULL,
  `seatno` varchar(255) DEFAULT NULL,
  `coach` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booked`
--

LOCK TABLES `booked` WRITE;
/*!40000 ALTER TABLE `booked` DISABLE KEYS */;
INSERT INTO `booked` VALUES (9,'cjoshi@mitaoe.ac.in','160001','7','AC'),(10,'cjoshi@mitaoe.ac.in','160001','8','AC'),(11,'cjoshi@mitaoe.ac.in','160001','9','AC'),(12,'cjoshi@mitaoe.ac.in','160001','10','AC'),(13,'cjoshi@mitaoe.ac.in','160001','11','AC'),(15,'cjoshi@mitaoe.ac.in','160001','13','AC'),(16,'cjoshi@mitaoe.ac.in','160001','14','AC'),(17,'cjoshi@mitaoe.ac.in','160001','15','AC'),(18,'cjoshi@mitaoe.ac.in','160001','16','AC'),(19,'cjoshi@mitaoe.ac.in','160001','17','AC'),(20,'cjoshi@mitaoe.ac.in','160001','18','AC'),(21,'cjoshi@mitaoe.ac.in','160001','19','AC'),(22,'cjoshi@mitaoe.ac.in','160001','20','AC'),(23,'cjoshi@mitaoe.ac.in','160001','21','AC'),(26,'cjoshi@mitaoe.ac.in','160001','24','AC'),(28,'cjoshi@mitaoe.ac.in','160001','26','AC'),(29,'cjoshi@mitaoe.ac.in','160001','27','AC'),(30,'cjoshi@mitaoe.ac.in','160001','28','AC'),(31,'cjoshi@mitaoe.ac.in','160001','29','AC'),(32,'cjoshi@mitaoe.ac.in','160001','Waiting','AC'),(33,'cjoshi@mitaoe.ac.in','160001','Waiting','AC'),(34,'cjoshi@mitaoe.ac.in','160001','25','AC'),(35,'cjoshi@mitaoe.ac.in','160001','1','AC'),(36,'cjoshi@mitaoe.ac.in','160001','2','AC'),(37,'smartron005@gmail.com','160001','3','SLR'),(38,'smartron005@gmail.com','160001','4','SLR'),(39,'smartron005@gmail.com','160001','5','SLR'),(40,'smartron005@gmail.com','160001','6','SLR'),(41,'smartron005@gmail.com','160001','7','SLR'),(42,'smartron005@gmail.com','160001','8','SLR'),(43,'smartron005@gmail.com','160001','9','SLR'),(44,'smartron005@gmail.com','160001','10','SLR'),(45,'smartron005@gmail.com','160001','11','SLR'),(46,'smartron005@gmail.com','160001','12','SLR'),(47,'smartron005@gmail.com','160001','13','SLR'),(48,'smartron005@gmail.com','160001','14','SLR'),(49,'smartron005@gmail.com','160001','15','SLR'),(50,'smartron005@gmail.com','160001','16','SLR'),(51,'smartron005@gmail.com','160001','17','SLR'),(52,'smartron005@gmail.com','160001','18','SLR'),(53,'smartron005@gmail.com','160001','19','SLR'),(54,'smartron005@gmail.com','160001','20','SLR'),(55,'smartron005@gmail.com','160001','21','SLR'),(56,'smartron005@gmail.com','160001','22','SLR'),(57,'smartron005@gmail.com','160001','23','SLR'),(58,'smartron005@gmail.com','160001','24','SLR'),(59,'smartron005@gmail.com','160001','25','SLR'),(60,'smartron005@gmail.com','160001','26','SLR'),(61,'smartron005@gmail.com','160001','27','SLR'),(62,'smartron005@gmail.com','160001','28','SLR'),(63,'smartron005@gmail.com','160001','29','SLR'),(64,'smartron005@gmail.com','160001','30','SLR'),(65,'smartron005@gmail.com','160001','1','SLR'),(67,'smartron005@gmail.com','160001','2','SLR');
/*!40000 ALTER TABLE `booked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seats`
--

DROP TABLE IF EXISTS `seats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seats` (
  `number` varchar(255) DEFAULT NULL,
  `coach` varchar(255) DEFAULT NULL,
  `seatno` varchar(255) DEFAULT NULL,
  KEY `number` (`number`),
  CONSTRAINT `seats_ibfk_1` FOREIGN KEY (`number`) REFERENCES `train` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seats`
--

LOCK TABLES `seats` WRITE;
/*!40000 ALTER TABLE `seats` DISABLE KEYS */;
INSERT INTO `seats` VALUES ('160001','AC','4'),('160001','AC','5'),('160001','AC','6'),('160001','AC','7'),('160001','AC','8'),('160001','AC','9'),('160001','AC','10'),('160001','AC','11'),('160001','AC','12'),('160001','AC','13'),('160001','AC','14'),('160001','AC','15'),('160001','AC','16'),('160001','AC','17'),('160001','AC','18'),('160001','AC','19'),('160001','AC','20'),('160001','AC','21'),('160001','AC','22'),('160001','AC','23'),('160001','AC','24'),('160001','AC','25'),('160001','AC','26'),('160001','AC','27'),('160001','AC','28'),('160001','AC','29'),('160001','AC','30'),('160002','AC','4'),('160002','AC','5'),('160002','AC','6'),('160002','AC','7'),('160002','AC','8'),('160002','AC','9'),('160002','AC','10'),('160002','AC','11'),('160002','AC','12'),('160002','AC','13'),('160002','AC','14'),('160002','AC','15'),('160002','AC','16'),('160002','AC','17'),('160002','AC','18'),('160002','AC','19'),('160002','AC','20'),('160002','AC','21'),('160002','AC','22'),('160002','AC','23'),('160002','AC','24'),('160002','AC','25'),('160002','AC','26'),('160002','AC','27'),('160002','AC','28'),('160002','AC','29'),('160002','AC','30'),('160003','AC','4'),('160003','AC','5'),('160003','AC','6'),('160003','AC','7'),('160003','AC','8'),('160003','AC','9'),('160003','AC','10'),('160003','AC','11'),('160003','AC','12'),('160003','AC','13'),('160003','AC','14'),('160003','AC','15'),('160003','AC','16'),('160003','AC','17'),('160003','AC','18'),('160003','AC','19'),('160003','AC','20'),('160003','AC','21'),('160003','AC','22'),('160003','AC','23'),('160003','AC','24'),('160003','AC','25'),('160003','AC','26'),('160003','AC','27'),('160003','AC','28'),('160003','AC','29'),('160003','AC','30'),('160001','AC','3');
/*!40000 ALTER TABLE `seats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `train` (
  `number` varchar(255) NOT NULL,
  `source` varchar(255) DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL,
  `schedule` varchar(255) DEFAULT NULL,
  `fair` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES ('160001','Pune','Dhule','23.30','240'),('160002','Dhule','Pune','15.30','240'),('160003','Pune','Aurangabad','16.00','249');
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Shubham SJ','admin@ssjtc.in','Shubham@18'),(2,'Shubham Joshi','ssjoshi@mitaoe.ac.in','123.Ceanation'),(3,'Chandan Joshi','cjoshi@mitaoe.ac.in','Cjoshi@015'),(4,'Shubham','smartron005@gmail.com','123.Ceanation'),(5,'Pranjal Patil','pranjalpatil@gmail.com','Pranjal@123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancy`
--

DROP TABLE IF EXISTS `vacancy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancy` (
  `number` varchar(255) DEFAULT NULL,
  `coach` varchar(255) DEFAULT NULL,
  `available` varchar(255) DEFAULT NULL,
  KEY `number` (`number`),
  CONSTRAINT `vacancy_ibfk_1` FOREIGN KEY (`number`) REFERENCES `train` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancy`
--

LOCK TABLES `vacancy` WRITE;
/*!40000 ALTER TABLE `vacancy` DISABLE KEYS */;
INSERT INTO `vacancy` VALUES ('160001','AC','28'),('160001','SLR','0'),('160002','AC','30'),('160002','SLR','30'),('160003','AC','30'),('160003','SLR','30');
/*!40000 ALTER TABLE `vacancy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waiting`
--

DROP TABLE IF EXISTS `waiting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `waiting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `trainid` varchar(255) DEFAULT NULL,
  `seatno` varchar(255) DEFAULT NULL,
  `coach` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiting`
--

LOCK TABLES `waiting` WRITE;
/*!40000 ALTER TABLE `waiting` DISABLE KEYS */;
INSERT INTO `waiting` VALUES (2,'smartron005@gmail.com','160001','Waiting','SLR'),(3,'smartron005@gmail.com','160001','Waiting','SLR'),(4,'smartron005@gmail.com','160001','Waiting','SLR'),(5,'smartron005@gmail.com','160001','Waiting','SLR'),(6,'smartron005@gmail.com','160001','Waiting','SLR'),(7,'smartron005@gmail.com','160001','Waiting','SLR'),(8,'smartron005@gmail.com','160001','Waiting','SLR'),(9,'smartron005@gmail.com','160001','Waiting','SLR'),(10,'smartron005@gmail.com','160001','Waiting','SLR'),(11,'smartron005@gmail.com','160001','Waiting','SLR'),(12,'smartron005@gmail.com','160001','Waiting','SLR'),(13,'smartron005@gmail.com','160001','Waiting','SLR'),(14,'smartron005@gmail.com','160001','Waiting','SLR');
/*!40000 ALTER TABLE `waiting` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-25 13:03:46

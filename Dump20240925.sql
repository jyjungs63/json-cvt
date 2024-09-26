-- MariaDB dump 10.17  Distrib 10.5.0-MariaDB, for Win64 (AMD64)
--
-- Host: 10.15.20.108    Database: leadsship_f
-- ------------------------------------------------------
-- Server version	10.9.3-MariaDB

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
-- Table structure for table `draft_condition_data`
--

DROP TABLE IF EXISTS `draft_condition_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `draft_condition_data` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `DRAFT_CONDITION` int(1) DEFAULT NULL,
  `VALUE` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `CP_VALUE` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `COMMENT` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hydrodynamic_design_results`
--

DROP TABLE IF EXISTS `hydrodynamic_design_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hydrodynamic_design_results` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `HULLFORM_DEVELOP_REPORT` longblob DEFAULT NULL,
  `LINES_IGES_WIRE` longblob DEFAULT NULL,
  `LINES_IGES_SURFACE` longblob DEFAULT NULL,
  `LINES_HOPT` longblob DEFAULT NULL,
  `LINES_DMP` longblob DEFAULT NULL,
  `LINES_STL` longblob DEFAULT NULL,
  `LINES_OFFSET` longblob DEFAULT NULL,
  `PNG_BIRD_EYE_VIEW` blob DEFAULT NULL,
  `PNG_SIDE_FRONT_VIEW` blob DEFAULT NULL,
  `ESD_DESIGN_REPORT` longblob DEFAULT NULL,
  `ESD_DRAWING` longblob DEFAULT NULL,
  `PROPELLER_DESIGN_REPORT` longblob DEFAULT NULL,
  `PROPELLER_DRAWING` longblob DEFAULT NULL,
  `RUDDER_DRAWING` longblob DEFAULT NULL,
  `SP_HYDROSTATIC_DATA` longblob DEFAULT NULL,
  `WAKE_MEASUREMENT_RESULT` longblob DEFAULT NULL,
  `SP_RESULTS_DESIGN_BARE` longblob DEFAULT NULL,
  `SP_RESULTS_DESIGN_ESD` longblob DEFAULT NULL,
  `SP_RESULTS_SCANT_BARE` longblob DEFAULT NULL,
  `SP_RESULTS_SCANT_ESD` longblob DEFAULT NULL,
  `SP_RESULTS_EEDI_BARE` longblob DEFAULT NULL,
  `SP_RESULTS_EEDI_ESD` longblob DEFAULT NULL,
  `SP_RESULTS_BALLAST_BARE` longblob DEFAULT NULL,
  `SP_RESULTS_BALLAST_ESD` longblob DEFAULT NULL,
  `MODEL_TEST_FULL_REPORT` longblob DEFAULT NULL,
  `CAVITATION_TEST_REPORT` longblob DEFAULT NULL,
  `APPENDIX_1` longblob DEFAULT NULL,
  `APPENDIX_2` longblob DEFAULT NULL,
  `APPENDIX_3` longblob DEFAULT NULL,
  `APPENDIX_4` longblob DEFAULT NULL,
  `APPENDIX_5` longblob DEFAULT NULL,
  `POW_MODEL_SCALE` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `COMMENTS` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `outfitting_design_results`
--

DROP TABLE IF EXISTS `outfitting_design_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outfitting_design_results` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `MACHINARY_ARRANGEMENT` longblob DEFAULT NULL,
  `CWATER_HEAT_BALANCE` longblob DEFAULT NULL,
  `LFSS_FLOW_DIAGRAM` longblob DEFAULT NULL,
  `ACCOMODATION` longblob DEFAULT NULL,
  `MOORING_ARRANGEMENT` longblob DEFAULT NULL,
  `EQUIPMENT_NUMBER` longblob DEFAULT NULL,
  `ELECTRIC_LOAD` longblob DEFAULT NULL,
  `AIP_CERTIFICATION` longblob DEFAULT NULL,
  `APPENDIX_1` longblob DEFAULT NULL,
  `APPENDIX_2` longblob DEFAULT NULL,
  `APPENDIX_3` longblob DEFAULT NULL,
  `APPENDIX_4` longblob DEFAULT NULL,
  `APPENDIX_5` longblob DEFAULT NULL,
  `APPENDIX_6` longblob DEFAULT NULL,
  `APPENDIX_7` longblob DEFAULT NULL,
  `APPENDIX_8` longblob DEFAULT NULL,
  `APPENDIX_9` longblob DEFAULT NULL,
  `COMMENTS` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `propeller_design_results`
--

DROP TABLE IF EXISTS `propeller_design_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `propeller_design_results` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PROP_STATUS` int(1) NOT NULL,
  `VALUE` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `COMMENTS` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`,`PROP_STATUS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ship_initial_results`
--

DROP TABLE IF EXISTS `ship_initial_design_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ship_initial_design_results` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `BASIC_SCHEME` longblob DEFAULT NULL,
  `LIGHTWEIGHT_DISTRIBUTION` longblob DEFAULT NULL,
  `GENERAL_ARRANGEMENT` longblob DEFAULT NULL,
  `RUDDER_ARRANGEMENT` longblob DEFAULT NULL,
  `TRIM_STABILITY` longblob DEFAULT NULL,
  `DAMAGE_STABILITY` longblob DEFAULT NULL,
  `EEDI_CALCULATION` longblob DEFAULT NULL,
  `SOLAS_VISIBILITY` longblob DEFAULT NULL,
  `TONNAGE_CAL` longblob DEFAULT NULL,
  `SRTP_RESULT` longblob DEFAULT NULL,
  `MIDSHIP_DRAWING` longblob DEFAULT NULL,
  `RULE_SCANTLING` longblob DEFAULT NULL,
  `OUTLINE_SPEC` longblob DEFAULT NULL,
  `POCKET_PLAN` longblob DEFAULT NULL,
  `REPORT_SUMMARY` longblob DEFAULT NULL,
  `PROJECT_FULL_REPORT` longblob DEFAULT NULL,
  `AIP_CERTIFICATION` longblob DEFAULT NULL,
  `APPENDIX_1` longblob DEFAULT NULL,
  `APPENDIX_2` longblob DEFAULT NULL,
  `APPENDIX_3` longblob DEFAULT NULL,
  `APPENDIX_4` longblob DEFAULT NULL,
  `APPENDIX_5` longblob DEFAULT NULL,
  `COMMENTS` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ship_project_data`
--

DROP TABLE IF EXISTS `ship_project_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ship_project_data` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `SHIP_TITLE` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `GENERAL_INFORMATION` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SHIP_INFORMATION` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ENGINE_ROOM` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PROPELLER` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ETC` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-25 15:13:17

    CREATE TABLE `project_data` (
  `PROJECT_NO` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `SHIP_TITLE` varchar(70) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `GENERAL_INFORMATION` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SHIP_INFORMATION` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ENGINE_ROOM` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PROPELLER` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ETC` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROJECT_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
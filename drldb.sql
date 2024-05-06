-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: drldb
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'CTSV'),(1,'SV'),(3,'TLSV');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add khoa',6,'add_khoa'),(22,'Can change khoa',6,'change_khoa'),(23,'Can delete khoa',6,'delete_khoa'),(24,'Can view khoa',6,'view_khoa'),(25,'Can add lop',7,'add_lop'),(26,'Can change lop',7,'change_lop'),(27,'Can delete lop',7,'delete_lop'),(28,'Can view lop',7,'view_lop'),(29,'Can add quyche',8,'add_quyche'),(30,'Can change quyche',8,'change_quyche'),(31,'Can delete quyche',8,'delete_quyche'),(32,'Can view quyche',8,'view_quyche'),(33,'Can add tag',9,'add_tag'),(34,'Can change tag',9,'change_tag'),(35,'Can delete tag',9,'delete_tag'),(36,'Can view tag',9,'view_tag'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add thanh tich ngoai khoa',11,'add_thanhtichngoaikhoa'),(42,'Can change thanh tich ngoai khoa',11,'change_thanhtichngoaikhoa'),(43,'Can delete thanh tich ngoai khoa',11,'delete_thanhtichngoaikhoa'),(44,'Can view thanh tich ngoai khoa',11,'view_thanhtichngoaikhoa'),(45,'Can add hoat dong',12,'add_hoatdong'),(46,'Can change hoat dong',12,'change_hoatdong'),(47,'Can delete hoat dong',12,'delete_hoatdong'),(48,'Can view hoat dong',12,'view_hoatdong'),(49,'Can add comment',13,'add_comment'),(50,'Can change comment',13,'change_comment'),(51,'Can delete comment',13,'delete_comment'),(52,'Can view comment',13,'view_comment'),(53,'Can add user',14,'add_usersv'),(54,'Can change user',14,'change_usersv'),(55,'Can delete user',14,'delete_usersv'),(56,'Can view user',14,'view_usersv'),(57,'Can add sinh vien minh chung hoat dong',15,'add_sinhvienminhchunghoatdong'),(58,'Can change sinh vien minh chung hoat dong',15,'change_sinhvienminhchunghoatdong'),(59,'Can delete sinh vien minh chung hoat dong',15,'delete_sinhvienminhchunghoatdong'),(60,'Can view sinh vien minh chung hoat dong',15,'view_sinhvienminhchunghoatdong'),(61,'Can add like',16,'add_like'),(62,'Can change like',16,'change_like'),(63,'Can delete like',16,'delete_like'),(64,'Can view like',16,'view_like'),(65,'Can add application',17,'add_application'),(66,'Can change application',17,'change_application'),(67,'Can delete application',17,'delete_application'),(68,'Can view application',17,'view_application'),(69,'Can add access token',18,'add_accesstoken'),(70,'Can change access token',18,'change_accesstoken'),(71,'Can delete access token',18,'delete_accesstoken'),(72,'Can view access token',18,'view_accesstoken'),(73,'Can add grant',19,'add_grant'),(74,'Can change grant',19,'change_grant'),(75,'Can delete grant',19,'delete_grant'),(76,'Can view grant',19,'view_grant'),(77,'Can add refresh token',20,'add_refreshtoken'),(78,'Can change refresh token',20,'change_refreshtoken'),(79,'Can delete refresh token',20,'delete_refreshtoken'),(80,'Can view refresh token',20,'view_refreshtoken'),(81,'Can add id token',21,'add_idtoken'),(82,'Can change id token',21,'change_idtoken'),(83,'Can delete id token',21,'delete_idtoken'),(84,'Can view id token',21,'view_idtoken'),(85,'Can add hoc ki',22,'add_hocki'),(86,'Can change hoc ki',22,'change_hocki'),(87,'Can delete hoc ki',22,'delete_hocki'),(88,'Can view hoc ki',22,'view_hocki');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-04-17 08:54:08.305424','1','SV',1,'[{\"added\": {}}]',3,1),(2,'2024-04-18 08:30:16.311356','2','CTSV',1,'[{\"added\": {}}]',3,1),(3,'2024-04-18 08:30:31.041289','3','TLSV',1,'[{\"added\": {}}]',3,1),(4,'2024-04-19 18:42:56.086871','1','Mùa hè',1,'[{\"added\": {}}]',9,1),(5,'2024-04-19 18:43:30.123015','1','Điều 1',1,'[{\"added\": {}}]',8,1),(6,'2024-04-19 18:43:35.426785','1','Trại hè',1,'[{\"added\": {}}]',12,1),(7,'2024-04-20 05:06:17.942070','1','SinhVienMinhChungHoatDong object (1)',1,'[{\"added\": {}}]',15,1),(8,'2024-05-04 07:34:54.563787','1','CNTT',1,'[{\"added\": {}}]',6,1),(9,'2024-05-04 07:35:11.080103','2','TCNH',1,'[{\"added\": {}}]',6,1),(10,'2024-05-04 07:50:13.668366','1','ThanhTichNgoaiKhoa object (1)',1,'[{\"added\": {}}]',11,1),(11,'2024-05-04 07:50:51.769485','1','DH20IT01',1,'[{\"added\": {}}]',7,1),(12,'2024-05-04 07:51:09.451430','7','test',2,'[{\"changed\": {\"fields\": [\"Avatar\", \"Khoa\", \"Lop\"]}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(13,'DRL','comment'),(12,'DRL','hoatdong'),(22,'DRL','hocki'),(6,'DRL','khoa'),(16,'DRL','like'),(7,'DRL','lop'),(8,'DRL','quyche'),(15,'DRL','sinhvienminhchunghoatdong'),(9,'DRL','tag'),(11,'DRL','thanhtichngoaikhoa'),(10,'DRL','user'),(14,'DRL','usersv'),(18,'oauth2_provider','accesstoken'),(17,'oauth2_provider','application'),(19,'oauth2_provider','grant'),(21,'oauth2_provider','idtoken'),(20,'oauth2_provider','refreshtoken'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-16 05:38:06.274346'),(2,'contenttypes','0002_remove_content_type_name','2024-04-16 05:38:06.354710'),(3,'auth','0001_initial','2024-04-16 05:38:06.640022'),(4,'auth','0002_alter_permission_name_max_length','2024-04-16 05:38:06.704952'),(5,'auth','0003_alter_user_email_max_length','2024-04-16 05:38:06.713486'),(6,'auth','0004_alter_user_username_opts','2024-04-16 05:38:06.722538'),(7,'auth','0005_alter_user_last_login_null','2024-04-16 05:38:06.731183'),(8,'auth','0006_require_contenttypes_0002','2024-04-16 05:38:06.735164'),(9,'auth','0007_alter_validators_add_error_messages','2024-04-16 05:38:06.742661'),(10,'auth','0008_alter_user_username_max_length','2024-04-16 05:38:06.750733'),(11,'auth','0009_alter_user_last_name_max_length','2024-04-16 05:38:06.758310'),(12,'auth','0010_alter_group_name_max_length','2024-04-16 05:38:06.777562'),(13,'auth','0011_update_proxy_permissions','2024-04-16 05:38:06.786719'),(14,'auth','0012_alter_user_first_name_max_length','2024-04-16 05:38:06.793937'),(15,'DRL','0001_initial','2024-04-16 05:38:08.149970'),(16,'admin','0001_initial','2024-04-16 05:38:08.290974'),(17,'admin','0002_logentry_remove_auto_add','2024-04-16 05:38:08.303679'),(18,'admin','0003_logentry_add_action_flag_choices','2024-04-16 05:38:08.317092'),(19,'oauth2_provider','0001_initial','2024-04-16 05:38:09.142710'),(20,'oauth2_provider','0002_auto_20190406_1805','2024-04-16 05:38:09.224767'),(21,'oauth2_provider','0003_auto_20201211_1314','2024-04-16 05:38:09.298901'),(22,'oauth2_provider','0004_auto_20200902_2022','2024-04-16 05:38:09.912994'),(23,'oauth2_provider','0005_auto_20211222_2352','2024-04-16 05:38:10.012083'),(24,'oauth2_provider','0006_alter_application_client_secret','2024-04-16 05:38:10.056252'),(25,'oauth2_provider','0007_application_post_logout_redirect_uris','2024-04-16 05:38:10.150704'),(26,'sessions','0001_initial','2024-04-16 05:38:10.192812'),(27,'DRL','0002_hocki_hoatdong_quy_che_quyche_diem_toi_da_and_more','2024-04-16 16:36:17.380425'),(28,'DRL','0003_like_is_like','2024-04-16 16:55:16.610720'),(29,'DRL','0004_alter_user_phone','2024-04-17 06:45:20.708015'),(30,'DRL','0005_alter_usersv_hoat_dongs','2024-04-19 10:26:57.307404'),(31,'DRL','0006_alter_usersv_hoat_dongs','2024-04-19 10:33:54.706557'),(32,'DRL','0007_alter_usersv_hoat_dongs','2024-04-19 12:05:23.518786'),(33,'DRL','0008_remove_usersv_hoat_dongs_hoatdong_user_svs','2024-04-19 18:50:03.105581'),(34,'DRL','0009_usersv_thanh_tich_ngoai_khoa','2024-04-20 02:20:14.208050'),(35,'DRL','0010_remove_usersv_thanh_tich_ngoai_khoa_and_more','2024-04-30 15:13:43.741829'),(36,'DRL','0011_alter_hoatdong_options_alter_hocki_options_and_more','2024-05-04 07:49:09.806799');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1lnnwh4z1pspwhr4gqa2e67wrv3pau6c','.eJxVjMsOwiAQRf-FtSEM5enSvd9AYBikaiAp7cr479qkC93ec859sRC3tYZt0BLmzM4M2Ol3SxEf1HaQ77HdOsfe1mVOfFf4QQe_9kzPy-H-HdQ46reegIyKYipFQSxSaweIhTQqUwCBpDfCCVdcMpOQqNBmC9ZJlXy2xnr2_gDbaTdO:1s38Oe:wqQO2PPNoTx12AX3-GbKEHgywSPe1Yo4rKKQe1sXuvg','2024-05-18 05:57:20.180296'),('ph1xisinij8de48xw1rkvztgdsagr4si','.eJxVjMsOwiAQRf-FtSEM5enSvd9AYBikaiAp7cr479qkC93ec859sRC3tYZt0BLmzM4M2Ol3SxEf1HaQ77HdOsfe1mVOfFf4QQe_9kzPy-H-HdQ46reegIyKYipFQSxSaweIhTQqUwCBpDfCCVdcMpOQqNBmC9ZJlXy2xnr2_gDbaTdO:1ry2XU:IZFWEUPdFC9Z6rtrprtVx_IMZ3X00a6RdpwD2rPxnkk','2024-05-04 04:41:24.868115');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_comment`
--

DROP TABLE IF EXISTS `drl_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `content` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hoat_dong_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DRL_comment_hoat_dong_id_7a95f3c8_fk_DRL_hoatdong_id` (`hoat_dong_id`),
  KEY `DRL_comment_user_id_f4a609ea_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `DRL_comment_hoat_dong_id_7a95f3c8_fk_DRL_hoatdong_id` FOREIGN KEY (`hoat_dong_id`) REFERENCES `drl_hoatdong` (`id`),
  CONSTRAINT `DRL_comment_user_id_f4a609ea_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_comment`
--

LOCK TABLES `drl_comment` WRITE;
/*!40000 ALTER TABLE `drl_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `drl_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_hoatdong`
--

DROP TABLE IF EXISTS `drl_hoatdong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_hoatdong` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mo_ta` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngay_du_kien` date NOT NULL,
  `ngay_dien_ra` date NOT NULL,
  `ngay_het` date NOT NULL,
  `diem_cong` double NOT NULL,
  `quy_che_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DRL_hoatdong_quy_che_id_bbc9e899_fk_DRL_quyche_id` (`quy_che_id`),
  CONSTRAINT `DRL_hoatdong_quy_che_id_bbc9e899_fk_DRL_quyche_id` FOREIGN KEY (`quy_che_id`) REFERENCES `drl_quyche` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_hoatdong`
--

LOCK TABLES `drl_hoatdong` WRITE;
/*!40000 ALTER TABLE `drl_hoatdong` DISABLE KEYS */;
INSERT INTO `drl_hoatdong` VALUES (1,'2024-04-20','2024-04-20',1,'Trại hè','<p><u><em><strong>Trại h&egrave; vui nhất 2024</strong></em></u></p>','2024-04-19','2024-04-19','2024-04-30',5,1),(2,'2024-04-20','2024-04-20',1,'test','test','2024-04-20','2024-04-20','2024-04-30',5,1),(3,'2024-04-20','2024-04-20',1,'test2','test2','2024-04-20','2024-04-20','2024-04-30',5,1);
/*!40000 ALTER TABLE `drl_hoatdong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_hoatdong_tags`
--

DROP TABLE IF EXISTS `drl_hoatdong_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_hoatdong_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hoatdong_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DRL_hoatdong_tags_hoatdong_id_tag_id_7116eac3_uniq` (`hoatdong_id`,`tag_id`),
  KEY `DRL_hoatdong_tags_tag_id_dbe70387_fk_DRL_tag_id` (`tag_id`),
  CONSTRAINT `DRL_hoatdong_tags_hoatdong_id_d5b869c4_fk_DRL_hoatdong_id` FOREIGN KEY (`hoatdong_id`) REFERENCES `drl_hoatdong` (`id`),
  CONSTRAINT `DRL_hoatdong_tags_tag_id_dbe70387_fk_DRL_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `drl_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_hoatdong_tags`
--

LOCK TABLES `drl_hoatdong_tags` WRITE;
/*!40000 ALTER TABLE `drl_hoatdong_tags` DISABLE KEYS */;
INSERT INTO `drl_hoatdong_tags` VALUES (1,1,1),(2,2,1),(3,3,1);
/*!40000 ALTER TABLE `drl_hoatdong_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_hoatdong_user_svs`
--

DROP TABLE IF EXISTS `drl_hoatdong_user_svs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_hoatdong_user_svs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hoatdong_id` bigint NOT NULL,
  `usersv_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DRL_hoatdong_user_svs_hoatdong_id_usersv_id_a1d7357d_uniq` (`hoatdong_id`,`usersv_id`),
  KEY `DRL_hoatdong_user_sv_usersv_id_9af9e660_fk_DRL_users` (`usersv_id`),
  CONSTRAINT `DRL_hoatdong_user_sv_usersv_id_9af9e660_fk_DRL_users` FOREIGN KEY (`usersv_id`) REFERENCES `drl_usersv` (`user_ptr_id`),
  CONSTRAINT `DRL_hoatdong_user_svs_hoatdong_id_29444911_fk_DRL_hoatdong_id` FOREIGN KEY (`hoatdong_id`) REFERENCES `drl_hoatdong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_hoatdong_user_svs`
--

LOCK TABLES `drl_hoatdong_user_svs` WRITE;
/*!40000 ALTER TABLE `drl_hoatdong_user_svs` DISABLE KEYS */;
INSERT INTO `drl_hoatdong_user_svs` VALUES (1,2,7),(2,3,7);
/*!40000 ALTER TABLE `drl_hoatdong_user_svs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_hocki`
--

DROP TABLE IF EXISTS `drl_hocki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_hocki` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nien_khoa` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `thoi_gian_bat_dau` date NOT NULL,
  `thoi_gian_ket_thuc` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_hocki`
--

LOCK TABLES `drl_hocki` WRITE;
/*!40000 ALTER TABLE `drl_hocki` DISABLE KEYS */;
/*!40000 ALTER TABLE `drl_hocki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_khoa`
--

DROP TABLE IF EXISTS `drl_khoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_khoa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_khoa`
--

LOCK TABLES `drl_khoa` WRITE;
/*!40000 ALTER TABLE `drl_khoa` DISABLE KEYS */;
INSERT INTO `drl_khoa` VALUES (1,'2024-05-04','2024-05-04',1,'CNTT'),(2,'2024-05-04','2024-05-04',1,'TCNH');
/*!40000 ALTER TABLE `drl_khoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_like`
--

DROP TABLE IF EXISTS `drl_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `hoat_dong_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `is_like` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DRL_like_user_id_hoat_dong_id_796e3929_uniq` (`user_id`,`hoat_dong_id`),
  KEY `DRL_like_hoat_dong_id_2a9b94ea_fk_DRL_hoatdong_id` (`hoat_dong_id`),
  CONSTRAINT `DRL_like_hoat_dong_id_2a9b94ea_fk_DRL_hoatdong_id` FOREIGN KEY (`hoat_dong_id`) REFERENCES `drl_hoatdong` (`id`),
  CONSTRAINT `DRL_like_user_id_a1bf1472_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_like`
--

LOCK TABLES `drl_like` WRITE;
/*!40000 ALTER TABLE `drl_like` DISABLE KEYS */;
/*!40000 ALTER TABLE `drl_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_lop`
--

DROP TABLE IF EXISTS `drl_lop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_lop` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_lop`
--

LOCK TABLES `drl_lop` WRITE;
/*!40000 ALTER TABLE `drl_lop` DISABLE KEYS */;
INSERT INTO `drl_lop` VALUES (1,'2024-05-04','2024-05-04',1,'DH20IT01');
/*!40000 ALTER TABLE `drl_lop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_quyche`
--

DROP TABLE IF EXISTS `drl_quyche`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_quyche` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mo_ta` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `diem_toi_da` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_quyche`
--

LOCK TABLES `drl_quyche` WRITE;
/*!40000 ALTER TABLE `drl_quyche` DISABLE KEYS */;
INSERT INTO `drl_quyche` VALUES (1,'2024-04-20','2024-04-20',1,'Điều 1','<p>Điều 1</p>',20);
/*!40000 ALTER TABLE `drl_quyche` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_sinhvienminhchunghoatdong`
--

DROP TABLE IF EXISTS `drl_sinhvienminhchunghoatdong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_sinhvienminhchunghoatdong` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `minh_chung` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `trang_thai` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hoat_dong_id` bigint NOT NULL,
  `sinh_vien_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DRL_sinhvienminhchun_hoat_dong_id_e423c20c_fk_DRL_hoatd` (`hoat_dong_id`),
  KEY `DRL_sinhvienminhchun_sinh_vien_id_4e929fa0_fk_DRL_users` (`sinh_vien_id`),
  CONSTRAINT `DRL_sinhvienminhchun_hoat_dong_id_e423c20c_fk_DRL_hoatd` FOREIGN KEY (`hoat_dong_id`) REFERENCES `drl_hoatdong` (`id`),
  CONSTRAINT `DRL_sinhvienminhchun_sinh_vien_id_4e929fa0_fk_DRL_users` FOREIGN KEY (`sinh_vien_id`) REFERENCES `drl_usersv` (`user_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_sinhvienminhchunghoatdong`
--

LOCK TABLES `drl_sinhvienminhchunghoatdong` WRITE;
/*!40000 ALTER TABLE `drl_sinhvienminhchunghoatdong` DISABLE KEYS */;
INSERT INTO `drl_sinhvienminhchunghoatdong` VALUES (1,'2024-04-20','2024-04-20',1,'Untitled.png','Đang xử lý',1,7);
/*!40000 ALTER TABLE `drl_sinhvienminhchunghoatdong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_tag`
--

DROP TABLE IF EXISTS `drl_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_tag`
--

LOCK TABLES `drl_tag` WRITE;
/*!40000 ALTER TABLE `drl_tag` DISABLE KEYS */;
INSERT INTO `drl_tag` VALUES (1,'2024-04-20','2024-04-20',1,'Mùa hè');
/*!40000 ALTER TABLE `drl_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_thanhtichngoaikhoa`
--

DROP TABLE IF EXISTS `drl_thanhtichngoaikhoa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_thanhtichngoaikhoa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` date NOT NULL,
  `updated_date` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `diem` double NOT NULL,
  `thanh_tich` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sinh_vien_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sinh_vien_id` (`sinh_vien_id`),
  CONSTRAINT `DRL_thanhtichngoaikh_sinh_vien_id_87123292_fk_DRL_users` FOREIGN KEY (`sinh_vien_id`) REFERENCES `drl_usersv` (`user_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_thanhtichngoaikhoa`
--

LOCK TABLES `drl_thanhtichngoaikhoa` WRITE;
/*!40000 ALTER TABLE `drl_thanhtichngoaikhoa` DISABLE KEYS */;
INSERT INTO `drl_thanhtichngoaikhoa` VALUES (1,'2024-05-04','2024-05-04',1,87,'Giỏi',7);
/*!40000 ALTER TABLE `drl_thanhtichngoaikhoa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_user`
--

DROP TABLE IF EXISTS `drl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `avatar` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `DRL_user_phone_373eafcc_uniq` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_user`
--

LOCK TABLES `drl_user` WRITE;
/*!40000 ALTER TABLE `drl_user` DISABLE KEYS */;
INSERT INTO `drl_user` VALUES (1,'pbkdf2_sha256$600000$IUdVf99luYE8K92MJxDT7I$pFq4MKe3Ytdzl7p36yHH06C5LCpqH8RtC7ZAO7HZDiY=','2024-05-04 05:57:20.075425',1,'admin','','','admin@admin.com',1,1,'2024-04-16 05:41:01.847453',NULL,''),(7,'pbkdf2_sha256$600000$W1rbueae9EVbS8FKACAVyu$Kj8DyxadSVqBh08/O+D7kNshxw3KCxnA4rmG6T4ahQs=',NULL,0,'test','test','test','test@gmail.com',0,1,'2024-04-18 07:32:13.000000','image/upload/v1714809069/g4gye3ww1raeol9n9h0q.png','123456'),(9,'pbkdf2_sha256$600000$Nf3vvGKJTcqL9luPyFXJIw$D9L0feqq4YYPoEIQiRI57J92xE/17Dctem6SMdCFACQ=',NULL,0,'test1','test1','test1','test1@gmail.com',0,1,'2024-04-18 08:15:57.372818','image/upload/v1713428159/nf0ga6w9rnius7qjooue.png',NULL),(13,'pbkdf2_sha256$600000$GhILsUHdeBGrGzcRTq4aG3$QGfO0nysbBmiOGJCI2sBFyVryxlG88geTvGUduWLabA=',NULL,0,'testctsv','testctsv','testctsv','testctsv@gmail.com',0,1,'2024-04-18 08:57:15.689555','image/upload/v1713430637/njmo4u1dy9hp5cm831fa.png',NULL);
/*!40000 ALTER TABLE `drl_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_user_groups`
--

DROP TABLE IF EXISTS `drl_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DRL_user_groups_user_id_group_id_809e76f7_uniq` (`user_id`,`group_id`),
  KEY `DRL_user_groups_group_id_c82bd4c4_fk_auth_group_id` (`group_id`),
  CONSTRAINT `DRL_user_groups_group_id_c82bd4c4_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `DRL_user_groups_user_id_403de664_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_user_groups`
--

LOCK TABLES `drl_user_groups` WRITE;
/*!40000 ALTER TABLE `drl_user_groups` DISABLE KEYS */;
INSERT INTO `drl_user_groups` VALUES (1,7,1),(6,9,3),(5,13,2);
/*!40000 ALTER TABLE `drl_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_user_user_permissions`
--

DROP TABLE IF EXISTS `drl_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DRL_user_user_permissions_user_id_permission_id_f1c194bb_uniq` (`user_id`,`permission_id`),
  KEY `DRL_user_user_permis_permission_id_0de5dc3b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `DRL_user_user_permis_permission_id_0de5dc3b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `DRL_user_user_permissions_user_id_8c933e22_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_user_user_permissions`
--

LOCK TABLES `drl_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `drl_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `drl_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drl_usersv`
--

DROP TABLE IF EXISTS `drl_usersv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drl_usersv` (
  `user_ptr_id` bigint NOT NULL,
  `khoa_id` bigint DEFAULT NULL,
  `lop_id` bigint DEFAULT NULL,
  `mssv` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  UNIQUE KEY `mssv` (`mssv`),
  KEY `DRL_usersv_khoa_id_0ab958ca_fk_DRL_khoa_id` (`khoa_id`),
  KEY `DRL_usersv_lop_id_5e94a10c_fk_DRL_lop_id` (`lop_id`),
  CONSTRAINT `DRL_usersv_khoa_id_0ab958ca_fk_DRL_khoa_id` FOREIGN KEY (`khoa_id`) REFERENCES `drl_khoa` (`id`),
  CONSTRAINT `DRL_usersv_lop_id_5e94a10c_fk_DRL_lop_id` FOREIGN KEY (`lop_id`) REFERENCES `drl_lop` (`id`),
  CONSTRAINT `DRL_usersv_user_ptr_id_74225651_fk_DRL_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drl_usersv`
--

LOCK TABLES `drl_usersv` WRITE;
/*!40000 ALTER TABLE `drl_usersv` DISABLE KEYS */;
INSERT INTO `drl_usersv` VALUES (7,1,1,'test');
/*!40000 ALTER TABLE `drl_usersv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint DEFAULT NULL,
  `id_token_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  UNIQUE KEY `id_token_id` (`id_token_id`),
  KEY `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr` FOREIGN KEY (`id_token_id`) REFERENCES `oauth2_provider_idtoken` (`id`),
  CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_accesstoken` VALUES (1,'VrfnWPGX3XUudFnmSQbMVwMxKXllgj','2024-04-20 15:00:26.645086','read write',2,7,'2024-04-20 05:00:26.645086','2024-04-20 05:00:26.645086',NULL,NULL),(2,'L34XUA7hTY9VzRf0TVENEaXVGHiQ2D','2024-04-20 15:16:27.988897','read write',2,9,'2024-04-20 05:16:27.988897','2024-04-20 05:16:27.988897',NULL,NULL);
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `redirect_uris` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_type` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `authorization_grant_type` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_secret` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `algorithm` varchar(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  `post_logout_redirect_uris` longtext COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_user_id_79829054_fk_DRL_user_id` (`user_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
INSERT INTO `oauth2_provider_application` VALUES (2,'AsZctVfQHD7HcVIy01Uxb5wCtcLiGdBxPLOuQ25Q','','confidential','password','pbkdf2_sha256$600000$ZpMZHRJBHnFuJXPcedn41F$7UTbYcbQti0driTZkc33ok91XpJroiO9h/KvMXIMNgA=','DRL Oauth2',1,0,'2024-04-20 04:55:34.334182','2024-04-20 04:55:34.334182','','');
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `code_challenge` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `code_challenge_method` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nonce` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `claims` longtext COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_idtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_idtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_idtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jti` char(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jti` (`jti`),
  KEY `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_idtoken_user_id_dd512b59_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_idtoken_user_id_dd512b59_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_idtoken`
--

LOCK TABLES `oauth2_provider_idtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `access_token_id` bigint DEFAULT NULL,
  `application_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  KEY `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_DRL_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_DRL_user_id` FOREIGN KEY (`user_id`) REFERENCES `drl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_refreshtoken` VALUES (1,'kRfQSgfimhntHLmzLRt8VOMPgDMPp2',1,2,7,'2024-04-20 05:00:26.705038','2024-04-20 05:00:26.705038',NULL),(2,'xXLNsPF34gUnk1qWJu5Dvv5eR4CKhN',2,2,9,'2024-04-20 05:16:27.992881','2024-04-20 05:16:27.992881',NULL);
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-06 22:02:13

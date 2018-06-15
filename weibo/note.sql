DROP TABLE IF EXISTS `note`;
CREATE TABLE `note` (
  `note_id` int(10) NOT NULL AUTO_INCREMENT,
  `note_title` text CHARACTER SET utf8 NOT NULL,
  `note_url` text CHARACTER SET utf8 NOT NULL,
  `note_context` text CHARACTER SET utf8,
  `note_push_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `note_update_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `note_spider_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `note_push_person_id` bigint(255) NOT NULL,
  `note_audit` int(1) DEFAULT '0',
  `note_update` int(1) DEFAULT '1',
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
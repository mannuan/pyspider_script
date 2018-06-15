DROP TABLE IF EXISTS `invitation`;
CREATE TABLE `invitation` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `note_id` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `note_title` text CHARACTER SET utf8,
  `note_url` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `note_context` text CHARACTER SET utf8,
  `source` varchar(50) CHARACTER SET utf8 NOT NULL,
  `push_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `crawl_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `push_name` varchar(50) CHARACTER SET utf8 NOT NULL,
  `audit` int(1) DEFAULT '0',
  `type_id` int(5) DEFAULT '17',
  `indexed` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `invitation_trend`;
CREATE TABLE `invitation_trend` (
  `id` int(10) NOT NULL,
  `crawl_time` varchar(20) NOT NULL,
  `reposts_count` int(10) NOT NULL DEFAULT '0',
  `comments_count` int(10) NOT NULL DEFAULT '0',
  `attitudes_count` int(10) NOT NULL DEFAULT '0',
  `looks_count` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`crawl_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--ALTER TABLE `invitation` DEFAULT CHARACTER SET utf8mb4;
--alter table website modify column id int(10) NOT NULL AUTO_INCREMENT;
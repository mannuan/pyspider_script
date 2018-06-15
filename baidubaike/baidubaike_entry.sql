DROP TABLE IF EXISTS `baidubaike_entry`;
CREATE TABLE `baidubaike_entry` (
  `id` bigint(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `url` text NOT NULL,
  `state` int(10) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
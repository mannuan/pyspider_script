DROP TABLE IF EXISTS `baidubaike`;
CREATE TABLE `baidubaike` (
  `content` text,
  `crawl_time` varchar(100),
  `river_name` varchar(100) NOT NULL,
  `url` text,
  PRIMARY KEY (`river_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
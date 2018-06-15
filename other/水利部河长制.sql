DROP TABLE IF EXISTS `shuilibuhezhangzhi`;
CREATE TABLE `shuilibuhezhangzhi` (
  `url` varchar(200) NOT NULL,
  `title` varchar(1000) NOT NULL,
  `created_at` varchar(50) NOT NULL,
  `text` varchar(10000),
  `editor` varchar(20),
  `forum_name` varchar(20) NOT NUll,
  `type_id` int(3) NOT NUll,
  `crawl_time` varchar(20) NOT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
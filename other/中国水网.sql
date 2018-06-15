DROP TABLE IF EXISTS `zhongguoshuiwang`;
CREATE TABLE `zhongguoshuiwang` (
  `url` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `file_type` varchar(200) NOT NULL,
  `created_at` varchar(50) NOT NULL,
  `dispatch_unit` varchar(200) NOT NULL,
  `file_number` varchar(100) NOT NULL,
  `key_words` varchar(200) NOT NULL,
  `abstract` varchar(1000) NOT NULL,
  `forum_name` varchar(20) NOT NULL,
  `type_id` int(5) NOT NULL,
  `file_name` varchar(10) NOT NULL,
  `file_url` varchar(200) NOT NULL,
  `crawl_time` varchar(20) NOT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
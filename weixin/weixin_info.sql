DROP TABLE IF EXISTS `weixin_info`;
CREATE TABLE `weixin_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `time` varchar(50) NOT NULL,
  `public_name` varchar(100) NOT NULL,
  `main_body` text NOT NULL,
  `spider_time` varchar(100) NOT NULL,
  `url` text,
  `type_id` int(5) DEFAULT '0',
  `indexed` int(1) DEFAULT '0',
  `pushed` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
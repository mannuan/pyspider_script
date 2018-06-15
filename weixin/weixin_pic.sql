DROP TABLE IF EXISTS `weixin_pic`;
CREATE TABLE `weixin_pic` (
  `img_url` varchar(1000) NOT NULL,
  `server_path` varchar(1000) NOT NULL,
  `local_path` varchar(1000) NOT NULL,
  `crawl_time` varchar(100) NOT NULL,
  PRIMARY KEY (`img_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
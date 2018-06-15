DROP TABLE IF EXISTS `type`;
CREATE TABLE `type` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

INSERT INTO type(name) values('未分类'),('标准'),('政府发文'),('治理方案'),('治理案例'),('治理评估'),('治理科技'),('动态');
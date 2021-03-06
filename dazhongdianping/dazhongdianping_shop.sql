DROP TABLE IF EXISTS `dazhongdianping_shop`;
CREATE TABLE `dazhongdianping_shop` (
  `address` varchar(1000),
  `crawl_time` varchar(100) NOT NULL,
  `authorityLabelType` int(10),
  `branchName` varchar(100),
  `categoryId` int(10),
  `categoryName` varchar(100),
  `cityId` int(100) NOT NULL,
  `defaultPic` text,
  `dishtags` text,
  `id` bigint(100) NOT NULL,
  `matchText` text,
  `name` varchar(1000) NOT NULL,
  `newShop` varchar(100),
  `orderDish` varchar(100),
  `priceText` varchar(200),
  `regionName` varchar(1000),
  `reviewCount` bigint(100),
  `scoreText` varchar(1000),
  `shopPower` int(100),
  `shopType` int(100),
  `status` int(100),
  `tag` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
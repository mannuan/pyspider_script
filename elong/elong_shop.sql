DROP TABLE IF EXISTS `elong_shop`;
CREATE TABLE `elong_shop` (
  `address` text,
  `businessAreaName` varchar(100),
  `commentPoint` varchar(100),
  `commentScore` int(100),
  `crawl_time` varchar(100),
  `districtName` varchar(100),
  `hotelName` varchar(100),
  `id` int(100) NOT NULL,
  `lmOriPrice` int(100),
  `lowestPrice` int(100),
  `minPriceInventories` varchar(100),
  `minPriceSubCouponInventories` varchar(100),
  `picUrl` text,
  `placeName` varchar(100),
  `starLevel` int(100),
  `totalCommentCount` int(100),
  `trafficInfo` varchar(100),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
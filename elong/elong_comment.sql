DROP TABLE IF EXISTS `elong_comment`;
CREATE TABLE `elong_comment` (
  `commentDateTime` varchar(100),
  `commentFrom` varchar(100),
  `commentScoreTotal` int(100),
  `content` text,
  `crawl_time` varchar(100),
  `id` bigint(100) NOT NULL,
  `isMarrow` int(100),
  `largeImagePath` text,
  `replys` text,
  `roomTypeName` varchar(100),
  `travelType` int(100),
  `userName` varchar(100),
  `userRank` int(100),
  PRIMARY KEY (`id`,`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
DROP TABLE IF EXISTS `weibo_user`;
CREATE TABLE `weibo_user` (
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(100),
  `user_verified_reason` varchar(100),
  `crawl_time` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- DROP TABLE IF EXISTS `weibo_weibo`;
-- CREATE TABLE `weibo_weibo` (
--   `user_id` varchar(50) NOT NULL,
--   `user_name` varchar(50) NOT NULL,
--   `weibo_id` varchar(50) NOT NULL,
--   `created_at` varchar(20) NOT NULL,
--   `source` varchar(50) NOT NUll,
--   `text` varchar(5000) NOT NULL,
--   `reposts_count` int(10) NOT NULL,
--   `comments_count` int(10) NOT NULL,
--   `attitudes_count` int(10) NOT NULL,
--   `crawl_time` varchar(50) NOT NULL,
--   PRIMARY KEY (`weibo_id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `weibo_weibo`;
CREATE TABLE `weibo_weibo` (
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `weibo_id` varchar(50) NOT NULL,
  `created_at` varchar(20) NOT NULL,
  `source` varchar(50) NOT NUll,
  `text` text NOT NULL,
  `reposts_count` int(10) NOT NULL,
  `comments_count` int(10) NOT NULL,
  `attitudes_count` int(10) NOT NULL,
  `crawl_time` varchar(50) NOT NULL,
  PRIMARY KEY (`weibo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `weibo_comment`;
CREATE TABLE `weibo_comment` (
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `weibo_id` varchar(50) NOT NULL,
  `comment_id` varchar(50) NOT NULL,
  `created_at` varchar(20) NOT NULL,
  `source` varchar(50) NOT NUll,
  `text` varchar(5000) NOT NULL,
  `like_counts` int(10) NOT NULL,
  `crawl_time` varchar(50) NOT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
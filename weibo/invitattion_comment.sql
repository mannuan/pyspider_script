DROP TABLE IF EXISTS `invitation_comment`;
CREATE TABLE `invitation_comment` (
  `id` int(10) NOT NULL,
  `comment_id` bigint(255) NOT NULL,
  `comment_context` text CHARACTER SET utf8 NOT NULL,
  `crawl_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `push_time` varchar(20) CHARACTER SET utf8 NOT NULL,
  `source` varchar(20) CHARACTER SET utf8 NOT NULL,
  `like_counts` int(10) NOT NULL DEFAULT '0',
  `push_name` varchar(20) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`,`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--alter table invitation_comment modify column comment_id bigint(255) NOT NULL;
--
--ALTER TABLE `invitation_comment` DEFAULT CHARACTER SET utf8mb4;
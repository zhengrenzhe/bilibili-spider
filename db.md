## 视频数据表

* id 自增id
* vid 视频id
* title 视频标题
* ptype 视频父类型
* ctype 视频子类型
* desc 视频描述
* created_time 创建时间
* spider_get_time 爬虫首次抓取时间
* author_name 作者名
* author_id 作者id
* tags 视频标签
* duration 视频时长
* cover_url 视频封面

## 视频增量数据表

* id 自增id
* vid 视频id（不能唯一）
* spider_update_time 抓取此次增量的时间
* danmu_count 弹幕数量
* play_count 播放数量
* reply_count 回复数量
* like_count 点赞数量
* coin_count 投币数量
* collect_count 收藏数量
* charger_count 视频充电数量

## 视频推荐数据表

* id 自增id
* vid 视频id（不能唯一）
* related_vid 相关的视频id

## 作者数据表

* id 自增id
* author_id 作者id
* author_name 作者名
* intro 作者介绍
* avatar 作者头像
* sex 性别
* level 等级
* birthday 作者生日

## 作者增量数据表

* id 自增id
* author_id 作者id
* follower_count 关注数
* fans_count 粉丝数
* play_count 播放量
* charger_count 作者充电数量
* videos_count 视频数量

## 作者视频数据表

* id 自增id
* author_id 作者id
* video_id 视频id
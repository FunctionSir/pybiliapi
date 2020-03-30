# pybiliapi
用API获取B站上的视频信息等等。
## 函数说明
bvid(aid) AV2BV str <br>
aid(bvid) BV2AV int <br>
cid(aid) 获取cid int <br>
cover(aid) 获取封面（URL）str <br>
view(aid) 获取观看量 int <br>
like(aid) 获取赞数 int <br>
favorite(aid) 获取收藏数 int <br>
danmaku(aid) 获取弹幕数 int <br>
coin(aid) 获取硬币数 int <br>
share(aid) 获取分享数 int <br>
reply(aid) 获取评论数 int <br>
up_name(aid) 获取某视频的UP的名字 str <br>
up_uid(aid) 获取某视频的UP的UID int <br>
up_face(aid) 获取某视频的UP的头像（URL) str <br>
xml_danmaku_url(aid) 获取XML弹幕文件的URL str <br>
xml_danmaku_text(aid) 获取XML弹幕文件内容 str <br>
## 使用样例
````python
biliapi.view(biliapi.aid('BV17x411w7KC')) 
````
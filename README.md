# PyAipao简介
    该github工程主要是使用GitHub Actions来实现每天的跑步工作。
# 准备工作
    1.一个github账号
    2.抓包抓到的IMEICode
    3.Server酱的SCKEY（可选，用于微信推送跑步结果）
#  上手教程
1.点击fork按钮将工程复制到你的仓库 
![fork](https://tva1.sinaimg.cn/large/0062ozFkgy1gkuqaddg5aj31hc03vglw.jpg)

2.获取 SCKEY
- 完成Server酱的注册和绑定 [点我直达](http://sc.ftqq.com)
- 在 [发送选项](http://sc.ftqq.com/?c=code) 这一页中找到SCYKEY
![SCKEY](https://tva1.sinaimg.cn/large/0062ozFkgy1gkuqbjv12aj30qw04vmx6.jpg)

3.获取 IMEICode
- 打开抓包软件抓包, 再打开阳光体育 App 登录, 在所有的数据包中找后缀有 `IMEICode= ` 的 URL 请求, 等号后面的字段即为七天有效的 `IMEICode` (若多次没抓到: 可来回切换几次飞行模式, 杀掉 App 后台重复尝试多次)

4.配置Github Actions
- 打开工程的`secrets`，在其中将SCKEY和IMEICode填入
![4.1](https://tva1.sinaimg.cn/large/0062ozFkgy1gkuqbs421rj31b00l476b.jpg)
- 打开`autorun.yml`，将时间改为你想让它每天按时跑的时间，默认为每天上午9点。
![4.2](https://tva1.sinaimg.cn/large/0062ozFkgy1gkuqbztqwbj30ly0gx3za.jpg)
  **注意**：`autorun.yml`里的时间为UTC时间而不是北京时间 [点我转换](http://www.timebie.com/cn/universalbeijing.php)

到这步已经配置完成了，它每天就会自己跑了。

5.(可选)手动开始跑步
- 如果想手动开始跑步，点击`Actions`，按照图示步骤操作即可。
![5.1](https://tva3.sinaimg.cn/large/0062ozFkgy1gkuqc5q35cj31bb0hvjt4.jpg)

# 参考链接
- [AutoAction](https://github.com/Saujyun/AutoAction)
- [AiPao](https://github.com/LiaoGuoYin/AiPao)

# 注意事项
**License GPL v3.0**

本文仅供研究，使用者造成的任何后果由使用者自行承担，与作者无关。
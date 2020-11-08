**安装mysql**

    https://www.cnblogs.com/cnbp/p/12620825.html
    
    注：打开C：\Windows\System32目录，找到cmd.exe，单击选中后右键，菜单中选择“以管理员身份运行”。
    C:\windows\system32
    
    用root 进入mysql后
    mysql>set password =password('你的密码');
    mysql>flush privileges;
    
**数据库可视化工具**
    
    安装：https://www.cnblogs.com/clschao/articles/10022040.html
    使用： https://blog.csdn.net/csdnsevenn/article/details/82731535
    
  

**Python 生成requirement 及使用requirements.txt安装类库**

    快速生成requirement.txt的安装文件
    pip freeze > requirements.txt
 
    安装所需要的文件
    pip install -r requirement.txt
    
    虚拟环境cd 
    1.conda 创建   2.pycharm自带创建

**转换下载源**
    
        采用第三方下载源——清华源
         
        清华大学开源软件镜像站,致力于为国内和校内用户提供高质量的开源软件镜像、Linux镜像源服务,
        帮助用户更方便地获取开源软件。本镜像站由清华大学TUNA团队负责维护。
        
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple somepackage
    
**scrapy 说明**
        
       
    scrapy简单使用方法
    
    1.创建项目：
    scrapy startproject 项目名
    例如：
    scrapy startproject job_spider
    
    windows下，cmd进入项目路径例如
    d:\pythonCode\spiderProject>scrapy startproject job_spider
    将创建项目名为 job_spider
    
    2.使用命令创建一个爬虫：
    scrapy genspider 爬虫名称 需要爬取的网址
    scrapy genspider 51job https://jobs.51job.com/baoding/p1/
    
    注意：爬虫名称不能和项目名相同
    
    d:\pythonCode\spiderProject\baidubaike>scrapy 51job https://jobs.51job.com/baoding/p1/
    
    命令执行后将在d:\pythonCode\spiderProject\baidubaike\baidubaike\spiders\下，生成a51job.py
    
    3.修改a51job.py文件
    爬虫的核心代码
    
    4.items.py
    
    要爬取的字段说明
    
     
    
    5.修改settings.py文件
    
    # 一些user-agent设置和ip代理的设置，但是需要将这些设置写进中间件文件 middlewares.py 中，设置一些反扒技巧
    1)开启 DEFAULT_REQUEST_HEADERS
    修改如下
    DEFAULT_REQUEST_HEADERS = {
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'en',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    
    2)将 ROBOTSTXT_OBEY = True 改为 ROBOTSTXT_OBEY = False
    说明：
    默认为True，就是要遵守robots.txt 的规则
    将此配置项设置为 False ，拒绝遵守 Robot协议
    
    3)开启 ITEM_PIPELINES
    ITEM_PIPELINES = {
         'baidubaike.pipelines.BaidubaikePipeline': 300,
    }
    其中，ITEM_PIPELINES是一个字典文件，键为要打开的ItemPipeline类，值为优先级，ItemPipeline是按照优先级来调用的，取值范围为1~1000，值越小，优先级越高。
    
    
    6.修改pipelines.py文件
     数据持久化方式
    
      
    7.运行爬虫
    scrapy crawl 爬虫名
    
    例如：d:\pythonCode\spiderProject\baidubaike\baidubaike>scrapy crawl baike
    
**反扒技巧**

     参考文档
     https://blog.csdn.net/bbwangj/article/details/89891463?utm_medium=distribute.pc_feed_404.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_feed_404.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecas

**scrapy中文学习文档**

    https://www.osgeo.cn/scrapy/
    
**xpath学习文档**
    
    https://www.w3school.com.cn/xpath/index.asp
  
**xpath 插件使用方法**

    xpath helper官方文档上介绍的使用方法如下：
    打开窗口后，按shift键并移动鼠标至你需要查看的区域即可立即在插件窗口中显示其代码查询结果。
    1）打开一个新的标签，并导航到你最喜欢的网页。
    2）按Ctrl-Shift键-X以打开XPath辅助控制台。
    3）按住Shift键鼠标在页面上的元素。查询框会不断更新，以显示鼠标指针下面的元素充分XPath查询。
    结果框其右侧将显示评价结果的查询。
    4）如果需要的话，可以直接在控制台编辑XPath查询。在结果框中将立即反映任何变化。
    5）再次按Ctrl-Shift键-X关闭控制台
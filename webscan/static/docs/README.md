
<center><font size=6 >Sec-Tools 使用文档 </font></center>
<br>
<center> 联系我们✉： <a target="_blank" href="mailto:Sec_Tools@163.com" rel="nofollow" >Sec_Tools@163.com </a></center>

> 一款在线Web安全渗透工具

## 团队成员

 <table>
   <tbody>
      <tr>
          <td style="text-align:center;">简～</td>
          <td style="text-align:center;">邓～</td>
		  <td style="text-align:center;">王～</td>
		  <td style="text-align:center;">林～</td>
      </tr>
    <tr>
		<td style="text-align:center;" ><img class="inverted" width="200" src="https://jwt1399.top/medias/avatar.png"></td>    
		<td style="text-align:center;"><img class="inverted" width="200" src="https://upload.jianshu.io/users/upload_avatars/16052738/fffbc8fc-a9c3-4a1c-ad56-157c32f57f79?imageMogr2/auto-orient/strip|imageView2/1/w/240/h/240"></td>  
		<td style="text-align:center;" ><img class="inverted" width="200" src="https://pic3.zhimg.com/v2-6fb8dc878b496af2ec012c1f001865b2_xl.jpg"></td>
		<td style="text-align:center;"><img class="inverted" width="200" src="https://tse2-mm.cn.bing.net/th/id/OIP.84TQxrsYyNGXAkgvPHEtyQAAAA?w=165&h=180&c=7&o=5&dpr=1.25&pid=1.7"></td>  
   </tr>
 </tbody></table>

## 相关技术

- **Python 3.8.0**

> 官网：https://www.python.org/

`Python 3.8` 支持许多高级特性，在 Web 漏扫这一块 Python 编写也十分灵活。

- **Django 3.1.4**

> 官网：https://www.djangoproject.com/

`Django` 是一个开放源代码的 Web 应用框架，由 Python 写成。采用了MTV的框架模式，Django 是 Python 语言中文档比较全的一个 Web 框架，因为文档比较全，适合新手上手，所以这里选了 Django。

- **MySQL**

`MySQL` 是 经典的关系型数据库，实际上因为 Django 可以完美的支持各种数据库，一般我们不需要对数据库进行直接操作，所以换其他的数据库也是可以的，因为对 MySQL 比较熟悉，就选择了 MySQL 了。

- **ECharts 5.0.1**

> 官网：https://echarts.apache.org/zh/index.html

`ECharts` 是百度开源的一个数据可视化的 JS 图表插件，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库 [ZRender](https://github.com/ecomfe/zrender)，提供直观，交互丰富，可高度个性化定制的数据可视化图表。

- **Font-Awsome 5.15.1**

> 官网：https://fontawesome.com/

`Fontawsome` 是一款基于 CSS 框架的网页字体图标库。

- **SimpleUI 2021.1.1**

> 官网：https://simpleui.72wo.com/simpleui/

`Simple UI` 是一款基于 Vue+Element-Ui 的 Django Admin 现代化主题。全球1800+网站都在使用！

- **Docsify 4.11.6**

> 官网：https://docsify.js.org/#/

`docsify` 是一个快速生成 `Vue` 风格文档的工具，它直接加载 `Markdown` 文件并动态渲染，同时还可以生成封面页。我们只需要写完 `Markdown` 文档，就可以看到类似下方图片的文档页面了。

- **Booststrap**

> 官网：https://www.bootcss.com/

`Bootstrap`是 Twitter 推出的一个用于前端开发的开源工具包。它由Twitter的设计师 Mark Otto 和 Jacob Thornton 合作开发,是一个 CSS/HTML 框架。

- **JQuery**

>官网： https://jquery.com/

`jQuery` 是一个 JavaScript 库，极大地简化了 JavaScript 编程。

- **AJAX**

`AJAX` 是与服务器交换数据的艺术，它在不重载全部页面的情况下，实现了对部分网页的更新。

- **Layer**

>官网： https://layer.layui.com/

`Layer` 是一款近年来备受青睐的web弹层组件，layer 甚至兼容了包括 IE6 在内的所有主流浏览器。

## TO DO

!> 不论是开发还是安全感觉都有很长的路要走，路漫漫其修远兮，吾将上下而求索，共勉 ！

- [x] 前端框架页面
- [x] 后台框架页面
- [x] 端口扫描功能
- [x] 安全导航功能
- [x] 信息泄露探测功能
- [x] 旁站探测功能
- [x] 引入SQLite数据库
- [x] 漏洞扫描功能
- [x] 目录扫描功能
- [x] 登录和注册功能
- [x] 关于页&文档页 
- [x] 引入Echart
- [x] 项目首页
- [x] 域名探测功能
- [ ] 漏洞扫描详情导出功能
- [ ] 引入MySQL数据库
- [ ] 小工具实现
- [ ] 代码变量、数据库结构优化

## 版本变更记录
### v2.7（2021-04-18）[👈](https://jwt1399.lanzous.com/ivcAzobluof)[Current]

- 新增`域名探测`功能；
- 新增`中间件漏洞`扫描；
- 修复`忘记密码`功能；
- 优化AWVS未启动报错信息；
- 优化`用户登录`逻辑；
- 优化`漏扫详情`页UI；
- 优化导航栏布局；
- 优化若干小细节；

### v2.6（2021-03-31）[👈](https://jwt1399.lanzous.com/iW06Qnjexfe)

- 新增漏洞`扫描详情`功能；
- 新增首页 `仪表盘`；
- 安全导航页导航栏`移动端优化`；
- 安全导航页目录栏`缩放优化`；
- 注册&登录界面优化；
- 文档页`导航栏优化`；
- 新增 `UI` 夜间模式；
- 修复若干`UI` 显示Bug；


### v2.5（2021-03-02）[👈](https://jwt1399.lanzous.com/itk5Hmdy1xi)

- 新增了`漏洞扫描`功能；
- 端口扫描页新增`常见端口查询表`；
- 信息泄露页新增`常见信息泄露列表`；
- 指纹识别页新增`数据分析`图表；
- 漏洞扫描页`界面优化`；

### v2.4（2021-02-22）[👈](https://jwt1399.lanzous.com/iAMEWlzky8d)

- 新增了`目录识别`功能；
- 重写`欢迎页`；
- 安全导航页`移动端界面`适配；
- 安全导航页`UI优化`；
- 目录识别页`界面优化`；
- 指纹识别页新增`常见指纹`显示与搜索；
- 引入`Boostrap Table`实现分页；
- 淘汰 `LayUI` 改用 `Layer` 进行弹窗；
- 文档页增加`导航栏`；

### v2.3（2021-02-08）[👈](https://jwt1399.lanzous.com/iErBilgjj6b)

- 全新的`页面布局`；
- UI适配`移动端`；
- 优化`导航页布局`；
- 优化一系列`UI`显示问题；
    - 优化了`手机端页脚`显示
    - 优化了`平板端导航条`显示
    - 页面底部增加`回到顶部`按钮
    - 按钮`触发跳转`页面相对位置
    - `回车键`触发查询按钮
    - 优化`导航页页脚`显示


### v2.2 （2021-02-03）[👈](https://jwt1399.lanzous.com/iN1L2lasn6d)

- 新增了`信息泄露探测`功能；
- 新增了`旁站探测`功能；
- 新增了导航页`数据分析`功能；
- 新增了`文档页`；
- 重构了`静态文件static`文件结构
- 优化了项目`文件结构`；
- 美化了`注册`页面；
- 引入了 `particles 动态粒子`背景效果；
- 修复了一些 `UI` 显示问题；

### v2.1 （2021-01-13）[👈](https://jwt1399.lanzous.com/iAj5ukctmfi)

- 新增了`指纹识别`功能；
- 新增了`登录和注册功能`功能；
- 新增了`欢迎页`；
- ~~新增了`文档页`；~~
- 修复了一些 `UI` 显示问题；

### v2.0（2021-01-04）[👈](https://jwt1399.lanzous.com/il9lAk508le)

- 新增了`端口扫描`功能；
- 新增了`安全导航`功能；
- 连入了 `SQLite` 数据库，后续考虑改为`MySQL`；
- 修复了一些 `UI` 显示问题；
- 修复了后台头部小图标无法显示问题；
- 新增了后台数据导入导出功能；

### v1.0（2020-12-20）[👈](https://jwt1399.lanzous.com/iFUM2k508dg)

- 基于`Tabler`框架构造了前端页面；
- 引入了基于`SimpleUi`的后台框架；
- 引入了`Font-Awsome 5.15.1`图标；
## Supported Browsers

<table>
  <thead>
    <tr>
      <th style="width: 20%">Browser</th>
      <th style="width: 20%">Version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="static/img/browsers/edge.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Edge</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/firefox.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Firefox</font></td>
      <td>last 3 versions, ESR</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/chrome.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Chrome</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/safari.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Safari</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/opera.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Opera</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/electron.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Electron</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/brave.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Brave</font></td>
      <td>last 3 versions</td>
    </tr>
    <tr>
      <td><img src="static/img/browsers/vivaldi.svg" width="24" height="24" class="me-2"><font _mstmutation="1"> Vivaldi</font></td>
      <td>last 3 versions</td>
    </tr>
  </tbody>
</table>

     
     
## 赞助💰

如果你觉得对你有帮助，你可以赞助我们一杯冰可乐！，你的支持是我们前进路上最大的动力！嘻嘻🤭

<table>
  <tbody>
     <tr>
         <td style="text-align:center;">支付宝支付</td>
         <td style="text-align:center;">微信支付</td>
     </tr>
   <tr>
    <td style="text-align:center;" ><img width="200" src="https://jwt1399.top/medias/reward/alipay.png"></td>    
      <td style="text-align:center;"><img width="200" src="https://jwt1399.top/medias/reward/wechat.png"></td>     
  </tr>
</tbody></table>

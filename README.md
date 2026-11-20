# Awesome OSINT · 简体中文版

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![简体中文](https://img.shields.io/badge/简体中文-汉化版-brightgreen.svg)](README.md) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE.txt)

[<img src="assets/osint-logo.svg" align="right" width="100" alt="OSINT Logo">](https://github.com/jivoi/awesome-osint)

一份汇集了众多优秀**开源情报（OSINT）工具与资源**的精选清单简体中文版。
[开源情报（OSINT）](https://en.wikipedia.org/wiki/Open-source_intelligence)是从公开可获取的来源中收集的情报；在情报界（IC）中，「开放」（open）指公开的、可公开获取的来源，以区别于隐蔽或秘密来源。

本清单面向所有从事网络威胁情报（CTI）、威胁狩猎或开源情报工作的人，从入门到进阶皆可参考。

> 🔎 **本版新增**：[可视化导航首页](index.html)（分类浏览 · 关键词搜索 · 深浅主题切换，本地双击即可打开，或在仓库启用 GitHub Pages 后在线访问）、全文中文化目录与条目说明、中文贡献指南。对照阅读：[English / 英文原版](README.en.md)。

> ⚠️ **合规使用提示**：本清单仅供合法授权的安全研究、教学与学习使用。使用任何工具前请确认已获得相应授权，遵守所在国家/地区的法律法规与目标服务的使用条款，尊重他人隐私与数据保护要求；请勿用于未授权的探测、骚扰或侵犯他人权益的行为，使用者需自行承担相应责任。

---

### 关于本仓库

| 项目 | 说明 |
| --- | --- |
| 上游原项目 | [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint)（作者 [@jivoi](https://github.com/jivoi) 及全体贡献者） |
| 本仓库性质 | 基于上游项目的**简体中文翻译 + 轻量二次开发**，为非官方独立衍生版本 |
| 上游协议 | [CC BY-SA 4.0](LICENSE.txt)（署名-相同方式共享 4.0 国际） |
| 本仓库协议 | 同样采用 [CC BY-SA 4.0](LICENSE.txt)，并完整保留上游署名 |
| 内容基准 | 同步自上游 `master` 分支（截至 2026-11-18） |
| 二次开发内容 | 中文可视化首页 `index.html`、中文化文档与目录锚点、重绘矢量图标、站点配置调整（图标版权归本汉化版，原项目图标版权归上游所有） |
| 维护说明 | 本仓库为独立汉化版本，请勿向上游仓库提交与本仓库相关的 Pull Request |

祝你玩得开心、狩猎愉快 🧙‍♂️

---

## <a id="toc"></a>📖 目录

 - [贡献指南](#s1)
 - [致谢](#s2)
 - [通用搜索](#s3)
 - [Google Dorks（谷歌黑客语法）工具](#s4)
 - [主要国家级搜索引擎](#s5)
 - [元搜索](#s6)
 - [注重隐私的搜索引擎](#s7)
 - [数据泄露搜索引擎](#s8)
 - [专用搜索引擎](#s9)
 - [暗网搜索引擎](#s10)
 - [可视化搜索与聚类搜索引擎](#s11)
 - [相似网站搜索](#s12)
 - [文档与幻灯片搜索](#s13)
 - [威胁行为者搜索](#s14)
 - [实时网络威胁地图](#s15)
 - [文件搜索](#s16)
 - [粘贴板站点](#s17)
 - [代码搜索](#s18)
 - [主要社交网络](#s19)
 - [实时搜索、社交媒体搜索与通用社交媒体工具](#s20)
 - [社交媒体工具](#s21)
   - [Twitter](#s22)
   - [Facebook](#s23)
   - [Instagram](#s24)
   - [TikTok](#s25)
   - [Pinterest](#s26)
   - [Reddit](#s27)
   - [VKontakte](#s28)
   - [WhatsApp](#s29)
   - [Tumblr](#s30)
   - [LinkedIn](#s31)
   - [Telegram](#s32)
   - [Steam](#s33)
   - [GitHub](#s34)
 - [博客搜索](#s35)
 - [论坛与讨论板搜索](#s36)
 - [用户名查询](#s37)
 - [人物调查](#s38)
 - [邮箱搜索 / 邮箱核查](#s39)
 - [电话号码研究](#s40)
 - [车辆 / 汽车研究](#s41)
 - [专家搜索](#s42)
 - [企业调查](#s43)
 - [求职搜索资源](#s44)
 - [问答站点](#s45)
 - [域名与 IP 研究](#s46)
 - [关键词发现与研究](#s47)
 - [网页历史与网站快照](#s48)
 - [语言工具](#s49)
 - [图片搜索](#s50)
 - [图像分析](#s51)
 - [视频搜索及其他视频工具](#s52)
 - [学术资源与灰色文献](#s53)
 - [地理空间研究与地图工具](#s54)
 - [新闻](#s55)
 - [新闻摘要与发现工具](#s56)
 - [事实核查](#s57)
 - [数据与统计](#s58)
 - [网页监控](#s59)
 - [浏览器](#s60)
 - [离线浏览](#s61)
 - [VPN 服务](#s62)
 - [信息图与数据可视化](#s63)
 - [社交网络分析](#s64)
 - [隐私与加密工具](#s65)
 - [DNS](#s66)
 - [海事](#s67)
 - [其他工具](#s68)
 - [威胁情报](#s69)
 - [游戏平台](#s70)
 - [音乐流媒体服务](#s71)
 - [OSINT 视频](#s72)
 - [OSINT 博客](#s73)
 - [OSINT RSS 订阅源](#s74)
 - [其他资源](#s75)
 - [相关 Awesome 精选清单](#s76)
 - [许可证](#s77)

## <a id="s1"></a>[↑](#toc) 贡献指南

若你想添加工具或资源，请先阅读 [CONTRIBUTING](./CONTRIBUTING.md)。也欢迎帮忙 🥰 用优质资源一起壮大这份清单。

## <a id="s2"></a>[↑](#toc) 致谢

本清单部分内容取自 [i-inteligence](https://www.i-intelligence.eu) 的 [OSINT 工具与资源手册](https://www.i-intelligence.eu/open-source-intelligence-tools-and-resources-handbook/)。

感谢我们的主要贡献者
[jivoi EK_](https://github.com/jivoi) & 
[spmedia](https://github.com/spmedia)

## <a id="s3"></a>[↑](#toc) 通用搜索

*用户最常用的主要搜索引擎。*

* [Aol](https://search.aol.com) - 面向美国用户的网络门户。
* [Bing](https://www.bing.com) - 微软的搜索引擎。
* [Brave](https://search.brave.com) - 私密、独立且透明的搜索引擎。
* [Goodsearch](https://www.goodsearch.com) - 用于查找在线购物优惠的搜索引擎。
* [Google Search](https://www.google.com) - 最受欢迎的搜索引擎。
* [Instya](https://www.instya.com) -  你可以搜索购物网站、词典、问答站点、新闻、图片、视频等内容。
* [Lycos](https://www.lycos.com) - 可搜索图片、视频、新闻和商品的搜索引擎。
* [Mojeek](https://www.mojeek.com/) - 不断成长的独立搜索引擎，不会追踪你。
* [Perplexity](https://www.perplexity.ai) - 由 AI 驱动、附带来源引用的搜索引擎。
* [Phind](https://phindai.org/) - 面向开发者和技术问题优化的 AI 搜索引擎。
* [Search.com](https://www.search.com) - 在一个地方调用多家优秀引擎来搜索网络。
* [Wolfram Alpha](https://www.wolframalpha.com) - Wolfram Alpha 是由 Wolfram Alpha 开发的计算知识引擎（答案引擎），它借助 Wolfram 突破性的
算法、知识库与 AI 技术计算出专家级的答案。
* [Yahoo! Search](https://www.yahoo.com) -  帮你精准找到所需内容的搜索引擎。
* [YOU](https://you.com) - AI 搜索引擎。

## <a id="s4"></a>[↑](#toc) Google Dorks（谷歌黑客语法）工具

*Google Dorks（谷歌黑客语法）工具*

* [AtDork](https://github.com/amnottdevv/atdork) - 专业的 OSINT 搜索语法工具，具备自适应延迟、熔断器和后端自动回退机制，可避免 IP 封禁与速率限制。
* [DorkCraft](https://github.com/juandresrodca/DorkCraft) - Google 搜索语法生成器，可为开源情报（OSINT）与信息收集/侦察构建高级搜索查询。
* [DorkEye](https://github.com/xPloits3c/DorkEye) - 自动化 Google 搜索语法工具，借助验证码绕过与封禁规避，可从文件每秒生成数千条高级查询来发现暴露的文件。它还能检测漏洞、运行多智能体分析并提取元数据。
* [DorkGenius](https://dorkgenius.com/) - DorkGenius 是为 Google、Bing 和 DuckDuckGo 生成自定义搜索查询的终极工具。 - 这款前沿应用借助 AI 的力量，帮助你创建高级搜索查询，精准找到网上所需内容。
* [DorkGPT](https://www.dorkgpt.com/) - 借助 AI 生成 Google Dorks（谷歌黑客语法）。
* [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database) - GHDB 是用于查找公开可用信息的搜索查询（我们称之为搜索语法/dork）索引，面向渗透测试人员与安全研究人员。
* [SearchDorks](https://kriztalz.sh/search-dorks/) - 使用 AI 生成搜索引擎（Google、FOFA、Shodan、Censys、ZoomEye）的搜索语法。

## <a id="s5"></a>[↑](#toc) 主要国家级搜索引擎

*按国家/地区划分的本地化搜索引擎。*

* [Alleba (Philippines)](https://www.alleba.com) - 菲律宾搜索引擎
* [Baidu (China)](https://www.baidu.com) - 中国使用的主要搜索引擎
* [Daum (South Korea)](https://www.daum.net/)
* [Eniro (Sweden)](https://www.eniro.se)
* [Gerdoo (Iran)](https://gerdoo.me)
* [Najdi (Slovenia)](https://www.najdi.si)
* [Naver (South Korea)](https://www.naver.com)
* [Onet.pl (Poland)](https://www.onet.pl)
* [Orange (France)](https://www.orange.fr)
* [Parseek (Iran)](https://www.parseek.com)
* [SAPO (Portugal)](https://www.sapo.pt)
* [Search.ch (Switzerland)](https://www.search.ch)
* [Seznam(Czech Republic)](https://seznam.cz)
* [SoGou (China)](https://www.sogou.com/)
* [Walla (Israel)](https://www.walla.co.il)
* [Yandex (Russia)](https://www.yandex.com)
* [Zarebin (Iran)](https://zarebin.ir)

## <a id="s6"></a>[↑](#toc) 元搜索

*较为小众、使用较少的搜索引擎。*

* [All-in-One](https://all-io.net)
* [AllTheInternet](https://www.alltheinternet.com)
* [Etools](https://www.etools.ch)
* [FaganFinder](https://www.faganfinder.com/engines)
* [iZito](https://www.izito.com)
* [Myallsearch](https://www.myallsearch.com)
* [Qwant](https://www.qwant.com) - 依托 Microsoft Bing 的法国搜索引擎。
* [SearXNG](https://searxng.org/) - 尊重隐私的开源元搜索引擎。
* [Swisscows](https://swisscows.com/)

## <a id="s7"></a>[↑](#toc) 注重隐私的搜索引擎

*侧重匿名化与隐私保护的搜索引擎。*
  
* [DuckDuckGo](https://duckduckgo.com) - 一款强调保护搜索者隐私的互联网搜索引擎。
* [Disconnect Search](https://search.disconnect.me/) - 阻止搜索引擎追踪你的搜索记录。
* [Gibiru](https://gibiru.com/) - Gibiru 提供“未经审查的搜索结果”，不收集个人数据，例如记录用户的 IP 地址或搜索查询。
* [Kagi Search](https://kagi.com/) - 解放你的搜索。没有广告，没有监控。尊重你的时间。你是客户，绝不是产品。
* [Mojeek](https://www.mojeek.com/) - Mojeek 是一款不断成长的独立搜索引擎，不会追踪你。
* [Qwant](https://www.qwant.com/) - 尊重你隐私的搜索引擎。
* [Startpage](https://www.startpage.com/) - 全球最注重隐私的搜索引擎。
* [SearXNG](https://searxng.org/) - 尊重隐私的开源元搜索引擎。
* [swisscows](https://swisscows.com/en) - 匿名搜索引擎，一款位于瑞士、适合全家人使用且注重隐私的搜索引擎。

## <a id="s8"></a>[↑](#toc) 数据泄露搜索引擎

*可用于检查你的数据是否已泄露的搜索引擎*

* [CheckLeaked](https://checkleaked.cc/) - 检查邮箱、用户名或电话号码是否出现在数据泄露中，并展示来源；提供免费搜索、开发者 API 和聊天机器人。
* [CredenShow](https://credenshow.com/) - 抢在他人之前发现你已泄露的凭据。
* [HIB Ransomed](https://haveibeenransom.com/) - 因为人们有权知道自己的数据是否已泄露。
* [HEROIC.NOW](https://heroic.com/) - 你的数据是否在暗网上泄露了？免费扫描你的身份信息。
* [IKnowYour.Dad](https://iknowyour.dad/) - 数据泄露搜索引擎。
* [Leaker](https://github.com/vflame6/leaker) - 被动式泄露枚举命令行工具，可同时检索 10 个泄露数据库。
* [NOX](https://github.com/nox-project/nox-framework) - 用于深度数据泄露分析与身份关联拓展的递归异步框架。
* [OsintCat](https://www.osintcat.net/) - 检查邮箱地址是否在已知数据泄露中暴露。可跨多个泄露数据库快速查询，并提供简单易用的 API。
* [StealSeek](https://stealseek.io/) - 功能强大的搜索引擎，旨在帮助你查找和分析数据泄露。
* [Vendor History](https://vendorhistory.com/) - 检查企业所用的软件供应商是否发生过数据泄露：涵盖 255 家供应商的州级泄露通告、SEC 网络安全备案、CISA 已被利用漏洞清单和勒索软件声明，每条都附来源链接。免费，无需注册。
## <a id="s9"></a>[↑](#toc) 专用搜索引擎

*针对特定信息或主题的搜索引擎。*

* [2lingual Search](https://www.2lingual.com)
* [Abusech](https://hunting.abuse.ch) - 只需一条简单查询，即可跨所有 abuse.ch 平台进行检索
* [Abuseipdb](https://www.abuseipdb.com/) - 由系统管理员举报的 IP、域名和子网滥用行为库
* [BeVigil](https://bevigil.com/search) - 搜索移动应用中的子域名、URL、参数等资产
* [BGP.tools](https://bgp.tools) - 用于网络侦察与分析的现代 BGP 工具包
* [BGP.he.net](https://bgp.he.net) - 免费的 BGP 与网络情报工具包
* [bgpmap.net](https://bgpmap.net) - 免费的多观测点 BGP Looking Glass，用于 IP 和前缀侦察，提供按前缀的 AS 路径图、RPKI 验证以及可分享的快照。
* [BrightCloud](https://brightcloud.com/tools/url-ip-lookup.php) - 检查某个 URL 或 IP 地址相关的信誉、分类及潜在威胁。
* [Browserleaks](https://browserleaks.com/) - BrowserLeaks 检测浏览器的隐私与指纹泄露
* [Censys](https://search.censys.io/) - 用于监控和分析联网设备的搜索工具
* [CertKit Certificate Search](https://www.certkit.io/tools/ct-logs/) - 快速检索公开的 SSL/TLS 证书记录。
* [Cisco Talos Intelligence](https://talosintelligence.com/reputation_center) - IP 与域名信誉中心，用于实时威胁检测
* [Cloudflare Radar](https://radar.cloudflare.com) - 互联网流量模式、攻击态势与技术趋势。
* [Criminal IP](https://www.criminalip.io/) - 网络威胁情报（CTI）搜索引擎与攻击面管理（ASM）平台 
* [CRT Certificate Search](https://crt.sh) - 可搜索证书透明度日志中记录的公开 SSL/TLS 证书
* [FOFA](https://en.fofa.info/) - 资产搜索与分析工具。
* [FullHunt](https://fullhunt.io/) - FullHunt 可识别并保护你的外部攻击面。
* [Google Custom Search](https://www.google.com/cse)
* [GrayhatWarfare](https://grayhatwarfare.com/) - 搜索并索引开放的 Amazon S3 存储桶，帮助用户发现并查看可能暴露的数据。
* [GreyNoise](https://viz.greynoise.io/) - 搜索暴露在互联网上的资产与恶意 IP。
* [Harmari (Unified Listings Search)](https://www.harmari.com/search/unified)
* [Hunter Search Engine](https://hunter.how/) - 搜索暴露的互联网资产、开放的 Web 目录等。
* [Intelligence X](https://intelx.io/tools) - 付费 OSINT 工具，允许用户跨多种来源检索信息，包括暗网和公开的数据泄露。
* [Internet Archive](https://archive.org/)
* [Islegitsite](https://www.islegitsite.com/) - 基于公开来源分析网站的信誉、域名与安全状况，判断其是否可信。
* [MalwareBazaar](https://bazaar.abuse.ch/browse/) - 按哈希、家族、标签等条件搜索并下载已确认的恶意软件样本。
* [Mamont](https://www.mmnt.ru/)
* [Million Short](https://millionshort.com)
* [Netlas.io](https://app.netlas.io/)
* [ODIN](https://search.odin.io/) - 用于搜索主机、CVE 以及暴露的存储桶/文件，并显示网站是否存在漏洞。每天可免费搜索 10 次。 
* [OCCRP Aleph](https://aleph.occrp.org/)
* [ONYPHE](https://search.onyphe.io/) - 索引整个互联网上暴露资产与服务的 OSINT 引擎。
* [packet.guru](https://packet.guru/) - 浏览器指纹与连接可信度审计：WebRTC/DNS 泄露测试、JA4/JA3 TLS 与被动 TCP/IP 指纹、ECH 状态以及 IP 信誉（VPN、代理、数据中心、Tor），返回两个独立的 0–100 隐私与信任评分。无需注册，全部在客户端运行。
* [Shadowserver](https://dashboard.shadowserver.org/) - 展示 Shadowserver 基金会收集的网络威胁全球统计数据的仪表盘。
* [Shodan](https://www.shodan.io/) - Shodan 是面向物联网（IoT）的搜索引擎，可通过多种过滤条件搜索连接到互联网的各种服务器。
* [WIPO](https://www3.wipo.int/branddb/en/)
* [Wpscan](https://wpscan.com) - 扫描你的 WordPress 站点并即时生成安全报告。
* [YARAif](https://yaraify.abuse.ch/scan/) - 协作式 YARA 引擎，通过文件模式匹配提供开放的威胁情报。
* [Zanran](https://zanran.com)
* [ZoomEye](https://www.zoomeye.ai/) - ZoomEye 是网络空间搜索引擎，可用于 IP、域名、互联网资产发现，以及服务器、路由器和摄像头的暴露面分析。

## <a id="s10"></a>[↑](#toc) 暗网搜索引擎
* [Ahmia](https://ahmia.fi)
* [Aleph Open Search](https://open-search.aleph-networks.eu)

## <a id="s11"></a>[↑](#toc) 可视化搜索与聚类搜索引擎

*同时抓取多个站点（Google、Yahoo、Bing、Goo 等）并返回结果的搜索引擎。*

* [Carrot2](https://search.carrot2.org) - 将搜索结果按主题归类整理。
* [Zapmeta](https://www.zapmeta.com)

## <a id="s12"></a>[↑](#toc) 相似网站搜索

*查找相似网站，适合用于商业竞争调研。*

* [SimilarSites](https://www.similarsites.com) - 发现彼此相似的网站
* [SitesLike](https://www.siteslike.com) - 按类别查找相似网站

## <a id="s13"></a>[↑](#toc) 文档与幻灯片搜索

*搜索 PDF、Word 文档、演示幻灯片等文件中的数据。*

* [DocumentCloud](https://www.documentcloud.org) - 用于分析、标注和发布文档的平台。
* [Epstein Exposed](https://epsteinexposed.com) - 综合性可检索数据库，收录 200 多万份美国司法部（DOJ）爱泼斯坦案文件、1700 多名相关人员、飞行日志、邮件以及关系网络图可视化。
* [Free Full PDF](https://www.freefullpdf.com)
* [Offshore Leak Database](https://offshoreleaks.icij.org)
* [RECAP Archive](https://www.courtlistener.com/recap/) - PACER 法院文档的公开档案库。
* [Scribd](https://www.scribd.com)
* [SlideShare](https://www.slideshare.net)

## <a id="s14"></a>[↑](#toc) 威胁行为者搜索

*搜索威胁行为者及其相关信息。*

* [APT Groups and Operations](https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml?pli=1#) - 了解威胁行为者、其背后支持国、所用工具与方法等。
* [Bi.Zone](https://gti.bi.zone/) - 收录 148 个威胁组织及其详细的战术、技术与程序（TTPs）。
* [BreachHQ](https://breach-hq.com/threat-actors) - 提供所有已知网络威胁行为者的列表，这些行为者也被称为恶意行为者、APT 组织或黑客。
* [Dark Web Informer](https://darkwebinformer.com/threat-actor-database/) - 截至 2025 年 5 月 29 日，已追踪 854 个威胁行为者。
* [ETDA](https://apt.etda.or.th/cgi-bin/listgroups.cgi) - 搜索威胁行为者组织及其使用的工具。
* [FortiGuard Labs](https://www.fortiguard.com/threat-actor) - 由 FortiGuard Labs 提供支持的威胁行为者百科全书，给出可落地的洞察，帮助安全团队准备并优化高级威胁狩猎与响应。
* [KNOWLEDGENOW](https://know.netenrich.com/content/track/threat-actor) - 热门威胁趋势。
* [lazarusholic](https://lazarus.day/actors/) - 共收录 203 个威胁行为者。
* [Malpedia](https://malpedia.caad.fkie.fraunhofer.de/actors) - 获取威胁行为者组织列表。
* [MISP Galaxy](https://www.misp-galaxy.org/360net/) - 由 360.net 识别的已知或推测的对手组织。
* [OPENHUNTING.IO](https://openhunting.io/threat-library) - 汇集信息的威胁库。
* [SOCRadar LABS](https://socradar.io/labs/threat-actor/) - 了解威胁行为者的战术、技术和过往活动。访问详细档案并追踪其活动，紧跟最新威胁以及战术、技术与程序（TTPs）。
* [Thales](https://cds.thalesgroup.com/en/cyberthreat/attacks-page) - 在图形化攻击浏览器中查找威胁行为者组织。
* [Threat Actor Usernames Scrape](https://github.com/spmedia/Threat-Actor-Usernames-Scrape) - 汇集最新情报以及从各类网络犯罪来源和论坛抓取的 90 多万个威胁行为者用户名。

## <a id="s15"></a>[↑](#toc) 实时网络威胁地图

*实时网络威胁地图以可视化形式帮助了解正在发生的攻击。*

* [Bitdefender Threat Map](https://threatmap.bitdefender.com/) - Bitdefender 提供的网络威胁实时地图。
* [BunkerWeb Live Cyber Attack Threat Map](https://threatmap.bunkerweb.io/) - 展示由 BunkerWeb（开源下一代 Web 应用防火墙）拦截的实时网络攻击。
* [Check Point Live Cyber Threat Map](https://threatmap.checkpoint.com/) - 探索 2025 年最主要的网络威胁，包括勒索软件、信息窃取木马和云漏洞。
* [Cisco Talos Intelligence](https://talosintelligence.com/ebc_spam) - 
* [Fortiguard Labs](https://fortiguard.fortinet.com/threat-map) - FortiGuard Outbreak Alerts 提供关于当前正在发生、并波及众多企业、组织和行业的重大网络安全攻击的关键信息。
* [HCL Threat Map](https://www.hcltech.com/hcl-threat-map) - HCLTech 提供的网络威胁地图。
* [IBM X-Force Exchange Current Malicious Activity](https://exchange.xforce.ibmcloud.com/activity/map) -  
* [Imperva Live Threat Map](https://www.imperva.com/cyber-threat-attack-map/) - 实时全球视图，展示由 Imperva 安全服务缓解的 DDoS 攻击、入侵尝试和机器人攻击。
* [Kaspersky Cyberthreat live Map](https://cybermap.kaspersky.com/) - 在这里查看你是否正遭受网络攻击。
* [LIONIC Cyber Threat Map](https://www.lionic.com/monitoring/) - 
* [NETSCOUT Cyber Threat Map](https://horizon.netscout.com/) - 实时 DDoS 攻击地图
* [Radware Live Cyber Threat Map](https://livethreatmap.radware.com/) - Radware 实时威胁地图基于其全球威胁诱捕网络，近乎实时地呈现正在发生的网络攻击信息。
* [Secure Gateway Live Cyber Threat Map](https://securegateway.com/map/v5/) -
* [Thale's Cyberthreat Map](https://cds.thalesgroup.com/en/cyberthreat/hitmap) - 借助 Thales 网络威胁地图发现网络安全趋势，探索受攻击地区、高频攻击、受影响行业和流行恶意软件。
* [ThreatsEye | Live Cyber Threat Map](https://threatseye.io/threats-map) - 实时可视化全球网络攻击与威胁，监控全球正在发生的网络安全事件、攻击来源、目标和威胁类别。
* [World Monitor Tech](https://tech.worldmonitor.app) - 实时网络威胁情报仪表盘，整合 CISA 公告、活跃的恶意软件活动、CVE 订阅源和全球网络事件热力图，并结合地缘政治与军事背景。
* [Zscaler Global Threat Map Dashboard](https://threatlabz.zscaler.com/cloud-insights/threat-map-dashboard) - 展示过去 24 小时内观察到的威胁，包括其反病毒引擎检测到的威胁、恶意软件和高级持续性威胁（APT）。


## <a id="s16"></a>[↑](#toc) 文件搜索

*搜索各类文件。*

* [eyedex](https://www.eyedex.org/) - 开放目录搜索引擎。
* [de digger](https://www.dedigger.com/) - 可让你查找 Google Drive 中公开可见的任意类型文件。
* [Find Security Contacts](https://findsecuritycontacts.com) - 公开索引，列出从各域名 security.txt 文件中提取的安全联系方式（邮箱、策略等）。
* [Meawfy](https://meawfy.com/) - 高级 Mega.nz 文件搜索引擎，借助智能爬虫技术搜索并发现 Mega.nz 上的文件，可即时访问超过 900 万个已索引文件。
* [ODCrawler](https://odcrawler.xyz/) - 面向开放目录的搜索引擎，可查找数百万个公开可用的文件！
* [SearchFiles.de](https://searchfiles.de/)

## <a id="s17"></a>[↑](#toc) 粘贴板站点

*查找已上传到 Pastebin 及其他同类粘贴板站点的信息*

* [BeanPaste](https://beanpaste.fun/) - 轻巧的文本分享方式。
* [bpaste](https://bpa.st/) - 欢迎使用 bpaste，这是一个粘贴板站点，可与他人分享代码。
* [CentOS Pastebin Service](https://paste.centos.org/) - Stikked 是一款开源 PHP 粘贴板程序，致力于保持简洁易用的界面。
* [cl1p](https://Cl1p.net) - 互联网剪贴板。
* [commie](https://commie.io/) - commie 是支持逐行注释的粘贴板脚本。
* [Context](https://ctxt.io/) - 几秒内即可把所见内容分享给他人。
* [ControlC Pastebin](https://Controlc.com) - 托管文本最简单的方式。
* [Cutapaste](https://cutapaste.net/) - 精简代码，轻松分享。
* [Defuse](https://defuse.ca/pastebin.htm) - 加密粘贴板 - 让你的数据保持私密与安全！
* [dpaste](https://Dpaste.com)
* [Etusivu](https://pastebin.fi/) - pastebin.com 的开源克隆，默认语言为芬兰语。
* [GitHub gist](https://gist.github.com)
* [HashBin](https://hashb.in/#Q===) - HashBin 是一款连自身都无法看到粘贴内容的粘贴板站点。
* [hastebin](https://www.toptal.com/developers/hastebin/)
* [ideone](https://Ideone.com)
* [ivpaste](https://Ivpaste.com)
* [jsbin](https://Jsbin.com)
* [justpaste](https://Justpaste.it)
* [Katbin](https://katb.in) - 小巧轻量的粘贴板站点。
* [Linkode(alpha)](https://linkode.org/) - Linkode 是实用的粘贴板站点！
* [Logpasta](https://logpasta.com/) - 简单、安全的日志粘贴服务，支持命令行模式。
* [lesma.eu](https://lesma.eu/) - 简洁的粘贴应用，同时兼容浏览器与命令行。
* [Nachricht](https://nachricht.co/) - 通过 Nachricht.co，你可以通过互联网发送阅后即焚、加密的一次性消息，甚至不必放弃你惯用的即时通讯工具或社交网络。我们是一项独立、安全且完全免费的服务！
* [NoPaste](https://nopaste.boris.sh/) - NoPaste 是类似 Pastebin 的开源站点，可存储任意代码片段并生成链接以便分享。
* [nopaste.net](https://nopaste.net/) - nopaste.net 是临时文件托管、粘贴板和跨设备剪贴板服务。你可以上传文件或文本，并把链接分享给他人。
* [Notes](https://notes.io/) - 快、易、简。
* [nekobin](https://nekobin.com/) - 粘贴代码，保存并分享链接！
* [New Paste](https://paste1.com/) - 我想粘贴，因为打字太无聊了！
* [n0paste](https://n0paste.eu/) - 在线粘贴并分享你的代码。
* [paaster](https://paaster.io/) - Paaster 是一款安全易用的粘贴板应用，优先考虑隐私与简洁。借助端到端加密和粘贴历史，Paaster 确保你粘贴的代码保持机密且随时可用。
* [Pastebin.cz](https://www.pastebin.cz/en/) - 简洁的粘贴板站点。
* [Paste.Cash](https://www.paste.cash/) - Paste.CASH 是由 Cash Hosting 托管的注重隐私的加密粘贴板，每次粘贴都使用 256 位 AES 加密。
* [paste.centos](https://paste.centos.org)
* [paste.debian](https://Paste.debian.net)
* [paste.in.ua](https://paste.in.ua/) - 简洁的粘贴板站点。
* [paste.kde](https://Paste.kde.org)
* [Paste.Monster](https://paste.monster/) - 在线分享你的想法，提供 API。
* [paste.ubuntu](https://paste.ubuntu.com)
* [Paste.Quest](https://pastequest.com/) - 在线复制粘贴文本，随时随地与任何人分享。可使用密码选项为粘贴内容设置密码。
* [Pastery](https://www.pastery.net/) - 世界上最贴心的粘贴板站点！
* [PasteSite.Net](https://pastesite.net/) - 新一代粘贴板站点。
* [paste.sh](https://paste.sh/) - 这是一个加密粘贴站点。只需在此输入或粘贴代码并分享 URL，即会自动保存。
* [PasteShr](https://www.pasteshr.com/) - 在线存储任意文本以便分享，还提供搜索功能！
* [Rentry](https://rentry.co/) - Rentry.co 是支持预览、自定义 URL 和编辑的 Markdown 粘贴服务，快速、简洁且免费。
* [SafeNote](https://safenote.co/) - SafeNote 是一款免费的 Web 服务，可私密地分享便笺或文件，即便是黑客也无法窥探。
* [scrt.link](https://scrt.link/) - 通过仅能使用一次、随后自动销毁的链接来分享秘密。
* [snippet.host](https://snippet.host/) - 极简的文本与代码片段托管。
* [Spacebin](https://spaceb.in/) - Spacebin 是用 Go 实现的现代粘贴板服务，可承载笔记、小说、代码或任何其他形式的文本。
* [TutPaste](https://tutpaste.com/) - 欢迎使用我们快速免费的在线粘贴工具。可随时随地与任何人粘贴并分享文本或代码片段，无需注册。
* [vaultbin](https://vaultb.in/) - Vaultbin 是 Pastebin 和 Hastebin 的极速安全替代品。
* [Verybin](https://www.verybin.com/) - 匿名加密粘贴板，数据使用 256 位 AES 在浏览器中加密/解密，且不记录 IP 地址。
* [Write.as](https://write.as/) - 写下文字，发布到互联网。
* [ZBin](https://zbin.dev/) - 私密且安全的粘贴板站点。
* [ZeroBin](https://sebsauvage.net/paste/) - ZeroBin 是极简的开源在线粘贴板，服务器对粘贴的数据一无所知。数据使用 256 位 AES 在浏览器中加密/解密。


## <a id="s18"></a>[↑](#toc) 代码搜索

*按网站源代码进行搜索*

* [AnalyzeID](https://analyzeid.com/) - 查找同一人拥有的其他网站
* [Code Finder](https://codefinder.dev/) - 查找 GitHub 仓库的终极搜索引擎
* [GitHub Code Search](https://github.com/search?type=code) - GitHub 增强版代码搜索，支持高级过滤。
* [grep.app](https://grep.app/) - 在整个 GitHub 公开仓库中按指定字符串或正则表达式搜索代码。
* [NerdyData](https://nerdydata.com) - 面向源代码的搜索引擎。
* [PublicWWW](https://publicwww.com/)
* [SearchCode](https://searchcode.com) - 帮助在 10 多个来源中查找函数、API 和类库的真实示例。
* [Sourcebot](https://www.sourcebot.dev/) - 在本机索引数千个仓库，并通过快速、强大且现代的 Web 界面进行检索。
* [SourceGraph](https://sourcegraph.com/search) - 搜索数百万个开源仓库中的代码。
## <a id="s19"></a>[↑](#toc) 主要社交网络

* [Bluesky](https://bsky.app) - 基于 AT Protocol（AT 协议）构建的去中心化社交网络。
* [Draugiem (Latvia)](https://www.draugiem.lv)
* [Facebook](https://www.facebook.com)
* [Instagram](https://www.instagram.com)
* [Linkedin](https://www.linkedin.com)
* [Mixi (Japan)](https://mixi.jp)
* [Odnoklassniki (Russia)](https://ok.ru)
* [Pinterest](https://www.pinterest.com) - 是一款图片分享社交媒体服务，通过可视化方式轻松发现、分享和保存创意。
* [Qzone (China)](https://qzone.qq.com)
* [Reddit](https://www.reddit.com)
* [Threads](https://www.threads.net) - Meta 推出的以文字为主的对话应用。
* [Tinder](https://www.gotinder.com)
* [Tumblr](https://www.tumblr.com)
* [Twitter](https://twitter.com)
* [Weibo (China)](https://weibo.com)
* [VKontakte](https://vk.com)
* [Xing](https://www.xing.com)

## <a id="s20"></a>[↑](#toc) 实时搜索、社交媒体搜索与通用社交媒体工具

* [Audiense](https://www.audiense.com) - 用于识别目标受众、发掘可行洞察并制定业务增长策略的工具。
* [Brandwatch](https://www.brandwatch.com)
* [Buffer](https://buffer.com)
* [Buzz sumo](https://buzzsumo.com) - "借助我们的内容洞察激发创意、创作高表现内容、监测表现并发现意见领袖。"
* [Epieos](https://epieos.com) - 通过邮箱和电话号码搜索社交账号
* [Geocreepy](https://www.geocreepy.com)
* [Hootsuite](https://hootsuite.com)
* [IDCrawl](https://www.idcrawl.com/) - 在主流社交网络中搜索姓名。
* [Klear](https://klear.com)
* [Mail.Ru Social Network Search](https://go.mail.ru/search_social)
* [MustBePresent](https://mustbepresent.com)
* [Oblivion](https://github.com/loseys/Oblivion)
* [OpinionCrawl](https://www.opinioncrawl.com)
* [OSINTNova](https://app.osintnova.com/) - 由 AI 驱动的开源情报（OSINT）平台，用于高级数字调查和情报分析
* [Predicta Search](https://predictasearch.com) - 通过邮箱和电话号码搜索社交账号
* [Rival IQ](https://www.rivaliq.com)
* [Social Searcher](https://www.social-searcher.com)
* [SocialBakers](https://www.socialbakers.com)
* [SocialBlade](https://socialblade.com)
* [Tagboard](https://tagboard.com)

## <a id="s21"></a>[↑](#toc) 社交媒体工具

### <a id="s22"></a>[↑](#toc) Twitter

* [ExportData](https://www.exportdata.io/) - 用于导出历史推文、粉丝与关注列表以及历史趋势的数据导出工具。
* [Foller.me](https://foller.me)
* [MyTweetAlerts](https://www.mytweetalerts.com/) - 基于 Twitter 搜索创建自定义邮件提醒的工具。
* [RiteTag](https://ritetag.com)
* [Tagdef](https://tagdef.com)
* [Trends24](https://trends24.in)
* [TweetAPI Twitter ID Finder](https://tweetapi.com/tools/twitter-id-finder) - 查询 Twitter 用户名或个人主页链接背后的用户 ID，或根据 ID 查找当前用户名。免费，无需注册。
* [TweetMap](https://github.com/cga-harvard/Data_Science_Big_Data_Projects/tree/master/scripts/Geotweets)
* [TwexAPI Twitter Viewer](https://twexapi.io/twitter-viewer) - 无需登录或注册账号即可查看公开的 X（Twitter）个人主页及其最新帖子。
* [Twitter Advanced Search](https://twitter.com/search-advanced?lang=en)
* [Twitter Audit](https://www.twitteraudit.com)
* [Twitter Chat Schedule](https://tweetreports.com/twitter-chat-schedule)
* [Twitter Search](https://search.twitter.com)
* [Xquik](https://xquik.com) - 实时 X（Twitter）数据平台，支持推文搜索、用户查询、粉丝/关注列表提取、互动指标、账号监控、回复/转发/引用提取、社区与 Space 数据以及互关检查。

### <a id="s23"></a>[↑](#toc) Facebook

* [Facebook Friend List Scraper](https://github.com/narkopolo/fb_friend_list_scraper) - 用于抓取大量 Facebook 好友列表且不受速率限制的工具。
* [Facebook GraphQL Scraper](https://github.com/XD-MHLOO/facebook-gql-scraper) - 用于抓取 Facebook 个人资料、帖子、评论、表情回应、群组、Marketplace 和搜索引擎的 Python 库。
* [Facebook Search](https://search.fb.com/)
* [Fanpage Karma](https://www.fanpagekarma.com)
* [Fb-sleep-stats](https://github.com/sqren/fb-sleep-stats) - 利用 Facebook 追踪好友的睡眠习惯。
* [Find my Facebook ID](https://randomtools.io) - 查找你的 Facebook 个人数字 ID，用于 Facebook Graph API 操作、fb:admins 和社交插件。
* [haveibeenzuckered](https://haveibeenzuckered.com/) - 一个包含 5.33 亿个 Facebook 账号的大型数据集被公开提供下载。这些数据是通过利用一个漏洞获取的，据 Facebook 称该漏洞已于 2019 年 8 月修复。可检查某个电话号码是否出现在本次 Facebook 数据泄露中。
* [Lookup-ID.com](https://lookup-id.com) - 查找你的 Facebook 个人主页 ID / 群组 ID / 公共主页 ID。
* [SearchIsBack](https://searchisback.com)
* [Wolfram Alpha Facebook Report](https://www.wolframalpha.com/input/?i=facebook+report)

### <a id="s24"></a>[↑](#toc) Instagram

* [Dolphin Radar](https://www.dolphinradar.com/web-viewer-for-instagram) - 一款 Instagram 帖子查看器，可轻松查看公开账号的帖子、快拍和个人主页。免费查看次数限制：1 次。
* [Iconosquare](https://iconosquare.com)
* [IGDetective](https://www.igdetective.com) - 无需登录即可对公开 Instagram 账号进行调查：匿名快拍查看器、显示账号近期关注/取关的粉丝追踪器、个人主页查看器，还可选择持续追踪并生成永久快拍存档（仅追踪功能需要账号）。
* [instagram_monitor](https://github.com/misiektoja/instagram_monitor) - 实时追踪 Instagram 用户活动和主页变化的工具，支持邮件提醒、CSV 日志记录、在终端显示媒体、匿名下载快拍等功能
* [InstagramPrivSniffer](https://github.com/obitouka/InstagramPrivSniffer) - 无需登录即可查看 Instagram 私密账号的媒体内容 😱。
* [insto](https://github.com/subzeroid/insto) - 交互式开源情报（OSINT）命令行 / REPL 工具，提供 35+ 斜杠命令：个人资料 + 媒体 + 粉丝 + 档案 + 地理指纹（`/where`）、共同粉丝交集（`/intersect`）、超级粉丝排名（`/fans`）、地点搜索（`/place`）、URL→元数据解析（`/postinfo`）、发帖频率直方图（`/timeline`）、Maltego CSV 导出。基于 Token（HikerAPI，无需 IG 账号 → 无封号风险），并可选登录态的 `aiograpi` 后端。
* [Osintgram](https://github.com/Datalux/Osintgram) - Osintgram 提供交互式 shell，可通过昵称对任意用户的 Instagram 账号进行分析。
* [Osintgraph](https://github.com/XD-MHLOO/Osintgraph) - 将目标的 Instagram 数据和关系映射到 Neo4j 中用于社交网络分析的工具。 
* [Toutatis](https://github.com/megadose/toutatis) - 一款可从 Instagram 账号提取电话号码等信息的工具

### <a id="s25"></a>[↑](#toc) TikTok
* [GetTikVideo](https://gettikvideo.com/tiktok-profile-picture-downloader) - 通过 TikTok 个人主页链接获取全尺寸头像和最新公开视频；无需账号即可保存公开视频、图文帖子和快拍。
* [TikTokStalker](https://tiktok.einzzcookie.org) - 查询 TikTok 相关的各类信息

### <a id="s26"></a>[↑](#toc) Pinterest

* [Pingroupie](https://pingroupie.com)
* [Pinterest Pin Stats](https://chromewebstore.google.com/detail/pinterest-pin-stats-sort/mcmkeopcpbfgjlakblglpcccpodbjkel) - 显示每个 Pin 图隐藏的 Pinterest 统计数据。

### <a id="s27"></a>[↑](#toc) Reddit

*帮助你深入了解某个 Reddit 用户或子版块的工具。*

* [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) - 用于访问和操作 Reddit 大量数据转储的工具，提供 API 和 Web 界面，便于研究与审核。
* [Imgur](https://imgur.com/search?q=) - Reddit 用户最常用的图片托管网站。
* [Mostly Harmless](https://kerrick.github.io/Mostly-Harmless/#features) - Mostly Harmless 会检查你当前浏览的页面，看它是否已被提交到 Reddit。
* [Pushshift API](https://pushshift.io/) - 功能强大的 API，可访问 Reddit 历史数据（包括帖子、评论和元数据）用于分析与研究——更多信息见[此处](https://www.reddit.com/r/pushshift/)。
* [Pullpush](https://pullpush.io/) - PullPush 是一项用于索引和检索 Reddit 用户所提交内容的服务，有助于查找已删除/被移除的帖子和评论。
* [REDARCS](https://the-eye.eu/redarcs/) - Reddit 2005-2023 年存档。
* [Reddit Suite](https://chrome.google.com/webstore/detail/reddit-enhancement-suite/kbmfpngjjgdllneeigpgjifpgocmfgmb) - 增强你的 Reddit 使用体验。
* [Reddit User Analyser](https://atomiks.github.io/reddit-user-analyser/) - Reddit 用户账号分析器。
* [RedditMetis](https://redditmetis.com/) - RedditMetis 是一款 Reddit 用户分析工具，可查看某个 Reddit 账号的概览和统计数据，包括热门帖子和用户活动等。
* [Subreddits](https://subreddits.org) - 发现新的子版块。
* [Reddit Comment Search](https://redditcommentsearch.com/) - 通过评论历史分析 Reddit 用户。
* [Universal Scammer List](https://universalscammerlist.com/) - 这是 /r/universalscammerlist 子版块的网站部分。该子版块与本站及一个 Reddit 机器人共同维护一份恶意 Reddit 账号名单，尽可能降低其造成的危害。这份名单简称为 "USL"。
* [Reddit Comment Lookup](https://randomtools.io/reddit-comment-search/) - 按 Reddit 用户名搜索 Reddit 评论。


### <a id="s28"></a>[↑](#toc) VKontakte

*对俄罗斯社交媒体网站 VKontakte 执行各类开源情报（OSINT）调查。*

* [Дезертир](https://vk.com/app3046467)
* [Barkov.net](https://vk.barkov.net)
* [VK5](https://vk5.city4me.com)
* [VK Community Search](https://vk.com/communities)
* [VK People Search](https://vk.com/people)
* [VK.watch](https://vk.watch/)

### <a id="s29"></a>[↑](#toc) WhatsApp

* [2Chat](https://2chat.co/tools/whatsapp-checker) - 检查某个号码是否注册了 WhatsApp。
* [Groupio](https://en.groupio.app/) - 查找和搜索 WhatsApp 群组。
* [Whatsapp CheckLeaked](https://whatsapp.checkleaked.cc/) - WhatsApp 号码搜索与头像检查工具，提供 API 选项。

### <a id="s30"></a>[↑](#toc) Tumblr

* [Tumblr Search](https://www.tumblr.com/search)

### <a id="s31"></a>[↑](#toc) LinkedIn

* [the-endorser](https://github.com/eth0izzle/the-endorser) - 通过背书/技能梳理 LinkedIn 上人物之间关系的工具。
* [LinkedInDumper](https://github.com/l4rm4nd/LinkedInDumper) - 从 LinkedIn API 导出/抓取/提取公司员工信息的脚本。

### <a id="s32"></a>[↑](#toc) Telegram

* [CCTV](https://github.com/IvanGlinkin/CCTV) - Close-Circuit Telegram Vision 以其开源设计和对 Telegram API 的集成革新了位置追踪。可实现 50-100 米内的精确定位，用户能出于物流或安全目的实时监控他人，重新定义我们感知周围环境的方式。
* [GroupDa](https://groupda.com/telegram/group/search) - 可用于搜索 Telegram 频道，支持按类别、国家和语言筛选。
* [Maltego Telegram](https://github.com/vognik/maltego-telegram) - 借助 Maltego 对 Telegram 开展开源情报（OSINT）的丰富实体与转换（Transform）集合。
* [Telegram Finder](https://www.telegram-finder.io/) - 通过电话号码、LinkedIn 链接或邮箱查找 Telegram 用户的工具。
* [Telerecon](https://github.com/sockysec/Telerecon) - 用于研究和调查 Telegram 的信息收集（侦察）框架。
* [TgramSearch](https://tgramsearch.com/) - 便捷搜索 Telegram 频道，并提供收录超过 700000 个 Telegram 频道的结构化目录，支持 8 种以上语言。
* [Telegram Channel Joiner](https://github.com/spmedia/Telegram-Channel-Joiner) - 使用这款频道加入脚本轻松养大你的免费与 Premium Telegram 账号。
* [Telepahty](https://github.com/proseltd/Telepathy-Community) - Telepathy 是一款存档 Telegram 聊天并分析应用内通信模式的工具。通过揭示用户互动、消息频率和内容趋势，帮助调查人员理解 Telegram 群组和频道中的动态与关系。
* [Teleteg](https://teleteg.com/) - 终极 Telegram 搜索引擎。免费套餐可查看 10 条结果。  
* [Telegago](https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg#gsc.tab=0&gsc.q=%20&gsc.page=1) - 专门用于查找公开和私密 Telegram 频道与聊天室的 Google 高级搜索。 
* [Telegram-Archive](https://github.com/GeiserX/Telegram-Archive) - 自托管的 Telegram 账号聊天与媒体备份，按计划定时运行，保留编辑记录与已删除消息，并提供本地 Web 查看器，可搜索所有聊天。
* [Telegram Nearby Map](https://github.com/tejado/telegram-nearby-map) - 基于 OpenStreetMap 和 Telegram 官方库构建的 Web 应用，用于查找附近用户的位置。
* [Telegram channels scraper TeleGraphite ](https://github.com/hamodywe/telegram-scraper-TeleGraphite) - Telegram 抓取器、JSON 导出器与 Telegram 频道抓取工具。
* [TeleSearch](https://telesearch.me/) - 借助 TeleSearch 快速轻松地搜索并找到你想要的 Telegram 频道、群组、机器人和游戏。
* [TeleTracker](https://github.com/tsale/TeleTracker) - TeleTracker 是一组简洁的 Python 脚本，面向调查 Telegram 频道的人员。它可帮助你快速发送消息并轻松收集有用的频道信息。
* [tg-chat-dump](https://github.com/renkagod/tg-chat-dump) - 将整个 Telegram 群组、频道或论坛存档为可搜索的 SQLite 数据库以及按主题划分的文本和 JSONL 文件，在 Telegram 导出模式下每分钟可处理 10 万条以上消息。支持按日期、作者和消息类型筛选。
* [TGScope](https://tgscope.io/) - 收录 300 万+ 公开 Telegram 频道的搜索引擎与目录，可按主题、语言和规模浏览，提供各频道统计数据以及汇集提及地点、公司和人物的帖子的事件页面。
* [TGScope Channel Creation Date](https://tgscope.io/tools/telegram-channel-creation-date) - 通过用户名、t.me 链接或数字 ID 判断 Telegram 频道或超级群组创建时间的 Web 工具。
* [TGStat](https://tgstat.com/) - 分析 Telegram 频道、群组、指标和热门动态的开源情报（OSINT）平台。
* [Tme-s](https://github.com/axmaier/tme-s) - 通过未登录状态下的 t.me/s/ 网页预览读取公开 Telegram 频道：无需 API 密钥、无需手机号、无需账号。支持关键词过滤、JSON 输出，仅依赖 Python 标准库。
* [TOsint](https://github.com/drego85/tosint) - Tosint（Telegram OSINT）是一款功能强大的工具，用于从 Telegram 机器人和频道中提取有价值的信息。它是安全研究人员、调查人员以及任何希望从各类 Telegram 实体收集洞察的人的重要资源。

**Telegram 机器人**
* [AgentFNS_Bot](https://t.me/AgentFNS_bot) — 使用官方数据（INN/OGRN）即时免费核查交易对手。
* [AVinfoBot](https://t.me/AVskp_Bot) — 通过车牌/VIN/手机号查询二手车历史。
* [AvtoNomer](https://t.me/avtonomerbot) — 借助 platesmania.com 按车牌查找车辆照片。
* [avtogram_bot](https://telegram.me/ABTOGRAMBOT) — 付费车辆报告（VIN/车牌）：事故、罚款、抵押留置。
* [avtocodbot](https://t.me/avtocodbot) — 付费 VIN/车牌查询。
* [bmi_np_bot](https://t.me/MNProbot) — 识别手机号运营商及基本信息。
* [ChatSearchRobot](https://t.me/ChatSearchRobot) — 查找主题相近的聊天；收录 70.9 万+ 个 VK 聊天。
* [ClerkBot](https://t.me/clerksecretbot) — 手机号 + 用户名查询；车辆信息。
* [creationdatebot](https://t.me/creationdatebot) — 估算 Telegram 账号创建日期。
* [CryptoBot](https://t.me/CryptoBot) — 匿名加密货币钱包。
* [datXpert](https://telegram.me/datxpertbot) — 通过 IntelX 搜索泄露数据。
* [Detectiva](https://detectiva.link/rezervBot) — 手机号/邮箱查询，提供 6 种搜索类型。
* [Discord Sensor](https://telegram.me/discordsensorbot) — 获取 Discord 账号数据。
* [dCallsBot](https://t.me/dCallsBot) — 匿名通话、号码伪装、eSIM/DID。
* [EasyVIN](https://t.me/EasyVINbot) — 低价的 VIN/车牌历史查询。
* [egrul_bot](https://t.me/egrul_bot) — 免费的交易对手核查机器人。
* [EyeTON](https://telegram.me/istoneyebot) — TON 钱包关系图 + 关联个人资料。
* [FindStickerCreator](https://t.me/SPOwnerBot) — 查找任意 Telegram 贴纸包的创建者。
* [Фари](https://telegram.me/faribybot) — 从 getcar.by 查询 VIN 历史记录。
* [GeoMacFinder](https://t.me/geomacbot) — 通过 MAC/BSSID 查找 Wi-Fi 接入点位置。
* [getChatList](https://telegram.me/getchatlistbot) — 显示用户的群组列表。
* [Getairplane](https://telegram.me/getairplane_bot) — 手机号 → 航班历史（20 年）。
* [GetSendGifts](https://telegram.me/GetSendGiftsProBot) — 显示谁赠送了 Telegram 礼物。
* [HimeraSearch](https://t.me/HimeraNeGBL8Pro1dp_Search_bot) — 开源情报（OSINT）/人力情报（HUMINT）搜索：手机号、邮箱、车辆、人物、法院记录。
* [Insight](https://t.me/ibhld_bot) — 根据订阅内容显示兴趣偏好。
* [InstaAnonym](https://t.me/instaanonymbot) — 匿名 Instagram/VK 查看器。
* [InstaBot](https://telegram.me/InstaBot) — 下载 Instagram 媒体内容。
* [ITP Infotrack](https://infotrackpeople.org/) — 人物、车辆、房产查询。
* [Leak OSINT](https://telegram.me/Leak_SSINTbot) — 手机号泄露检测。
* [Maigret OSINT bot](https://t.me/osint_maigret_bot) — 在 1,366 个站点上搜索用户名。
* [mnp_bot](https://t.me/mnp_bot) — 手机号运营商 + 归属地。
* [MotherSearchBot](https://t.me/MotherSearchBot) — 类似 Google 的 Telegram 搜索。
* [NEUROAUTOSEARCH](https://t.me/noblackAuto_bot) — 车辆数据库搜索 + 神经网络。
* [OkSearch](https://telegram.me/OkSearchBot) — 按关键词搜索频道、机器人、群组。
* [OpenDataUABot](https://t.me/OpenDataUABot) — 乌克兰开源情报（OSINT）机器人。
* [OPENLOAD Bot](https://t.me/OPENLOADTOPBOT) — 半自动化的开源情报（OSINT）/漏洞扫描套件。
* [Osintkit](https://t.me/osintkit_check_bot) — 乌克兰信息查询：护照、税号、邮箱、手机号、地址、车辆、Telegram。
* [PasswordSearch](https://telegram.me/PasswordSearchBot) — 显示某个邮箱泄露的密码。
* [PimEyes](https://telegram.me/pimeyesbot) — 跨社交网络的人脸搜索。
* [RegDateBot](https://t.me/regdate_clone_bot) — 通过 ID/转发消息查询注册日期。
* [SangMata (beta)](https://t.me/SangMata_beta_bot) — 通过 /search_id 查询改名历史。
* [SangMataInfo_bot](https://t.me/SangMataInfo_bot) — 用户名变更历史。
* [SaveYoutubeBot](https://t.me/SaveYoutubeBot) — 查找并下载 YouTube 视频。
* [Search_firm_bot](https://t.me/Search_firm_bot) — 搜索组织机构、银行、邮政编码。
* [Searchforchats](https://telegram.me/searchforchatsbot) — 按关键词搜索聊天。
* [Sherlock](https://t.me/Getcontact123qwerty_bot?start=_ref_jGW8Sa_iEmG9V) — 姓名/手机号/邮箱搜索 + 车辆数据。
* [ShtrafKZBot](https://t.me/ShtrafKZBot) — 罚款、税费、滞纳金；交通违法记录。
* [SMS Activate](https://t.me/PrivatePhoneBot) — 来自 50 多个国家的虚拟号码。
* [SpyGGbot](https://telegram.me/SpyGGbot) — TON 余额、NFT 持有者、Fragment 用户名。
* [Surftg_bot](https://t.me/surftg_bot) — 搜索 Telegram 消息。
* [TuriBot](https://t.me/TuriBot) — 通过 Telegram ID 反查用户名。
* [Unamer](https://telegram.me/unamer_bot) — 用户名归属历史。
* [username_to_id_bot](https://t.me/username_to_id_bot) — 返回用户/聊天/频道/机器人的 ID。
* [UsInfoBot](https://t.me/usinfobot) — 通过 ID 反查用户名（内联模式）。
* [WhoisDomBot](https://t.me/WhoisDomBot) — 域名/IP 的 Whois 查询 + dig/trace。

### <a id="s33"></a>[↑](#toc) Steam

* [OSINT-Steam](https://osint-steam.vercel.app/en) - 一款[开源](https://github.com/Berchez/OSINT-steam)工具，可从 Steam 个人资料返回公开信息，例如好友列表和可能的位置。

* [Steam-OSINT](https://github.com/matiash26/steam-osint) - 开源 OSINT 工具，可精确分析 Steam 上的共同好友，支持完整好友列表。

### <a id="s34"></a>[↑](#toc) GitHub

* [GHNames](https://ghnames.com/) - GitHub 查询工具，可搜索用户名历史、关联邮箱和已删除的仓库。
* [github_monitor](https://github.com/misiektoja/github_monitor) - 实时追踪 GitHub 用户活动的工具，包括个人资料和仓库变化，支持邮件提醒、CSV 日志记录、检测用户拉黑或取消拉黑你等功能
* [GithubRecon](https://kriztalz.sh/github-recon/) - 通过用户名或邮箱查询 GitHub 用户并收集关联数据。
* [GitLeak](https://gitleak.io) - 面向 GitHub 的开源情报（OSINT）工具，通过 .patch 元数据提取隐藏的邮箱地址、提交时区和活动规律。
* [Related Repos](https://relatedrepos.com/) - 发现相关的开源项目，查找替代方案和其他相似仓库，每日更新。
* [Shotstars](https://github.com/snooppr/shotstars) - 用于检查 GitHub 仓库的高级工具，提供 star 统计，包括虚假 star 分析和数据可视化。
## <a id="s35"></a>[↑](#toc) 博客搜索


* [Notey](https://www.notey.com) - 博客文章搜索引擎。
* [Twingly](https://www.twingly.com)

## <a id="s36"></a>[↑](#toc) 论坛与讨论板搜索

* [4chan Search](https://4chansearch.com/)
* [Boardreader](https://boardreader.com)
* [Facebook Groups](https://www.facebook.com)
* [Google Groups](https://groups.google.com)
* [Linkedin Groups](https://www.linkedin.com)
* [Ning](https://www.ning.com)
* [Yahoo Groups](https://groups.yahoo.com)

## <a id="s37"></a>[↑](#toc) 用户名查询

* [Blackbird](https://github.com/p1ngul1n0/blackbird) - 在 600 多个网站上搜索用户名。
* [Cupidcr4wl](https://github.com/OSINTI4L/cupidcr4wl) - 用户名和电话号码搜索工具，通过爬取成人内容平台来判断目标账号或人物是否存在。
* [Digital Footprint Check](https://www.digitalfootprintcheck.com/free-checker.html)  - 免费检查数百个站点上是否已注册该用户名。
* [Helix](https://github.com/thalha-a9/helix) - 在 8,000 多个站点上检查用户名，用不可能存在的用户名对每个命中结果实时复核，并绘制账号之间的关联图。
* [IDCrawl](https://www.idcrawl.com/username) - 在主流社交网络中搜索用户名。
* [Maigret](https://github.com/soxoj/maigret) - 通过用户名收集某个人的档案。
* [Name Chk](https://www.namechk.com) - 检查 30 多个域名和 90 多个社交媒体账号平台。
* [Name Checkup](https://namecheckup.com) - 是一款搜索工具，可检查某个用户名在所有社交媒体上的可用性，此外还能检查给定域名的可用性。
* [NexFil](https://github.com/thewhiteh4t/nexfil) - 检查几乎所有社交网站上的用户名。
* [Seekr](https://github.com/seekr-osint/seekr) - 一款多功能一体化工具包，用于收集和管理开源情报（OSINT）数据，配有简洁的 Web 界面。可用于记笔记和用户名查询。
* [Sherlock](https://github.com/sherlock-project/sherlock) - 在多个平台/网站上搜索用户名。
* [SherlockEye](https://sherlockeye.io/) - 搜索与某个用户名相关联的公开信息，揭示其在网络上的关联个人资料和活动。
* [Trace](https://trace.manus.space) - 实时开源情报（OSINT）平台，可在 600 多个平台上搜索用户名、邮箱、电话号码和全名，具备数据泄露检测和 AI 风险评分功能。
* [TraceFind](https://tracefind.info) - 即时揭开任意用户名背后的真相，扫描数千个站点检查该用户名是否存在。
* [Snoop](https://github.com/snooppr/snoop/blob/master/README.en.md) - 在网络上搜索昵称（开源情报领域）
* [Social Analyzer](https://github.com/qeeqbox/social-analyzer) - 提供 API、命令行和 Web 应用，用于在 1000 个社交媒体 \ 网站上分析和查找某个人的个人资料。
* [Threat Actor Username Search](https://threatactorusernames.com) - 在 300 万+ 个威胁行为者用户名中搜索，找出犯罪分子和恶意分子在网上发帖与活动的场所。
* [user-scanner](https://github.com/kaifcodec/user-scanner.git) — 检查某个用户名在开发/社交/游戏/创作类站点上的存在情况
* [User Search](https://www.usersearch.org) - 通过用户名、邮箱、电话号码或照片在社交网络、交友网站、论坛、加密货币论坛、聊天站点和博客中查找某人，支持 3000 多个站点！
* [User Searcher](https://www.user-searcher.com) - User-Searcher 是一款强大且免费的工具，帮助你在 2000 多个网站中搜索用户名。
* [WhatsMyName](https://whatsmyname.app/) - 在众多不同平台上检查用户名。


## <a id="s38"></a>[↑](#toc) 人物调查

* [192 (UK)](https://www.192.com) - 按人物、企业、地址搜索。免费信息有限，付费数据需另行购买。
* [411 (US)](https://www.411.com) - 按人物、电话号码、地址和企业搜索。免费信息有限，付费数据需另行购买。
* [Ancestry](https://www.ancestry.com) - 付费数据，绑定信用卡可免费试用。
* [Apollo.io](https://www.apollo.io/) - 免费的 B2B 电话号码和邮箱查找工具，免费套餐每用户每年 1200 点数。
* [BeenVerified](https://www.backgroundchecks.com/solutions/beenverified)
* [Black Book Online](https://www.blackbookonline.info) - 免费。全国范围的公共记录查询目录。
* [BuscaPaginasBlancas](https://github.com/GeiserX/BuscaPaginasBlancas) - 用于从西班牙白页（Paginas Blancas）提取联系信息的开源情报（OSINT）工具。
* [California Justice Watch](https://cajusticewatch.com) - 免费。加州的公共记录问责数据：58 名地区检察官、196 名公设辩护人、1,620 名在任法官、1,500 名有记录在案不当行为的执法人员、247 条司法绩效委员会（CJP）纪律处分记录（并可对 250 份 CJP 裁决 PDF 全文检索），以及 671 项 POST 吊销认证记录。开放 API + MCP 服务器。
* [Canada411](https://www.canada411.ca) - 按人物、电话号码和企业搜索。免费。
* [Classmates](https://www.classmates.com) - 以高中校友为主的人物搜索。免费账号可创建个人资料并查看其他会员，联系其他会员则需要付费账号。
* [ContactOut](https://contactout.com/) - 解锁全球最精准的联系数据，查找 3 亿专业人士的邮箱和电话号码。
* [CrunchBase](https://www.crunchbase.com) - 企业信息数据库，侧重投资、收购和高管数据，并兼顾市场研究以及为创始人与投资人牵线搭桥。
* [FaceCheck.ID](https://facecheck.id) - 以人脸搜索互联网。
* [Family Search](https://familysearch.org) - 热门家谱网站。免费，但需要注册。由耶稣基督后期圣徒教会资助。
* [FamilyTreeNow](https://familytreenow.com) - 研究家族与家谱，无需注册，可搜索地址、电话号码、邮箱地址以及关联关系。
* [FinalNotes Obituary Research Guide](https://www.finalnotes.page/obituary-research-guide/) - 指导如何查找讣告记录、保留来源线索，并将讣告线索转化为有据可查的家族史叙述。
* [Federal Bureau of Prisons - Inmate Locator (US)](https://www.bop.gov/inmateloc) - 可搜索 1982 年至今被关押的联邦囚犯。 
* [Fold3 (US Military Records)](https://www.fold3.com) - 搜索军事记录。免费访问的搜索筛选功能有限，高级访问需要订阅。
* [Genealogy Bank](https://www.genealogybank.com) - 付费数据，绑定信用卡可免费试用。
* [Genealogy Links](https://www.genealogylinks.net) - 收录超过 5 万条链接的家谱目录。
* [InfoTracer](https://infotracer.com/) - 人物搜索。（搜索为付费服务）
* [Judyrecords](https://www.judyrecords.com/) - 免费。可检索全美 4 亿多起法院案件。
* [Kompass](https://www.kompass.com) - 企业名录与搜索。
* [LERS Portal Directory (Ministry of Cyber Affairs)](https://ministryofcyberaffairs.com/lers) - 各平台执法数据请求（LERS）门户目录（WhatsApp、Google、Apple、Telegram、TikTok、Binance），为经授权的调查人员提供申请资格与提交步骤。
* [Mugshots](https://mugshots.com/)
* [Offendersearch](https://offendersearch.app) - 免费。一次查询即可搜索美国全部 58 个州、属地和部落的性犯罪者登记库；结果经过评分、去重，并附有指向每条匹配背后官方登记记录的链接。公开 API + 开放数据 + MCP 服务器。
* [OpenSanctions](https://www.opensanctions.org/search/) - 提供制裁和公职人员信息。
* [PeekYou](https://peekyou.com/) - PeekYou 支持在更多站点上核查来搜索人物，也可查询逮捕记录。
* [recap-cli](https://github.com/NPCmillionaire/recap-cli) - 免费的开源命令行工具，用于从 RECAP 存档（CourtListener）搜索并下载美国联邦法院的案卷和文档。需要免费的 API token。
* [Reunion](https://reunion.com) - 人物搜索。免费信息有限，付费数据需另行购买。
* [Socialcatfish](https://socialcatfish.com/) - 覆盖全球的超大规模人物搜索，检索基于 2000 亿条记录。
* [SearchBug](https://www.searchbug.com) - 人物搜索。免费信息有限，付费数据需另行购买。
* [Spokeo](https://www.spokeo.com) - 人物搜索。免费信息有限，付费数据需另行购买。
* [Surfface](https://surfface.com) - 人脸搜索与人物查找工具，可将人脸关联到社交媒体个人资料及其他公开数据。
* [The National Archives (UK)](https://www.nationalarchives.gov.uk) - 搜索英国国家档案馆。
* [UniCourt](https://unicourt.com/) - 免费搜索次数有限，付费数据需另行购买。可检索全美 1 亿多起法院案件。
* [UK Phone Book](https://www.ukphonebook.com/) - 以类似 192.com 的方式搜索人物
* [VerifiedHer](https://verifiedher.com) - 免费的在线创作者与网红登记库，回答"她是真人吗？"——逐人页面给出有来源的判定（真人 / AI 虚拟形象 / 未核实）、记录在案的官方账号以及已知的仿冒账号。
* [VineLink](https://www.vinelink.com/#state-selection) - 面向犯罪受害者的在押人员搜索与通知服务，对接美国多个惩教机构的收押系统。
* [Voter Records](https://voterrecords.com/) - 免费的政治研究工具，可研究超过 1 亿条美国选民记录。
* [White Pages (US)](https://www.whitepages.com) - 人物搜索。免费信息有限，付费数据需另行购买。
* [ZabaSearch](https://www.zabasearch.com/)

## <a id="s39"></a>[↑](#toc) 邮箱搜索 / 邮箱核查

* [Blackbird](https://github.com/p1ngul1n0/blackbird) - 在多个平台搜索与指定邮箱相关联的账号。
* [Blacklist Checker](https://blacklistchecker.com/) - Blacklist Checker 是一款邮箱黑名单检测、监控与 API 工具，可在数秒内检查 100 多个黑名单
* [DeHashed](https://dehashed.com/) - DeHashed 凭借庞大的数据集和泄露通知方案帮助防范账号盗用（ATO）。可将员工和消费者的登录信息与全球最大的、由第三方数据泄露中公开的聚合资产库进行比对，在犯罪分子滥用被盗信息之前加固密码，保护你的企业。
* [Email Address Validator](https://www.email-validator.net)  - 提升送达率、降低退信率、防范欺诈并减少转化漏斗流失。
* [Email Extractor](https://99tools.net/email-extractor/)  - 基于浏览器的工具，可从批量文本或原始数据中快速提取邮箱地址以便进一步调查。
* [Email Format](https://email-format.com) - 可查询不同公司所用邮箱地址格式的网站。
* [Email Permutator](https://www.polished.app/email-permutator/) - 一款功能强大的工具，帮助专业人士为特定联系人生成一系列可能的邮箱地址。 
* [EmailHippo](https://tools.verifyemailaddress.io) - 邮箱地址验证平台，可检查给定邮箱地址是否存在。
* [EmailRep](https://emailrep.io) - 邮箱地址信誉与风险评分服务。
* [Epieos Tools](https://tools.epieos.com) - 面向邮箱调查的开源情报（OSINT）工具合集。
* [Ghunt](https://github.com/mxrch/GHunt) - 调查 Google 邮箱和文档。
* [Gitrecon](https://github.com/atiilla/gitrecon) - Node.js 工具，用于扫描 GitHub 仓库中暴露的邮箱地址和姓名。
* [h8mail](https://github.com/khast3x/h8mail) - 密码泄露搜寻与邮箱开源情报（OSINT）工具，可本地运行或借助付费服务，支持追查关联邮箱。
* [Have I Been Pwned](https://haveibeenpwned.com) - 检索多起数据泄露事件，查看你的邮箱地址是否已遭泄露。
* [Holehe](https://github.com/megadose/holehe) - 可检查某个邮箱是否注册于 twitter、instagram 等不同站点，并从提供"忘记密码"功能的站点检索信息。
* [Hunter](https://hunter.io) - Hunter 让你在数秒内找到邮箱地址，并与对业务至关重要的人建立联系。
* [InfoStealers](https://infostealers.info/en/info) - 对暗网暴露的信息窃取木马（infostealer）日志建立索引，使安全团队、调查人员、研究人员和数字取证专业人员能够搜索和利用这些数据。
* [IntelBase](https://intelbase.is/) - 专注于邮箱反查和邮箱数据富化的取证平台。
* [LeakCheck](https://leakcheck.io/) - 数据泄露搜索引擎，收录来自 3000 多个数据库的 75 亿+ 条记录，可按邮箱、用户名、关键词、密码或企业域名搜索。
* [LeakRadar](https://leakradar.io/) - 在信息窃取日志中扫描已泄露的邮箱和域名，提供主动的泄露防范和实时告警。
* [MailAccess](https://github.com/KatrielMoses/MailAccess) - 免费的邮箱开源情报（OSINT）工具，可检查 800 多个平台、通过 HIBP 查询泄露暴露情况、通过 Hudson Rock 查询信息窃取日志，并构建带置信度评分的跨平台身份关系图。`pip install mailaccess`
* [MailTester](https://mailtester.com) - 搜寻邮箱并提升邮件送达率
* [Minerva OSINT](https://minervaosint.com) - 邮箱搜索工具，可从上百个网站查找并聚合目标邮箱的相关数据。
* [Multirbl](https://multirbl.valli.org/dnsbl-lookup) - MultiRBL Valli 可同时检查某个 IP 或域名是否被列入多个公共 RBL（黑名单）。
* [mxtoolbox](https://mxtoolbox.com/) - 免费的在线工具，用于排查/诊断邮件服务器问题。
* [OpenLeads](https://github.com/Samyrrrrrr990/openleads) - 开源命令行工具，从公开来源（OpenStreetMap、GitHub、OpenAlex、SEC EDGAR、公司团队页面）查找人物及其工作邮箱，并将每个地址标注为"实测发现"、"按规则推导"或"猜测"。本地运行，无需 API 密钥。
* [OSINTEye](https://github.com/atiilla/OsintEye) - OSINT Eye：一款用于 GitHub 情报、社交媒体侦察和子域名发现的 WPF 桌面应用
* [Pipl](https://pipl.com) - 身份解决方案提供商。
* [Reacher](https://reacher.email) - 实时邮箱验证 API，使用 Rust 编写，100% 开源。
* [SherlockEye](https://sherlockeye.io/) - 在互联网上的多个来源中搜索与某个邮箱地址相关联的公开数据。
* [Snov.io](https://snov.io/email-finder) - 在任意网站上查找邮箱地址。
* [Spamhaus](https://check.spamhaus.org/) - 信誉查询检测工具。
* [SpoofCheck](https://spoofchecker.online/) - 免费的邮件伪造测试：检查某个域名的 SPF、DKIM、DMARC、MTA-STS 和 MX 记录，并对其被仿冒的难易程度评级（A 到 F）。
* [ThatsThem](https://thatsthem.com/reverse-email-lookup) - 邮箱反查。
* [Toofr](https://www.toofr.com) - 数秒内找到任何人的邮箱地址。
* [TraceFind](https://tracefind.info) - 即时揭开任意邮箱背后的真相，扫描数百个站点检查邮箱是否存在、有无泄露等。
* [user-scanner](https://github.com/kaifcodec/user-scanner.git) - 输入邮箱，在各类热门站点、游戏中扫描，并获取该邮箱是否已注册的信息。
* [Verify Email](https://verify-email.org) - 最快、最准确的邮箱验证工具。
* [VoilaNorbert](https://www.voilanorbert.com) - 查找任何人的联系信息，用于潜在客户调研或人才招募。

## <a id="s40"></a>[↑](#toc) 电话号码研究

* [EmobileTracker.com](https://www.emobiletracker.com/) - 一项专门用于追踪手机号并在 Google 地图上定位的服务，可提供机主姓名、位置、国家、电信运营商等信息。
* [FreeCarrierLookup](https://freecarrierlookup.com/) - 输入电话号码，即可返回运营商名称以及该号码是移动号还是固话。我们还提供美国和加拿大*号码的邮件转短信（email-to-SMS）和邮件转彩信（email-to-MMS）网关地址。
* [Infobel](https://www.infobel.com/) - 在 73 个国家搜索超过 1.64 亿条企业和个人记录，可查找地点、本地服务商及其联系方式、评价、营业时间等。
* [InMobPrefix](https://github.com/hstsethi/in-mob-prefix) - 关于印度手机号码前缀及其所属邦、运营商的数据集、图表和模型。
* [Phone Validator](https://www.phonevalidator.com/index.aspx) - 相当准确的电话号码查询服务，尤其擅长识别 Google Voice 号码。
* [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga) - 面向电话号码的高级信息收集与开源情报（OSINT）框架。
* [Reverse Phone Lookup](https://www.reversephonelookup.com/) - 提供电话运营商、地区、服务提供商和交换机等详细信息。
* [SearchPeopleFREE](https://www.searchpeoplefree.com/phone-lookup) - 支持按姓名、地址、邮箱地址或电话反查，可用于查明某个电话号码的机主或某处地址的居住者。
* [Spy Dialer](https://spydialer.com/) - 获取手机语音信箱并查询机主姓名。
* [Sync.ME](https://sync.me/) - 来电显示与骚扰拦截应用。
* [TraceFind](https://tracefind.info) - 即时揭开任意电话号码背后的真相，扫描多个站点检查号码是否存在、有无泄露、是否有效等。
* [Truecaller](https://truecaller.com) - 全球电话号码反查。
* [Twilio](https://www.twilio.com/docs/lookup/v2-api) - 查询电话号码的运营商类型、位置等信息。Twilio 提供附带额度的免费账号，可用于调用其 API。通常每次查询美国和加拿大号码仅约 $0.01-$0.02。
* [USPhoneBook](https://www.usphonebook.com/) - 电话号码与地址反查，以及领先的数据。

## <a id="s41"></a>[↑](#toc) 车辆 / 汽车研究

* [FaxVIN](https://www.faxvin.com/) - 车辆历史报告。这是一款车牌查询工具，可返回 VIN、车辆品牌与型号、车龄以及众多其他细节。 
* [EpicVIN](https://epicvin.com/) - 车辆报告汇总自多种数据源，包括州政府机构及 NMVTIS 等机构的历史事故记录。通过车牌查询可返回 VIN 和车辆里程。

## <a id="s42"></a>[↑](#toc) 专家搜索

* [Academia](https://academia.edu) - 用于分享学术研究的平台。
* [ExpertiseFinder](https://www.expertisefinder.com)
* [ExpertPages](https://expertpages.com)
* [Experts.com](https://www.experts.com)
* [HARO](https://www.helpareporter.com)
* [Idealist](https://www.idealist.org)
* [Innocentive](https://www.innocentive.com)
* [Library of Congress: Ask a Librarian](https://www.loc.gov/rr/askalib)
* [Maven](https://www.maven.co)
* [MuckRack](https://muckrack.com) - 庞大的美国政府公共记录数据库，通过联邦和州级公共记录申请获取。自动化工具可代为提出公共记录申请并持续跟进，直到取得记录为止。
* [National Speakers Association](https://www.nsaspeaker.org)
* [Newswise](https://www.newswise.com)
* [Patent Attorneys/Agent Search](https://oedci.uspto.gov/OEDCI/) - 有资格在美国专利局程序中代理个人的美国律师官方名录。
* [PRNewswire](https://prnmedia.prnewswire.com)
* [ReseacherID](https://www.researcherid.com)
* [SheSource](https://www.shesource.org)
* [Sources](https://www.sources.com)
* [TRExpertWitness](https://trexpertwitness.com)
* [Zintro](https://www.zintro.com)

## <a id="s43"></a>[↑](#toc) 企业调查

* [AllStocksLinks](https://www.allstocks.com/links)
* [Better Business Bureau](https://www.bbb.org)
* [Bloomberg](https://www.bloomberg.com/research/company/overview/overview.asp)
* [BrownBook](https://www.brownbook.net/)
* [Bureau Van Dijk](https://www.bvdinfo.com)
* [Business Source](https://www.ebscohost.com/academic/business-source-complete)
* [Canadian Business Research](https://www.canada.ca/en/services/business/research.html)
* [capitol-cli](https://github.com/NPCmillionaire/capitol-cli) - 免费的开源命令行工具，根据官方 STOCK Act 申报文件追踪美国众议院议员的股票交易，附带委员会交叉引用和逾期申报标记。
* [Caselaw Access Project](https://case.law/) - 收录美国各州上诉法院历史案件（非最新）全文的合集。  
* [Company Registration Round the World](https://www.commercial-register.sg.ch/home/worldwide.html)
* [Company Research Resources by Country Comparably](https://www.comparably.com)
* [CompeteShark](https://competeshark.com)
* [Corporate Information](https://www.corporateinformation.com) - 汇总自公开来源的全球上市公司信息。
* [CorporationWiki](https://www.corporationwiki.com/)
* [CrunchBase](https://www.crunchbase.com) - 提供初创企业的详细信息，尤其侧重于特定企业所使用的融资来源和融资流程。 
* [Data.com Connect](https://connect.data.com)
* [EDGAR U.S. Securities and Exchange Commission Filings](https://www.edgar-online.com) - 所有美国上市公司的定期报告与大量公司披露文件。
* [Europages](https://www.europages.co.uk)
* [Ezilon](https://www.ezilon.com)
* [Factiva](https://global.factiva.com)
* [Forbes Global 2000](https://www.forbes.com/global2000/)
* [Fylings](https://www.fylings.com) - 面向非洲的免费企业情报平台：可在 18 个以上官方国家登记机构（尼日利亚 CAC、坦桑尼亚 BRELA、毛里求斯 CBRD、塞内加尔 RCCM 等）中搜索并核实企业，每条记录都附有官方来源和最近核实日期。
* [Glassdoor](https://www.glassdoor.com)
* [globalEdge](https://globaledge.msu.edu)
* [GoodFirms](https://www.goodfirms.co/)
* [govint](https://github.com/NPCmillionaire/govint) - 免费的命令行工具，可在美国政府记录（SEC EDGAR、制裁名单、USAspending、GLEIF、FEC、SAM.gov、FARA 等）中搜索某家公司或某个人，关联结果并生成附来源的档案。
* [GuideStar](https://www.guidestar.org)
* [Hoovers](https://www.hoovers.com)
* [Inc. 5000](https://www.inc.com/inc5000)
* [Judyrecords](https://www.judyrecords.com/) - 免费。可检索全美 4 亿多起法院案件。
* [Knowledge guide to international company registration](https://www.icaew.com/en/library/subject-gateways/business-management/company-administration/knowledge-guide-international-company-registration)
* [Lacis](https://c4seus.github.io/lacis/) - 免费的开源桌面工具，支持 Linux 和 Windows，可根据国家企业登记册和 BODACC 将法国公司、其董事及地址绘制成附来源的关联图，并标记大规模集中注册或"凤凰公司"等模式。界面为法语。
* [Linkedin](https://www.linkedin.com) - 常用的社交媒体平台，侧重职业档案和招聘，覆盖众多行业。对于收集某实体内特定人员活跃情况的信息非常有用。
* [Mergent Intellect](https://www.mergentintellect.com)
* [Mergent Online](https://www.mergentonline.com/login.php)
* [National Company Registers](https://en.wikipedia.org/wiki/List_of_company_registers)
* [OpenCorporates](https://opencorporates.com) - 全球范围搜索已注册的企业实体及其关联的个人高管或投资人。
* [OpenOwnership Register](https://register.openownership.org/)
* [Overseas Company Registers](https://www.gov.uk/government/publications/overseas-registries/overseas-registries)
* [Plunkett Research](https://www.plunkettresearchonline.com)
* [Scoot](https://www.scoot.co.uk)
* [Section 16 Deadline Calculator](https://github.com/Turner-Levey/section-16-deadline-calculator)  - 纯浏览器运行的开源工作表，用于规划常见的 SEC 表格 3、4、5 持股申报截止期限，支持输出备注和 CSV 复制内容。
* [SEMrush](https://www.semrush.com)
* [Serpstat](https://serpstat.com)
* [SpyFu](https://www.spyfu.com)
* [Tracxn](https://tracxn.com) - 搜索公司的收购、投资人、人员、研究等信息
* [UniCourt](https://unicourt.com/) - 免费搜索次数有限，付费数据需另行购买。可检索全美 1 亿多起法院案件。
* [Vault](https://www.vault.com) - 知名的美国最大企业排行榜。
* [WhiteIntel](https://whiteintel.dev) - 免费的企业与离岸所有权关系图：可跨 31 个公共登记机构（Companies House、GLEIF、ICIJ Offshore Leaks、OpenSanctions、SEC EDGAR）追溯一家公司的实益所有人，提供制裁筛查和完整标注引用的档案。支持 AI 智能体通过 MCP 查询。
* [Xing](https://www.xing.com)
* [YouControl](https://youcontrol.com.ua/en/)
## <a id="s44"></a>[↑](#toc) 求职搜索资源

* [Beyond](https://www.beyond.com)
* [CampusCareerCenter](https://www.campuscareercenter.com)
* [CareerBuilder](https://www.careerbuilder.com)
* [College Recruiter](https://www.collegerecruiter.com)
* [Craiglist](https://losangeles.craigslist.org)
* [Dice](https://www.dice.com)
* [Eluta (Canada)](https://www.eluta.ca)
* [Eurojobs](https://www.eurojobs.com)
* [Fish4Jobs](https://www.fish4.co.uk)
* [Glassdoor](https://www.glassdoor.com)
* [Indeed](https://www.indeed.com) - 一个在线求职网站，求职者可免费搜索职位、发布简历并进行企业调查。
* [Jobs (Poland)](https://www.jobs.pl)
* [Jobsite (UK)](https://www.jobsite.co.uk)
* [Linkedin](https://www.linkedin.com)
* [Monster](https://www.monster.com)
* [Naukri (India)](https://www.naukri.com)
* [RecruitEm](https://recruitin.net/)
* [Reed (UK)](https://www.reed.co.uk)
* [Seek (Australia)](https://www.seek.com.au)
* [SimplyHired](https://www.simplyhired.com)
* [Xing](https://www.xing.com)
* [ZipRecruiter](https://www.ziprecruiter.com)

## <a id="s45"></a>[↑](#toc) 问答站点

* [Answers.com](https://www.answers.com)
* [Ask](https://www.ask.com)
* [eHow](https://www.ehow.com)
* [Quora](https://www.quora.com)
* [StackExchange](https://stackexchange.com)
* [Yahoo Answers](https://answers.yahoo.com)
* [Ответы](https://otvet.mail.ru/)

## <a id="s46"></a>[↑](#toc) 域名与 IP 研究

* [aa419 Fake Sites Database](https://db.aa419.org/fakebankslist.php) - 该网站列出由 Artists Against 419 社区识别的欺诈网站，如虚假银行和在线诈骗。
* [Accuranker](https://www.accuranker.com)
* [ahrefs](https://ahrefs.com) - 用于反向链接研究、自然流量研究、关键词研究、内容营销等的工具。
* [Azure Tenant Resolution by PingCastle](https://tenantresolution.pingcastle.com) - 通过域名或 ID 查询 Azure 租户。
* [Bgpview.io](https://bgpview.io) - bgpview.io 网站可查询互联网上 ASN、IP 和 BGP 路由的详细信息。
* [Bing Webmaster Tools](https://www.bing.com/toolbox/webmaster)
* [Browserling](https://www.browserling.com) - Browserling 是一个在线沙箱，用户可实时跨浏览器和操作系统安全地测试潜在恶意链接。
* [BuiltWith](https://builtwith.com) - 帮助你查明构建特定网站所用的全部技术。
* [Central Ops](https://centralops.net)
* [Cerast Intelligence](https://search.cerast-intelligence.com/) - 通过持续的全网扫描，收录在各域名中发现的暴露面板与错误配置的可检索存档；可查询指定域名已记录的暴露结果。
* [CC.LA](https://cc.la) - 免费提供 WHOIS、RDAP、DNS、IP WHOIS、域名服务器历史、SSL 证书查询以及网络诊断工具（ping/traceroute/MTR）。还提供即将到期域名日历、TLD 库、域名监控和域名可用性检查。无需注册。
* [CrawlGraph](https://crawlgraph.com) - 借助开放的 Common Crawl 超链接图谱，绘制指向任意域名的链接来源。免费、免注册，可查询引荐域名和竞争对手的链接足迹，用于域名研究。
* [Crypto Scam & Crypto Phishing URL Threat Intel Feed](https://github.com/spmedia/Crypto-Scam-and-Crypto-Phishing-Threat-Intel-Feed) - 加密货币钓鱼与加密货币诈骗网站的最新情报源，每日自动更新。
* [Dedicated or Not](https://dedicatedornot.com)
* [digga](https://digga.dev) - 免费开源的域名与基础设施研究工具包，整合了 DNS、RDAP、WHOIS、被动子域名发现、IP 与 ASN 数据、邮箱认证检查以及 TLS 证书检视。无需账户。
* [DNS History](https://completedns.com/dns-history/)
* [DNSai](https://dnsai.com/dns-tools/) - 免费提供 DNS、WHOIS、DKIM 发现、SPF/DMARC 分析和黑名单检查，结果以通俗英文呈现，无需注册。
* [DNSDumpster](https://dnsdumpster.com) - 帮助你发现与特定域名相关的主机。
* [DNSStuff](https://www.dnsstuff.com)
* [DNSViz](https://dnsviz.net)
* [Domain Crawler](https://www.domaincrawler.com)
* [Domain Dossier](https://centralops.net/co/DomainDossier.aspx)
* [Domain Hunter](https://github.com/WhiteBite/Domain-Hunter) - 免费、开源、100% 客户端运行的批量域名可用性检查与名称生成工具：直接从浏览器调用注册局 RDAP 接口（无需服务器、无需 API 密钥、无追踪），可跨 148 个 TLD 区域检查多达 3,000 个名称；对低可信度 ccTLD 提供 DNS-over-HTTPS 佐证，附带注册商实时报价与 3 年总拥有成本（TCO），并支持 CSV/Markdown 导出。采用 MIT 许可。([live demo](https://whitebite.github.io/Domain-Hunter/))
* [Domain Intelligence](https://oti-labs.com/domain-intelligence-api) - 一次调用即可聚合 DNS、WHOIS/RDAP、SSL、子域名（CT 日志 + DNS 爆破）以及 SPF/DMARC 配置状况。提供免费额度；采用 MIT 许可。
* [DomainRecon](https://kriztalz.sh/domain-recon/) - 检索指定网站的 DNS 记录、子域名、SSL 证书以及 WHOIS / RDAP 数据。
* [Domain Tools](https://whois.domaintools.com) - Whois 查询以及域名/IP 历史数据。
* [Easy whois](https://www.easywhois.com)
* [Exonera Tor](https://exonerator.torproject.org) - 收录曾属于 Tor 网络的 IP 地址数据库，可回答在指定日期某个 IP 地址上是否运行过 Tor 中继。
* [Focsec](https://focsec.com) - 威胁情报 API，可检测某个 IP 地址是否与 VPN、代理、TOR 或机器人相关联。
* [Follow.net](https://follow.net)
* [Fullhunt](https://fullhunt.io/) - FullHunt 是一款开源情报（OSINT）工具，专注于识别并保护暴露在互联网上的资产。
* [GraphyStories](https://app.graphystories.com)
* [HoneyLabs](https://honeylabs.net) - 来自分布式蜜罐网络的免费单 IP 报告：该 IP 扫描了什么、命中的 CVE 利用路径、TLS（JA4）、HTTP（Akin）与 SSH（HASSH）客户端指纹、捕获的载荷以及经 VirusTotal 验证其所投递的恶意软件。可通过网页匿名查询，也支持 JSON API 和 MCP 服务器。
* [Hudson Rock](https://www.hudsonrock.com/threat-intelligence-cybercrime-tools) - 免费的网络犯罪情报工具包，用于检查是否因信息窃取类（Infostealer）恶意软件感染而导致数据暴露。
* [Hybrid Analysis](https://www.hybrid-analysis.com) - 在线服务，免费对可疑文件和 URL 进行详细分析。
* [HypeStat](https://www.hypestat.com)
* [IP.THC.ORG](https://ip.thc.org/) - 无限次的反向 DNS、子域名和反向 CNAME 查询，同时提供 JSON API。 
* [Icann Lookup](https://lookup.icann.org/en/lookup) - 该网站可查询互联网上的域名注册信息（WHOIS）。
* [Infosniper](https://www.infosniper.net)
* [isMalicious](https://ismalicious.com) - 威胁情报平台，聚合多个安全情报源中的恶意 IP 与域名数据，提供实时信誉评分和威胁分类。
* [IntoDNS.ai](https://intodns.ai) - AI 驱动的 DNS 与邮箱安全扫描器，支持 SPF、DKIM、DMARC、DNSSEC 检查并给出修复建议。
* [IP 2 Geolocation](https://ip2geolocation.com)
* [IP2Location](https://www.ip2location.com/demo) - 全面的 IP 情报数据库与 API，用于精准地理定位、ASN 映射以及 VPN/Tor/代理检测。
* [IP Geolocation API DB-IP](https://db-ip.com) - 提供 IP 地理定位与情报数据。
* [ip2geo.dev](https://ip2geo.dev) - IP 地理定位 API，根据 IP 地址提供城市、国家、时区、ASN 和货币数据。
* [IP Location](https://www.iplocation.net) - 用于将 IP 地址或 MAC 地址映射到联网计算机或移动设备在现实世界中的地理位置。
* [IP Location.io](https://iplocation.io) - IPLocation.io 可让你免费查询某个 IP 的位置。
* [IPFingerprints](https://www.ipfingerprints.com) - 用于查找某个 IP 地址的大致地理位置，并附带 ISP、时区、区号、州/省等其它有用信息。
* [IPOK](https://ipok.io) - 免费、免登录的 IP 信誉查询，聚合多达 8 个风险来源，标注住宅 IP 与数据中心 IP，并刻画 /24 C 段邻居。还提供命令行工具（CLI）和 Chrome 扩展。
* [IPVoid](https://www.ipvoid.com) - IP 地址工具集。
* [ISP.Tools](https://www.isp.tools) - 免费平台，提供面向 ISP 和基础设施从业者的网络诊断工具（ping、traceroute、MTR、DNS、WHOIS、HTTP 等）。
* [Kloth](https://www.kloth.net/services)
* [Majestic](https://majestic.com) - 查明有哪些网站链接到你的网站。
* [Mark Monitor WHOIS](https://whois-webform.markmonitor.com/whois/) - 显示域名注册信息。
* [MaxMind](https://www.maxmind.com)
* [MetaDefender](https://metadefender.com) - 面向 URL、文件、证书、域名和可疑哈希的威胁分析服务。
* [Netcraft Site Report](https://toolbar.netcraft.com/site_report?url=undefined#last_reboot) - 在线数据库，提供特定网站的详细信息及其相关历史记录报告。
* [OpenLinkProfiler](https://www.openlinkprofiler.org/)
* [openSquat](https://github.com/atenreiro/opensquat) - 开源工具，搜索新注册域名源，以发现仿冒特定品牌或关键词的域名抢注（typosquatting）、IDN 同形字、分身域名（doppelganger）和 bitsquatting 域名。
* [osint-recon](https://github.com/JMarchiori13/osint-recon) - 用 Rust 编写的被动式开源情报（OSINT）信息收集框架：涵盖子域名、DNS、ASN、证书透明度历史、GitHub 搜索语法（dorking）、技术指纹识别、邮箱和文档元数据，适用于经授权的红队行动。
* [Pentest-Tools.com](https://pentest-tools.com/information-gathering/google-hacking) - 使用 Google Dorks（谷歌黑客语法）等高级搜索运算符挖掘目标网站的高价值信息。
* [PhishStats](https://phishstats.info/)
* [Pulsedive](https://pulsedive.com)
* [Qualys SSL Check](https://www.ssllabs.com/ssltest/) - SSL 测试配置合规性检查。
* [Quantcast](https://www.quantcast.com)
* [Quick Sprout](https://www.quicksprout.com)
* [RedirectDetective](https://redirectdetective.com)
* [Remote DNS Lookup](https://remote.12dt.com)
* [Robtex](https://www.robtex.com) - 基于 IP 地址和域名的研究网站，提供反向 DNS 查询、Whois、AS Macros 等多种服务。
* [SameID](https://sameid.net)
* [ScanMalware](https://scanmalware.com) - 免费 URL 扫描器，在沙箱浏览器中渲染页面并报告钓鱼与恶意软件判定结果、网络请求、技术栈、TLS/JARM 指纹和截图；另提供近期扫描的公开信息源，可按域名、IP、ASN 或 favicon 哈希检索。
* [SecurityTrails](https://securitytrails.com/dns-trails) - 用于搜索当前与历史 DNS 记录、当前与历史 WHOIS、站点所用技术，并可按电话号码、邮箱、地址、IP 等进行 whois 查询的 API。
* [SubDomainRadar.io](https://subdomainradar.io) - 快速子域名查找工具，具备多种搜索模式和最广泛的数据源，并提供实时通知。
* [SEMrush](https://www.semrush.com)
* [SEOTools for Excel](https://seotoolsforexcel.com)
* [Similar Web](https://www.similarweb.com) - 比较任意网站的流量统计与分析数据。
* [SmallSEOTools](https://smallseotools.com)
* [Squatm3gator](https://github.com/david3107/squatm3gator) - 枚举通过各类域名抢注手法改写原始域名而生成的可注册域名。
* [StatsCrop](https://www.statscrop.com)
* [TinyScan](https://www.tiny-scan.com) - 又一款强大的 URL 扫描工具，可提供任意 URL 的全面信息，包括 IP 地址、位置、截图、技术栈、性能指标等。
* [TracerouteVisualizer](https://kriztalz.sh/traceroute-visualizer/) - 在线工具，将 mtr / traceroute / flyingroutes 的输出显示在地图上进行可视化分析。
* [urlDNA](https://urldna.io/) -  释放网站洞察力！urldna.io 可分析 URL、监控品牌并追踪钓鱼网站。
* [URLhaus](https://urlhaus.abuse.ch) - URLhaus 共享恶意 URL，以对抗恶意软件和僵尸网络威胁。
* [urlQuery](https://urlquery.net)
* [urlscan](https://urlscan.io/) -  免费扫描和分析网站的服务。
* [URLVoid](https://www.urlvoid.com) - 通过多个黑名单引擎和在线信誉工具分析网站，帮助识别欺诈和恶意网站。
* [Vacato](https://vacato.io) - 免费的 RDAP 域名可用性监控清单：定时检查，状态看似可注册时通过 Telegram/邮箱/Slack 通知（并非注册商或抢注服务）。免费额度：10 个域名。
* [Validin](https://app.validin.com/) - 免费搜索当前与历史 DNS 记录的网站和 API。
* [Verisign](https://dnssec-debugger.verisignlabs.com)
* [ViewDNS.info](https://viewdns.info)
* [Virus Total](https://www.virustotal.com/) - 分析可疑域名、IP、URL 和文件，以检测恶意软件及其它数据泄露事件。
* [VPNDetection](https://vpndetection.io) - 检查某个 IP 是否为 VPN、代理、Tor 出口节点或托管主机地址。免费、免注册。另有 Chrome 扩展，可查询你在任意页面上选中的 IP。
* [w3snoop](https://webboar.com.w3snoop.com) - 免费提供特定网站综合报告的网站。
* [Web-Check](https://web-check.as93.net/) - 一站式查看网站和服务器元数据的工具。
* [WebMeUp](https://webmeup.com) - 网络上最新、增长最快的反向链接索引，也是 SEO PowerSuite 反向链接数据的主要来源。
* [Webscore](https://garvit835.github.io/WebScore/) - 输入网站 URL 即可检查其合法性。
* [Webscout](https://webscout.io/)  - 面向 IP 地址和域名的大规模情报与元数据瑞士军刀。
* [Website Informer](https://website.informer.com)
* [WebsiteTechMiner.py](https://github.com/cybersader/WebsiteTechMiner-py) - 自动从 "BuiltWith" 或 "Wappalyzer" API 采集网站画像数据并汇总为 CSV，涵盖技术栈信息、技术画像数据、网站报告、网站技术查询、网站架构查询等。
* [WhatIsMyIPAddress](https://whatismyipaddress.com)
* [Who.is](https://who.is/) - 域名 whois 信息。
* [Whois Arin Online](https://whois.arin.net) - 用于查询 ARIN 注册数据库中 Whois 数据的 Web 服务。
* [WhoIsHostingThis](https://www.whoishostingthis.com)
* [WhoisMind](https://www.whoismind.com)
* [Whoisology](https://whoisology.com)
* [WhoIsRequest](https://whoisrequest.com)
* [WhosBuilt](https://whosbuilt.com) - 域名报告，整合技术栈、托管、DNS 和注册商信号，并附带带来源链接的建站者署名，将可能的建站者与所有者区分开来。
* [WiGLE](https://wigle.net/) - Wi-Fi "驾驶攻击"（wardriving）数据库，包含一张全球地图，汇集众包的 Wi-Fi 网络位置、名称及其它属性信息。可下载软件以向公共信息集贡献数据。
* [You Get Signal](https://www.yougetsignal.com)

## <a id="s47"></a>[↑](#toc) 关键词发现与研究

* [Google Adwords](https://adwords.google.com) - 获取每月关键词搜索量数据与统计。
* [Google Trends](https://www.google.com/trends) - 查看有多少用户在搜索特定关键词。
* [Keyword Discovery](https://www.keyworddiscovery.com)
* [Keyword Spy](https://www.keywordspy.com)
* [KeywordTool](https://keywordtool.io)
* [One Look Reverse Dictionary](https://www.onelook.com/reverse-dictionary.shtml)
* [Soovle](https://www.soovle.com)
* [Ubersuggest](https://ubersuggest.org)
* [Word Tracker](https://www.wordtracker.com)
* [Yandex Wordstat](https://wordstat.yandex.com)

## <a id="s48"></a>[↑](#toc) 网页历史与网站快照

* [Archive.is](https://archive.is) - 可为你的网站存档快照的网站，即使原始页面消失，快照也始终在线。
* [BlackWidow](https://softbytelabs.com/wp/blackwidow/)
* [CachedView](https://cachedview.com)
* [stored.website](https://stored.website)
* [Wayback Machine](https://web.archive.org/) - 探索网站的历史。
* [Wayback Machine Archiver](https://github.com/jsvine/waybackpack)
* [Wayback-Archive](https://github.com/GeiserX/Wayback-Archive) - 从 Wayback Machine 下载完整网站，并完整保留资源以便离线查看。
* [waybackpy](https://github.com/akamhy/waybackpy) - 对接 Wayback Machine API 的 Python 包和命令行工具。
* [WayTrace](https://waytrace.org/) - 从 Wayback Machine 的存档快照中重建域名历史：邮箱、子域名、暴露的 API 密钥、分析与广告 ID、人物等，每项均标注首次到末次出现日期。被动式、开源。
* [Web Resource Ledger](https://webresourceledger.com) - 将网页捕获为带签名和时间戳的 WACZ 包，任何人都无需账户即可验证。提供 Web 界面、API 和 MCP 服务器，有免费额度。

## <a id="s49"></a>[↑](#toc) 语言工具

* see the [Awesome Translations list](https://github.com/mbiesiad/awesome-translations#tools)

## <a id="s50"></a>[↑](#toc) 图片搜索

* [Baidu Images](https://image.baidu.com)
* [Bing Images](https://www.bing.com/images)
* [Clarify](https://clarify.io)
* [Dupli Checker](https://www.duplichecker.com/reverse-image-search.php) - 可通过上传图片、输入图片 URL、或键入关键词及任意想要探索的词语来搜索图片。
* [FaceCheck.ID](https://facecheck.id) - 人脸识别搜索引擎。
* [Faceagle](https://faceagle.com/) - Faceagle 是一款人脸识别搜索引擎。
* [Flickr](https://flickr.com/search/)
* [GeoSpyer](https://github.com/atiilla/geospy "Original service: https://geospy.web.app/") - 借助 Graylark 的 AI 地理定位服务来查明照片拍摄地点的 Python 工具。
* [Google Image](https://images.google.com)
* [Google Lens](https://lens.google.com/)
* [Image Identification Project](https://www.imageidentify.com)
* [KartaVision](https://kartavision.com/) - 面向 KartaView 影像的搜索引擎，支持自然语言搜索和以图搜图。
* [Lenso.ai](https://lenso.ai) - 带人脸识别的反向图片搜索工具，用于查找人物、相似图片、照片副本、相同地点等。
* [Lycos Image Search](https://search.lycos.com)
* [PhotoBucket](https://photobucket.com)
* [PicTriev](https://www.pictriev.com) - 人脸搜索引擎。
* [PimEyes](https://pimeyes.com) - 在线人脸搜索引擎，遍历互联网查找包含指定人脸的图片。
* [Pixsy](https://www.pixsy.com/) - 重新掌控你的图片，查看你的图片在网上被何处、以何种方式使用！
* [Reverse Image Search Anywhere](https://reverseimage.app/) - 免费的浏览器扩展和网页工具，可跨 Google Lens、Yandex、Bing 视觉搜索和 TinEye 搜索图片，包括那些直接图片 URL 失效的站点上的图片。
* [Search4faces](https://search4faces.com/) - 通过照片在互联网上搜索人物的服务。
* [Surfface](https://surfface.com) - 人脸搜索与找人工具，索引来自社交媒体和网络的社交档案及公开图片。
* [TinEye](https://tineye.com) - 反向图片搜索引擎。
* [Yahoo Image Search](https://images.search.yahoo.com)
* [Yandex Images](https://www.yandex.com/images)
## <a id="s51"></a>[↑](#toc) 图像分析

* [ChronoVerify](https://chronoverify.com) - API 与免费网页工具，可读取 EXIF 和 XMP、依据官方信任列表校验 C2PA 内容凭证（Content Credentials），并运行经典像素取证，为任意图片返回一个带类型的判定结论。
* [DiffChecker](https://www.diffchecker.com/image-diff/)
* [EXIFEditor.io](https://exifeditor.io) - 浏览器内的 EXIF 图片元数据编辑器、查看器和分析工具。
* [ExifLooter](https://github.com/aydinnyunus/exiflooter)
* [ExifTool](https://www.sno.phy.queensu.ca/~phil/exiftool)
* [Forensically](https://29a.ch/photo-forensics/)
* [forensics.media](https://forensics.media/tools/)  - 免费的浏览器内图像取证套件：EXIF/元数据查看器、误差水平分析（ELA）、克隆/复制移动与双重 JPEG 检测。全程在客户端运行，不上传任何数据。
* [FotoForensics](https://www.fotoforensics.com)
* [GeoSpy](https://geospy.web.app/) - 基于 AI 的图像开源情报（OSINT）工具。
* [ImgOps](https://imgops.com/)
* [ImpulseAdventure](https://www.impulseadventure.com/photo/jpeg-snoop.html)
* [JIMPL](https://jimpl.com/) - 在线 EXIF 数据查看器。
* [JPEG Audit](https://jpegaudit.com) - 免费的在线 JPEG 取证：EXIF/IPTC/XMP 与 GPS 数据、带严重级别判定的自动篡改检查、JPEG 结构与量化表、感知哈希，以及利用 EXIF 相机方位角进行的街景比对。
* [JPEGsnoop](https://sourceforge.net/projects/jpegsnoop)
* [Metadata Viewer](https://kriztalz.sh/metadata-viewer/) - 在线 EXIF 数据查看器。
* [ProfileImageIntel](https://profileimageintel.com/) - 面向社交媒体和 WhatsApp 头像的工具，用于查明头像的上传时间。
* [TracePoint](https://kluter.github.io/TracePoint/) - 利用几何射线交点定位照片的拍摄原点。客户端运行，不上传数据。
* [TrueScreen C2PA Viewer](https://truescreen.io/c2pa-viewer/) - 免费的浏览器内工具，可读取并校验文件的内容凭证（C2PA 清单），无需上传、无需账户。
* [WhatsInMyFile](https://whatsinmyfile.com/) - 浏览器内的元数据与隐藏内容检查工具，适用于照片、PDF 和 Office 文件；不上传任何数据。

## <a id="s52"></a>[↑](#toc) 视频搜索及其他视频工具

* [Archivarix Tube Search](https://tube.archivarix.net/) - 用于查找已删除、已移除和无法访问的 YouTube 视频的搜索引擎。 
* [AudienceCue](https://audiencecue.com/en/tools/youtube-comment-downloader) - 将最新的公开 YouTube 视频或 Shorts 评论下载为 CSV，供研究工作流使用。
* [Bing Videos](https://www.bing.com/?scope=video)
* [Clarify](https://clarify.io)
* [DailyMotion](https://www.dailymotion.com)
* [Deturl](https://deturl.com) - 从任意网页下载 YouTube 视频。
* [DownloadHelper](https://www.downloadhelper.net) - 从任意网站下载任意视频，就是这么好用！
* [Earthcam](https://www.earthcam.com) - EarthCam 是面向旅游与娱乐的领先实时网络摄像头直播网络。
* [Filmot](https://filmot.com/) - 在 YouTube 字幕内搜索，索引了 5.28 亿个视频、4500 万个频道中的超过 5.73 亿条字幕。
* [Find YouTube Video](https://findyoutubevideo.thetechrobo.ca/) - 目前可跨 5 个 YouTube 存档按 ID 搜索特定视频，对查找已删除或私密的 YouTube 视频非常有用。
* [Frame by Frame](https://chrome.google.com/webstore/detail/frame-by-frame/cclnaabdfgnehogonpeddbgejclcjneh/) - 浏览器插件，可让你逐帧观看 YouTube 视频。
* [Geosearch](https://www.geosearchtool.com)
* [Insecam](https://insecam.org/) - 实时摄像头目录。
* [Internet Archive: Open Source Videos](https://archive.org/details/opensource_movies)
* [Metatube](https://www.metatube.com)
* [Tubuep](https://github.com/bibanon/tubeup) - 通过 yt-dlp 下载在线视频，再重新上传到 Internet Archive 予以保存。注意：如果也想存档评论，需要安装 0.0.33 版本并使用 --get-comments 参数；这样仍可享有 yt-dlp 的新修复与功能，但 tubeup 已有的 bug 无法修复，除非手动处理。
* [Veoh](https://www.veoh.com)
* [Video Stabilization Methods](https://github.com/yaochih/awesome-video-stabilization)
* [Vimeo](https://vimeo.com)
* [Yahoo Video Search](https://video.search.yahoo.com)
* [YouTube Geofind](https://mattw.io/youtube-geofind/)
* [YouTube Metadata](https://mattw.io/youtube-metadata/)
* [YouTube](https://www.youtube.com)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp/) - 可从几乎所有在线平台下载视频，并附带信息、缩略图、字幕、描述和评论（评论仅支持 Youtube 等少数站点及一些小站点）。如果某站点不受支持，或缺少包括评论在内的有用或关键元数据，请提交 issue。

## <a id="s53"></a>[↑](#toc) 学术资源与灰色文献

* [Academia](https://www.academia.edu)
* [Academic Journals](https://www.academicjournals.org)
* [African Journal Online](https://www.ajol.info) -  是世界上规模最大、最权威的非洲出版学术期刊平台。
* [American Society of Civil Engineers](https://ascelibrary.org)
* [Base](https://www.base-search.net)
* [Bibsonomy](https://www.bibsonomy.org)
* [Core](https://core.ac.uk/search)
* [Elsevier](https://www.elsevier.com)
* [Google Scholar](https://scholar.google.com)
* [Grey Guide](https://greyguide.isti.cnr.it)
* [Grey Literature – List of Gateways](https://csulb.libguides.com/graylit)
* [GreyNet International](https://www.greynet.org)
* [HighWire: Free Online Full-text Articles](https://highwire.stanford.edu/lists/freeart.dtl)
* [Journal Guide](https://www.journalguide.com)
* [Journal Seek](https://journalseek.net)
* [JSTOR](https://www.jstor.org) - 可检索超过 1000 万篇学术期刊文章、图书和原始资料。
* [Leibniz Information Centre For Science and Technology University Library](https://www.tib.eu/en/search-discover/) - 收录德国公共资助项目的全部报告以及大量科学论文。
* [Microsoft Academic](https://academic.research.microsoft.com)
* [NRC Research Press](https://www.nrcresearchpress.com)
* [OA.mg](https://oa.mg) - 收录超过 2.4 亿篇学术文献的数据库，目录中所有开放获取（Open Access）论文均提供 PDF 全文（约 4000 万篇）。
* [Open Access Scientific Journals](https://www.pagepress.org)
* [Open Grey](https://www.opengrey.eu)
* [Oxford Journals](https://www.oxfordjournals.org)
* [PubMed](https://www.ncbi.nlm.nih.gov/pubmed) - 可检索来自 MEDLINE、生命科学期刊和在线图书的超过 2700 万条生物医学文献引文。
* [Quetzal Search](https://www.quetzal-search.info)
* [Research Gate](https://www.researchgate.net)
* [SAGE Journals](https://online.sagepub.com)
* [Science Publications](https://www.thescipub.com)
* [ScienceDirect](https://www.sciencedirect.com)
* [ScienceDomain](https://www.sciencedomain.org)
* [SCIRP](https://www.scirp.org)
* [Springer](https://link.springer.com)
* [Taylor & Francis Online](https://www.tandfonline.com)
* [The Open Syllabus Project](https://opensyllabusproject.org/)
* [Wiley](https://www.wiley.com)
* [World Digital Library](https://www.wdl.org)


## <a id="s54"></a>[↑](#toc) 地理空间研究与地图工具

* [Aleph](https://github.com/Belluxx/Aleph) - 可下载地球上任意区域或地点的卫星影像、街景照片、3D 模型、建筑物和海拔数据。无需 API 密钥。
* [Apify's Google Maps Scraper](https://apify.com/compass/crawler-google-places)
* [ArcGIS](https://livingatlas.arcgis.com/en/browse/)
* [Atlas](https://atlas.co)
* [Baidu Maps](https://map.baidu.com/)
* [Batchgeo](https://batchgeo.com)
* [Bing Maps](https://www.bing.com/maps)
* [CartoDB](https://cartodb.com)
* [Colorbrewer](https://colorbrewer2.org)
* [digiKam](https://www.digikam.org/)
* [Dominoc925](https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html)
* [DualMaps](https://www.mapchannels.com/dualmaps7/map.htm)
* [Esri](https://www.esri.com)
* [Flash Earth](https://www.flashearth.com)
* [GeoGig](https://geogig.org)
* [GeoInfer](https://geoinfer.com) - 图像地理定位工具，无需 EXIF 数据。
* [ReverseImageLocation](https://reverseimagelocation.com) - AI 驱动的地理定位工具，可从图像中识别地点。
* [GeoNames](https://www.geonames.org)
* [Google Earth Pro](https://www.google.com/intl/en/earth/versions/#earth-pro)
* [Google Earth](https://www.google.com/earth)
* [Google Maps](https://www.google.com/maps)
* [Google My Maps](https://www.google.com/maps/about/mymaps)
* [GPSVisualizer](https://www.gpsvisualizer.com)
* [GrassGIS](https://grass.osgeo.org)
* [Here](https://here.com)
* [Hyperlapse](https://github.com/TeehanLax/Hyperlapse.js)
* [Inspire Geoportal](https://inspire-geoportal.ec.europa.eu)
* [Instant Google Street View](https://www.instantstreetview.com)
* [InstantAtlas](https://www.instantatlas.com)
* [KartaView](https://kartaview.org/map/)
* [Leaflet](https://leafletjs.com)
* [Liveuamap](https://liveuamap.com/)
* [Map Maker](https://maps.co)
* [MapAList](https://mapalist.com)
* [MapBox](https://www.mapbox.com)
* [Mapchart.net](https://mapchart.net)
* [MapChecking](https://www.mapchecking.com/)
* [MapHub](https://maphub.net)
* [Mapillary](https://www.mapillary.com/app/)
* [MapJam](https://mapjam.com)
* [Mapline](https://mapline.com)
* [Mapquest](https://www.mapquest.com)
* [Modest Maps](https://modestmaps.com)
* [NGA GEOINT](https://github.com/ngageoint)
* [Open Street Map](https://www.openstreetmap.org)
* [OpenLayers](https://openlayers.org)
* [Overhead24](https://overhead24.com) - 实时 3D 地球仪，展示所有公开轨道数据的卫星，并标注活跃冲突地区上空的军用卫星、近距离接近事件和近期机动变轨。免费、无需账户。
* [Perry Castaneda Library](https://www.lib.utexas.edu/maps)
* [Pic2Map](https://www.pic2map.com/)
* [Polymaps](https://polymaps.org)
* [QGIS](https://qgis.org)
* [QuickMaps](https://chrome.google.com/webstore/detail/quick-maps/bgbojmobaekecckmomemopckmeipecij)
* [SAS Planet](https://www.sasgis.org/sasplaneta/)  - 用于查看、下载和拼接卫星图像的软件。
* [Satellites Pro](https://satellites.pro/)
* [SatIntel](https://github.com/ANG13T/SatIntel)
* [Scribble Maps](https://scribblemaps.com)
* [Sentinel Hub](https://www.sentinel-hub.com/explore/sentinelplayground/)
* [ShadowFinder-Web](https://kluter.github.io/ShadowFinder-Web) - 通过阴影分析对照片进行地理定位。Bellingcat 的 ShadowFinder 的浏览器移植版，无需 Jupyter、无需账户，全程客户端运行。
* [SOAR](https://soar.earth/)
* [StoryMaps](https://storymaps.arcgis.com/en)
* [Street Crime Map](https://streetcrimemap.co.uk/) - 英格兰、威尔士和北爱尔兰的街道级警方记录，按地区和类别统计，并附覆盖范围说明。
* [SunCalc](https://www.suncalc.org/)
* [Tableau](https://www.tableausoftware.com)
* [USGS (EarthExplorer)](https://earthexplorer.usgs.gov/)
* [ViaMichelin](https://www.viamichelin.com)
* [View in Google Earth](https://www.mgmaps.com/kml/#view)
* [Wikimapia](https://wikimapia.org)
* [Windy](https://www.windy.com/)
* [World Monitor](https://www.worldmonitor.app) - 实时全球情报平台，提供实时冲突追踪、军用飞行器与船舶监控、GPS 干扰数据、卫星影像，以及 5 个专项仪表盘中的地缘政治风险评分。
* [WorldMap Harvard](https://worldmap.harvard.edu)
* [Worldwide OSINT Tools Map](https://cipher387.github.io/osintmap/) - 按适用地区整理的全球数据库与开源情报（OSINT）来源地图。
* [Yahoo Maps](https://maps.yahoo.com)
* [Zeemaps](https://www.zeemaps.com)
* [Zoom Earth](https://zoom.earth/)

## <a id="s55"></a>[↑](#toc) 新闻

* [1st Headlines](https://www.1stheadlines.com)
* [ABYZNewsLinks](https://www.abyznewslinks.com)
* [Agence France-Presse (AFP)](https://www.afp.com)
* [AllYouCanRead](https://www.allyoucanread.com)
* [APITube](https://apitube.io) - 新闻 API，覆盖 180 多个国家、60 多种语言的 50 万多个来源，以结构化 JSON 返回文章，附带情感、实体和主题信息；免费额度为每天 100 次请求。
* [BBC News](https://www.bbc.co.uk/news)
* [Bing News](https://www.bing.com/news)
* [CNN](https://edition.cnn.com)
* [DailyEarth](https://dailyearth.com)
* [DPA International](https://www.dpa-international.com)
* [Euronews](https://www.euronews.com)
* [Factiva](https://www.dowjones.com/factiva)
* [France24](https://www.france24.com)
* [Google News](https://news.google.com)
* [Google News Print Archive](https://news.google.com/newspapers)
* [News Now](https://www.newsnow.co.uk)
* [Newseum - Today Front Pages](https://www.newseum.org/todaysfrontpages)
* [Newspaper Map](https://newspapermap.com)
* [Newspapers.com](https://www.newspapers.com)
* [NewsWhip](https://www.newswhip.com)
* [OnlineNewspapers](https://www.onlinenewspapers.com)
* [Paperboy](https://www.thepaperboy.com)
* [PR Newswire](https://www.prnewswire.com)
* [Press Reader](https://www.pressreader.com)
* [Reuters](https://www.reuters.com)
* [Silobreaker](https://www.silobreaker.com)
* [WorldNews](https://wn.com)
* [World-Newspapers](https://www.world-newspapers.com)
* [Yahoo News](https://news.yahoo.com)
## <a id="s56"></a>[↑](#toc) 新闻摘要与发现工具

* [Flipboard](https://flipboard.com)
* [Inshorts](https://www.inshorts.com)
* [Newsinshorts](https://newsinshorts.com)
* [Nod](https://get-nod.com)
* [Reeder](https://reederapp.com)
* [Spike](https://www.newswhip.com)
* [Storyful](https://storyful.com)
* [Superdesk](https://www.superdesk.org)
* [Trooclick](https://trooclick.com)

## <a id="s57"></a>[↑](#toc) 事实核查


* [Captin Fact](https://captainfact.io/)
* [Check](https://meedan.com/check)
* [Emergent](https://www.emergent.info)
* [Fact Check](https://www.factcheck.org)
* [Full Fact](https://fullfact.org)
* [Snopes](https://www.snopes.com) - 关于都市传说、民间传说、神话、谣言和错误信息的权威互联网参考资料来源。
* [Verification Handbook](https://verificationhandbook.com)

## <a id="s58"></a>[↑](#toc) 数据与统计

* [AGOA Data Center](https://agoa.info)
* [AidData](https://aiddata.org)
* [AWS Public Datasets](https://aws.amazon.com/datasets)
* [Bank for International Settlements Statistics](https://www.bis.org/statistics/index.htm)
* [BP Statistical Review of World Energy](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html)
* [CEPII](https://www.cepii.fr/CEPII/en/welcome.asp)
* [CIA World Factbook](https://www.cia.gov/the-world-factbook/)
* [Crime Brasil](https://crimebrasil.com.br) - 整合巴西犯罪统计数据的开放数据平台（RS 街区级、MG/RJ 市镇级、全国 PRF/DATASUS）。提供免费 API，采用 CC BY 4.0 许可。
* [DataInt Databook](https://databook.dataint.net) - 涵盖 250 个国家的国情参考页面（人口、经济、地理、基础设施、国防、治理），数据汇编自世界银行、联合国、联合国教科文组织和《世界概况》，每项数据均标注来源。支持 25 种语言。仅提供网页参考，无 API 或批量下载。
* [Data.gov.uk](https://data.gov.uk)
* [DBPedia](https://wiki.dbpedia.org)
* [European Union Open Data Portal](https://open-data.europa.eu/en/data)
* [Eurostat](https://ec.europa.eu/eurostat)
* [Freebase](https://developers.google.com/freebase)
* [Gapminder World](https://www.gapminder.org/data)
* [globalEDGE Database of International Business Statistics](https://globaledge.msu.edu/tools-and-data/dibs)
* [Google Finance](https://www.google.com/finance)
* [Google Public Data Explorer](https://www.google.com/publicdata/directory)
* [Government of Canada Open Data](https://open.canada.ca/en)
* [HIS Piers](https://www.ihs.com/products/piers.html)
* [Human Development Reports](https://hdr.undp.org/en/global-reports)
* [ILO World Employment and Social Outlook Trends](https://www.ilo.org/global/research/global-reports/weso/2015/lang--en/index.htm)
* [ILOSTAT](https://www.ilo.org/ilostat/faces/oracle/webcenter/portalapp/pagehierarchy/Page137.jspx?_afrLoop=443508925711569&clean=true#%40%3F_afrLoop%3D443508925711569%26clean%3Dtrue%26_adf.ctrl-state%3Dl4dwldaf3_9)
* [IMF World Economic Outlook Database](https://www.imf.org/external/ns/cs.aspx?id=28)
* [Index Mundi](https://www.indexmundi.com)
* [International Energy Agency Statistics](https://www.iea.org/statistics)
* [International Labour Comparisons](https://www.bls.gov/fls/chartbook.htm)
* [International Trade Center](https://www.intracen.org/ByCountry.aspx)
* [Junar](https://junar.com)
* [LandMatrix](https://landmatrix.org)
* [Latinobarometro](https://www.latinobarometro.org)
* [Library, University of Michigan: Statistics and Datasets](https://www.lib.umich.edu/browse/Statistics%20and%20Data%20Sets)
* [NarcoScope](https://narcoscope.com) - 面向公共利益的查询工具，展示官方毒品市场价格、前体物流动、查获情况与公共卫生背景，附来源链接并明确标注证据缺口。
* [Nation Master](https://www.nationmaster.com/statistics)
* [OECD Aid Database](https://www.oecd.org/dac/stats/data.htm)
* [OECD Data](https://data.oecd.org)
* [OECD Factbook](https://www.oecd-ilibrary.org/economics/oecd-factbook_18147364)
* [Paul Hensel’s General Informational Data Page](https://www.paulhensel.org/dataintl.html)
* [Penn World Table](https://www.rug.nl/research/ggdc/data/pwt/pwt-8.1)
* [Pew Research Center](https://www.pewinternet.org/datasets)
* [Population Reference Bureau Data Finder](https://www.prb.org/DataFinder.aspx)
* [PRS Risk Indicators](https://www.prsgroup.com)
* [SESRIC Basic Social and Economic Indicators](https://www.sesric.org/baseind.php)
* [SESRIC Databases](https://www.sesric.org/databases-index.php)
* [Statista](https://www.statista.com)
* [The Atlas of Economic Complexity](https://atlas.cid.harvard.edu)
* [The Data and Story Library](https://lib.stat.cmu.edu/DASL)
* [Trading Economics](https://www.tradingeconomics.com)
* [Transparency.org Corruption Perception Index](https://www.transparency.org/cpi2015)
* [UAV Radar](https://uavradar.live/) - 乌克兰和俄罗斯区级的防空警报与无人机袭击统计：按地区列出 30 天滚动周期内发生了多少次警报、结束了多少次，以及通常持续多久。提供免费 JSON API，无需注册，采用 CC BY 4.0 许可。
* [UN COMTRADE Database](https://comtrade.un.org)
* [UN Data](https://data.un.org)
* [UNCTAD Country Fact Sheets](https://unctad.org/en/Pages/DIAE/World%20Investment%20Report/Country-Fact-Sheets.aspx)
* [UNCTAD Investment Country Profiles](https://unctad.org/en/Pages/Publications/Investment-country-profiles.aspx)
* [UNCTAD STAT](https://unctadstat.unctad.org)
* [UNDPs Human Development Index](https://hdr.undp.org/en/data)
* [UNECE](https://w3.unece.org/PXWeb/en)
* [UNESCO Institute for Statistics](https://uis.unesco.org)
* [UNIDO Statistical Databases](https://www.unido.org/resources/statistics/statistical-databases.html)
* [UNStats Social Indicators](https://unstats.un.org/unsd/demographic/products/socind)
* [Upsala Conflict Data Program](https://www.pcr.uu.se/research/UCDP)
* [US Data and Statistics](https://www.usa.gov/statistics)
* [Vizala](https://vizala.com)
* [WHO Data](https://www.who.int/gho/en)
* [World Bank Data](https://data.worldbank.org)
* [World Bank Data](https://datatopics.worldbank.org/consumption/home)
* [World Bank Doing Business](https://www.doingbusiness.org)
* [World Bank Enterprise Surveys](https://www.enterprisesurveys.org)
* [World Integrated Trade Solution](https://wits.worldbank.org)
* [WTO Statistics](https://www.wto.org/english/res_e/statis_e/statis_e.htm)
* [Zanran](https://zanran.com)

## <a id="s59"></a>[↑](#toc) 网页监控

* [Alltop](https://alltop.com)
* [Awasu](https://www.awasu.com)
* [Bridge.Suumitsu](https://bridge.suumitsu.eu)
* [ChangeDetection.io](https://changedetection.io)
* [ChangeDetection.io Open Source](https://github.com/dgtlmoon/changedetection.io)
* [ChangeDetection](https://www.changedetection.com)
* [Deltafeed](https://bitreading.com/deltafeed)
* [DiggReader](https://digg.com/login?next=%2Freader)
* [FeedBooster](https://www.qsensei.com)
* [Feed Filter Maker](https://feed.janicek.co)
* [Feedly](https://www.feedly.com)
* [FeedReader](https://www.feedreader.com)
* [FetchRSS](https://fetchrss.com)
* [Flipboard](https://flipboard.com)
* [FollowThatPage](https://www.followthatpage.com)
* [Google Alerts](https://www.google.com/alerts) - 内容变更检测与通知服务。
* [InfoMinder](https://www.infominder.com/webminder)
* [Mention](https://en.mention.com)
* [Netvibes](https://www.netvibes.com)
* [Newsblur](https://newsblur.com)
* [OmeaReader](https://www.jetbrains.com/omea/reader)
* [OnWebChange](https://onwebchange.com)
* [Reeder](https://reederapp.com)
* [RSS Bridge](https://bridge.suumitsu.eu)
* [RSS Feed Reader](https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp)
* [RSS Search Engine](https://ctrlq.org/rss)
* [RSSOwl](https://www.rssowl.org)
* [Selfoss](https://selfoss.aditu.de)
* [Silobreaker](https://www.silobreaker.com)
* [Talkwalker](https://www.talkwalker.com)
* [Topic Watch](https://github.com/0xzerolight/topic_watch) - 自托管新闻监控工具，借助大语言模型（LLM）仅在出现真正新信息时才发出通知。
* [The Old Reader](https://theoldreader.com)
* [versionista](https://versionista.com)
* [visualping](https://visualping.io)
* [Wayback-Diff](https://github.com/GeiserX/Wayback-Diff)
* [WebReader](https://www.getwebreader.com)
* [WebSite Watcher](https://www.aignes.com/index.htm)
* [Winds](https://winds.getstream.io)

## <a id="s60"></a>[↑](#toc) 浏览器

* [Atom](https://browser.ru/)
* [Brave](https://brave.com) - 是一款开源网页浏览器，可让你彻底拦截广告和网站跟踪器。
* [Bromite](https://www.bromite.org/) - Bromite 是 Chromium 的一个分支，具备广告拦截和增强隐私功能，把浏览器的控制权交还给你。仅支持 Android。
* [CentBrowser](https://www.centbrowser.com)
* [Chrome](https://www.google.com/chrome)
* [Comodo Dragon](https://www.comodo.com/home/browsers-toolbars/browser.php)
* [Coowon](https://coowon.com)
* [Edge](https://www.microsoft.com/en-us/windows/microsoft-edge/microsoft-edge)
* [Firefox](https://www.mozilla.org)
* [LibreWolf](https://librewolf.net) - 注重隐私的 Firefox 分支，默认启用更强的安全设置。
* [Maxthon](https://www.maxthon.com)
* [Mullvad Browser](https://mullvad.net/en/browser) - 与 Tor Project 合作开发、注重隐私的浏览器。
* [Opera](https://www.opera.com)
* [Safari](https://www.apple.com/safari)
* [Sleipnir](https://www.fenrir-inc.com/jp/sleipnir)
* [Slimjet](https://www.slimjet.com)
* [SRWare Iron](https://www.srware.net/en/software_srware_iron.php)
* [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en) - Tor 是一款自由软件，通过让你在互联网上匿名通信，防止他人获知你的位置或浏览习惯。
* [Torch](https://www.torchbrowser.com)
* [UCBrowser](https://www.ucweb.com)
* [Vivaldi](https://vivaldi.com) - 强大、私密且个性化的网页浏览器。
* [Waterfox](https://www.waterfox.net/) - 快速且私密的网页浏览器，使用 Waterfox 开箱即可获得隐私保护。
* [Yandex Browser](https://browser.yandex.com/desktop/main)

## <a id="s61"></a>[↑](#toc) 离线浏览

* [A1 Website Download](https://www.microsystools.com/products/website-download) - 将整个网站下载到磁盘。
* [Cyotek WebCopy](https://www.cyotek.com/cyotek-webcopy) - 是一款免费工具，可将网站内容自动下载到本地设备。
* [gmapcatcher](https://github.com/heldersepu/gmapcatcher)
* [HTTrack](https://www.httrack.com) - 可将互联网上的网站下载到本地目录，递归创建所有目录，把 HTML、图片及其他文件从服务器抓取到你的计算机。
* [Resolver](https://metaproductsrevolver.com)
* [SiteSucker](https://ricks-apps.com/osx/sitesucker/index.html)
* [WebAssistant](https://www.proxy-offline-browser.com/download.html)
* [Website Ripper Copier](https://www.tensons.com/products/websiterippercopier)

## <a id="s62"></a>[↑](#toc) VPN 服务

* [OffShore.cat](https://offshore.cat/?page=vpn) - 面向注重隐私用户的 VPN 清单 
* [TorrentFreak List of VPNs](https://torrentfreak.com/vpn-services-anonymous-review-2017-170304/)
* [VPN Comparison by That One Privacy Guy](https://thatoneprivacysite.net/) - 是一份顶级 VPN 服务的汇总清单。

## <a id="s63"></a>[↑](#toc) 信息图与数据可视化

* [Aeon](https://www.aeontimeline.com)
* [Arbor.js](https://arborjs.org)
* [Befunky](https://www.befunky.com)
* [Bizint](https://www.bizint.com)
* [Cacoo](https://cacoo.com)
* [Canva](https://www.canva.com)
* [Chart.js](https://www.chartjs.org) - 一个可轻松创建图表的 JavaScript 库
* [chartblocks](https://www.chartblocks.com)
* [creately](https://creately.com)
* [Crossfilter](https://square.github.io/crossfilter)
* [csvkit](https://github.com/wireservice/csvkit)
* [D3js](https://d3js.org) - 是一个功能强大的数据可视化 JavaScript 库。
* [Data Visualization Catalogue](https://datavizcatalogue.com)
* [Datawrapper](https://datawrapper.de)
* [Dropmark](https://www.dropmark.com)
* [dygraphs](https://dygraphs.com)
* [easely](https://www.easel.ly)
* [Exhibit](https://www.simile-widgets.org/exhibit)
* [Flot](https://www.flotcharts.org)
* [FusionCharts](https://www.fusioncharts.com)
* [Google Developers: Charts](https://developers.google.com/chart)
* [GraphX](https://spark.apache.org/graphx)
* [Highcharts](https://www.highcharts.com)
* [Hohli](https://charts.hohli.com)
* [Infogr.am](https://infogr.am)
* [Inkscape](https://inkscape.org)
* [Java Infovis Toolkit](https://philogb.github.io/jit)
* [JpGraph](https://jpgraph.net)
* [jqPlot](https://www.jqplot.com) - 一款用途广泛、可扩展的 jQuery 绘图插件。
* [Knoema](https://knoema.com)
* [Leaflet](https://leafletjs.com) - 一个开源 JavaScript 库，用于构建适配移动端的交互式地图。
* [Linkuroius](https://linkurio.us)
* [Listify](https://listify.okfnlabs.org) - 几秒钟内即可把 Google 电子表格变成美观且可搜索的列表。
* [LocalFocus](https://www.localfocus.nl)
* [Lucidchart](https://www.lucidchart.com) - 智能图表绘制应用，让团队协同做出更优决策、共创未来。
* [Mapline](https://mapline.com)
* [Nodebox](https://www.nodebox.net) - 一套工具集，让你按自己的方式进行生成式设计。
* [Observable](https://observablehq.com/) - 一种现代方式，基于开源构建强大、高性能、多语言的数据应用。
* [OpenLayers](https://openlayers.org) - 一个高性能、功能丰富的地图库，满足你所有的制图需求。
* [Palladio](https://hdlab.stanford.edu/palladio) - 轻松可视化复杂的历史数据。
* [Perspective](https://github.com/finos/perspective) - 交互式数据可视化与分析组件，非常适合大型、流式及静态数据集。
* [Piktochart](https://piktochart.com)
* [Pixxa](https://www.pixxa.com)
* [Plotly](https://plot.ly)
* [Preceden](https://www.preceden.com/) - 为任意主题创建可视化时间轴
* [QlikView](https://www.visualintelligence.co.nz/qlikview)
* [Quadrigram](https://www.quadrigram.com)
* [Raphael](https://dmitrybaranovskiy.github.io/raphael)
* [RAW](https://raw.densitydesign.org)
* [Snappa](https://snappa.io)
* [StoryMap](https://storymap.knightlab.com)
* [Tableau Public](https://public.tableau.com)
* [Tableau](https://www.tableau.com)
* [Textures.js](https://riccardoscalco.github.io/textures)
* [Tik-tok](https://datanews.github.io/tik-tok)
* [Tiki-toki](https://www.tiki-toki.com)
* [Timeflow](https://github.com/FlowingMedia/TimeFlow/wiki)
* [Timeline](https://timeline.knightlab.com)
* [Timeline](https://www.simile-widgets.org/timeline)
* [Timetoast](https://www.timetoast.com)
* [Venngage](https://venngage.com)
* [Vis.js](https://visjs.org)
* [Visme](https://www.visme.co)
* [Visualize Free](https://visualizefree.com)
* [visually](https://create.visual.ly)
* [Vortex](https://www.dotmatics.com/products/vortex)
* [ZingChart](https://www.zingchart.com)
## <a id="s64"></a>[↑](#toc) 社交网络分析

* [Gephi](https://gephi.org) - 是一款开源的图与网络可视化软件。
* [ORA-LITE](https://www.cmu.edu/casos-center/research/tools/)
* [Sentinel Visualizer](https://www.fmsasg.com)
* [Visual Investigative Scenarios](https://vis.occrp.org)
* [Wynyard Group](https://wynyardgroup.com)

## <a id="s65"></a>[↑](#toc) 隐私与加密工具

* [Abine](https://www.abine.com)
* [Adium](https://adium.im)
* [Bitwarden](https://bitwarden.com) - 开源密码管理器，支持跨平台。
* [CCleaner](https://www.piriform.com/ccleaner)
* [Chatsecure](https://chatsecure.org)
* [Disconnect](https://disconnect.me)
* [Duck Duck Go Search Engine](https://duckduckgo.com)
* [EncSF MP](https://encfsmp.sourceforge.net)
* [Epic Privacy Browser](https://www.epicbrowser.com)
* [Eraser](https://eraser.heidi.ie)
* [FileVault](https://support.apple.com/en-us/HT204837)
* [Free Proxy List](https://github.com/proxifly/free-proxy-list) - 免费 HTTP、SOCKS4 和 SOCKS5 代理，每 5 分钟测试并刷新一次，按国家分类提供列表。有助于让调查流量避开调查者自身的 IP。
* [Ghostery](https://www.ghostery.com)
* [GNU PG](https://www.gnupg.org/download/index.html)
* [GPG Tools](https://gpgtools.org)
* [Guardian Project](https://guardianproject.info)
* [Guerrilla Mail](https://www.guerrillamail.com)
* [Hotspot Shield](https://www.hotspotshield.com)
* [HTTPs Everywhere](https://www.eff.org/https-everywhere/)
* [I2P](https://geti2p.net)
* [justdeleteme](https://justdelete.me)
* [KeePass Password Safe](https://keepass.info) - 是一款免费开源的密码管理器，采用最安全的加密算法来保护你的密码。
* [Lastpass](https://lastpass.com)
* [Lockbin](https://lockbin.com)
* [Mailbox](https://mailbox.org)
* [Mailvelope](https://www.mailvelope.com)
* [Master Password](https://masterpasswordapp.com)
* [MetaClean](https://github.com/Moresyl/metaclean) - 跨平台桌面应用，可在 OSINT 调查中分享文件前，在本地移除文件中的敏感元数据。
* [Nixory](https://nixory.sourceforge.net)
* [NoScript](https://noscript.net)
* [Open DNS](https://www.opendns.com/home-internet-security)
* [Open PGP](https://www.enigmail.net/index.php/en)
* [Oscobo Search Engine](https://oscobo.co.uk)
* [OSSEC](https://ossec.github.io)
* [Panopticlick](https://panopticlick.eff.org)
* [Peerblock](https://forums.peerblock.com)
* [Pidgin](https://www.pidgin.im)
* [Pixel Block](https://chrome.google.com/webstore/detail/pixelblock/jmpmfcjnflbcoidlgapblgpgbilinlem)
* [Privacy.com](https://privacy.com) - 用于保障在线隐私与安全的虚拟支付卡。
* [Privacy Badger](https://www.eff.org/privacybadger)
* [Privazer](https://privazer.com)
* [Proton Mail](https://protonmail.com)
* [Qubes](https://www.qubes-os.org) - 一款以安全为核心的桌面操作系统，旨在通过隔离提供安全保障。
* [Securesha](https://securesha.re)
* [Silent circle](https://www.silentcircle.com)
* [Signal](https://signal.org) - 端到端加密的消息与通话。
* [Snort](https://www.snort.org)
* [Spideroak](https://spideroak.com)
* [Spoof Me](https://spoof-me.com/) - Chrome/Firefox 扩展，将浏览器指纹信号（User Agent、语言、时区、屏幕、硬件）伪装成一致的身份，并标记读取指纹 API 的站点。有助于隐藏调查者真实的设备与区域设置。
* [Steganography Online Codec](https://www.pelock.com/products/steganography-online-codec)
* [Surveilliance Self Defense](https://ssd.eff.org)
* [Tails](https://tails.boum.org)
* [Thunderbird](https://www.thunderbird.net/en-US/)
* [Tor Project](https://www.torproject.org)
* [uBlock Origin](https://github.com/gorhill/uBlock)
* [Wickr](https://wickr.com)
* [WOT](https://www.mywot.com)
* [ZMail](https://zmail.sourceforge.net)

## <a id="s66"></a>[↑](#toc) DNS
* [Amass](https://github.com/owasp-amass/amass) - amass 工具会检索互联网数据源、执行子域名暴力枚举、搜索网页存档，并利用机器学习生成更多子域名猜测。DNS 名称解析通过众多公共服务器完成，使权威服务器看到的流量来自不同位置。使用 Go 编写。
* [Columbus Project](https://github.com/elmasy-com/columbus) - Columbus Project 是一项高级子域名发现服务，提供快速、强大且易用的 API。
* [dnsx](https://github.com/projectdiscovery/dnsx) - ProjectDiscovery 出品的快速、多用途 DNS 工具包，用于执行 DNS 探测、解析记录和过滤 DNS 响应。
* [Merklemap](https://www.merklemap.com/) - 发现并枚举与某个网站关联的所有子域名，包括那些未公开的子域名。其原理是摄取证书透明度日志。
* [Subhunt](https://github.com/ahmadouniass/Subdomains-finder-subhunt) - 多源子域名枚举工具，查询 crt.sh 证书透明度日志、HackerTarget 和 RapidDNS。支持带状态码的 HTTP/HTTPS 存活探测、存活/失效过滤、多格式导出（TXT/JSON/CSV）以及完整的命令行界面。

## <a id="s67"></a>[↑](#toc) 海事

* [Logibook](https://logibook.dataint.net) - 涵盖 250 个国家的贸易与物流参考资料：汇集港口、机场、码头、贸易区和承运商等 58,730 个有来源标注的实体，数据构建自 NGA 世界港口索引、UN/LOCODE、SMDG 码头与班轮代码表、ISO 6346 集装箱代码、UNCTAD 班轮航运连通性以及世界银行港口吞吐量。每个港口页面还显示最近的机场、城市和贸易区及其距离。每项数据均标注来源和年份。仅提供网页参考，无 API 或批量下载。
* [Phantom Tide](https://github.com/tg12/phantomtide) - 跨领域 OSINT 仪表板，整合船舶追踪、空域活动、官方通告、环境背景和卫星探测，用于海事与空域分析。
* [PortInsight.io](https://portinsight.io/ports) - 免费提供七大港口的实时锚地等待时间、船舶数量和月度拥堵报告，基于 AIS 测算并公开了方法。注册免费账户可获取港口及船舶到港邮件提醒。
* [VesselFinder](https://www.vesselfinder.com) - 一个免费的 AIS 船舶追踪网站。VesselFinder 显示由全球 AIS 网络探测到的实时船舶位置与海上交通。

## <a id="s68"></a>[↑](#toc) 其他工具

* [aadinternals](https://aadinternals.com/osint) - 为 Azure Active Directory（AAD）和 Microsoft 365 的高级分析与安全测试提供工具和洞察。
* [ArkhamMirror](https://github.com/mantisfury/ArkhamMirror) - 本地优先的 AI 文档情报工具，具备离线 RAG、矛盾检测、知识图谱和视觉 AI 表格提取能力。
* [Barcode Reader](https://online-barcode-reader.inliteresearch.com) - 用 C#、VB、Java、C\C++、Delphi、PHP 等语言解码条形码。
* [BeVigil-CLI](https://github.com/Bevigil/BeVigil-OSINT-CLI) - 统一的命令行界面与 Python 库，通过 BeVigil OSINT API 搜索子域名、URL、从移动应用索引出的应用等资产。
* [btc-toolkit](https://github.com/devdavidejesus/btc-toolkit) - 读取比特币链上数据的命令行工具：解码 OP_RETURN 消息和铭文、查看地址与交易，并依据所在区块的 Merkle 证明验证交易。
* [Cyberbro](https://github.com/stanfrbd/cyberbro) - 自托管应用，提供 Docker 部署，可轻松检索可观察对象并检查其信誉。从原始输入中提取 IoC，并通过多个服务核查其信誉。
* [CyberGordon](https://cybergordon.com) - CyberGordon 是一个威胁情报搜索引擎，整合了 30 多个来源。
* [CrowdSec](https://github.com/crowdsecurity/crowdsec) - 一款开源、免费、协作式的 IPS/IDS 软件，使用 Go 编写，能够分析访问者行为并针对各类攻击给出相应的响应。
* [Datasploit](https://github.com/DataSploit/datasploit) - 可对用户名、邮箱地址和域名执行多种 OSINT 技术的工具。
* [Dehashed CLI](https://github.com/hmaverickadams/DeHashed-API-Tool) - 通过 DeHashed API 检索数据泄露库的命令行工具。
* [Dorkgpt](https://www.dorkgpt.com) - 利用人工智能生成高级搜索语句，用于查找互联网上特定或隐藏的信息。
* [DuckDuckGo URL scraper](https://github.com/its0x08/duckduckgo) - 一个简单的 DuckDuckGo URL 抓取工具。
* [FaviconHash](https://kriztalz.sh/favicon-hash/) - 生成网站 favicon 的哈希值，供 Shodan、VirusTotal、Censys、ZoomEye 或 FOFA 使用。
* [FOCA](https://github.com/ElevenPaths/FOCA) - 用于查找文档中元数据和隐藏信息的工具。
* [Glit](https://github.com/shadawck/glit) -  检索与某个 git 仓库、git 用户或 git 组织相关的用户的所有邮件。
* [Greynoise](https://greynoise.io/) - “反威胁情报”：Greynoise 刻画互联网的背景噪声，让用户专注于真正重要的事情。
* [IntelHub](https://github.com/tomsec8/IntelHub) – 基于浏览器的开源 OSINT 扩展。所有分析均在本地运行（无需服务器）。功能包括文本分析器、元数据分析器、站点与存档分析、反向图片搜索、加密货币/Telegram 分析器。
* [Hunchly](https://www.hunch.ly/) - Hunchly 是一款专为在线调查设计的网页抓取工具。
* [IntellyWeave](https://github.com/vericle/intellyweave)  - 由 AI 驱动的 OSINT 平台，具备 GLiNER 实体抽取、Mapbox 三维地理空间可视化，以及跨 30 多个国际档案库的多智能体档案研究能力。
* [keyFinder](https://github.com/momenbasel/keyFinder) - Chrome 扩展，通过扫描脚本、meta 标签、隐藏字段、Web 存储和网络响应，结合 80 多种检测模式与香农熵分析，被动发现任意网页上泄露的 API 密钥、令牌、机密和凭据。
* [LinkScope Client](https://github.com/AccentuSoft/LinkScope_Client) - LinkScope Client 的 Github 仓库。
* [LinkScope](https://accentusoft.com/) - LinkScope 是一款开源情报（OSINT）与图形化链接分析工具，用于为调查任务收集和关联信息。
* [Maltego](https://www.maltego.com/) - Maltego 是一款开源情报（OSINT）与图形化链接分析工具，用于为调查任务收集和关联信息。
* [Mozilla HTTP Observatory](https://developer.mozilla.org/en-US/observatory) - Observatory⁩ 通过分析对最佳安全实践的遵循情况来增强 Web 安全性。
* [Obsidian](https://obsidian.md) - 知识库与笔记工具，非常适合 OSINT 案件管理。
* [OpenGraph Intel (OGI)](https://github.com/khashashin/ogi) - 开源链接分析与 OSINT 框架。AI 驱动的调查工具
* [OpenRefine](https://github.com/OpenRefine) - 免费开源的强力工具，用于处理杂乱数据并加以改善。
* [Orbit](https://github.com/s0md3v/Orbit) - 通过递归爬取交易历史，绘制加密钱包之间的关系。
* [OSINT Framework](https://osintframework.com/) - 基于 Web 的 OSINT 框架。
* [OSINT-Tool](https://www.osint-tool.com/) - 一款浏览器扩展，可在你访问的任意网页上直接使用一整套 OSINT 实用工具（Dehashed、Epieos、Domaintools、Exif 数据、反向图片搜索等）。
* [OSINT.SH](https://osint.sh/) - 信息收集工具集。
* [OsintStalker](https://github.com/milo2012/osintstalker) - 用于 Facebook 和地理位置 OSINT 的 Python 脚本。
* [Outwit](https://www.outwit.com) - 从在线来源查找、抓取并整理各类数据和媒体。
* [PGPKeyAnalyser](https://kriztalz.sh/pgp-key-analyser/) - 在线分析和查看 PGP 密钥的详细信息，无需下载 asc 文件。
* [Photon](https://github.com/s0md3v/Photon) - 专为 OSINT 设计的爬虫
* [Pyba](https://github.com/fauvidoTechnologies/PyBrowserAutomation/) - 浏览器自动化框架，只需少量代码即可使用 DFS 和 BFS 模式搜索网页并执行 OSINT，非常适合探索性任务。
* [pygreynoise](https://github.com/GreyNoise-Intelligence/pygreynoise) - Greynoise 的 Python 库
* [QuickCode](https://quickcode.io/) - Python 和 R 数据分析环境。
* [ReconFTW](https://github.com/six2dez/reconftw) - 自动化信息收集框架，面向漏洞赏金和渗透测试，集成了多种工具。
* [Router Passwords](https://www.routerpasswords.com) - 路由器默认密码的在线数据库。
* [SerpApi](https://serpapi.com/) - 可轻松抓取 Google 搜索及 25 多个搜索引擎，返回原始 JSON。支持 10 种 API 封装。
* [SerpScan](https://github.com/Alaa-abdulridha/SerpScan) - 功能强大的 PHP 脚本，让你可在命令行中直接利用 dorking 搜索语法的强大能力。分析来自 Google、Bing、Yahoo、Yandex 和 Badiu 的数据。
* [Sintelix](https://sintelix.com/) - Sintelix 是一款开源情报（OSINT）与图形化链接分析工具，用于为调查任务收集和关联信息。
* [sn0int](https://github.com/kpcyrd/sn0int) - 半自动 OSINT 框架与包管理器。
* [SpiderFoot](https://github.com/smicallef/spiderfoot) - SpiderFoot 的 Github 仓库。
* [SpiderFoot](https://www.spiderfoot.net) - SpiderFoot 是一个开源情报（OSINT）自动化平台，拥有 200 多个模块，用于威胁情报、攻击面监控、安全评估和资产发现。
* [SpiderSuite](https://github.com/3nock/SpiderSuite) - 一款先进的跨平台图形界面 Web 安全爬虫。
* [Sub3 Suite](https://github.com/3nock/sub3suite) - 研究级的工具套件，用于情报收集与目标测绘，具备主动和被动（100 多个模块）情报收集能力。
* [Text Machine](https://textmachine.org/en/text-tools/cipher-identifier) - 识别未知的编码或加密字符串，在无需密钥时就地解码（Base64、十六进制、二进制、摩尔斯、培根密码、波利比奥斯方阵、A1Z26、埃特巴什、凯撒），其余情况则提供频率分析以及自动的维吉尼亚和替换密码求解器。在浏览器中运行，无需注册，不上传任何数据。
* [The Harvester](https://github.com/laramies/theHarvester) - 从搜索引擎、PGP 密钥服务器和 SHODAN 计算机数据库等不同公开来源收集邮箱、子域名、主机、员工姓名、开放端口和横幅信息。
* [Unfurl](https://dfir.blog/unfurl/) - Unfurl 会分析 URL 并将其拆解为对数字调查有用的取证要素。
* [Waybackurls](https://github.com/tomnomnom/waybackurls) - 获取 Wayback Machine 收录的某个域名的所有 URL。
* [Zen](https://github.com/s0md3v/Zen) - 轻松查找 Github 用户的邮箱地址、URL 及其他数据


## <a id="s69"></a>[↑](#toc) 威胁情报

- [Threat Actor Usernames](https://threatactorusernames.com/) -  检索 300 多万条威胁行为者用户名记录，发现他们在哪些网络平台活动和发帖。
* [defend.network](https://defend.network) - 免费、无需登录的网络威胁情报站点，每日发布威胁简报、每周发布漏洞报告，每条 CVE 都与 NVD 和 CISA KEV 目录交叉核对。内容按威胁类型、行业和严重程度组织，并附修复建议。RSS 订阅源位于 defend.network/feed.xml。
* [DFIR Platform](https://platform.dfir-lab.ch) - 威胁情报平台，提供多源 IOC 富化、钓鱼邮件分析、暴露面扫描和域名信誉评分。提供免费套餐。
* [Dread Scraper](https://github.com/NPCmillionaire/dread-scraper) - 慢速、可断点续传的存档工具，针对选定的 Dread 论坛版面，流量经 Tor 路由。将主题帖和回复保存到本地 SQLite 数据库并支持全文检索，便于离线开展威胁情报研究。
* [GitGuardian - Public GitHub Monitoring](https://www.gitguardian.com/monitor-public-github-for-secrets) - 实时监控公开 GitHub 仓库，检测机密和敏感信息，防止黑客把 GitHub 当作侵入你业务的后门。
* [onion-lookup](https://onion.ail-project.org/) - 免费的在线服务和 API，用于检查 Tor 隐藏服务（.onion 地址）是否存在并获取其关联元数据。onion-lookup 依赖一个私有 AIL 实例来获取元数据。
* [OnionScan](https://github.com/s-rah/onionscan) - 免费开源工具，用于调查暗网。其主要目标是帮助研究人员和调查者监控和追踪暗网站点。
* [MalwareIntel](https://malwareintel.es) - 免费威胁情报平台，将 70 多个网络威胁情报（CTI）源聚合为知识图谱。包含 273K+ 个 IOC、4200+ 个恶意软件家族、3632 条检测规则（Sigma/YARA）、Sigma 转 SIEM 转换器，以及按家族打包 TTP + IOC + 规则的检测包。
* [Malwagon](https://malwagon.com) - 在线恶意软件分析沙箱。可引爆提交的文件或 URL 并发布报告，还允许按指标搜索历史公开扫描记录：IP、域名、URL、互斥体、注册表项、哈希或 JA3/JA4 指纹。报告无需账户即可查看；免费套餐额外提供提交、API 和命令行客户端。
* [OTX AlienVault](https://otx.alienvault.com/) - Open Threat Exchange 是全球情报社区的邻里守望组织。它让私营企业、独立安全研究人员和政府机构能够公开协作，共享关于新兴威胁、攻击方法和恶意行为者的最新信息，从而提升整个社区的安全水平。
* [Pharos AI](https://conflicts.app) - 实时开源情报仪表板，用于追踪冲突，具备交互式地理空间可视化、多源 RSS 监控和行为者档案。
* [PhishingSecLists](https://github.com/spmedia/PhishingSecLists) - 该清单配合 Web 扫描工具（Gobuster、ffuf、Burp Suite、DirBuster）使用。这些清单专门针对钓鱼、加密货币诈骗落地页及其他可疑恶意网站进行模糊测试而定制设计。命中时可获得有价值的情报。
* [STIX Viewer](https://stix-viewer.threatlandscape.io/) - 免费的在线 STIX 2.1 查看器／可视化工具。
* [Taranis AI](https://github.com/taranis-ai/taranis-ai) - 开源 OSINT 平台，借助 AI/NLP 辅助工作流，从网页、RSS、邮箱及其他来源收集、富化、分析并发布情报。
* [Threat Actor Usernames Scrape](https://github.com/spmedia/Threat-Actor-Usernames-Scrape) - 汇集最新情报，以及从各类网络犯罪来源和论坛抓取的 90 多万个威胁行为者用户名。
* [ThreatLens](https://github.com/AbdaullahAG/Threat_Intel_Project) - 专业的多源威胁情报命令行工具，通过多个免费 API 调查 IP、域名、哈希和 CVE，具备自动日志解析和彩色编码报告功能。
* [VoidAccess](https://github.com/KatrielMoses/voidaccess) - 自托管的开源暗网威胁情报平台，将完整的 OSINT 调查流程自动化。支持查询优化、多引擎 Tor 搜索、实体抽取（钱包、CVE、IP、行为者句柄、哈希）、关系图谱，以及 STIX 2.1、MISP、Sigma 和 CSV 格式的结构化导出。可基于 Docker 和免费大语言模型运行，采用 MIT 许可证。
* [Voidly Censorship Index](https://voidly.ai/censorship-index) - 实时全球互联网审查情报，聚合 1960 万条实时 OONI 样本和 160 万条历史记录，覆盖 119 个以上国家。提供可引用的事件数据库（5,356 起事件、16,822 条证据）、基于机器学习的断网预警订阅源、ISP 级风险评分，以及面向阻断、DNS 污染和 BGP 级中断信号的公开 REST/MCP API。数据采用 CC BY 4.0 许可。

## <a id="s70"></a>[↑](#toc) 游戏平台

* [lol_monitor](https://github.com/misiektoja/lol_monitor) - 用于实时跟踪 LoL（英雄联盟）玩家游戏活动的工具，包括检测用户开始或结束对局，支持邮件提醒、CSV 日志记录、游戏时长统计等
* [psn_monitor](https://github.com/misiektoja/psn_monitor) - 用于实时跟踪 Sony Playstation（PSN）玩家游戏活动的工具，包括检测用户上线/离线或游玩游戏，支持邮件提醒、CSV 日志记录、游戏时长统计等
* [steam_monitor](https://github.com/misiektoja/steam_monitor) - 用于实时跟踪 Steam 玩家游戏活动的工具，包括检测用户上线/离线或游玩游戏，支持邮件提醒、CSV 日志记录、游戏时长统计等
* [xbox_monitor](https://github.com/misiektoja/xbox_monitor) - 用于实时跟踪 Xbox Live 玩家游戏活动的工具，包括检测用户上线/离线或游玩游戏，支持邮件提醒、CSV 日志记录、游戏时长统计等

## <a id="s71"></a>[↑](#toc) 音乐流媒体服务

* [lastfm_monitor](https://github.com/misiektoja/lastfm_monitor) - 用于实时跟踪 Last.fm 用户收听活动的工具，包括检测用户上线与离线、暂停或恢复播放、所有播放过的歌曲及其时长、跳过的歌曲，并支持可选的自动播放、邮件提醒、CSV 日志记录、会话统计等
* [spotify_profile_monitor](https://github.com/misiektoja/spotify_profile_monitor) - 用于实时跟踪 Spotify 用户活动及资料变更（含播放列表）的工具，支持邮件提醒、CSV 日志记录、在终端显示媒体内容、检测头像变更等
* [spotify_monitor](https://github.com/misiektoja/spotify_monitor) - 用于实时跟踪 Spotify 好友收听活动的工具，包括检测用户上线与离线、播放过的歌曲及其时长、跳过的歌曲，并支持可选的自动播放、邮件提醒、CSV 日志记录、会话统计等

## <a id="s72"></a>[↑](#toc) OSINT 视频

* [Amazing mind reader reveals his ‘gift’](https://www.youtube.com/watch?v=F7pYHN9iC9I)
* [Bendobrown](https://www.youtube.com/c/Bendobrown)
* [Data to Go](https://www.youtube.com/watch?v=_YRs28yBYuI)
* [SANS OSINT Summit 2021 (Playlist)](https://www.youtube.com/playlist?list=PLs4eo9Tja8bj3jJvv42LxOkhc2_ylpS9y)
* [See how easily freaks can take over your life](https://www.youtube.com/watch?v=Rn4Rupla11M)

## <a id="s73"></a>[↑](#toc) OSINT 博客

* [Bellingcat](https://www.bellingcat.com/)
* [eInvestigator](https://www.einvestigator.com/)
* [IntelTechniques](https://inteltechniques.com/)
* [NixIntel](https://nixintel.info/)
* [OSINT Techniques](https://www.osinttechniques.com/blog)
* [OSINT Ambition Publication](https://publication.osintambition.org/)
* [OSINT Team](https://www.osintteam.com/)
* [OSINTCurious](https://osintcurio.us/)
* [Sector035](https://sector035.nl/)
* [Skopenow](https://www.skopenow.com/news)
* [Social Links](https://blog.sociallinks.io/)
## <a id="s74"></a>[↑](#toc) OSINT RSS 订阅源

* [EUvsDisinfo](https://euvsdisinfo.eu/category/blog/feed/) - 聚焦虚假信息叙事与影响力行动的研究、分析与案例。
* [Fake News – Inforrm's Blog](https://inforrm.org/tag/fake-news/feed/) - 与虚假信息调查相关的媒体法与错误信息分析。
* [Krebs on Security](https://krebsonsecurity.com/feed/) - 关于网络犯罪、数据泄露与威胁行为者的调查报道。
* [OSINT Combine Blog](https://www.osintcombine.com/blog-feed.xml) - 最新的 OSINT 技战法、调查方法与监控工作流。
* [SANS Internet Storm Center Diary (Full Text)](https://isc.sans.edu/rssfeed_full.xml) - 高价值安全事件报告、恶意软件观测与操作安全分析。
* [The Citizen Lab](https://citizenlab.ca/feed/) - 关于监控、间谍软件、审查制度及数字威胁的研究，适用于进阶 OSINT 工作。
* [Trace Labs Blog](https://www.tracelabs.org/blog/rss.xml) - 失踪人员 OSINT 方法论、案件支持与调查工作流。

## <a id="s75"></a>[↑](#toc) 其他资源

* [appsec.fyi OSINT Resources](https://appsec.fyi/osint.html) - 面向网络安全的 OSINT 资源精选，包含工具、技术方法与实战文章。
* [Aware-online.com](https://www.aware-online.com/en/osint-tools) - 面向调查工作的 OSINT 工具与方法论精选。
* [Bellingcat's Online Investigation Toolkit](https://bit.ly/bcattools)
* [Bellingcat Online Researcher Survey: Tool Wishes](https://docs.google.com/spreadsheets/d/1vNJRMrlwI7i06diBJtRJWrvt4YuPOqlbUV5o00P_YmE/edit#gid=1378107220) — Bellingcat 二月调研中研究者希望拥有的 OSINT 工具愿望清单。
* [Cipherstick](https://cipherstick.tech) - 免费 OSINT 谜题练习，无需注册账号。
* [OSINT Dojo](https://www.osintdojo.com/resources/)
* [OSINT Belarus](https://t.me/s/osintby)
* [These Are the Tools Open Source Researchers Say They Need](https://www.bellingcat.com/resources/2022/08/12/these-are-the-tools-open-source-researchers-say-they-need/) — Bellingcat 于 2022 年 2 月开展的调研结果。
* [OSINT Updates - a free weekly newsletter for OSINTers](https://osintupdates.com/)

## <a id="s76"></a>[↑](#toc) 相关 Awesome 精选清单

* [awesome-anti-forensic](https://github.com/remiflavien1/awesome-anti-forensic) - 由 @remiflavien1 维护
* [awesome-ctf](https://github.com/apsdehal/awesome-ctf) - 由 @apsdehal 维护
* [awesome-forensics](https://github.com/Cugu/awesome-forensics) - 由 @cugu 维护
* [awesome-hacking](https://github.com/carpedm20/awesome-hacking) - 由 @carpedm20 维护
* [awesome-honeypots](https://github.com/paralax/awesome-honeypots) - 由 @paralax 维护
* [awesome-incident-response](https://github.com/meirwah/awesome-incident-response) - 由 @meirwah 维护
* [awesome-lockpicking](https://github.com/fabacab/awesome-lockpicking) - 由 @fabacab 维护
* [awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) - 由 @rshipp 维护
* [awesome-pentest](https://github.com/enaqx/awesome-pentest) - 由 @enaqx 维护
* [awesome-privacy](https://github.com/Lissy93/awesome-privacy/) - 由 @Lissy93 维护
* [awesome-sec-talks](https://github.com/PaulSec/awesome-sec-talks) - 由 @PaulSec 维护
* [awesome-security](https://github.com/sbilly/awesome-security) - 由 @sbilly 维护
* [awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) - 由 @hslatman 维护
* [infosec reference](https://github.com/rmusser01/Infosec_Reference) - 由 @rmusser01 维护
* [OSINT-BIBLE](https://github.com/frangelbarrera/OSINT-BIBLE) - 由 @frangelbarrera 维护
* [personal-security-checklist](https://github.com/Lissy93/personal-security-checklist) - 由 @Lissy93 维护
* [SecLists](https://github.com/danielmiessler/SecLists) - 由 @danielmiessler 维护
* [security-list](https://github.com/zbetcheckin/Security_list) - 由 @zbetcheckin 维护
## <a id="s77"></a>[↑](#toc) 许可证

![cc license](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

本作品采用 [知识共享 署名-相同方式共享 4.0 国际（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/) 许可协议授权。

**署名与来源**：本仓库是 [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint)（作者 [@jivoi](https://github.com/jivoi) 及全体贡献者，原作同样采用 CC BY-SA 4.0）的简体中文翻译与改编版本。依据 CC BY-SA 4.0，本仓库保留原作者署名、提供原作品链接、明确标注所作出的修改，并以相同许可协议发布；完整协议文本见 [LICENSE.txt](LICENSE.txt)。

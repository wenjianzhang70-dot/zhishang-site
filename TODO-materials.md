# 待补充资料（第二版，基于画册）
详见 company-facts.md 第 6、7 节。
网站上还写着 [待提供] / [to be provided] 的有：询价回复时效、WhatsApp/微信、证书名称和编号。
以下项目按保守默认处理，可随时改：
- 不写前雇主名称
- 不放个人手机号
- 不用客户品牌包装照片
- 不放车灯应用照片
- 胶水、模具两家只放在「关于我们」的关联公司区块
英文关键词（rigid box gluing machine、hot melt gluing machine for rigid box、glue dispensing machine、glue spraying machine、case making machine、lid-and-base box、book-style box、greyboard）的搜索量都还没核实。

## 已从公开页面隐藏、等老板回复的内容（2026-10-12）
- 每个产品页的「贸易信息」表（起订量、付款方式、交期、包装、整机质保）和「常见问题」。代码保留在 `<template id="hold-trade-faq">` 里，不显示；拿到答案后去掉 template 标签即可显示。
- 询价回复时效、WhatsApp / 微信号、证书名称与编号，页面上已不显示「待提供」字样，等资料到了再补上。

## 术语待确认（2026-10-12）
- 「坑卡」英文暂译 **recessed card insert**，请老板确认海外客户实际叫法（如 insert tray / card insert / cavity insert）。英文页面已去掉括号里的中文「(坑卡)」。
- 「皮壳」英文暂译 **case**；「万能胶」英文统一为 **universal glue**。

## 设备细节照片（2026-10-12 新增）
- 每台机器请提供 **3 张真实近距离照片**：划胶头（喷胶机为喷胶头）、控制手柄、控制面板。
- 现在 ZS-S088C、ZS-S088E-4、ZS-S088P 页面上的细节小图是**从主图裁出来的**，不是真实特写，清晰度不够；其他机型还没有细节图。
- 要求：光线充足、背景干净、横拍，尽量 ≥ 2000 px 宽。

## 正式上线检查清单
- [ ] 所有页面去掉 `<meta name="robots" content="noindex">`（build.py 里的 page()）
- [ ] build.py 里的 URL/BASE 从 `https://wenjianzhang70-dot.github.io/zhishang-site/` 换成官方域名，重新生成：canonical、hreflang、JSON-LD 链接、sitemap.xml、robots.txt 的 Sitemap 地址
- [ ] 绑定自定义域名（GitHub Pages CNAME + DNS），开启 HTTPS
- [ ] 确认后提交 sitemap 到 Google Search Console / 百度站长

## 自定义域名 zhishangkj.com（2026-10-13）
- 已绑定 GitHub Pages：A 记录指向 185.199.108.153 / 185.199.109.153，www 用 CNAME 指向 wenjianzhang70-dot.github.io，仓库根目录有 CNAME 文件。
- 建议补充 A 记录 185.199.110.153、185.199.111.153，以及 AAAA 记录（GitHub 官方推荐填满 4 个 IP）。
- **建议在 GitHub 做域名验证（Verified domain）**：GitHub 账户 Settings → Pages → Add a domain，按提示在 DNS 加一条 TXT 记录（_github-pages-challenge-wenjianzhang70-dot.zhishangkj.com）。这样别人无法把 zhishangkj.com 接到自己的仓库上，防止域名被接管。
- 仍保留 noindex，正式上线时按上面的清单去掉。

## 非标机照片（2026-10-13）
- ZS-FB-019、ZS-FB-026 现在只有车间实拍（背景杂），请提供**白底整机照片**（整机完整入镜、横拍）。FB-026 目前用模糊放大的同图做两侧背景，原图未裁切。

## 旧站视频（v16，来源 glue-machine.com，原片在 refs/oldsite-videos/）
已上线：ZS-S088E-4（-JeG0…）、ZS-S088D-4（4YeK0…）、ZS-S088A（8JyG0…）、首页生产线（ipaK0…）。
未上线（待定）：
- ABUIABA6GAAg-LiQ0AYopP_y1AE.mp4：字幕称"in-line four-axis cold"，与 S088E-4 重复，备用。
- ABUIABA6GAAg9pmG0AYogMKZ6QM.mp4：家具用随线四轴冷胶，与 S088E-4 重复，备用。
- ABUIABA6GAAgxoyK0AYonLuOlgM.mp4：S088E-4 视频的 480p 版本，重复。
- ABUIABA6GAAghYaK0AYorOXH5gE.mp4：S088D-4 视频加闪光特效版，重复。
- ABUIABA6GAAgmaaQ0AYo5PXx1QM.mp4：S088D-4 同类（AV1 编码，画面含手机号/Jelly 字样），备用。
- ABUIABA6GAAgmrWQ0AYo6YKa8gU.mp4：123 秒"Hot sale"混剪，含多台不同机器，无法对应单一型号。

## 旧站图片（v17）
已用：S088E-4/R-4/B/A/A-R 各 2-3 张不同角度或划胶照片（img/os-*），关于我们页 2 张展会照片（355×240，分辨率低，有高清图请替换）。
未用、待确认：
- 老站「四轴柜式冷胶」页 6 张照片（橙色台面柜式机），与网站现用 S088C 图外观不同，无法确认是 C 还是 D 系列。
- 老站「三轴柜式热胶刮胶」页 11 张照片（白色机罩 + 橙色孔板 + 推车上的热熔胶机），与现用 S088D-4 图外观不同。
- 老站首页的非标机图（多工位自动线、蓝色机架线、黄色机罩机、白色塑料件），没有型号。
- 老站英文长描述（家具、MDF 等应用）在画册/PPT 中没有依据，未采用。

## v18：请老板确认
- ZS-S088E-4 是否也有「单机 + 绿色输送线」的配置？老网站有这种照片，画册是双机连线。确认前网站不放单机照片（已从 E-4 图库移除）。

## v21 老网站分类页
- 老网站 /cn/ 中文栏目（约 58 篇 NewsDetail、产品、关于）全是「海南电动观光车」的模板残留内容，与至尚无关，未采用。英文 /News 和 3 个 NewsDetail 是空页。因此没有建文章栏目。建议让建站服务商删除老网站中文栏目。
- 待确认：随线四轴喷胶机（老网站 PG12025965）是否真实机型、型号和参数。
- 待确认：冲孔机 / 贴丝带机的型号、中文正式叫法。
- FB-017 老网站资料（PLC+触摸屏、振动盘上料、伺服、CE、质保 12 个月、交期）和 12 张照片：非标机目前只有卡片没有详情页，是否要给 FB 系列做详情页？
- 三狮模具成立年份（2017 / 2020）。

## v22 已解决（老板 10-13）
- 随线四轴喷胶机：真实机型，已发布（无型号，参数同 E-4）。待补：喷胶宽度。
- 热熔胶 VOC：属实，保留。
- 三狮模具成立年份：2020。
- 冲孔/贴丝带机型号：暂不提供。

## v24 应用领域（请老板确认）
- 「礼盒 / 精品盒」推荐 ZS-S088E-4、ZS-S088R-4；「天地盒」推荐 ZS-S088E-4、ZS-S088R-4、ZS-S088C，两者重叠很多（只差 S088C），描述也相近。网站保留为两个条目，未编造区别。是否合并或补充区别，请老板定。

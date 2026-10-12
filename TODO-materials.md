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

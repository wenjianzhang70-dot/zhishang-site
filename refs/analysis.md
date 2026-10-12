# 参考网站分析（结构学习，不抄文字、图片和品牌）

截图存放：`refs/nordson.png`、`refs/graco.png`、`refs/robatech.png`、`refs/valco.png`，均为 Chrome headless 在 1440 宽下截的整页。
抓取时间：2026-10-12。graco.com 的首页和行业页对 headless 返回 404，所以 Graco 改为截它的产品页。

## A. 国际大牌

### 1. Nordson（工业涂装事业部页）
来源：https://www.nordson.com/en/divisions/industrial-coating-systems（截图 refs/nordson.png，文字已用 WebFetch 核对）
- 导航：顶栏有 Products & Applications / Divisions / Resource Library / About / Contact Us；下面是事业部二级导航：Applications and Solutions / Industries / Resource Center / Contact us。
- 页面从上到下：
  1. 活动大图轮播（FABTECH 展会）
  2. 「Applications and Solutions」8 张卡片，每张是产品图 + 一句话 + Learn more
  3. 「Popular Products」8 个热门型号卡片 + 「View all products」
  4. 「Your Problem Solver」，按行业讲问题和对应方案
  5. 「Industries We Serve」
  6. Newsroom
  7. 「Case Studies」：标题都是「客户名 | 场景」，并写出量化结果，例如「Frost-trol doubled output and achieved a reduction in powder consumption of about 20%」
  8. Events
  9. Find Local Support / Technical Support / Contact Sales 三个入口
- 我们采用：
  - 「按应用找」和「按产品找」两个入口并列。
  - 案例标题用「客户 | 场景 + 量化结果」的格式（等用户提供真实案例再用）。
  - 页尾把「技术支持」和「销售咨询」分成两个入口。

### 2. Graco（InvisiPac HM25c 产品页）
来源：https://www.graco.com/us/en/in-plant-manufacturing/product-group/invisipac-hm25c-hot-melt-adhesive-dispense-system.html（截图 refs/graco.png）
- 产品页结构：
  1. 左边产品图库，右边型号名 + 一段摘要
  2. 两个按钮「CONTACT AN EXPERT」「WHERE TO BUY」
  3. 「Questions About this Product? … ask one of our experts」
  4. 锚点标签：Features / Ordering Information / Specifications & Documents
  5. Features 是一组要点列表
  6. Ordering Information 是可筛选的型号表（按 Channels、Voltage、Pattern Controller 筛选）
  7. 说明书和样本 PDF 下载
  8. 「Call Support Monday–Friday 7 a.m.–4 p.m. Central Time」
- 我们采用（**这是对至尚最有用的一家**）：
  - 每个机型一页：照片 + 摘要 + 「咨询这台机」按钮，下面依次是功能要点、参数表、PDF 下载。
  - 同系列的变体（标准/加大、冷胶/热胶）放进一张对比表，不拆成好几页。
  - 写明在线时间。

### 3. Robatech（首页）
来源：https://www.robatech.com/en（截图 refs/robatech.png，文字已用 WebFetch 核对）
- 页面从上到下：
  1. 大图标语
  2. 「SOLUTIONS FOR INDUSTRIAL ADHESIVE APPLICATION」三个入口：APPLICATIONS / PRODUCTS / INDUSTRIES
  3. NEWSROOM
  4. 「OUR CUSTOMERS ABOUT ROBATECH」客户证言轮播，每条写姓名 + 职位 + 公司。其中有中国客户，例如「Chuanyong Cao, ZhongShan Dayuan Industrial Co., Ltd.」
  5. Green Gluing 可持续专题
  6. 全球办事处列表
- 产品同时覆盖热熔胶和冷胶：「Products for hot melt adhesive and PUR as well as cold glue application」
- 我们采用：
  - 首页三入口（应用 / 产品 / 行业）。
  - 客户证言写「真名 + 公司 + 职位」（需要客户授权）。
  - 冷胶、热胶分开讲，正好对应至尚的「-冷胶 / -热胶」两条线。

### 4. Valco Melton（首页）
来源：https://www.valcomelton.com/（截图 refs/valco.png，文字已用 WebFetch 核对）
- 页面从上到下：
  1. 大图轮播，每张一个卖点，例如「Ensure your customers receive defect-free boxes every time」
  2. 三个彩色快捷按钮条
  3. 一段公司定位加 3 条要点
  4. 「Founded on the Premise of Innovation, Established by Trust」数字条：「1952」「#1」「96+」
  5. 三个大按钮：联系我们 / 申请报价 / 找配件
  6. 页脚有电话和地址
- 我们采用：
  - 首页数字条，但只放画册里有的真实数字：2018 成立、售后「市内4小时」、「省内先试用一星期」。
  - 页尾「联系 / 报价」两个大按钮。

## B. 中国同类出口厂家（和至尚的产品更接近）
1. **东莞品创 Pinchuang**（天地盒/礼盒成型机，东莞同城）
   来源：https://www.pinchuangautomation.com/rigid-box-making-machine
   - 结构：页首一段写精度「±0.1 mm accuracy」，接着是机型列表和卖点（视觉定位、胶水控制），然后是 FAQ，FAQ 里写了尺寸范围和售后条款（技术员上门，买家付机票食宿；也可以远程协助），最后是带地址、邮箱、电话的联系区。
   - 我们采用：FAQ 区。海外买家最常问的尺寸范围、售后、培训，都用问答形式写出来。
2. **HEASN LS-1246B**
   来源：https://www.heasn.com.cn/solution/detail153.html
   - 结构：产品页按「GENERAL FEATURES / FEEDING SECTION / GLUING SECTION / VISUAL POSITIONING…」分模块列要点，再写速度「15-25pcs/min」。
   - 我们采用：功能要点按工位或模块分组，不堆成一整段。
3. **Wellmark WM-650AP**（第三方 B2B 目录页）
   来源：https://www.isp.org.cn/pz6f4b7a3-cz5e62a9b-accurate-positioning-gluing-machine-with-multi-functional.html
   - 结构：Alibaba 式属性表，包括 MOQ、Price: Negotiable、Payment Terms: T/T, L/C、Delivery Time、Packaging Details: wooden case、After-sales Service、Glue type。
   - 我们采用：每个机型加一块「贸易信息」表（MOQ、付款方式、交期、包装）。**这些值画册里没有，需要用户提供。**
4. **LiShunyuan LY-RMDJ2702**（在线点胶机，跟至尚的划胶机最像）
   来源：https://box-makingmachine.quality.qualitydress.com/pz7994402-ly-rmdj2702-auto-adhesive-dispensing-machine-up-to-10-30pcs-min.html
   - 描述原文：「used for dispensing inside, bottom and top of mobile phone box, moon cake box and cosmetic gift box. It can draw any shape… cold glue, hot glue」
   - 用词值得注意：英文用的是 **adhesive dispensing machine / glue dispensing**，应用写 rigid box / gift box。
5. **Alibaba 上的点胶/涂胶机**（经 Accio 转载）
   来源：https://www.accio.com/product-alibaba/1600183196876
   - 结构：开店年限「9 yrs」、评分「4.9/5.0 24 reviews」、起订量和价格、Key attributes（Warranty、Voltage、Weight 等）、买家国家列表。
   - 启示：Alibaba 买家习惯先看评分、质保、重量、包装尺寸。至尚画册里多数机型没有重量和包装尺寸，需要补。
6. 另外两家有直接的天地盒类竞品页，供以后比价，这次没有展开分析：XINWEI https://www.sinweimachine.com/ 和 Hongming https://rigidboxesmachine.com/

**关键发现：** 至尚实际卖的是**礼盒、天地盒、皮壳、坑卡这类精品包装用的划胶/点胶设备**（来源：画册 P4–P8），不是瓦楞纸箱封箱线。
上一版网站用的那套关键词，比如 case sealing、corrugated box、tray former，跟至尚的产品对不上。
同类中国厂家常用的英文词是：「rigid box」「gift box」「adhesive dispensing machine」「gluing machine」「hot glue / cold glue」（来源：上面 B1、B4、B5）。

## C. 开源模板（用来参考结构，不直接拿来用）
- AstroFlow（MIT，制造/物流模板，含 Capabilities、Use Cases、Facilities、Request Quote 页）：https://github.com/sudeep2003/AstroFlow
- AstroWind（开源 Astro + Tailwind 通用模板）：https://github.com/arthelokyo/astrowind
- nextjs-automation-website-template（MIT 免费版缺产品详情页、行业区、表单，完整版收费）：https://github.com/themixlyweb/nextjs-automation-website-template
- 之前讨论的克隆工具 JCodesMore/ai-website-cloner-template：只适合参考结构，这次没有运行它。

## D. B2B 制造业网站最佳实践（第三方来源）
- 参数要写成网页上的 HTML 表格，PDF 只作下载补充，因为「PDFs don't rank or get cited well; on-page specs do」：https://atomicdesign.net/learning-center/manufacturing/product-spec-catalog-best-practices/
- 按产品系列建页，一页一张参数表，不要一个 SKU 一页：https://berdisdev.com/blog/manufacturing-company-website/
- 每个产品页都放询价按钮或表单，并预填产品名；表单不超过 5 个字段；写明多久回复：https://www.wecreate.com/insights/manufacturing-websites-that-convert-buyers
- RFQ 检查清单：报价入口离首页不超过两次点击；必填字段 ≤7；能上传附件；写明回复时长；表单旁放电话和邮箱，以及一个信任标志；390px 手机宽度可用：https://factoryinvestigator.com/rfq-friction-index/

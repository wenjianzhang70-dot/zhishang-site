import json
P=lambda s:f'<span class="ph">{s}</span>'
LOGO='<svg viewBox="0 0 40 40"><rect width="40" height="40" rx="6" fill="#0F2A44"/><path d="M10 28 Q20 6 30 28" stroke="#F2A900" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="20" cy="31" r="3" fill="#F2A900"/></svg>'
def mach(kind):
  # neutral generated illustrations
  base='<rect x="40" y="110" width="220" height="16" fill="#5B6B7A"/>'
  if kind==0: art='<rect x="60" y="40" width="70" height="70" rx="4" fill="#1d3d5e"/><rect x="70" y="52" width="30" height="16" fill="#F2A900"/><path d="M130 70 H200 V95" stroke="#F2A900" stroke-width="5" fill="none"/><rect x="190" y="95" width="20" height="10" fill="#0F2A44"/>'
  elif kind==1: art='<rect x="50" y="30" width="200" height="10" fill="#1d3d5e"/><rect x="60" y="30" width="10" height="80" fill="#1d3d5e"/><rect x="230" y="30" width="10" height="80" fill="#1d3d5e"/><rect x="140" y="40" width="24" height="40" fill="#0F2A44"/><path d="M152 80 V98" stroke="#F2A900" stroke-width="4"/><rect x="100" y="98" width="110" height="12" fill="#2c5378"/>'
  else: art='<rect x="40" y="80" width="220" height="30" fill="#1d3d5e"/><path d="M90 80 l20-25 h50 l20 25z" fill="#2c5378"/><rect x="200" y="40" width="30" height="40" fill="#0F2A44"/><path d="M215 80 V70" stroke="#F2A900" stroke-width="4"/><circle cx="60" cy="118" r="7" fill="#0F2A44"/><circle cx="240" cy="118" r="7" fill="#0F2A44"/>'
  return f'<svg viewBox="0 0 300 150" role="img" aria-label="illustration">{art}{base}</svg>'
HERO='<svg viewBox="0 0 480 340" aria-hidden="true"><rect x="20" y="40" width="440" height="270" rx="10" fill="#16365a"/><rect x="40" y="60" width="400" height="16" fill="#24496f"/><rect x="200" y="76" width="60" height="90" rx="4" fill="#24496f"/><rect x="215" y="96" width="30" height="20" fill="#F2A900"/><path d="M230 166 V200" stroke="#F2A900" stroke-width="6"/><circle cx="230" cy="206" r="6" fill="#F2A900"/><rect x="60" y="230" width="360" height="18" fill="#5B6B7A"/><rect x="90" y="208" width="80" height="22" fill="#2c5378"/><rect x="300" y="208" width="80" height="22" fill="#2c5378"/><path d="M300 219 h80" stroke="#F2A900" stroke-width="3" stroke-dasharray="6 5"/><rect x="40" y="270" width="120" height="20" rx="3" fill="#24496f"/></svg>'
I=['<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l8 4v5c0 5-4 8-8 9-4-1-8-4-8-9V7z"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20h16M6 16V9M12 16V5M18 16v-4"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>']
T={
'en':dict(lang='en',ph='[PLACEHOLDER]',title='Glue Dispensing Machine &amp; Hot Melt Gluing Machine Manufacturer | Zhishang Technology',desc='Manufacturer of hot-melt glue machines, automatic dispensing systems and carton gluing equipment for packaging lines. Factory-direct pricing, OEM support, worldwide shipping.',
 co='Zhishang Technology Co., Ltd.',nav=['Products','Specs','Applications','About','Contact'],sw=('中文','zh/'),
 h1='Precision in Every Bead',hp='Gluing &amp; dispensing systems for packaging lines worldwide. Hot melt gluing machines, glue dispensing machines and carton gluing machines built for consistent beads and low glue waste.',
 c1='Request a Quote',c2='View Products',stats=[('[XX]+','Years in business'),('[XX]+','Countries served'),('[XXXX]','Units installed')],
 ph2=('Product Range','Equipment for every gluing step in your packaging line.'),
 kw='Also: hot melt adhesive melter · cold glue applicator · glue spray system · glue pattern controller · case sealing glue system',prods=[('Hot Melt Gluing Machines','Tank melters and glue guns for fast-setting bonds on cartons and cases.',['Tank capacity: [X] L','Melt rate: [X] kg/h','Temperature control ±[X] °C']),
  ('Automatic Glue Dispensing Machines','Programmable XYZ dispensing for beads, dots and patterns with repeatable accuracy.',['Working area: [X × X] mm','Repeatability: ±[X] mm','Visual path teaching']),
  ('Carton Gluing Machines','Inline glue application for folder-gluers, case erectors and box sealing.',['Line speed: up to [X] m/min','Cold glue / hot-melt options','Fits existing conveyors'])],
 sp=('Technical Specifications','Template. Values to be filled from real model data.'),
 th=['Parameter','Model [ZS-XXX]','Model [ZS-XXX]','Model [ZS-XXX]'],
 rows=['Glue type','Tank / reservoir capacity','Melt rate / output','Temperature range','Positioning accuracy','Power supply','Dimensions (L×W×H)','Weight'],
 ap=('Applications','Where our machines are used.'),apps=[('Folding Carton Gluers','Inline glue for folder-gluer lines.'),('Case Erectors','Hot melt for case forming.'),('Corrugated Boxes','Sealing and box forming.'),('Food Packaging','Clean, low-odour application.'),('Beverage Trays','High-speed tray gluing.'),('Paper Bags','Seam and bottom gluing.'),('Pharmaceutical Cartons','Traceable, consistent sealing.'),('E-commerce Box Sealing &amp; Gift Boxes','Mailers and rigid gift boxes.')],
 why=('Why Zhishang','What buyers care about, answered up front.'),whys=[('Fast delivery','Standard models ship in [X] days.'),('Reliable quality','Every machine is run-tested before shipping.'),('Factory-direct pricing','No middlemen, transparent quotes.'),('Engineering support','OEM/ODM customisation and remote commissioning.')],
 fac=('Factory & Certifications','Photos and certificates to be supplied.'),certs=['CE [TBC]','ISO 9001 [TBC]','Factory photo','Workshop photo','Testing photo'],
 cs=('Case Studies','Real customer projects. To be supplied.'),cases=[('[Customer / Country]','[Industry]: [Problem → Solution → Result, e.g. glue usage −X%]')]*3,
 inq=('Request a Quote','Tell us about your product and line. We reply within [24] hours.'),
 f=['Name','Company','Email','Country','Product of interest','Message','Send Inquiry'],fopts=['Hot-melt glue machine','Automatic dispensing system','Carton gluing line','Not sure. Need advice'],
 ct='Contact',ci=[('Address','[Factory address, City, Province, China]'),('Email','[sales@yourdomain.com]'),('Phone / WhatsApp','[+86 XXX XXXX XXXX]'),('Hours','Mon–Sat, 8:30–18:00 (UTC+8)')],
 foot='Zhishang Technology Co., Ltd. [English name to be confirmed]. All rights reserved. Preview draft.'),
'zh':dict(lang='zh-CN',ph='[待替换]',title='至尚科技 | 包装画胶机、点胶机、热熔胶机生产厂家',desc='至尚科技有限公司专业生产热熔胶机、全自动点胶机、纸箱糊盒涂胶设备，工厂直供，支持定制，服务国内外包装企业。',
 co='至尚科技有限公司',nav=['产品中心','技术参数','应用行业','关于我们','联系我们'],sw=('EN','../'),
 h1='每一道胶线，都精准如一',hp='至尚科技 · 包装画胶与点胶设备，服务全球工厂。热熔胶机、全自动点胶机、纸箱涂胶设备，出胶均匀、省胶、易接入现有产线。',
 c1='获取报价',c2='查看产品',stats=[('[XX]+','年行业经验'),('[XX]+','服务国家/地区'),('[XXXX]','台设备装机')],
 ph2=('产品中心','覆盖包装线上每一个涂胶环节。'),
 kw='更多：热熔胶熔胶机 · 冷胶涂胶机 · 喷胶系统 · 胶型控制器 · 封箱涂胶系统',prods=[('热熔胶机','胶箱式熔胶机与胶枪，适合纸箱、彩盒快速粘合。',['胶箱容量：[X] L','熔胶速度：[X] kg/h','控温精度：±[X] °C']),
  ('全自动点胶机','三轴可编程点胶，支持画线、打点、图形轨迹。',['工作范围：[X × X] mm','重复精度：±[X] mm','视觉示教编程']),
  ('纸箱糊盒涂胶设备','用于糊盒机、开箱机、封箱机的在线涂胶。',['线速度：最高 [X] m/min','冷胶/热熔胶可选','兼容现有输送线'])],
 sp=('技术参数','模板，待填入真实机型数据。'),th=['参数','型号 [ZS-XXX]','型号 [ZS-XXX]','型号 [ZS-XXX]'],
 rows=['适用胶水','胶箱/胶桶容量','熔胶量/出胶量','温度范围','定位精度','电源','外形尺寸（长×宽×高）','重量'],
 ap=('应用行业','我们的设备用在这些地方。'),apps=[('糊盒机','折叠纸盒在线涂胶'),('开箱机','纸箱成型热熔胶'),('瓦楞纸箱','封箱、成型'),('食品包装','洁净、低气味涂胶'),('饮料托盘','高速托盘糊盒'),('纸袋','封边、糊底'),('医药纸盒','稳定可追溯的封合'),('电商封箱与礼盒','飞机盒、精品礼盒')],
 why=('为什么选择至尚','采购最关心的问题，先回答清楚。'),whys=[('交期快','标准机型 [X] 天内发货'),('质量稳','每台出厂前通电试机'),('工厂直供','无中间商，报价透明'),('技术支持','OEM/ODM 定制、远程调试')],
 fac=('工厂与资质','工厂照片和证书待提供。'),certs=['CE [待确认]','ISO 9001 [待确认]','厂房照片','车间照片','检测照片'],
 cs=('客户案例','真实客户项目，待提供。'),cases=[('[客户名 / 地区]','[行业]：[问题 → 方案 → 效果，如省胶 X%]')]*3,
 inq=('在线询价','告诉我们您的产品和产线情况，[24] 小时内回复。'),
 f=['姓名','公司','邮箱','国家/地区','感兴趣的产品','需求描述','提交询价'],fopts=['热熔胶机','全自动点胶机','纸箱糊盒涂胶设备','不确定，需要建议'],
 ct='联系我们',ci=[('地址','[工厂地址，省市区]'),('邮箱','[sales@yourdomain.com]'),('电话 / 微信','[+86 XXX XXXX XXXX]'),('工作时间','周一至周六 8:30–18:00')],
 foot='至尚科技有限公司 版权所有 · 预览草稿 · [ICP 备案号待办理]')}
URL='https://wenjianzhang70-dot.github.io/zhishang-site/'
def page(k,css,href):
  t=T[k];ph=P(t['ph'])
  ids=['products','specs','applications','about','contact']
  nav=''.join(f'<a href="#{i}">{n}</a>' for i,n in zip(ids,t['nav']))
  prods=''.join(f'<article class="card">{mach(i)}<h3>{a}</h3><p>{b}</p><ul>{"".join(f"<li>{x}</li>" for x in c)}</ul></article>' for i,(a,b,c) in enumerate(t['prods']))
  rows=''.join(f'<tr><td>{r}</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>' for r in t['rows'])
  apps=''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in t['apps'])
  whys=''.join(f'<div class="card">{I[i]}<h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(t['whys']))
  certs=''.join(f'<div>{c}</div>' for c in t['certs'])
  cases=''.join(f'<div class="card">{mach(i)}<h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(t['cases']))
  f=t['f'];opts=''.join(f'<option>{o}</option>' for o in t['fopts'])
  ci=''.join(f'<p><b>{a}</b><br>{b}</p>' for a,b in t['ci'])
  ld={"@context":"https://schema.org","@type":"Organization","name":t['co'],"url":URL,"description":t['desc']}
  return f'''<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title><meta name="description" content="{t['desc']}">
<link rel="canonical" href="{URL}{'' if k=='en' else 'zh/'}"><link rel="alternate" hreflang="en" href="{URL}"><link rel="alternate" hreflang="zh-CN" href="{URL}zh/">
<meta property="og:title" content="{t['title']}"><meta property="og:description" content="{t['desc']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@600;700&family=Inter:wght@400;600&family=IBM+Plex+Mono&family=Noto+Sans+SC:wght@400;700&display=swap"><link rel="stylesheet" href="{css}"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><div class="wrap"><a class="logo" href="#">{LOGO}<span>{t['co']} {ph}</span></a><nav>{nav}</nav><a class="lang" href="{t['sw'][1]}">{t['sw'][0]}</a></div></header>
<main>
<section class="hero"><div class="wrap"><div><h1>{t['h1']}</h1><svg class="bead" viewBox="0 0 520 14" aria-hidden="true"><path d="M4 7 C80 2 140 12 220 7 S380 2 516 7"/></svg><p>{t['hp']}</p><div class="cta"><a class="btn" href="#quote">{t['c1']}</a><a class="btn ghost" href="#products">{t['c2']}</a></div>
<div class="stats">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a,b in t['stats'])}</div></div>{HERO}</div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="products"><div class="wrap"><h2>{t['ph2'][0]}</h2><p class="sub">{t['ph2'][1]} {ph}</p><div class="grid g3">{prods}</div><p class="kw">{t['kw']}</p></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="specs" class="alt"><div class="wrap"><h2>{t['sp'][0]}</h2><p class="sub">{t['sp'][1]} {ph}</p><div class="tbl"><table><thead><tr>{"".join(f"<th>{h}</th>" for h in t['th'])}</tr></thead><tbody>{rows}</tbody></table></div></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="applications"><div class="wrap"><h2>{t['ap'][0]}</h2><p class="sub">{t['ap'][1]}</p><div class="grid g4">{apps}</div></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="about" class="alt"><div class="wrap"><h2>{t['why'][0]}</h2><p class="sub">{t['why'][1]} {ph}</p><div class="grid g4">{whys}</div>
<h2 style="margin-top:56px">{t['fac'][0]}</h2><p class="sub">{t['fac'][1]} {ph}</p><div class="cert">{certs}</div></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="cases"><div class="wrap"><h2>{t['cs'][0]}</h2><p class="sub">{t['cs'][1]} {ph}</p><div class="grid g3">{cases}</div></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="contact" class="alt"><div class="wrap contact"><div id="quote"><h2>{t['inq'][0]}</h2><p class="sub">{t['inq'][1]}</p>
<form action="mailto:sales@example.com" method="post" enctype="text/plain"><div><label>{f[0]}</label><input name="name" required></div><div><label>{f[1]}</label><input name="company"></div>
<div><label>{f[2]}</label><input type="email" name="email" required></div><div><label>{f[3]}</label><input name="country"></div>
<div class="full"><label>{f[4]}</label><select name="product">{opts}</select></div><div class="full"><label>{f[5]}</label><textarea name="message"></textarea></div>
<div class="full"><button class="btn" type="submit">{f[6]}</button> {P(t['ph']+' mailto / form backend')}</div></form></div>
<div><h2>{t['ct']}</h2>{ci}</div></div></section></main>
<footer><div class="wrap">© 2026 {t['foot']}</div></footer></body></html>'''
open('index.html','w').write(page('en','assets/style.css',''))
open('zh/index.html','w').write(page('zh','../assets/style.css',''))
open('sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}</loc></url><url><loc>{URL}zh/</loc></url></urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n')

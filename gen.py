import json
P=lambda s:f'<span class="ph">{s}</span>'
LOGO='<svg viewBox="0 0 40 40"><rect width="40" height="40" rx="6" fill="#0F2A44"/><path d="M10 28 Q20 6 30 28" stroke="#F2A900" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="20" cy="31" r="3" fill="#F2A900"/></svg>'
def mach(kind):
  ys=[(40,95),(60,110),(30,80)][kind%3]
  return f'<svg viewBox="0 0 300 150" role="img" aria-label="placeholder image"><rect width="300" height="150" fill="#0F2A44"/><path d="M20 {ys[0]} C90 {ys[0]-20} 160 {ys[0]+25} 280 {ys[0]}" stroke="#F2A900" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M20 {ys[1]} C100 {ys[1]+15} 200 {ys[1]-15} 280 {ys[1]}" stroke="#F2A900" stroke-opacity=".45" stroke-width="2" fill="none" stroke-dasharray="2 8" stroke-linecap="round"/><text x="150" y="140" fill="#5B6B7A" font-size="11" text-anchor="middle" font-family="sans-serif">PHOTO PLACEHOLDER</text></svg>' 
HERO='''<svg class="carton" viewBox="0 0 480 340" role="img" aria-label="Illustration of a corrugated carton with a glue bead on the closing flap"><defs><pattern id="flute" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 4 Q2 0 4 4 T8 4" stroke="#8c6232" stroke-width="1" fill="none"/></pattern></defs><polygon points="70,150 300,150 410,110 180,110" fill="#d9a86a"/><polygon points="70,150 300,150 300,320 70,320" fill="#c4904f"/><polygon points="300,150 410,110 410,280 300,320" fill="#b07d40"/><rect x="70" y="150" width="230" height="6" fill="url(#flute)"/><polygon points="180,110 410,110 440,45 210,45" fill="#e2b77c"/><line x1="180" y1="110" x2="410" y2="110" stroke="#8c6232" stroke-width="2"/><rect x="120" y="220" width="120" height="40" fill="none" stroke="#8c6232" stroke-width="2" stroke-dasharray="4 4" opacity=".6"/><path class="beadline" d="M190 104 L402 104"/><g transform="translate(402 20)"><rect x="-14" y="-16" width="28" height="44" rx="3" fill="#24496f"/><rect x="-4" y="28" width="8" height="40" fill="#5B6B7A"/></g></svg>'''
ICO=['<path d="M6 14 H42 V40 H6 Z M6 14 L14 6 H50 L42 14 M42 40 L50 32 V6"/><path d="M6 21 Q10 18 14 21 T22 21 T30 21 T38 21"/>', '<path d="M10 12 H38 V42 H10 Z M10 12 L16 4 H44 L38 12 M38 42 L44 34 V4 M16 4 L22 12"/>', '<path d="M6 20 H42 V42 H6 Z M4 14 H44 V20 H4 Z M24 14 V42 M24 14 C18 4 12 10 24 14 C36 10 30 4 24 14"/>', '<path d="M12 14 H36 L40 44 H8 Z M18 14 C18 4 30 4 30 14"/>', '<path d="M4 26 H44 V40 H4 Z"/><circle cx="12" cy="20" r="6"/><circle cx="24" cy="20" r="6"/><circle cx="36" cy="20" r="6"/>', '<path d="M10 16 H38 V44 H10 Z M10 16 L24 6 L38 16 M16 28 H32 M16 34 H28"/>', '<path d="M4 18 L24 10 L44 18 V38 L24 46 L4 38 Z M4 18 L24 26 L44 18 M24 26 V46"/>', '<rect x="16" y="8" width="16" height="36" rx="2"/><path d="M16 16 H32"/><circle cx="24" cy="30" r="4"/>']
I=['<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l8 4v5c0 5-4 8-8 9-4-1-8-4-8-9V7z"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20h16M6 16V9M12 16V5M18 16v-4"/></svg>','<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>']
T={
'en':dict(lang='en',ph='[PLACEHOLDER]',title='Packaging Gluing Machine &amp; Folding Carton Glue Systems | Zhishang',desc='Packaging gluing machines: carton gluing machines, folding carton gluer glue systems, case sealing hot melt systems and glue dispensing machines for packaging. Factory direct.',
 co='Zhishang Technology Co., Ltd.',nav=['Products','Specs','Applications','About','Contact'],sw=('中文','zh/'),
 h1='Precision in Every Bead',hp='Gluing &amp; dispensing systems for packaging lines worldwide. Hot melt gluing machines, glue dispensing machines and carton gluing machines built for consistent beads and low glue waste.',
 c1='Request a Quote',c2='View Products',stats=[('[XX]+','Years in business'),('[XX]+','Countries served'),('[XXXX]','Units installed')],bar=[('Up to [X] m/min','Line speed'),('[X]%','Glue saving'),('[TBC]','Compatible folder-gluer / case-sealer brands')],
 ph2=('Product Range','Equipment for every gluing step in your packaging line.'),
 kw='Related: packaging gluing machine · box gluing machine · hot melt glue applicator · glue detection system for folding carton · rigid box gluing machine · paper bag gluing machine · cold glue system for folding carton',prods=[('Hot Melt Glue Systems for Packaging','Hot melt melters for packaging lines with applicators, incl. case sealing hot melt systems.',['Tank capacity: [X] L','Melt rate: [X] kg/h','Temperature control ±[X] °C']),
  ('Glue Dispensing Machines for Packaging','Programmable XYZ dispensing for beads, dots and patterns with repeatable accuracy.',['Working area: [X × X] mm','Repeatability: ±[X] mm','Visual path teaching']),
  ('Carton Gluing Machines','Folding carton gluer glue systems (hot melt or cold glue) for folder-gluers and box sealing.',['Line speed: up to [X] m/min','Cold glue / hot-melt options','Fits existing conveyors'])],
 sp=('Technical Specifications','Template. Values to be filled from real model data.'),
 th=['Parameter','Model [ZS-XXX]','Model [ZS-XXX]','Model [ZS-XXX]'],
 rows=['Glue type','Tank / reservoir capacity','Melt rate / output','Temperature range','Positioning accuracy','Power supply','Dimensions (L×W×H)','Weight'],
 ap=('Applications','Where our machines are used.'),apps=[('Corrugated Box Gluing','Case erector glue system and tray former glue system for shipping cases.'),('Folding Carton Gluing','Folding carton (color box) gluing on folder-gluers, incl. window patching glue.'),('Gift Box &amp; Rigid Box','Rigid box wrapping, lining and corner gluing.'),('Paper Bag Bottom Gluing','Seam and bottom gluing on paper bag lines.'),('Beverage Tray &amp; Tray Former','Hot melt for wrap-around trays and tray formers.'),('Food / Beverage Carton Gluing','Clean, low-odour sealing, incl. pizza box.'),('E-commerce Carton Sealing','High-speed mailer and shipping box sealing.'),('Cosmetic Box','Precise beads on small premium folding cartons.')],
 why=('Why Zhishang','What buyers care about, answered up front.'),whys=[('Fast delivery','Standard models ship in [X] days.'),('Reliable quality','Every machine is run-tested before shipping.'),('Factory-direct pricing','No middlemen, transparent quotes.'),('Engineering support','OEM/ODM customisation and remote commissioning.')],
 fac=('Factory & Certifications','Photos and certificates to be supplied.'),certs=['CE [TBC]','ISO 9001 [TBC]','Factory photo','Workshop photo','Testing photo'],
 cs=('Case Studies','Real customer projects. To be supplied.'),cases=[('[Customer / Country]','[Industry]: [Problem → Solution → Result, e.g. glue usage −X%]')]*3,
 inq=('Request a Quote','Tell us about your product and line. We reply within [24] hours.'),
 f=['Name','Company','Email','Country','Product of interest','Message','Send Inquiry'],fopts=['Hot-melt glue machine','Automatic dispensing system','Carton gluing line','Not sure. Need advice'],
 ct='Contact',ci=[('Address','[Factory address, City, Province, China]'),('Email','[sales@yourdomain.com]'),('Phone / WhatsApp','[+86 XXX XXXX XXXX]'),('Hours','Mon–Sat, 8:30–18:00 (UTC+8)')],
 foot='Zhishang Technology Co., Ltd. [English name to be confirmed]. All rights reserved. Preview draft.'),
'zh':dict(lang='zh-CN',ph='[待替换]',title='至尚科技 | 包装涂胶机、糊盒机胶系统、热熔胶机、点胶机厂家',desc='至尚科技有限公司专业生产热熔胶机、全自动点胶机、纸箱糊盒涂胶设备，工厂直供，支持定制，服务国内外包装企业。',
 co='至尚科技有限公司',nav=['产品中心','技术参数','应用行业','关于我们','联系我们'],sw=('EN','../'),
 h1='每一道胶线，都精准如一',hp='至尚科技 · 包装画胶与点胶设备，服务全球工厂。热熔胶机、全自动点胶机、纸箱涂胶设备，出胶均匀、省胶、易接入现有产线。',
 c1='获取报价',c2='查看产品',stats=[('[XX]+','年行业经验'),('[XX]+','服务国家/地区'),('[XXXX]','台设备装机')],bar=[('最高 [X] m/min','线速度'),('[X]%','省胶'),('[待确认]','兼容糊盒机/封箱机品牌')],
 ph2=('产品中心','覆盖包装线上每一个涂胶环节。'),
 kw='更多：包装涂胶机 · 糊盒机冷胶系统 · 热熔胶枪 · 彩盒胶线检测系统 · 精品盒涂胶机 · 纸袋涂胶机',prods=[('热熔胶机','胶箱式熔胶机与胶枪，适合纸箱、彩盒快速粘合。',['胶箱容量：[X] L','熔胶速度：[X] kg/h','控温精度：±[X] °C']),
  ('全自动点胶机','三轴可编程点胶，支持画线、打点、图形轨迹。',['工作范围：[X × X] mm','重复精度：±[X] mm','视觉示教编程']),
  ('纸箱糊盒涂胶设备','用于糊盒机、开箱机、封箱机的在线涂胶。',['线速度：最高 [X] m/min','冷胶/热熔胶可选','兼容现有输送线'])],
 sp=('技术参数','模板，待填入真实机型数据。'),th=['参数','型号 [ZS-XXX]','型号 [ZS-XXX]','型号 [ZS-XXX]'],
 rows=['适用胶水','胶箱/胶桶容量','熔胶量/出胶量','温度范围','定位精度','电源','外形尺寸（长×宽×高）','重量'],
 ap=('应用行业','我们的设备用在这些地方。'),apps=[('瓦楞纸箱涂胶','开箱机、托盘成型机热熔胶系统'),('彩盒糊盒涂胶','糊盒机涂胶、开窗贴膜胶'),('礼盒 / 精品盒','裱糊、包边、贴角'),('纸袋糊底','纸袋封边、糊底'),('饮料托盘','裹包托盘、托盘成型'),('食品/饮料纸盒','洁净低气味封合，含披萨盒'),('电商封箱','飞机盒、快递箱高速封箱'),('化妆品盒','小型精品彩盒精准胶线')],
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
  apps=''.join(f'<div class="card app"><svg class="boxico" viewBox="0 0 48 48" aria-hidden="true">{ICO[i]}</svg><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(t['apps']))
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
<div class="stats">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a,b in t['stats'])}</div></div>{HERO}</div></section><div class="statbar"><div class="wrap">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a,b in t['bar'])}</div></div>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="applications"><div class="wrap"><h2>{t['ap'][0]}</h2><p class="sub">{t['ap'][1]}</p><div class="grid g4">{apps}</div></div></section><div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="products"><div class="wrap"><h2>{t['ph2'][0]}</h2><p class="sub">{t['ph2'][1]} {ph}</p><div class="grid g3">{prods}</div><p class="kw">{t['kw']}</p></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div><section id="specs" class="alt"><div class="wrap"><h2>{t['sp'][0]}</h2><p class="sub">{t['sp'][1]} {ph}</p><div class="tbl"><table><thead><tr>{"".join(f"<th>{h}</th>" for h in t['th'])}</tr></thead><tbody>{rows}</tbody></table></div></div></section>
<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div>
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
open('index.html','w').write(page('en','assets/style.css?v=3',''))
open('zh/index.html','w').write(page('zh','../assets/style.css?v=3',''))
open('sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}</loc></url><url><loc>{URL}zh/</loc></url></urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n')

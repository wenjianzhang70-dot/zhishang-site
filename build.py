import os,json,html,shutil
BASE='/';URL='https://zhishangkj.com/'
F3=('机器可以根据划胶需求进行任意位置摆放','The machine can be placed at any position according to gluing requirements.')
F5=('全新升级控制系统，速度更快，性能更稳定','Fully upgraded control system: faster speed, more stable performance.')
FL2=('划胶尺寸大，划胶产品通用性强，灵活性高，操作简便','Large gluing size, strong versatility across glued products, high flexibility and easy operation.')
COLD=('可以划白胶、黄胶、万能胶，可以划盒子底部、侧面和盒子平面侧面同时划','Applies white glue, yellow glue and universal glue; can glue the bottom, sides and flat faces of a box at the same time.')
HOT=('可以划热熔胶，压敏胶，可以划盒子底部、侧面和盒子平面侧面同时划','Applies hot melt and pressure-sensitive adhesive; can glue the bottom, sides and flat faces of a box at the same time.')
INL1=('适用于盒子类产品进行连线作业，一台机节省两个人划胶','Suited to inline operation on box products; one machine saves two people on manual gluing.')
INL2=('可以配手工流水线，也可以搭配自动天地盒机连线作业','Works with manual assembly lines, or inline with automatic lid-and-base box machines.')
SMALL=('适用于小尺寸盒子、皮壳、首饰盒，奢侈品盒，代妆品盒，坑卡类产品进行划胶','Suited to small boxes, cases, jewelry boxes, luxury boxes, cosmetic boxes and recessed card insert products.')
FLATC=('可以划白胶、黄胶、万能胶，可以划盒子底部、皮壳，坑卡盒类平面划胶','Applies white glue, yellow glue and universal glue to box bottoms, cases and flat recessed card insert surfaces.')
LC=('适用于大尺寸皮壳、坑卡类产品进行划胶','Suited to large cases and recessed card insert products.')
def M(slug,model,zh,en,cat,img,dims,size,speed,power,width,features,ph=1):
  return dict(slug=slug,model=model,zh=zh,en=en,cat=cat,img=img,dims=dims,size=size,speed=speed,power=power,width=width,volt='220V/AC——50Hz',air='0.6MPa',features=features,page=ph)
MACH=[
 M('zs-s088e-4','ZS-S088E-4','随线四轴划胶机-冷胶','Inline Four-Axis Gluing Machine – Cold Glue','inline','s088e-4','1600*1080*1550MM','600*600*130MM/50*50*25MM','1.2M/S','2300W','3-10MM',[INL1,INL2,F3,COLD,F5],'P4 p05'),
 M('zs-s088r-4','ZS-S088R-4','随线四轴划胶机-热胶','Inline Four-Axis Gluing Machine – Hot Glue','inline','s088r-4','1600*1080*1550MM','600*600*130MM/50*50*25MM','1.2M/S','5300W','3-10MM',[INL1,INL2,F3,HOT,F5],'P4 p06'),
 M('zs-s088c','ZS-S088C','四轴柜式划胶机-冷胶','Four-Axis Cabinet Gluing Machine – Cold Glue','cabinet','s088c','1330*1090*1600MM','900*600*150MM/50*50*10MM','1.2M/S','2300W','3-10MM',[('适用于大尺寸盒子、折叠盒，书型盒，皮壳、坑卡类产品进行划胶','Suited to large boxes, folding boxes, book-style boxes, cases and recessed card insert products.'),FL2,F3,COLD,F5],'P5 p07'),
 M('zs-s088c-4','ZS-S088C-4','四轴柜式划胶机-热胶','Four-Axis Cabinet Gluing Machine – Hot Glue','cabinet','s088c-4','1330*1090*1600MM','900*600*150MM/50*50*10MM','1.2M/S','5300W','3-10MM',[('适用于大尺寸盒子、皮壳、坑卡类产品进行划胶，刮胶，替代双面胶','Suited to large boxes, cases and recessed card insert products; gluing and glue scraping as a replacement for double-sided tape.'),FL2,F3,HOT,F5],'P5 p08'),
 M('zs-s088d','ZS-S088D','三轴柜式划胶机-冷胶','Three-Axis Cabinet Gluing Machine – Cold Glue','cabinet','s088d','1330*1090*1600MM','900*600MM/50*50MM','1.2M/S','2000W','3-10MM',[('适用于大尺寸皮壳、坑卡类产品进行划胶，划胶精度高，一台机替代2人','Suited to large cases and recessed card insert products; high gluing precision; one machine replaces 2 workers.'),FL2,F3,FLATC,F5],'P6 p09'),
 M('zs-s088d-4','ZS-S088D-4','三轴柜式划胶机-热胶','Three-Axis Cabinet Gluing Machine – Hot Glue','cabinet','s088d-4','1330*1090*1500MM','900*600MM/50*50MM','1.2M/S','4000W','3-10MM',[LC,FL2,F3,('可以刮热胶，替代双面胶，节省撕离型纸的人工和时间','Scrapes hot glue to replace double-sided tape, saving the labor and time of peeling release paper.'),F5],'P6 p10'),
 M('zs-s088b','ZS-S088B /ZS-S088B-2','四轴双工位划胶机(标准/加大)','Four-Axis Dual-Station Glue Dispensing Machine (Standard / Large)','dual','s088b','890*840*1590MM / 1140*890*1590MM','480*300*2*130MM / 540*420*2*130MM','0.9M/S','1400W','3-10MM',[SMALL,FL2,F3,COLD,F5],'P7 p11'),
 M('zs-s088a','ZS-S088A /ZS-S088A-2','三轴双工位划胶机(标准/加大)','Three-Axis Dual-Station Glue Dispensing Machine (Standard / Large)','dual','s088a','890*840*1350MM / 1140*890*1350MM','450*300*2*150MM / 500*420*2*150MM','0.9M/S','1400W','3-10MM',[LC,FL2,F3,FLATC,F5],'P7 p12'),
 M('zs-s088a-r','ZS-S088A-R /ZS-S088A-2-R','三轴双工位划胶机-热胶(标准/加大)','Three-Axis Dual-Station Glue Dispensing Machine – Hot Glue (Standard / Large)','dual','s088a-r','890*840*1590MM / 1140*890*1590MM','480*300*2*130MM / 540*420*2*130MM','0.9M/S','1400W','3-10MM',[SMALL,FL2,F3,HOT,F5],'P8 p13'),
 M('zs-s088p','ZS-S088P','三轴喷胶机','Three-Axis Glue Spraying Machine','spray','s088p','1400*1100*1500MM','880*520*130MM / 50*50*1MM','1M/S','1400W','3-20MM',[('适用于平面喷胶类产品，主要用于皮盒面料类喷胶','For flat glue-spraying work, mainly spraying adhesive on leather-box covering materials.'),('喷胶均匀，减少胶水浪费，提升喷涂效率','Even spraying, less glue waste, higher spraying efficiency.'),F3,('可以喷白乳胶、万能胶喷胶类胶水','Sprays white latex glue, universal glue and other sprayable adhesives.'),F5],'P8 p14'),
 M('zs-yh4040','ZS-YH4040','随线压泡机','Inline Bubble Press Machine','press','yh4040','1500*1500*1500MM','400*400*120MM / 60*60*30MM','20pcs/minute','1200W',None,[('适用于压底部，压吸塑，压纸托，适用于手机盒，平板盒，香水盒等','Presses box bottoms, blister inserts and paper trays; for phone boxes, tablet boxes, perfume boxes and more.'),('可以一次压一个或者两个，模式可以切换，提升效率','Presses one or two at a time with switchable modes for higher efficiency.'),F3,('单头可以压100-1200个，双头可以压2000-2400','Single head can press 100-1200 pieces; double head can press 2000-2400 pieces.')],'P9 p16'),
]
CS=dict(slug='cs4539',model='CS4539',zh='半自动小皮壳机',en='Semi-Automatic Small Case Making Machine',cat='case',img='cs4539',page='P9 p15',rows=[
 ('设备型号','Device model','半自动小皮壳机 CS4539'),('成型时间','Forming time','约1.2秒/个'),('最大成型尺寸','Maximum molding size','450-390mm'),('最小成型尺寸','Minimum molding size','35mm-35mm'),('纸板厚度','Cardboard thickness','0.8*20mm'),('工作速度','Working speed','15-34个/分钟'),('面纸厚度','Paper thickness','70-300g'),('电源','Power supply','220V/50ZH'),('气压','Air pressure','0.6-0.8Mpa'),('整机功率','Total machine power','1KW'),('出口木架尺寸','Export wooden crate size','长1450*宽1000*高1850mm'),('机器重量','Total weight','约490KG'),('外形尺寸','Overall dimensions','长1400*宽950*高1700mm')])
NS=[('ZS-FB-001','酒盒装板机','Wine Box Board Assembly Machine (custom)','fb-001','P10 p17'),('ZS-FB-002','自动折内托机露','Automatic Paper Tray / Insert Folding Machine',None,'P10 p18')]
CATS={'inline':('随线划胶机','Inline Gluing Machines'),'cabinet':('柜式划胶机','Cabinet Gluing Machines'),'dual':('双工位划胶机','Dual-Station Glue Dispensing Machines'),'spray':('喷胶机','Glue Spraying Machine'),'press':('压泡机','Bubble Press Machine'),'case':('皮壳机','Case Making Machine'),'ns':('非标定制','Custom (Non-Standard) Machines')}
EM='362804136@qq.com';TEL='0769 22250346'
ADDR=('东莞市东城街道环城东路东城段 42号','No. 42, Dongcheng Section, Huancheng East Road, Dongcheng Subdistrict, Dongguan, Guangdong, China')
L={'en':dict(lang='en',pre='',other='zh/',sw='中文',co='Dongguan Zhishang Automation Technology Co., Ltd',brand='Zhishang Technology',tag='Focused on gluing equipment',
 nav=[('products/','Products'),('applications/','Applications'),('about/','About'),('service/','Service'),('contact/','Contact')],quote='Request a Quote',ask='Ask about this machine',
 h1='Gluing & Glue Dispensing Machines for Rigid Boxes',hp='Inline, cabinet and dual-station gluing machines for rigid boxes, lid-and-base boxes, book-style boxes, cases and greyboard. Cold glue and hot melt models, plus glue spraying and bubble pressing.',
 spec='Technical Parameters',feat='Features',src='Data from the Zhishang product brochure.',view='View details',allp='All products',
 lab=['Model','Machine name','Overall size (L/W/H)','Effective size','Working speed','Rated power','Glue line width','Voltage','Air pressure']),
 'zh':dict(lang='zh-CN',pre='zh/',other='',sw='EN',co='东莞市至尚自动化科技有限公司',brand='至尚科技',tag='专注划胶设备行业',
 nav=[('products/','产品中心'),('applications/','应用领域'),('about/','关于我们'),('service/','服务承诺'),('contact/','联系我们')],quote='在线询价',ask='咨询这台机器',
 h1='专注划胶设备行业',hp='随线、柜式、双工位划胶机，适用于天地盒、书型盒、皮壳、坑卡等精品包装；冷胶、热胶机型齐全，另有喷胶机、压泡机。',
 spec='技术参数',feat='功能特点',src='数据来源：至尚产品画册。',view='查看详情',allp='全部产品',
 lab=['机器型号','机器名称','外观尺寸 (L/W/H)','有效尺寸','工作速度','额定功率','划胶宽度','适用电压','气压'])}
LOGO='<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="6" fill="#0F2A44"/><path d="M10 28 Q20 6 30 28" stroke="#F2A900" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="20" cy="31" r="3" fill="#F2A900"/></svg>'
BEAD='<svg class="bead" viewBox="0 0 520 14" aria-hidden="true"><path d="M4 7 C80 2 140 12 220 7 S380 2 516 7"/></svg>'
DIV='<div class="divider" aria-hidden="true"><svg viewBox="0 0 180 14"><path d="M3 7 C40 3 80 11 120 7 S160 4 177 7"/></svg></div>'
e=html.escape
def page(lg,path,title,desc,body):
  t=L[lg];here=t['pre']+path;alt=L['zh' if lg=='en' else 'en']['pre']+path
  nav=''.join(f'<a href="{BASE}{t["pre"]}{h}">{n}</a>' for h,n in t['nav'])
  zhfont='' if lg=='en' else ' class="zh"'
  return f'''<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{URL}{here}"><link rel="alternate" hreflang="en" href="{URL}{'' if lg=='en' else ''}{path if lg=='en' else alt}"><link rel="alternate" hreflang="zh-CN" href="{URL}{'zh/'+path if lg=='en' else here}">
<link rel="icon" href="{BASE}favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="{BASE}img/favicon-32.png"><link rel="apple-touch-icon" href="{BASE}img/favicon-180.png"><script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Organization","name":t['co'],"alternateName":"至尚科技 ZHI SHANG TECHNOLOGY","url":URL+t['pre'],"logo":URL+"img/logo.png","email":EM,"telephone":"+86 769 22250346"},ensure_ascii=False)}</script><link rel="stylesheet" href="{BASE}assets/fonts.css"><link rel="stylesheet" href="{BASE}assets/site.css?v=15"></head><body{zhfont}>
<header><div class="wrap"><a class="logo" href="{BASE}{t['pre']}"><img src="{BASE}img/logo-120h.png" width="240" height="62" alt="{'至尚科技 ZHI SHANG TECHNOLOGY'}"></a><button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="mnav" onclick="var o=document.body.classList.toggle('navopen');this.setAttribute('aria-expanded',o)"><span></span><span></span><span></span></button><nav id="mnav">{nav}<a class="navq" href="{BASE}{t['pre']}contact/#quote">{t['quote']}</a></nav><a class="btn sm" href="{BASE}{t['pre']}contact/">{t['quote']}</a><a class="lang" href="{BASE}{alt}">{t['sw']}</a></div></header>
<main>{body}</main>
<template id="hold-float-contact"><aside class="fcontact"><a href="#">WhatsApp</a><a href="mailto:{EM}">Email</a><a href="#">WeChat</a></aside></template>
<template id="hold-video"><section class="vslot"><div class="wrap"><video controls preload="none" playsinline poster=""><source src="" type="video/mp4"></video></div></section></template>
<template id="hold-dark-hero"><section class="hero dark"><div class="wrap"><div><h1></h1></div></div></section></template>
<script>(function(){{var a=document.getElementById('askcta'),b=document.getElementById('pbar');if(a&&b&&'IntersectionObserver' in window){{new IntersectionObserver(function(es){{var v=!es[0].isIntersecting&&es[0].boundingClientRect.top<0;b.hidden=!v;document.body.style.paddingBottom=v?b.offsetHeight+'px':''}}).observe(a)}}else if(b){{b.hidden=false;document.body.style.paddingBottom=b.offsetHeight+'px'}}}})();(function(){{if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window))return;document.documentElement.classList.add('mo');var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target)}}}})}},{{rootMargin:'0px 0px -8% 0px'}});document.querySelectorAll('main section h2,.pcard,.card,.entry,.bead,.glue').forEach(function(el){{el.classList.add('rv');io.observe(el)}})}})()</script><a class="mcta" href="{BASE}{t['pre']}contact/#quote">{t['quote']}</a>
<footer><div class="wrap fgrid"><div><span class="flogo"><img src="{BASE}img/logo-120h.png" width="186" height="48" alt="至尚科技 ZHI SHANG TECHNOLOGY" loading="lazy"></span><br><b>{t['co']}</b><br>{ADDR[0] if lg=='zh' else ADDR[1]}<br>{'电话/传真' if lg=='zh' else 'Tel/Fax'}: {TEL} · <a href="mailto:{EM}">{EM}</a></div><div class="small">© 2026 {t['co']}</div></div></footer></body></html>'''
import re as _re
from PIL import Image as _I
_SZ={}
def _pic(m):
  tag=m.group(0);name=m.group(1)
  if name not in _SZ: _SZ[name]=_I.open('img/'+name+'.jpg').size
  w,h=_SZ[name];eager='data-eager' in tag
  tag=tag.replace(' data-eager','').replace(' loading="lazy"','').replace(' loading=lazy','')
  tag=tag[:-1]+f' width="{w}" height="{h}" decoding="async"'+(' fetchpriority="high"' if eager else ' loading="lazy"')+'>'
  return f'<picture><source srcset="{BASE}img/{name}.webp" type="image/webp">{tag}</picture>'
def W(lg,path,html_):
  html_=_re.sub(r'<img src="'+BASE+r'img/([\w-]+)\.jpg"[^>]*>',_pic,html_)
  d=os.path.join(L[lg]['pre'],path);os.makedirs(d or '.',exist_ok=True);open(os.path.join(d,'index.html'),'w').write(html_)
def nm(m,lg): return m['zh'] if lg=='zh' else m['en']
def card(m,lg):
  t=L[lg];k=[(t['lab'][4],m['speed']),(t['lab'][6],m['width'])] if m.get('width') else [(t['lab'][4],m.get('speed','')),]
  ks=''.join(f'<li><span>{a}</span><code>{b}</code></li>' for a,b in k)
  return f'<a class="pcard" href="{BASE}{t["pre"]}products/{m["slug"]}/"><img src="{BASE}img/{m["img"]}.jpg" alt="{e(nm(m,lg))} {m["model"]}" loading="lazy"><div><small>{m["model"]}</small><h3>{nm(m,lg)}</h3><ul class="keys">{ks}</ul><span class="more">{t["view"]} →</span></div></a>'
APPS={'en':[('Rigid / gift boxes','Lid-and-base and gift boxes; inline with automatic lid-and-base box machines.','ZS-S088E-4, ZS-S088R-4'),('Lid-and-base boxes','Bottom, side and flat-face gluing in one pass.','ZS-S088E-4, ZS-S088R-4, ZS-S088C'),('Book-style & folding boxes','Large-format boxes on the four-axis cabinet machine.','ZS-S088C'),('Cases & leather covers','Large and small cases; hot glue scraping to replace double-sided tape.','ZS-S088D, ZS-S088D-4, CS4539'),('Recessed card inserts','Flat glue lines on recessed card insert products.','ZS-S088A, ZS-S088D'),('Jewelry, luxury & cosmetic boxes','Small boxes on dual-station machines.','ZS-S088B, ZS-S088A-R'),('Phone, tablet & perfume boxes','Pressing bottoms, blister and paper trays.','ZS-YH4040'),('Leather-box covering materials','Even glue spraying with less waste.','ZS-S088P')],
'zh':[('礼盒 / 精品盒','天地盒、礼盒；可搭配自动天地盒机连线','ZS-S088E-4、ZS-S088R-4'),('天地盒','盒子底部、侧面和平面侧面同时划','ZS-S088E-4、ZS-S088R-4、ZS-S088C'),('书型盒 / 折叠盒','大尺寸盒子，四轴柜式机','ZS-S088C'),('皮壳','大小皮壳；刮热胶替代双面胶','ZS-S088D、ZS-S088D-4、CS4539'),('坑卡','坑卡盒类平面划胶','ZS-S088A、ZS-S088D'),('首饰盒、奢侈品盒、化妆品盒','小尺寸盒子，双工位机','ZS-S088B、ZS-S088A-R'),('手机盒、平板盒、香水盒','压底部、压吸塑、压纸托','ZS-YH4040'),('皮盒面料喷胶','喷胶均匀，减少胶水浪费','ZS-S088P')]}
ENT={'zs-s088e-4': 'Inline 4-Axis Cold Glue Dispensing Machine for Rigid Boxes', 'zs-s088r-4': 'Inline 4-Axis Hot Melt Gluing Machine for Rigid Boxes', 'zs-s088c': '4-Axis Cabinet Cold Glue Dispensing Machine', 'zs-s088c-4': '4-Axis Cabinet Hot Melt Glue Dispensing Machine', 'zs-s088d': '3-Axis Cabinet Cold Glue Dispensing Machine', 'zs-s088d-4': '3-Axis Cabinet Hot Melt Glue Dispensing Machine', 'zs-s088b': '4-Axis Dual-Station Glue Dispensing Machine (Standard / Large)', 'zs-s088a': '3-Axis Dual-Station Glue Dispensing Machine (Standard / Large)', 'zs-s088a-r': '3-Axis Dual-Station Hot Melt Gluing Machine (Standard / Large)', 'zs-s088p': '3-Axis Glue Spraying Machine', 'zs-yh4040': 'Inline Rigid Box Bubble Pressing Machine', 'cs4539': 'Semi-Automatic Small Case Making Machine'}
HL={'zs-s088e-4': ('一台机节省两个人划胶，可与自动天地盒机连线作业', 'Inline Rigid Box Gluing Machine – Replaces Two Operators, Links to Automatic Lid-and-Base Box Lines'), 'zs-s088r-4': ('一台机节省两个人划胶，可与自动天地盒机连线作业', 'Inline Rigid Box Gluing Machine – Replaces Two Operators, Links to Automatic Lid-and-Base Box Lines'), 'zs-s088c': ('白胶、黄胶、万能胶都能划，盒底和侧面同时划', 'Cabinet Glue Dispensing Machine – Runs White Glue, Yellow Glue and Universal Glue, Glues Box Bottom and Sides at Once'), 'zs-s088c-4': ('大尺寸盒子划胶、刮胶，替代双面胶', 'Cabinet Hot Melt Gluing Machine – Glues and Scrapes Large Boxes Instead of Double-Sided Tape'), 'zs-s088d': ('一台机替代 2 人', '3-Axis Cold Glue Dispensing Machine – One Machine Replaces Two Operators'), 'zs-s088d-4': ('刮热胶替代双面胶，省去撕离型纸的人工', '3-Axis Hot Melt Gluing Machine – Replaces Double-Sided Tape, No More Peeling Release Liners'), 'zs-s088b': ('专做小尺寸盒、皮壳、首饰盒和奢侈品盒', 'Dual-Station Glue Dispensing Machine for Small Rigid Boxes, Cases, Jewelry and Luxury Boxes'), 'zs-s088a-r': ('专做小尺寸盒、皮壳、首饰盒和奢侈品盒', 'Dual-Station Glue Dispensing Machine for Small Rigid Boxes, Cases, Jewelry and Luxury Boxes'), 'zs-s088a': ('大尺寸皮壳、坑卡平面划胶，双工位', 'Dual-Station Glue Dispensing Machine – Flat Gluing for Large Cases and Recessed Card Inserts'), 'zs-s088p': ('皮盒面料喷胶均匀，减少胶水浪费', 'Glue Spraying Machine – Even Coating on Box Covering Materials, Less Glue Waste'), 'zs-yh4040': ('一次压一个或两个', 'Rigid Box Bubble Pressing Machine – Presses One or Two Boxes per Cycle'), 'cs4539': ('约 1.2 秒成型一个', 'Semi-Automatic Case Making Machine – About 1.2 s per Case')}
GROUPS=[('cold',('冷胶划胶机','Cold Glue Machines'),('白胶、黄胶、万能胶','White, yellow and universal glue')),('hot',('热胶划胶机','Hot Glue Machines'),('热熔胶、压敏胶','Hot melt and pressure-sensitive adhesive')),('spray',('喷胶机','Glue Spraying'),('白乳胶、万能胶等喷胶类胶水','White latex, universal and other sprayable glues')),('press',('压泡机','Bubble Pressing'),('压底部、压吸塑、压纸托','Bottoms, blister inserts, paper trays')),('case',('皮壳机','Case Making'),('半自动小皮壳成型','Semi-automatic small case forming'))]
def grpof(m):
  if m['cat'] in ('spray','press','case'): return m['cat']
  return 'hot' if is_hot(m) else 'cold'
def csen(v):
  for a,b in [('半自动小皮壳机 CS4539','Semi-automatic small case making machine CS4539'),('约1.2秒/个','approx. 1.2 s/pc'),('15-34个/分钟','15-34 pcs/min'),('约490KG','approx. 490KG'),('长','L'),('宽','W'),('高','H')]: v=v.replace(a,b)
  return v
B_INL=('盒子类产品；可与自动天地盒机连线','Box products; links to automatic lid-and-base box machines')
B_SM=('小尺寸盒子、皮壳、首饰盒、奢侈品盒、化妆品盒、坑卡','Small boxes, cases, jewelry, luxury and cosmetic boxes, recessed card inserts')
B_LC=('大尺寸皮壳、坑卡','Large cases, recessed card inserts')
G_C=('白胶、黄胶、万能胶','White glue, yellow glue, universal glue');G_H=('热熔胶、压敏胶','Hot melt, pressure-sensitive adhesive')
P_ALL=('盒子底部、侧面、平面侧面可同时划','bottom, sides and flat faces at once');P_FL=('盒底、皮壳、坑卡盒平面','box bottoms, cases, flat recessed card inserts')
def _ax(z,en,p): return (z+(' · '+p[0] if p else ''),en+(' · '+p[1] if p else ''))
FACTS={'zs-s088e-4':(B_INL,G_C,_ax('四轴 · 随线','4-axis · inline',P_ALL)),
'zs-s088r-4':(B_INL,G_H,_ax('四轴 · 随线','4-axis · inline',P_ALL)),
'zs-s088c':(('大尺寸盒子、折叠盒、书型盒、皮壳、坑卡','Large boxes, folding and book-style boxes, cases, recessed card inserts'),G_C,_ax('四轴 · 柜式','4-axis · cabinet',P_ALL)),
'zs-s088c-4':(('大尺寸盒子、皮壳、坑卡','Large boxes, cases, recessed card inserts'),G_H,_ax('四轴 · 柜式','4-axis · cabinet',P_ALL)),
'zs-s088d':(B_LC,G_C,_ax('三轴 · 柜式','3-axis · cabinet',P_FL)),
'zs-s088d-4':(B_LC,('热胶（刮胶）','Hot glue (scraping)'),_ax('三轴 · 柜式','3-axis · cabinet',None)),
'zs-s088b':(B_SM,G_C,_ax('四轴 · 双工位','4-axis · dual-station',P_ALL)),
'zs-s088a':(B_LC,G_C,_ax('三轴 · 双工位','3-axis · dual-station',P_FL)),
'zs-s088a-r':(B_SM,G_H,_ax('三轴 · 双工位','3-axis · dual-station',P_ALL)),
'zs-s088p':(('皮盒面料（平面喷胶）','Leather-box covering materials (flat spraying)'),('白乳胶、万能胶等喷胶类胶水','White latex glue, universal glue and other sprayable glues'),('三轴','3-axis')),
'zs-yh4040':(('手机盒、平板盒、香水盒','Phone, tablet and perfume boxes'),('压底部、压吸塑、压纸托','Bottoms, blister inserts, paper trays'),('随线 · 一次压一个或两个','Inline · one or two per cycle'))}
def build():
  allm=MACH+[CS]
  for lg in ('en','zh'):
    t=L[lg];P=BASE+t['pre']
    # HOME
    feat=[MACH[0],MACH[1],MACH[2],MACH[4],MACH[6],MACH[9],MACH[10],CS]
    stats=[('2018',('成立于东莞东城','Founded in Dongcheng, Dongguan')),('7 天' if lg=='zh' else '7 days',('国外机器故障维修时效','Overseas machine fault repair response')),('终身' if lg=='zh' else 'Lifetime',('划胶枪嘴包修包换','Glue nozzle repair and replacement')),('3-10MM',('划胶宽度（划胶机）','Glue line width (gluing machines)'))]
    st=''.join(f'<div><b>{a}</b><span>{b[0] if lg=="zh" else b[1]}</span></div>' for a,b in stats)
    if lg=='zh': stats_note='数据来自至尚画册：成立年份、售后时效、试用政策、参数。'
    else: stats_note='Figures from the Zhishang brochure.'
    entries=[('applications/',('按应用找','Find by application'),('天地盒、书型盒、皮壳、坑卡……','Rigid boxes, book-style boxes, cases, greyboard…')),('products/',('按产品找','Find by product'),('随线 / 柜式 / 双工位 / 喷胶 / 压泡 / 皮壳','Inline, cabinet, dual-station, spraying, pressing, case making')),('products/#ns',('非标定制','Custom machines'),('可定制各种非标规格，适用各种需求','Custom specifications built to your requirements'))]
    en_=''.join(f'<a class="entry" href="{P}{h}"><h3>{a[0] if lg=="zh" else a[1]}</h3><p>{b[0] if lg=="zh" else b[1]}</p><span>→</span></a>' for h,a,b in entries)
    prom=promises(lg)
    body=f'''<section class="hero"><div class="wrap"><div><p class="eyebrow">{t['co']}</p><h1>{t['h1']}</h1>{BEAD}<p>{t['hp']}</p><div class="cta"><a class="btn" href="{P}contact/">{t['quote']}</a><a class="btn ghost" href="{P}products/">{t['allp']}</a></div></div><div class="heroimg"><svg class="glue" viewBox="0 0 600 40" aria-hidden="true"><path d="M6 20 C90 6 150 34 240 20 S420 6 594 20"/><circle cx="594" cy="20" r="6"/></svg><img src="{BASE}img/s088e-4.jpg" alt="ZS-S088E-4 {'随线四轴划胶机-冷胶' if lg=='zh' else 'inline glue machine'}" data-eager></div></div></section>
<div class="statbar"><div class="wrap">{st}</div><div class="wrap note">{stats_note}</div></div>
<section class="wideimg"><img src="{BASE}img/factory.jpg" alt="{'至尚科技厂房外观' if lg=='zh' else 'Zhishang factory building'}"><div class="wrap"><p>{'东莞东城 · 2018 年成立' if lg=='zh' else 'Dongcheng, Dongguan · Founded 2018'}</p></div></section>
<section><div class="wrap"><div class="grid g3">{en_}</div></div></section>
<section><div class="wrap"><h2>{'主推机型' if lg=='zh' else 'Featured Machines'}</h2><div class="grid g4">{''.join(card(m,lg) for m in feat)}</div><p><a class="btn" href="{P}products/">{t['allp']}</a></p></div></section>
<section class="alt"><div class="wrap"><h2>{'三项承诺' if lg=='zh' else 'Our Three Commitments'}</h2>{prom}</div></section>
<section><div class="wrap two"><img src="{BASE}img/factory.jpg" alt="{'至尚科技厂房外观' if lg=='zh' else 'Zhishang factory building'}"><div><h2>{'关于至尚' if lg=='zh' else 'About Zhishang'}</h2><p>{about_p(lg)}</p><a class="btn ghost dark" href="{P}about/">{'了解更多' if lg=='zh' else 'Learn more'}</a></div></div></section>
{inquiry(lg,'')}'''
    title=('至尚科技 | 划胶机、点胶机、喷胶机、压泡机 - 东莞市至尚自动化科技有限公司' if lg=='zh' else 'Rigid Box Gluing Machine, Hot Melt Gluing Machine & Glue Dispensing Machine | Zhishang')
    desc=('东莞市至尚自动化科技有限公司，专注划胶设备行业：随线/柜式/双工位划胶机、喷胶机、压泡机、半自动小皮壳机，冷胶热胶机型齐全。' if lg=='zh' else 'Dongguan Zhishang Automation Technology: rigid box gluing machines, hot melt gluing machines for rigid boxes, glue dispensing and glue spraying machines, rigid box bubble pressing machines and case making machines.')
    W(lg,'',page(lg,'',title,desc,body))
    # PRODUCTS overview
    grp=''
    for c,(cz,ce),(dz,de) in GROUPS+[('ns',CATS['ns'],('',''))]:
      if c=='ns':
        ns=''.join(f'<div class="pcard static">{f"<figure class=render><img src={chr(34)}{BASE}img/{i}.jpg{chr(34)} alt={chr(34)}{m}{chr(34)} loading=lazy><figcaption>{'效果图' if lg=='zh' else 'Rendering'}</figcaption></figure>" if i else ""}<div><small>{m}</small><h3>{z if lg=="zh" else en_n}</h3><p>{"非标机，按需定制" if lg=="zh" else "Non-standard machine, built to order."}</p></div></div>' for m,z,en_n,i,pg in NS)
        grp+=f'<h2 id="ns">{cz if lg=="zh" else ce}</h2><p class="sub">{"可定制各种非标规格，适用各种需求。" if lg=="zh" else "We build custom machines to your specifications and requirements."}</p><div class="grid g3">{ns}</div>'
        continue
      ms=[m for m in allm if grpof(m)==c]
      grp+=f'<h2 id="{c}" class="rv">{cz if lg=="zh" else ce}</h2><p class="sub">{dz if lg=="zh" else de}</p><div class="grid g4">{"".join(card(m,lg) for m in ms)}</div>'
    comp=compare(lg)
    W(lg,'products',page(lg,'products/',('产品中心 | 划胶机 点胶机 喷胶机 - 至尚科技' if lg=='zh' else 'Rigid Box Gluing, Glue Dispensing & Spraying Machines | Zhishang'),('至尚全部机型与参数。' if lg=='zh' else 'All Zhishang machines with specifications: rigid box gluing machines, glue dispensing machine, glue spraying machine, case making machine.'),
      f'<section class="phead"><div class="wrap"><div class="crumbs"><a href="{P}">{'首页' if lg=='zh' else 'Home'}</a></div><h1>{t["nav"][0][1]}</h1>{BEAD}<p>{"按工艺浏览：冷胶、热胶、喷胶、压泡、皮壳成型、非标定制。" if lg=="zh" else "Browse by process: cold glue, hot glue, spraying, bubble pressing, case making and custom machines."}</p></div></section><section><div class="wrap">{grp}</div></section><section class="alt"><div class="wrap"><h2>{"参数对比" if lg=="zh" else "Specification Comparison"}</h2><p class="sub">{t["src"]}</p>{comp}</div></section>{inquiry(lg,"")}'))
    # product pages
    for m in allm:
      if m is CS:
        rows=''.join(f'<tr><th>{a if lg=="zh" else b}</th><td><code>{v if lg=="zh" else csen(v)}</code></td></tr>' for a,b,v in CS['rows']); feats=''
        summ=('半自动小皮壳机，用于小尺寸皮壳成型。' if lg=='zh' else 'Semi-automatic machine for forming small cases.')
      else:
        vals=[m['model'],nm(m,lg),m['dims'],m['size'],m['speed'],m['power'],m['width'],m['volt'],m['air']]
        rows=''.join(f'<tr><th>{t["lab"][i]}</th><td><code>{e(v)}</code></td></tr>' for i,v in enumerate(vals) if v)
        feats='<ol class="feats">'+''.join(f'<li>{f[0] if lg=="zh" else f[1]}</li>' for f in m['features'])+'</ol>'
        summ=(m['features'][0][0] if lg=='zh' else m['features'][0][1])
      cz,ce=CATS[m['cat']]
      if m is CS: kp=[(r[0]+'：'+r[2]) if lg=='zh' else (r[1]+': '+csen(r[2])) for r in CS['rows'][1:6]]
      else: kp=None
      _h=HL[m['slug']][0] if lg=='zh' else HL[m['slug']][1];_p=_h.split(' – ',1);hh=f'<h1>{e(_p[0])}</h1>'+(f'<p class="hsub">{e(_p[1])}</p>' if len(_p)>1 else '')
      if m is CS: pts='<ul class="pts">'+''.join(f'<li>{e(x)}</li>' for x in kp)+'</ul>'
      else:
        fx=FACTS[m['slug']];labs=(('适用产品','Products'),('胶水','Glue'),('结构 / 划胶位置','Build / gluing positions')) if m['cat']!='press' else (('适用产品','Products'),('工序','Process'),('结构','Build'))
        pts='<dl class="facts">'+''.join(f'<div><dt>{l[0] if lg=="zh" else l[1]}</dt><dd>{e(v[0] if lg=="zh" else v[1])}</dd></div>' for l,v in zip(labs,fx) if v)+'</dl>'
      body=f'''<section class="phead"><div class="wrap crumbs"><a href="{P}">{'首页' if lg=='zh' else 'Home'}</a> / <a href="{P}products/">{t['nav'][0][1]}</a> / {cz if lg=='zh' else ce}</div></section>
<section><div class="wrap pdetail"><div class="pinfo"><small class="model">{m['model']}</small><p class="pname">{nm(m,lg)}</p>{hh}{BEAD}{pts}
<div class="cta" id="askcta"><a class="btn" href="{P}contact/?model={m['model'].replace(' ','')}#quote">{t['ask']}</a><a class="btn ghost dark" href="mailto:{EM}?subject={('询价 ' if lg=='zh' else 'Inquiry ')+m['model']}">Email</a></div>
<p class="small">{'电话/传真' if lg=='zh' else 'Tel/Fax'}: {TEL}</p>
<nav class="tabs">{'' if m is CS else '<a href="#features">'+t['feat']+'</a>'}<a href="#specs">{t['spec']}</a></nav></div><div class="gallery"><img src="{BASE}img/{m['img']}.jpg" alt="{e(nm(m,lg))} {m['model']}" data-eager>{dets(lg,m)}</div></div></section>
<div class="pbar" id="pbar" hidden><div class="wrap"><span><code>{m['model']}</code> {nm(m,lg)}</span><a class="btn sm" href="{P}contact/?model={m['model'].replace(' ','')}#quote">{t['ask']}</a></div></div>
{f'<section id="features" class="alt"><div class="wrap"><h2>{t["feat"]}</h2>{feats}</div></section>' if feats else ''}
<section id="specs"><div class="wrap"><h2>{t['spec']}</h2><div class="tbl"><table class="spec">{rows}</table></div><p class="small">{t['src']}</p></div></section>
{extras(lg,m)}
{inquiry(lg,m['model'])}'''
      ti=f"{m['model']} {nm(m,lg)} | {'至尚科技' if lg=='zh' else 'Zhishang'}"
      W(lg,'products/'+m['slug'],page(lg,f'products/{m["slug"]}/',ti,f"{m['model']} {nm(m,lg)}. "+summ,body+ld_product(lg,m,summ)))
    # applications
    ap=''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p><p class="small">{"推荐机型" if lg=="zh" else "Machines"}: <code>{c}</code></p></div>' for a,b,c in APPS[lg])
    W(lg,'applications',page(lg,'applications/',('应用领域 | 天地盒 书型盒 皮壳 坑卡 划胶 - 至尚科技' if lg=='zh' else 'Applications: Rigid Box, Lid and Base Box, Book-Style Box & Case Gluing | Zhishang'),('至尚划胶设备适用的包装产品。' if lg=='zh' else 'Gluing applications for rigid boxes, lid-and-base boxes, book-style boxes, cases and greyboard.'),
      f'<section class="phead"><div class="wrap"><div class="crumbs"><a href="{P}">{'首页' if lg=='zh' else 'Home'}</a></div><h1>{t["nav"][1][1]}</h1>{BEAD}<p>{"以下应用均来自至尚画册各机型的适用说明。" if lg=="zh" else "Applications listed in the Zhishang brochure for each machine."}</p></div></section><section><div class="wrap"><div class="grid g4">{ap}</div></div></section>{inquiry(lg,"")}'))
    # about
    W(lg,'about',page(lg,'about/',('关于我们 - 东莞市至尚自动化科技有限公司' if lg=='zh' else 'About Dongguan Zhishang Automation Technology'),about_p(lg)[:150],about_body(lg)))
    W(lg,'service',page(lg,'service/',('服务承诺 - 至尚科技' if lg=='zh' else 'Service & Commitments | Zhishang'),('划胶枪嘴终身包修包换；国外机器故障维修 7 天；海外安装与技术支持请咨询。' if lg=='zh' else 'Lifetime glue nozzle repair and replacement, 7-day overseas fault repair response. Contact us for overseas installation and support options.'),
      f'<section class="phead"><div class="wrap"><div class="crumbs"><a href="{P}">{'首页' if lg=='zh' else 'Home'}</a></div><h1>{t["nav"][3][1]}</h1>{BEAD}</div></section><section><div class="wrap">{promises(lg)}<template id="hold-overseas-service"><ul class="pts"><li>远程视频支持 / Remote video support: [待确认]</li><li>工程师出国安装 / Engineer dispatch abroad: [待确认]</li><li>备件国际快递 / Spare parts shipping: [待确认]</li><li>英文说明书 / English manual: [待确认]</li><li>整机质保 / Machine warranty: [待确认]</li></ul></template><h2 style="margin-top:48px">{"服务理念" if lg=="zh" else "Service Concept"}</h2><p>{service_p(lg)}</p></div></section>{inquiry(lg,"")}'))
    W(lg,'contact',page(lg,'contact/',('联系我们 / 在线询价 - 至尚科技' if lg=='zh' else 'Contact & Request a Quote | Zhishang'),('东莞市至尚自动化科技有限公司联系方式。' if lg=='zh' else 'Contact Dongguan Zhishang Automation Technology.'),
      f'<section class="phead"><div class="wrap"><div class="crumbs"><a href="{P}">{'首页' if lg=='zh' else 'Home'}</a></div><h1>{t["nav"][4][1]}</h1>{BEAD}</div></section>{inquiry(lg,"",full=True)}'))
  # sitemap/robots
  urls=[]
  for root,_,fs in os.walk('.'):
    if 'index.html' in fs and not root.startswith(('./shots','./refs','./.git')): urls.append(URL+root[2:]+('/' if root!='.' else ''))
  open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u.replace("//","/").replace("https:/","https://")}</loc></url>' for u in sorted(urls))+'</urlset>\n')
  open('robots.txt','w').write(f'# preview build: pages carry noindex\nUser-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n')
TBD={'zh':'[待提供]','en':'[to be provided]'}
def is_hot(m): return any(f is HOT for f in m.get('features',[])) or m['slug'] in ('zs-s088d-4',)
def is_cold(m): return any(f in (COLD,FLATC) for f in m.get('features',[]))
def extras(lg,m):
  z=lg=='zh';T=TBD[lg]
  pack=('出口木架尺寸：长1450*宽1000*高1850mm' if z else 'Export wooden crate size: L1450*W1000*H1850mm') if m is CS else T
  scrib=m['cat'] in ('inline','cabinet','dual')
  warr=(('划胶枪嘴终身包修，包换（以旧换新）；整机质保 '+T) if z else ('Glue nozzle: lifetime repair and replacement (trade-in); whole-machine warranty '+T)) if scrib else (('整机质保 '+T) if z else ('Machine warranty '+T))
  rows=[('起订量','MOQ',T),('付款方式','Payment terms',T),('交期','Lead time',T),('包装','Packaging',pack),('质保','Warranty',warr),('售后时效','Service response','国外7天；国内：市内4小时，省内24小时，省外3天' if z else 'Overseas: within 7 days'),('海外支持','Overseas support','海外安装与技术支持方案请联系我们'+('；国内省内客户可先试用一星期再付款' ) if z else 'Contact us for overseas installation and support options')]
  trade=''.join(f'<tr><th>{a if z else c}</th><td>{d}</td></tr>' for a,c,d in rows)
  fq=[]
  if is_cold(m): fq.append(('能用哪些胶水？','Which glues can it use?',[f[0] if z else f[1] for f in m['features'] if f in (COLD,FLATC)][0]))
  elif m['slug'] in ('zs-s088d-4',): fq.append(('能用哪些胶水？','Which glues can it use?','可以刮热胶，替代双面胶，节省撕离型纸的人工和时间' if z else 'Hot glue (scraping), replacing double-sided tape.'))
  elif is_hot(m): fq.append(('能用哪些胶水？','Which glues can it use?',HOT[0] if z else HOT[1]))
  if m is not CS: fq.append(('需要什么电源和气源？','What power and air supply are needed?',f"{m['volt']}，{m['air']}" if z else f"{m['volt']}, {m['air']}"))
  if m.get('width'): fq.append(('划胶宽度多少？' if m['cat']!='spray' else '喷胶宽度多少？','What line width can it produce?',m['width']))
  if F3 in m.get('features',[]): fq.append(('能接入现有产线吗？','Can it fit into my existing line?',(F3[0]+('；'+INL2[0] if INL2 in m['features'] else '')) if z else (F3[1]+(' '+INL2[1] if INL2 in m['features'] else ''))))
  fq+= [('机器坏了多久能修？','How fast is after-sales service?','机器故障维修：国外7天；国内市内4小时，省内24小时，省外3天。' if z else 'Overseas machine faults: service response within 7 days.'),
        ('海外安装和技术支持怎么安排？','How are overseas installation and support arranged?','海外安装与技术支持方案请联系我们。国内省内客户可先试用一星期再付款。' if z else 'Contact us for overseas installation and support options.'),
        ('价格和交期？','Price and lead time?',T)]
  faq=''.join(f'<details><summary>{a if z else b_}</summary><p>{c}</p></details>' for a,b_,c in fq)
  rel=[x for x in MACH+[CS] if x['cat']==m['cat'] and x is not m] or [x for x in MACH if x['cat'] in ('inline','cabinet')][:3]
  relh=''.join(card(x,lg) for x in rel[:4])
  ldf={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":(a if z else b_),"acceptedAnswer":{"@type":"Answer","text":c}} for a,b_,c in fq if c!=T]}
  return f'''<template id="hold-trade-faq"><section class="alt"><div class="wrap two top"><div><h2>{'贸易信息' if z else 'Trade Information'}</h2><div class="tbl"><table class="spec">{trade}</table></div></div><div><h2>{'常见问题' if z else 'FAQ'}</h2><div class="faq">{faq}</div></div></div></section></template>
<section><div class="wrap"><h2>{'相关机型' if z else 'Related Models'}</h2><div class="grid g4">{relh}</div></div></section>'''
def ld_product(lg,m,summ):
  t=L[lg];P=URL+t['pre']
  d={"@context":"https://schema.org","@type":"Product","name":nm(m,lg),"model":m['model'],"mpn":m['model'],"image":URL+'img/'+m['img']+'.jpg',"description":summ,"brand":{"@type":"Brand","name":t['brand']},"manufacturer":{"@type":"Organization","name":t['co']},"url":P+'products/'+m['slug']+'/'}
  bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":'首页' if lg=='zh' else 'Home',"item":P},{"@type":"ListItem","position":2,"name":t['nav'][0][1],"item":P+'products/'},{"@type":"ListItem","position":3,"name":m['model'],"item":P+'products/'+m['slug']+'/'}]}
  return f'<script type="application/ld+json">{json.dumps(d,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(bc,ensure_ascii=False)}</script>'
DETL={'zh':['划胶头','控制手柄','控制面板'],'en':['Glue head','Teach pendant','Control panel']}
DETS={'zs-s088c':[0,1,2],'zs-s088e-4':[0,1],'zs-s088p':[0,2]}
def dets(lg,m):
  if m['slug'] not in DETS: return ''
  lab=DETL[lg][:]
  if m['slug']=='zs-s088p': lab[0]='喷胶头' if lg=='zh' else 'Spray head'
  if m['slug']=='zs-s088e-4': lab[1]='控制箱与手柄' if lg=='zh' else 'Control box and pendant'
  return '<div class="dets">'+''.join(f'<figure><img src="{BASE}img/det-{m["slug"]}-{i+1}.jpg" alt="{m["model"]} {lab[k]}"><figcaption>{lab[k]}</figcaption></figure>' for i,k in enumerate(DETS[m['slug']]))+'</div>'
def compare(lg):
  t=L[lg];hd=''.join(f'<th>{x}</th>' for x in [t['lab'][0],t['lab'][1],t['lab'][2],t['lab'][3],t['lab'][4],t['lab'][5],t['lab'][6]])
  rs=''.join(f'<tr><td><a href="{BASE}{t["pre"]}products/{m["slug"]}/"><code>{m["model"]}</code></a></td><td>{nm(m,lg)}</td><td><code>{m["dims"]}</code></td><td><code>{m["size"]}</code></td><td><code>{m["speed"]}</code></td><td><code>{m["power"]}</code></td><td><code>{m["width"] or "—"}</code></td></tr>' for m in MACH)
  return f'<div class="tbl"><table class="cmp"><thead><tr>{hd}</tr></thead><tbody>{rs}</tbody></table></div>'
def promises(lg):
  P=[('划胶枪嘴终身包修，包换（以旧换新）。划胶嘴为我司自主研发品牌，有发明专利和实用新型专利。','Lifetime repair and replacement (trade-in) for glue nozzles. The nozzle is our own developed brand, covered by invention and utility model patents.'),
     ('售后时效：国外机器故障维修 7 天。（国内：市内4小时，省内24小时，省外3天）','Overseas service response: machine faults are handled within 7 days.'),
     ('海外安装与技术支持方案请联系我们。（国内省内客户可先试用一星期再付款）','Contact us for overseas installation and support options.')]
  return '<div class="grid g3 prom">'+''.join(f'<div class="card"><b class="num">0{i+1}</b><p>{a if lg=="zh" else b}</p></div>' for i,(a,b) in enumerate(P))+'</div>'
def about_p(lg):
  return ('东莞市至尚自动化科技有限公司成立于2018年，位于东莞东城。主要研发生产：自动划胶机、喷胶机、压盒机及各种包装行业非标机械。公司是由“至尚精品包装”转型后成立的自动化公司，围绕包装产品优化升级、工艺优化、排拉布线、产能评估、生产计件制度推行等方案提供建议。' if lg=='zh' else
   'Dongguan Zhishang Automation Technology Co., Ltd was founded in 2018 in Dongcheng, Dongguan. We develop and build automatic gluing machines, glue spraying machines, box pressing machines and non-standard machinery for the packaging industry. The company grew out of Zhishang Boutique Packaging, so we also advise on packaging product upgrades, process optimization, line layout, capacity evaluation and piece-rate production systems.')
def service_p(lg):
  return ('我司无偿为客户提供包装行业技术经验，管理经验分享，各种行业资源共享。公司对售后时效和客户满意度有严格要求和管控。有些易损件实行以旧换新，免费更换等方式高效处理设备异常。' if lg=='zh' else
   'We share packaging-industry technical and management experience and industry resources with customers free of charge. After-sales response time and customer satisfaction are strictly managed; some wearing parts are handled by trade-in or free replacement to resolve equipment issues quickly.')
def about_body(lg):
  t=L[lg]
  mission=('打造优质的服务平台，以专业的水平为包装行业服务，整合资源为包装行业赋能。' if lg=='zh' else 'To build a high-quality service platform, serve the packaging industry professionally, and integrate resources to empower it.')
  team=('公司团队人员都有包装管理经验，同时对行业内各种小设备使用率、生产适用性具有丰富的经验。' if lg=='zh' else 'Our team members all have packaging management experience, plus extensive hands-on knowledge of how small equipment is used and fits production in this industry.')
  rel=[('广东九州顺驰环保新材料有限公司','Guangdong Jiuzhou Shunchi Environmental Protection New Materials Co., Ltd','至尚科技旗下的项目类公司，主要生产并销售纸品类万能胶。万能胶型号：DC-805 DC-402 DC-806 SC-906 DC-206；热熔胶：Q-8313D、Q-8501BA。','A project company under Zhishang Technology producing universal adhesives for paper products. Universal adhesive models: DC-805 DC-402 DC-806 SC-906 DC-206; hot melt: Q-8313D, Q-8501BA.'),
       ('东莞市三狮精密模具制造有限公司','Dongguan Sanshi Precision Mold Manufacturing Co., Ltd','成立于 2017 年，非标准模具、工装夹具设计加工，以及自动化设备零部件精密加工。正常订单 24 小时发货，加急订单 8 小时内发货。','Founded in 2017: non-standard molds and fixtures, plus precision machining of automation parts. Normal orders ship within 24 hours, urgent orders within 8 hours.')]
  rl=''.join(f'<div class="card"><h3>{a if lg=="zh" else b}</h3><p>{c if lg=="zh" else d}</p></div>' for a,b,c,d in rel)
  return f'''<section class="phead"><div class="wrap"><h1>{t['nav'][2][1]}</h1>{BEAD}</div></section>
<section><div class="wrap two"><img src="{BASE}img/factory.jpg" alt="{'至尚科技厂房外观' if lg=='zh' else 'Zhishang factory building'}"><div><h2>{'公司简介' if lg=='zh' else 'Company Profile'}</h2><p>{about_p(lg)}</p></div></div></section>
<section class="alt"><div class="wrap grid g3"><div class="card"><h3>{'公司使命' if lg=='zh' else 'Mission'}</h3><p>{mission}</p></div><div class="card"><h3>{'团队介绍' if lg=='zh' else 'Team'}</h3><p>{team}</p></div><div class="card"><h3>{'服务理念' if lg=='zh' else 'Service Concept'}</h3><p>{service_p(lg)}</p></div></div></section>
<section><div class="wrap grid g3"><img class="ph" src="{BASE}img/team.jpg" alt="{'至尚团队' if lg=='zh' else 'Zhishang team'}"><img class="ph" src="{BASE}img/workshop.jpg" alt="{'车间' if lg=='zh' else 'Workshop'}"><img class="ph" src="{BASE}img/certs.jpg" alt="{'企业荣誉证书' if lg=='zh' else 'Certificates'}"></div><div class="wrap"><p class="small">{'企业荣誉：实用新型专利证书等' if lg=='zh' else 'Corporate honors: utility model patent certificates and more.'}</p></div></section>
<section class="alt"><div class="wrap"><h2>{'关联公司' if lg=='zh' else 'Related Companies'}</h2><div class="grid g2">{rl}</div></div></section>'''
def inquiry(lg,model,full=False):
  t=L[lg];z=lg=='zh'
  opts=''.join(f'<option{" selected" if m["model"]==model else ""}>{m["model"]} {nm(m,lg)}</option>' for m in MACH+[CS])
  return f'''<section id="quote" class="alt"><div class="wrap contact"><div><h2>{t['quote']}</h2><p class="sub">{'请留下您的需求，我们会尽快回复。' if z else 'Tell us about your boxes and glue. We will reply as soon as possible.'}</p>
<form action="mailto:{EM}" method="post" enctype="text/plain"><div><label>{'姓名' if z else 'Name'}</label><input name="name" required></div><div><label>{'邮箱/电话' if z else 'Email / phone'}</label><input name="contact" required></div>
<div class="full"><label>{'机型' if z else 'Machine'}</label><select name="model" id="model"><option value="">{'不确定，需要建议' if z else 'Not sure, need advice'}</option>{opts}</select></div>
<div class="full"><label>{'产品与需求（盒型、尺寸、胶水类型）' if z else 'Your product (box type, size, glue type)'}</label><textarea name="message"></textarea></div>
<div class="full"><button class="btn" type="submit">{'发送询价' if z else 'Send inquiry'}</button> <span class="small">{'（预览版：提交将打开您的邮件程序）' if z else '(Preview: opens your email app)'}</span></div></form></div>
<div class="cbox"><h3>{'联系方式' if z else 'Contact'}</h3><p><b>{t['co']}</b></p><p>{'地址' if z else 'Address'}: {ADDR[0] if z else ADDR[1]}</p><p>{'电话/传真' if z else 'Tel/Fax'}: <a href="tel:+8676922250346">{TEL}</a></p><p>{'邮箱' if z else 'Email'}: <a href="mailto:{EM}">{EM}</a></p><p class="trust">{'划胶嘴拥有发明专利和实用新型专利' if z else 'Nozzle covered by invention and utility model patents'}</p></div></div>
<script>(function(){{var m=new URLSearchParams(location.search).get('model');if(!m)return;var s=document.getElementById('model');for(var o of s.options)if(o.text.replace(/ /g,'').indexOf(m)===0){{o.selected=true;break}}}})()</script></section>'''
for _m in MACH+[CS]: _m['en']=ENT[_m['slug']]
build()

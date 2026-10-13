# Guides (pain-point Q&A) pages. Content approved 2026-10-13 from design/qa-sample (drafts/painpoints/01).
import json, re
CSS = """
.qa{display:grid;grid-template-columns:minmax(0,1fr);gap:40px}
@media(min-width:1024px){.qa{grid-template-columns:minmax(0,1fr) 220px}.toc{display:block!important}}
.qa article{max-width:68ch;font-size:17px;line-height:1.7}.zh .qa article{font-size:16px;line-height:1.8;max-width:42em}
.qa h1{font-size:2rem;margin:6px 0 14px}.qa h2{font-size:1.45rem;margin:34px 0 10px}
.ansbox{background:#F3F5F7;border-left:4px solid #F2A900;padding:16px 18px;margin:0 0 6px}.ansbox p{margin:0}
.src{font-size:.8rem;color:#5B6B7A;margin:0 0 22px}
.why{margin:0 0 8px;color:#0F2A44;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.recs{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.recs .pcard img{height:240px;aspect-ratio:auto}
.recs .rec{display:flex;flex-direction:column}.recs .rec .pcard{flex:1}
.scf table{font-size:.92rem}.scf th{background:#0F2A44;color:#fff}.scf td:first-child{font-weight:600;color:#0F2A44}
.scf-m{display:none}.scf-m details{background:#fff;border:1px solid #dde2e8;border-left:3px solid #F2A900;border-radius:6px;margin-bottom:8px;padding:10px 14px}
.scf-m summary{font-weight:600;color:#0F2A44;cursor:pointer}.scf-m dl{margin:8px 0 0}.scf-m dt{font-size:.8rem;color:#5B6B7A}.scf-m dd{margin:0 0 6px}
.pend{background:#fff3cd;color:#7a5600;padding:0 4px;border-radius:3px;font-size:.85em;white-space:nowrap}
.toc{display:none;position:sticky;top:90px;align-self:start;font-size:.88rem;border-left:2px solid #dde2e8;padding-left:14px}
.toc b{display:block;color:#0F2A44;margin-bottom:6px}.toc a{display:block;color:#5B6B7A;text-decoration:none;padding:3px 0}
.ctab{background:#0F2A44;color:#d6deea;border-radius:8px;padding:26px;margin-top:34px}.ctab h2{color:#fff;margin-top:0}.ctab .btn{margin:6px 8px 0 0}
.refs{font-size:.85rem;color:#5B6B7A}.refs li{margin-bottom:4px}
.upd{font-size:.8rem;color:#5B6B7A;margin-top:24px}
@media(max-width:700px){.qa h1{font-size:1.5rem;margin-bottom:10px}.qa .phead{padding:14px 0 0}.recs{grid-template-columns:1fr}.recs .pcard img{height:150px}
 .scf table{display:none}.scf-m{display:block}}
"""
R = lambda k: f'<a class="small" href="#ref-{k}">[{k}]</a>'
PEND = '<span class="pend">[待老板确认]</span>'
EN = dict(lang='en', title='Hot Melt Glue Stringing: Causes and Fixes | Zhishang',
 crumbs='<a href="/">Home</a> / <a href="/guides/">Guides</a> / Hot melt glue stringing',
 h1='Why does hot melt glue string, and how do I stop it?',
 answer='Stringing ("angel hair") usually means the glue is cutting off poorly at the nozzle: the nozzle is too far from the work, the glue is too cool and viscous, the substrate is cold, the nozzle tip is damaged or charred, solenoid air pressure is low, or a draft is blowing on the bead.',
 src='Sources: H.B. Fuller Hot Melt Troubleshooting Guide; Henkel, "Preventing stringing in hot melt packaging adhesives"',
 scf_t='Symptom / Cause / Fix', scfh=['Symptom','Cause','Fix'],
 scf=[['Fine threads trail from the bead onto the box surface',f'Nozzle too far from the substrate {R("HBF-TS")} {R("HEN-STR")}',f'Bring the nozzle closer (H.B. Fuller: ideally 1/4 in) {R("HBF-BP")}'],
      ['Strings thicken, bead looks "ropey"',f'Glue temperature too low / viscosity too high {R("HBF-TS")} {R("HEN-STR")}',f'Increase temperature slightly, staying within the adhesive\'s recommended operating range {R("HBF-TS")} {R("HEN-STR")}'],
      ['Stringing worse first thing in the morning or in winter',f'Cold board or paper {R("HBF-TS")} {R("HEN-STR")}',f'Allow substrates to adjust to ambient temperature before gluing {R("HBF-TS")} {R("HEN-STR")}'],
      ['Strings appear even at correct temperature',f'Damaged or charred nozzle tip, poor cut-off {R("HEN-STR")}',f'Check the nozzle tip is not plugged and in good condition; check filters and hoses for char {R("HEN-STR")}'],
      ['Gun drips or snaps slowly',f'Low air pressure to the solenoid {R("HBF-TS")}',f'Ensure incoming air pressure is greater than 50 psi; inspect muffler buildup {R("HBF-TS")}'],
      ['Strings blow sideways',f'Fan or air-conditioning draft on the bead {R("HEN-STR")}',f'Shield the glue area from direct airflow {R("HEN-STR")}']],
 body=f'<p><b>Also check:</b> if the gun drips between beads, H.B. Fuller lists worn nozzles, module faults and low air pressure as causes {R("HBF-TS")}.</p>',
 faq_t='Common follow-up questions',
 faq=[('What is "angel hair" in hot melt gluing?','It is the thin strands of hot melt pulled away from the nozzle when the glue does not separate cleanly. The strands float through the air and land on equipment and products.'),
      ('How close should the nozzle be to the board?','H.B. Fuller recommends that the applicator is not too far from the substrate, ideally 1/4 inch (about 6 mm).'),
      ('Can a worn nozzle cause stringing?','Yes. Henkel notes that damage or char on the nozzle tip prevents the valve from operating properly, which leads to poor cut-off.')],
 rel_t='Related questions', rel=[('Why is my hot melt glue not sticking?','/guides/hot-glue-not-sticking/'),('Hot melt nozzle clogging and charring: what to do','/guides/hot-melt-nozzle-clogging-charring/'),('Hot melt vs cold glue (PVA) for rigid boxes','/guides/hot-melt-vs-white-pva-glue/')],
 rec_t='Gluing rigid boxes with hot melt by machine', rec_p=f'Zhishang hot-glue models apply hot melt and pressure-sensitive glue with a 3-10MM glue line. Glue nozzles carry lifetime repair and trade-in replacement {R("ZS")}. Working air pressure is 0.6MPa {R("ZS")}.', more='View details →',
 cards=[dict(why='Inline with a box line or auto lid-and-base machine',model='ZS-S088R-4',name='Inline 4-Axis Hot Melt Gluing Machine for Rigid Boxes',url='/products/zs-s088r-4/',img='s088r-4',keys=[('Effective size','600*600*130MM/50*50*25MM'),('Glue line width','3-10MM')]),
        dict(why='Larger boxes at a standalone workstation',model='ZS-S088C-4',name='4-Axis Cabinet Hot Melt Glue Dispensing Machine',url='/products/zs-s088c-4/',img='s088c-4',keys=[('Effective size','900*600*150MM/50*50*10MM'),('Glue line width','3-10MM')]),
        dict(why='Hot glue to replace double-sided tape',model='ZS-S088D-4',name='3-Axis Cabinet Hot Melt Glue Dispensing Machine',url='/products/zs-s088d-4/',img='s088d-4',keys=[('Effective size','900*600MM/50*50MM'),('Glue line width','3-10MM')])],
 cta_h='Moving hot melt gluing from hand guns to a machine?', cta_p='Send us your box size and glue. Prices are quoted per configuration. Specifications are for reference only; final specifications are subject to our quotation.', cta_b='Request a Quote', cta_url='/contact/#quote',
 ref_t='References', refs=['<span id="ref-HBF-TS">[HBF-TS]</span> H.B. Fuller, <a href="https://www.hbfuller.com/-/media/project/hbfuller/hbfuller/files/technologies/hot-melt/hbf_hotmelt_troubleshooting-guide_fnl(1).pdf">Hot Melt Adhesives Troubleshooting Guide</a> (PDF): Stringing, Dripping Nozzle',
   '<span id="ref-HBF-BP">[HBF-BP]</span> H.B. Fuller, <a href="https://www.hbfuller.com/-/media/project/hbfuller/hbfuller/files/detail/equipment-manufacturer-support/packaging-adhesive-best-practices.pdf">Packaging Adhesive Best Practices</a> (PDF): stringing / angel hair',
   '<span id="ref-HEN-STR">[HEN-STR]</span> Henkel, <a href="https://next.henkel-adhesives.com/us/en/articles/preventing-stringing-in-hot-melt-packaging-adhesives.html">Preventing stringing in hot melt packaging adhesives</a>',
   '<span id="ref-ZS">[ZS]</span> Zhishang product brochure p.02 (nozzle warranty), p.06, p.08, p.10 (hot-glue models)'],
 toc_t='On this page', toc=[('answer','Answer'),('scf','Symptom / Cause / Fix'),('faq','FAQ'),('related','Related'),('models','Machines'),('refs','References')],
 upd='Last updated: 2026-10-13')

ZH = dict(lang='zh', title='热熔胶拉丝怎么办？原因与解决方法 | 至尚科技',
 crumbs='<a href="/zh/">首页</a> / <a href="/zh/guides/">技术问答</a> / 热熔胶拉丝',
 h1='热熔胶为什么拉丝？怎么解决？',
 answer='拉丝一般是胶嘴断胶不干净：胶嘴离工件太远、胶温偏低黏度偏高、工件太冷、胶嘴头损坏或碳化、电磁阀气压不足，或有风直吹胶线。',
 src='依据：H.B. Fuller《热熔胶故障排除指南》；Henkel《防止包装热熔胶拉丝》',
 scf_t='问题 / 原因 / 解决办法', scfh=['问题','原因','解决办法'],
 scf=[['胶线拖出细丝落到盒面',f'胶嘴离工件太远 {R("HBF-TS")} {R("HEN-STR")}',f'胶嘴贴近工件（H.B. Fuller：最好 1/4 英寸） {R("HBF-BP")}'],
      ['丝变粗、胶线发黏',f'胶温低、黏度高 {R("HBF-TS")} {R("HEN-STR")}',f'在胶水推荐范围内略微升温 {R("HBF-TS")} {R("HEN-STR")}'],
      ['早上或冬天更严重',f'纸板、面纸太冷 {R("HBF-TS")} {R("HEN-STR")}',f'材料先放到车间环境温度 {R("HBF-TS")} {R("HEN-STR")}'],
      ['温度正常仍拉丝',f'胶嘴头损坏或碳化，断胶不好 {R("HEN-STR")}',f'检查胶嘴是否堵塞、完好；检查过滤网和胶管有无碳化 {R("HEN-STR")}'],
      ['断胶慢、滴胶',f'电磁阀气压不足 {R("HBF-TS")}',f'进气压力要高于 50 psi，检查消声器积胶 {R("HBF-TS")}'],
      ['丝被吹歪',f'风扇或空调直吹 {R("HEN-STR")}',f'给上胶区挡风 {R("HEN-STR")}']],
 body='',
 faq_t='常见追问',
 faq=[('热熔胶的“天使发”是什么？','就是胶从胶嘴断不干净时被拉出来的细丝。这些细丝会在空中飘，落到设备和产品上。'),
      ('胶嘴离纸板多近合适？','H.B. Fuller 建议胶枪不要离工件太远，最好约 1/4 英寸（约 6 mm）。'),
      ('胶嘴磨损会导致拉丝吗？','会。Henkel 指出，胶嘴头损坏或有碳化，阀门就不能正常工作，断胶就不干净。')],
 rel_t='相关问题', rel=[('热熔胶为什么粘不牢？','/zh/guides/hot-glue-not-sticking/'),('热熔胶嘴堵塞、碳化怎么办？','/zh/guides/hot-melt-nozzle-clogging-charring/'),('精品盒用热熔胶还是白胶？','/zh/guides/hot-melt-vs-white-pva-glue/')],
 rec_t='用机器给精品盒划热熔胶', rec_p=f'至尚热胶机型「可以划热熔胶，压敏胶」，划胶宽度 3-10MM；「划胶枪嘴终身包修，包换（以旧换新）」 {R("ZS")}。工作气压 0.6MPa {R("ZS")}。', more='查看详情 →',
 cards=[dict(why='流水线或自动天地盒机连线',model='ZS-S088R-4',name='随线四轴划胶机-热胶',url='/zh/products/zs-s088r-4/',img='s088r-4',keys=[('有效尺寸','600*600*130MM/50*50*25MM'),('划胶宽度','3-10MM')]),
        dict(why='大尺寸盒子，单机作业',model='ZS-S088C-4',name='四轴柜式划胶机-热胶',url='/zh/products/zs-s088c-4/',img='s088c-4',keys=[('有效尺寸','900*600*150MM/50*50*10MM'),('划胶宽度','3-10MM')]),
        dict(why='刮热胶，替代双面胶',model='ZS-S088D-4',name='三轴柜式划胶机-热胶',url='/zh/products/zs-s088d-4/',img='s088d-4',keys=[('有效尺寸','900*600MM/50*50MM'),('划胶宽度','3-10MM')])],
 cta_h='想把手工胶枪换成机器划胶？', cta_p='把盒子尺寸和用胶发给我们，按配置报价。参数仅供参考，以报价为准。', cta_b='在线询价', cta_url='/zh/contact/#quote',
 ref_t='参考资料', refs=[x.replace('Hot Melt Adhesives Troubleshooting Guide','热熔胶故障排除指南').replace('Packaging Adhesive Best Practices','包装胶粘剂最佳实践').replace('Preventing stringing in hot melt packaging adhesives','防止包装热熔胶拉丝（英文）').replace('Zhishang product brochure p.02 (nozzle warranty), p.06, p.08, p.10 (hot-glue models)','至尚宣传手册 p.02（枪嘴保修）、p.06、p.08、p.10（热胶机型）') for x in EN['refs']],
 toc_t='本页目录', toc=[('answer','答案'),('scf','问题 / 原因 / 解决'),('faq','常见追问'),('related','相关问题'),('models','机型'),('refs','参考资料')],
 upd='最后更新：2026-10-13')

GUIDES=[('hot-melt-glue-stringing',EN,ZH)]
def guide_body(L,published,BASE='/'):
    zh=L['lang']=='zh'
    cards=''.join(f'''<div class="rec"><p class="why">{c['why']}</p><a class="pcard" href="{c['url']}"><img src="{BASE}img/{c['img']}.jpg" alt="{c['name']} {c['model']}" loading="lazy"><div><small>{c['model']}</small><h3>{c['name']}</h3><ul class="keys">{''.join(f'<li><span>{k}</span><code>{v}</code></li>' for k,v in c['keys'])}</ul><span class="more">{L['more']}</span></div></a></div>''' for c in L['cards'])
    scf_t='<div class="tbl"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in L['scfh'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in r)+'</tr>' for r in L['scf'])+'</tbody></table></div>'
    scf_m='<div class="scf-m">'+''.join(f'<details><summary>{r[0]}</summary><dl><dt>{L["scfh"][1]}</dt><dd>{r[1]}</dd><dt>{L["scfh"][2]}</dt><dd>{r[2]}</dd></dl></details>' for r in L['scf'])+'</div>'
    faqs=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in L['faq'])
    ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in L['faq']]}
    rel=[(t,u) for t,u in L['rel'] if u.rstrip('/').split('/')[-1] in published]
    toc=''.join(f'<a href="#{i}">{t}</a>' for i,t in L['toc'] if i!='related' or rel)
    relh=f'<h2 id="related">{L["rel_t"]}</h2><ul>'+''.join(f'<li><a href="{u}">{t}</a></li>' for t,u in rel)+'</ul>' if rel else ''
    return f'''<style>{CSS}</style>{'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>' if L['faq'] else ''}
<section style="padding-top:18px"><div class="wrap qa"><article>
<div class="crumbs">{L['crumbs']}</div>
<h1>{L['h1']}</h1>
<div class="ansbox" id="answer"><p>{L['answer']}</p></div><p class="src">{L['src']}</p>
<h2 id="scf">{L['scf_t']}</h2><div class="scf">{scf_t}{scf_m}</div>
{L['body']}
{f'<h2 id="faq">{L["faq_t"]}</h2><div class="faq">{faqs}</div>' if L['faq'] else ''}
{relh}
<h2 id="models">{L['rec_t']}</h2><p>{L['rec_p']}</p><div class="recs">{cards}</div>
<div class="ctab" id="quote"><h2>{L['cta_h']}</h2><p>{L['cta_p']}</p><a class="btn" href="{L['cta_url']}">{L['cta_b']}</a><a class="btn ghost" href="https://wa.me/8615820928436">WhatsApp</a></div>
<h2 id="refs">{L['ref_t']}</h2><ol class="refs">{''.join(f'<li>{r}</li>' for r in L['refs'])}</ol>
<p class="upd">{L['upd']}</p></article>
<aside class="toc"><b>{L['toc_t']}</b>{toc}</aside></div></section>'''
def desc(L): return re.sub(r'\s*\[\d\]','',re.sub('<[^>]+>','',L['answer']))[:155]

# Guides 02-06 (approved 2026-10-13), parsed from drafts/painpoints/*.md with machine cards.
import pathlib
def links(s): return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
def refs(s): return re.sub(r'\[(\d)\]',r'<a class="small" href="#ref-\1">[\1]</a>',s)
def fmt(s): return refs(links(re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)))
def parse(md,lang):
    fm=dict(re.findall(r'^(\w+): "?(.*?)"?$',md.split('---')[1],re.M))
    sec=re.search(rf'## {lang.upper()}\n(.*?)(?=\n## )',md,re.S).group(1)
    srcs=re.findall(r'^\d+\. (.+?): (https?://\S+)$',md.split('## Sources')[1],re.M)
    ans=re.search(r'> \*\*.*?\*\*\s*(.*)',sec).group(1)
    rows=[[c.strip() for c in l.strip('|').split('|')] for l in sec.splitlines() if l.startswith('|')]
    head,body=rows[0],rows[2:]
    paras=[l for l in sec.splitlines() if l.strip() and not l.startswith(('|','>'))]
    zh=lang=='zh'
    scf=[[r[0],r[1],r[2]+(' '+refs(r[3]) if len(r)>3 and r[3]!='—' else '')] for r in body]
    scf=[[fmt(x) for x in r] for r in scf]
    L=dict(lang=lang,title=fm['title_'+lang]+(' | 至尚科技' if zh else ' | Zhishang'),
      crumbs=('<a href="/zh/">首页</a> / <a href="/zh/guides/">技术问答</a> / ' if zh else '<a href="/">Home</a> / <a href="/guides/">Guides</a> / ')+fm['title_'+lang],
      h1=fm['title_'+lang],answer=fmt(ans),src=('依据：' if zh else 'Sources: ')+'；'.join(n for n,u in srcs),
      scf_t=' / '.join(head[:3]),scfh=head[:3],scf=scf,body=''.join(f'<p>{fmt(p)}</p>' for p in paras),
      faq_t='',faq=[],rel_t='',rel=[],rec_t='',rec_p='',more='',cards=[],
      cta_h='想把手工上胶换成机器划胶？' if zh else 'Moving gluing from hand to machine?',
      cta_p='把盒子尺寸和用胶发给我们，按配置报价。参数仅供参考，以报价为准。' if zh else 'Send us your box size and glue. Prices are quoted per configuration.',
      cta_b='在线询价' if zh else 'Request a Quote',cta_url='/zh/contact/#quote' if zh else '/contact/#quote',
      ref_t='参考资料' if zh else 'References',refs=[f'<span id="ref-{i+1}">[{i+1}]</span> <a href="{u}">{n}</a>' for i,(n,u) in enumerate(srcs)],
      toc_t='本页目录' if zh else 'On this page',toc=[('answer','答案' if zh else 'Answer'),('scf',' / '.join(head[:3])),('refs','参考资料' if zh else 'References')],
      upd=('最后更新：2026-10-13' if zh else 'Last updated: 2026-10-13'))
    return fm['slug'],L

M={'zs-s088e-4':('s088e-4','随线四轴划胶机-冷胶','Inline 4-Axis Cold Glue Dispensing Machine for Rigid Boxes','流水线或自动天地盒机连线（冷胶）','Inline with a box line (cold glue)','600*600*130MM/50*50*25MM'),
 'zs-s088r-4':('s088r-4','随线四轴划胶机-热胶','Inline 4-Axis Hot Melt Gluing Machine for Rigid Boxes','流水线或自动天地盒机连线（热胶）','Inline with a box line (hot melt)','600*600*130MM/50*50*25MM'),
 'zs-s088c':('s088c','四轴柜式划胶机-冷胶','4-Axis Cabinet Cold Glue Dispensing Machine','大尺寸盒子，单机作业（冷胶）','Larger boxes, standalone (cold glue)','900*600*150MM/50*50*10MM'),
 'zs-s088c-4':('s088c-4','四轴柜式划胶机-热胶','4-Axis Cabinet Hot Melt Glue Dispensing Machine','大尺寸盒子，单机作业（热胶）','Larger boxes, standalone (hot melt)','900*600*150MM/50*50*10MM'),
 'zs-s088d':('s088d','三轴柜式划胶机-冷胶','3-Axis Cabinet Cold Glue Dispensing Machine','三轴柜式，单机作业（冷胶）','3-axis cabinet, standalone (cold glue)','900*600MM/50*50MM'),
 'zs-s088d-4':('s088d-4','三轴柜式划胶机-热胶','3-Axis Cabinet Hot Melt Glue Dispensing Machine','刮热胶，替代双面胶','Hot glue to replace double-sided tape','900*600MM/50*50MM')}
PICK={'02':['zs-s088e-4','zs-s088r-4'],'03':['zs-s088r-4','zs-s088c-4','zs-s088d-4'],'04':['zs-s088e-4','zs-s088r-4'],'05':['zs-s088e-4','zs-s088r-4'],'06':['zs-s088e-4','zs-s088r-4','zs-s088c','zs-s088d','zs-s088d-4']}
def add_cards(L,num):
    zh=L['lang']=='zh'
    L['rec_t']='相关机型' if zh else 'Related machines'
    L['rec_p']=('至尚划胶机按程序路径自动划胶，划胶宽度 3-10MM，工作气压 0.6MPa（宣传手册）。参数仅供参考，以报价为准。' if zh else 'Zhishang machines dispense glue along a programmed path, with a 3-10MM glue width and 0.6MPa working air pressure (product brochure). Specifications are for reference only; final specifications are subject to our quotation.')
    L['more']='查看详情 →' if zh else 'View details →'
    L['cards']=[dict(why=M[k][3 if zh else 4],model=k.upper(),name=M[k][1 if zh else 2],url=('/zh' if zh else '')+f'/products/{k}/',img=M[k][0],keys=[('有效尺寸' if zh else 'Effective size',M[k][5]),('划胶宽度' if zh else 'Glue line width','3-10MM')]) for k in PICK[num]]
    L['toc'].insert(-1,('models','机型' if zh else 'Machines'))
for _f in sorted((pathlib.Path(__file__).parent/'drafts/painpoints').glob('0[2-6]-*.md')):
    _md=_f.read_text(); _s,_en=parse(_md,'en'); _,_zh=parse(_md,'zh')
    add_cards(_en,_f.stem[:2]); add_cards(_zh,_f.stem[:2]); GUIDES.append((_s,_en,_zh))

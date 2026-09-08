# Builds the Payhip images for the three coaching plans.
# One template, three sets of numbers — the dot grid is the same language the
# site uses on the package cards, so a buyer sees the same thing twice.
import io, sys, os
D = os.path.dirname(os.path.abspath(__file__))

PLANS = [
  dict(slug='weekly', eyebrow='Monthly coaching', name='Weekly',
       n='4', price='€259', dots=1, badge='4 sessions a month',
       sub='One paper a month, taken<br>the way it is actually marked.',
       bullets=[('The full method','5 modules, 7 workbooks, 6 audios'),
                ('Four 50-minute sessions','one to one, on video'),
                ('Each paper rehearsed once','all four, in turn')]),
  dict(slug='twice-weekly', eyebrow='Most chosen', name='Twice weekly',
       n='8', price='€499', dots=2, badge='8 sessions a month',
       sub='Learn a paper, then sit it<br>under timed conditions.',
       bullets=[('Everything in Weekly','at twice the pace'),
                ('Eight 50-minute sessions','one to one, on video'),
                ('A timed mock of each paper','marked and talked through')]),
  dict(slug='intensive', eyebrow='Monthly coaching', name='Intensive',
       n='12', price='€699', dots=3, badge='12 sessions a month',
       sub='Three a week, until sitting<br>the paper is dull.',
       bullets=[('Everything in Twice weekly','at three a week'),
                ('Twelve 50-minute sessions','taught by Antoine himself'),
                ('A full mock exam','spoken and written, end to end')]),
]
SKILLS = ['Listening','Reading','Writing','Speaking']

FONTS = """
@font-face{font-family:PF;src:url(font6.ttf);font-weight:700;}
@font-face{font-family:PF;src:url(font7.ttf);font-weight:800;}
@font-face{font-family:PF;src:url(font5.ttf);font-weight:700;font-style:italic;}
@font-face{font-family:IN;src:url(font4.ttf);font-weight:400;}
@font-face{font-family:IN;src:url(font3.ttf);font-weight:500;}
@font-face{font-family:IN;src:url(font2.ttf);font-weight:600;}
@font-face{font-family:IN;src:url(font1.ttf);font-weight:700;}
"""

def grid(p, scale=1.0):
    rows=[]
    for s in SKILLS:
        d=''.join('<i class="d%s"></i>'%(' on' if k<p['dots'] else '') for k in range(3))
        rows.append('<div class="r"><span class="p">%s</span><span class="ds">%s</span></div>'%(s,d))
    return '<div class="cv">%s</div>'%''.join(rows)

def bullets(p):
    return ''.join('<li><b>%s</b> — %s</li>'%(a,b) for a,b in p['bullets'])

LAND = """<!doctype html><meta charset="utf-8"><style>%(fonts)s
*{margin:0;padding:0;box-sizing:border-box;}
body{width:1600px;height:900px;overflow:hidden;background:#0c2a2a;font-family:IN;
 display:grid;grid-template-columns:590px 1fr;align-items:center;gap:84px;padding:0 96px;position:relative;}
body::before{content:"";position:absolute;inset:0;
 background:radial-gradient(1000px 680px at 22%% 44%%, rgba(212,180,99,.16), transparent 62%%);}
.left{position:relative;text-align:center;}
.num{font-family:PF;font-weight:800;font-size:300px;line-height:1;color:#d4b463;letter-spacing:-.04em;}
.numsub{font-family:PF;font-style:italic;font-weight:700;font-size:38px;color:#f6f1e4;margin-top:14px;}
.per{font-size:19px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#7f9a90;margin-top:20px;}
.cv{margin-top:46px;display:grid;gap:15px;padding:0 66px;}
.r{display:flex;align-items:center;justify-content:space-between;}
.p{font-size:21px;color:#a9bfb6;}
.ds{display:flex;gap:9px;}
.d{width:15px;height:15px;border-radius:50%%;border:2px solid rgba(212,180,99,.42);}
.d.on{background:#d4b463;border-color:#d4b463;}
.right{position:relative;}
.eyebrow{font-size:19px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#d4b463;}
h1{font-family:PF;font-weight:800;font-size:86px;line-height:1.03;color:#f6f1e4;letter-spacing:-.022em;margin-top:24px;}
.sub{font-family:PF;font-style:italic;font-weight:700;font-size:31px;color:#a9bfb6;margin-top:22px;line-height:1.32;}
ul{list-style:none;margin-top:40px;}
li{position:relative;padding-left:34px;font-size:23px;line-height:1.5;color:#cfe0d8;margin-top:17px;}
li::before{content:"";position:absolute;left:0;top:16px;width:19px;height:2px;background:#a8843c;}
li b{color:#f6f1e4;font-weight:600;}
.foot{margin-top:50px;display:flex;align-items:center;gap:18px;}
.pill{font-size:17px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0c2a2a;background:#d4b463;padding:11px 22px;border-radius:100px;}
.site{font-size:19px;color:#8aa39a;}
</style>
<div class="left">
  <div class="num">%(n)s</div>
  <div class="numsub">50-minute sessions</div>
  <div class="per">every month</div>
  %(grid)s
</div>
<div class="right">
  <div class="eyebrow">%(eyebrow)s</div>
  <h1>%(name)s</h1>
  <div class="sub">%(sub)s</div>
  <ul>%(bullets)s</ul>
  <div class="foot"><span class="pill">%(price)s / month</span><span class="site">delfmasterclass.com</span></div>
</div>"""

SQ = """<!doctype html><meta charset="utf-8"><style>%(fonts)s
*{margin:0;padding:0;box-sizing:border-box;}
body{width:1200px;height:1200px;overflow:hidden;background:#0c2a2a;font-family:IN;
 display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 92px;position:relative;}
body::before{content:"";position:absolute;inset:0;
 background:radial-gradient(880px 760px at 50%% 38%%, rgba(212,180,99,.17), transparent 64%%);}
.w{position:relative;width:100%%;}
.eyebrow{font-size:22px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;color:#d4b463;}
.num{font-family:PF;font-weight:800;font-size:262px;line-height:1;color:#d4b463;letter-spacing:-.04em;margin-top:22px;}
.numsub{font-size:25px;font-weight:600;letter-spacing:.06em;color:#a9bfb6;margin-top:14px;}
h1{font-family:PF;font-weight:800;font-size:84px;line-height:1.04;color:#f6f1e4;letter-spacing:-.022em;margin-top:30px;}
.sub{font-family:PF;font-style:italic;font-weight:700;font-size:33px;color:#a9bfb6;margin-top:20px;line-height:1.34;}
.cv{margin-top:50px;display:grid;gap:16px;padding:0 268px;}
.r{display:flex;align-items:center;justify-content:space-between;}
.p{font-size:24px;color:#a9bfb6;}
.ds{display:flex;gap:11px;}
.d{width:17px;height:17px;border-radius:50%%;border:2px solid rgba(212,180,99,.42);}
.d.on{background:#d4b463;border-color:#d4b463;}
.foot{margin-top:60px;display:flex;align-items:center;justify-content:center;gap:20px;}
.pill{font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0c2a2a;background:#d4b463;padding:13px 26px;border-radius:100px;}
.site{font-size:21px;color:#8aa39a;}
</style>
<div class="w">
  <div class="eyebrow">%(eyebrow)s</div>
  <div class="num">%(n)s</div>
  <div class="numsub">50-minute sessions every month</div>
  <h1>%(name)s</h1>
  <div class="sub">%(sub)s</div>
  %(grid)s
  <div class="foot"><span class="pill">%(price)s / month</span><span class="site">delfmasterclass.com</span></div>
</div>"""

for p in PLANS:
    ctx = dict(p, fonts=FONTS, grid=grid(p), bullets=bullets(p))
    io.open(os.path.join(D,'plan-%s-product.html'%p['slug']),'w',encoding='utf-8').write(LAND % ctx)
    io.open(os.path.join(D,'plan-%s-square.html'%p['slug']),'w',encoding='utf-8').write(SQ % ctx)
    print('écrit', p['slug'])

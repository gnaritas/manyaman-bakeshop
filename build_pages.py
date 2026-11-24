#!/usr/bin/env python3
"""Man Yaman Bake Shop — Vernon, CT. Template-v2 multi-page site build.
Every claim traced in evidence.json (card t_5fc04d16): menu/hours from Patch Vernon
opening coverage (2026-11-20); address-unit/phone/email from the shop's own FB Page
intro; geo/ZIP from OSM Nominatim geocode of 101 West Street Vernon. Unknowns
(prices, owner names) omitted — never guessed. Zero JS beyond the CSS checkbox drawer.
Design: 'kakanin layers' — ube purple + cream + sapin-sapin stripe accents.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://manyaman-bakeshop-demo.up.railway.app'
BRAND = 'Man Yaman Bake Shop'
CITY = 'Vernon, CT'
STREET = '101 West Street, Unit B'
ZIP = '06066'
FULL_ADDR = '101 West Street, Unit B, Vernon, CT 06066'
PHONE_D = '(860) 281-4546'
PHONE_T = '+18602814546'
EMAIL = 'manyamanbakeshop@gmail.com'
FB = 'https://www.facebook.com/manyamanbakeshop'
IG = 'https://www.instagram.com/manyamanbakeshop'
LAT, LON = 41.8622488, -72.4657632  # OSM Nominatim exact match, 101 West Street, Vernon Center (evidence.json)
MAPQ = 'https://www.google.com/maps?q=101%20West%20St%2C%20Vernon%2C%20CT%2006066'
EMBED = 'https://www.google.com/maps?q=101+West+St,+Vernon,+CT+06066&output=embed'

# --- menu (verbatim item descriptions from Patch Vernon opening coverage) ---
BREADS = [
    ('Classic Pandesal', 'Lightly sweet, airy Filipino bread rolls coated in breadcrumbs.'),
    ('Moringa Pandesal', 'Sweet bread rolls made with moringa, also known as malunggay, leaves.'),
    ('Ube-Cheese Pandesal', 'Soft bread rolls filled with purple yam and cheese.'),
    ('Filipino Cheese Bread', 'Soft rolls topped with a sweet-and-savory cheese crumble.'),
    ('Spanish Bread', 'Soft rolls filled with a buttery breadcrumb and sugar mixture.'),
    ('Pan de Coco', 'Sweet yeast rolls filled with caramelized shredded coconut.'),
    ('Pan de Mungo', 'Fluffy buns filled with sweet red mung bean paste.'),
    ('Classic Ensaymada', 'Buttery Filipino brioche topped with butter, sugar and grated cheese.'),
    ('Special Ensaymada', 'Rich Filipino brioche topped with butter, sugar and aged cheese.'),
]
SAVORY = [
    ('Chicken Empanada', 'Flaky pastry filled with seasoned chicken and vegetables.'),
    ('Pork Empanada', 'Baked pastry filled with seasoned ground pork and vegetables.'),
]
COOKIES = [
    ('Ube White Chocolate Chip Cookies', 'Ube cookies studded with white chocolate.'),
    ('Chocolate Chip Cookies', 'Classic chocolate chip cookies.'),
    ('Oatmeal Raisin Cookies', 'Oatmeal raisin cookies.'),
]
CAKES = [
    ('Ube Cake Roll', 'Sponge cake rolled with purple yam cream filling.'),
    ('Ube Cake', 'Layered purple yam cake with light frosting.'),
    ('Ube Flan Cake', 'Purple yam sponge cake topped with caramel leche flan.'),
]
KAKANIN = [
    ('Sapin-Sapin', 'Multicolored layered rice cake featuring jackfruit, coconut and purple yam flavors.'),
    ('Bibingka', 'Traditional baked rice cake made with coconut milk and topped with cheese and salted egg.'),
    ('Biko', 'Sticky rice cooked with coconut milk and brown sugar, topped with toasted coconut cream.'),
    ('Ube Biko', 'Sticky rice infused with purple yam flavor.'),
    ('Kutsinta', 'Chewy steamed rice cakes served with grated coconut.'),
    ('Puto Cheese', 'Steamed rice cakes topped with cheese.'),
    ('Cassava Cake', 'Baked cake made with grated cassava and sweet coconut milk.'),
    ('Maja Blanca', 'Coconut pudding with sweet corn and toasted coconut.'),
    ('Leche Flan', 'Rich custard topped with caramel syrup.'),
    ('Binangkal', 'Fried dough balls coated with sesame seeds.'),
]

HOURS_ROWS = [
    ('Monday', 'Closed'),
    ('Tuesday', '7 a.m.–noon · 2–6 p.m.'),
    ('Wednesday', '7 a.m.–noon · 2–6 p.m.'),
    ('Thursday', '7 a.m.–noon · 2–6 p.m.'),
    ('Friday', '7 a.m.–noon · 2–6 p.m.'),
    ('Saturday', '7 a.m.–noon · 2–5 p.m.'),
    ('Sunday', '6–9 a.m. · 2–5 p.m.'),
]

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<!-- BUILT-2026-11-24 -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com">
</head>
<body>'''

NAV = f'''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">Man&nbsp;Yaman <span>Bake&nbsp;Shop</span></a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/breads">Breads</a>
    <a href="/kakanin">Kakanin</a>
    <a href="/about">Our&nbsp;Story</a>
    <a href="/contact">Visit</a>
    <a class="btn btn-sm" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D.replace("(", "").replace(")", "").replace(" ", "-")}</a>
  </nav>
</header>'''

FOOTER = f'''<footer class="foot">
  <div class="footgrid">
    <div class="footcol">
      <p class="fbrand">{BRAND}</p>
      <p>{STREET}<br>Vernon, CT {ZIP}</p>
      <p><a href="tel:{PHONE_T}">{PHONE_D}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="footcol">
      <p class="fcap">Explore</p>
      <p><a href="/menu">Full&nbsp;Menu</a><br><a href="/breads">Breads&nbsp;&amp;&nbsp;Empanadas</a><br><a href="/kakanin">Kakanin&nbsp;&amp;&nbsp;Cakes</a><br><a href="/about">Our&nbsp;Story</a></p>
    </div>
    <div class="footcol">
      <p class="fcap">Open</p>
      <p>Tue–Fri&nbsp;7–12&nbsp;&amp;&nbsp;2–6<br>Sat&nbsp;7–12&nbsp;&amp;&nbsp;2–5<br>Sun&nbsp;6–9&nbsp;&amp;&nbsp;2–5<br>Mon&nbsp;closed</p>
    </div>
    <div class="footcol">
      <p class="fcap">Follow</p>
      <p><a href="{FB}" rel="noopener">Facebook</a><br><a href="{IG}" rel="noopener">Instagram</a></p>
    </div>
  </div>
  <p class="footline">{BRAND} · Vernon, CT · © 2026</p>
</footer>'''

def breadcrumbs(name, path):
    nodes = [
        {'@type': 'BreadcrumbListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'},
        {'@type': 'BreadcrumbListItem', 'position': 2, 'name': name, 'item': ORIGIN + path},
    ]
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': nodes}, ensure_ascii=False)

HOURS_LD = []
_slot = {'Tu': [('07:00', '12:00'), ('14:00', '18:00')],
         'We': [('07:00', '12:00'), ('14:00', '18:00')],
         'Th': [('07:00', '12:00'), ('14:00', '18:00')],
         'Fr': [('07:00', '12:00'), ('14:00', '18:00')],
         'Sa': [('07:00', '12:00'), ('14:00', '17:00')],
         'Su': [('06:00', '09:00'), ('14:00', '17:00')]}
for _d, _slots in _slot.items():
    for _o, _c in _slots:
        HOURS_LD.append({'@type': 'OpeningHoursSpecification', 'dayOfWeek': _d, 'opens': _o, 'closes': _c})

def menu_ld():
    secs = [
        ('Baked Goods', BREADS), ('Cakes and Sweets', CAKES), ('Cookies', COOKIES),
        ('Savory Goods', SAVORY), ('Traditional Filipino Desserts (Kakanin)', KAKANIN),
    ]
    return [
        {'@type': 'MenuSection', 'name': nm,
         'hasMenuItem': [{'@type': 'MenuItem', 'name': i, 'description': d} for i, d in lst]}
        for nm, lst in secs
    ]

def ld_home():
    bakery = {
        '@context': 'https://schema.org', '@type': 'Bakery',
        '@id': ORIGIN + '/#bakery',
        'name': BRAND,
        'alternateName': 'ManYaman Bakeshop',
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'telephone': '+1 860-281-4546',
        'email': EMAIL,
        'servesCuisine': 'Filipino',
        'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Vernon',
                    'addressRegion': 'CT', 'postalCode': ZIP, 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'openingHoursSpecification': HOURS_LD,
        'sameAs': [FB, IG],
        'hasMenu': {'@type': 'BakeryMenu', 'name': f'{BRAND} menu', 'hasMenuSection': menu_ld()},
    }
    faq = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [
            {'@type': 'Question', 'name': 'Where is Man Yaman Bake Shop?',
             'acceptedAnswer': {'@type': 'Answer', 'text': f'At {FULL_ADDR}. Call {PHONE_D} any time.'}},
            {'@type': 'Question', 'name': 'When are you open?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'Tuesday through Friday 7 a.m.–noon and 2–6 p.m., Saturday 7 a.m.–noon and 2–5 p.m., Sunday 6–9 a.m. and 2–5 p.m. Closed Monday.'}},
            {'@type': 'Question', 'name': 'What is kakanin?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'Kakanin are traditional Filipino rice cakes and desserts — at Man Yaman that includes sapin-sapin, bibingka, biko, ube biko, kutsinta, puto cheese, cassava cake, maja blanca, leche flan and binangkal.'}},
            {'@type': 'Question', 'name': 'What should I try first?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'Classic pandesal early in the day, Spanish bread or ensaymada for celebrations, and sapin-sapin or ube biko for something sweet.'}},
        ],
    }
    return [json.dumps(bakery, ensure_ascii=False), json.dumps(faq, ensure_ascii=False)]

def ld_page(name, path, desc=None, service=None):
    out = [breadcrumbs(name, path)]
    if service:
        svc = {
            '@context': 'https://schema.org', '@type': 'Service',
            'name': service, 'description': desc or service,
            'areaServed': {'@type': 'City', 'name': 'Vernon', 'addressRegion': 'CT'},
            'provider': {'@type': 'Bakery', 'name': BRAND,
                         'address': {'@type': 'PostalAddress', 'streetAddress': STREET,
                                     'addressLocality': 'Vernon', 'addressRegion': 'CT',
                                     'postalCode': ZIP, 'addressCountry': 'US'}},
        }
        out.append(json.dumps(svc, ensure_ascii=False))
    return out

def item_rows(items):
    out = []
    for nm, d in items:
        out.append(f'      <li><b>{nm}</b><span>{d}</span></li>')
    return '\n'.join(out)

def sec(cat, items, lead=None, cls=''):
    leadp = f'<p class="seclead">{lead}</p>' if lead else ''
    return f'''<section class="cat {cls}">
  <h2>{cat}</h2>
  {leadp}
  <ul class="items">
{item_rows(items)}
  </ul>
</section>'''

def strip():
    return '<div class="layers" aria-hidden="true"></div>'

def hero(kicker, h1, lead, cta):
    return f'''<section class="hero">
  <p class="kicker">{kicker}</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <p class="cta">
    <a class="btn btn-big" href="/menu">See&nbsp;the&nbsp;Menu</a>
    <a class="btn btn-ghost btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a>
  </p>
  {strip()}
</section>'''

STYLE = '''*{margin:0;padding:0;box-sizing:border-box}
:root{
  --ube:#46194a;--ube2:#63335f;--plum:#8d5587;--gold:#d29a2f;--jade:#3f7050;--pink:#c4708c;
  --cream:#fbf3e6;--panel:#fffdf8;--ink:#241327;--mist:#6d5c70;--line:#e8dcc8;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
html{scroll-behavior:smooth}
body{background:var(--cream);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.55}
p{overflow-wrap:break-word}
a{color:var(--ube)}
.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:var(--ube);color:#fff;padding:8px 12px;z-index:20}
header.site{display:flex;align-items:center;gap:14px;flex-wrap:wrap;max-width:1080px;margin:0 auto;padding:14px 20px}
.brand{font-family:var(--serif);font-size:1.55rem;color:var(--ube);text-decoration:none;letter-spacing:.4px}
.brand span{font-size:1.05rem;color:var(--plum)}
.navtoggle{position:absolute;opacity:0;pointer-events:none}
.navbtn{margin-left:auto;display:flex;flex-direction:column;gap:5px;padding:8px 4px;cursor:pointer}
.navbtn i,.navbtn i::before,.navbtn i::after{content:"";display:block;width:26px;height:3px;background:var(--ube);border-radius:2px;position:relative}
.navbtn i::before{position:absolute;top:-8px}
.navbtn i::after{position:absolute;top:8px}
nav.links{display:none;width:100%}
.navtoggle:checked ~ nav.links{display:flex;flex-direction:column;gap:2px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px}
nav.links a{padding:9px 10px;text-decoration:none;color:var(--ink);border-radius:7px;font-size:.98rem}
nav.links a:hover{background:var(--cream);color:var(--ube)}
.btn{display:inline-block;background:var(--ube);color:#fff;text-decoration:none;border-radius:9px;font-weight:600;border:2px solid var(--ube)}
.btn:hover{background:var(--ube2);border-color:var(--ube2)}
.btn-big{padding:13px 22px;font-size:1.02rem}
.btn-sm{padding:8px 13px;font-size:.9rem;color:#fff}
.btn-sm:hover{color:#fff}
.btn-ghost{background:transparent;color:var(--ube)}
.btn-ghost:hover{background:var(--ube);color:#fff}
.hero{max-width:1080px;margin:0 auto;padding:48px 20px 0}
.kicker{font-size:.8rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:14px}
h1{font-family:var(--serif);font-size:clamp(2rem,5.4vw,3.3rem);line-height:1.14;color:var(--ube);max-width:24ch}
h1 em{font-style:italic;color:var(--plum)}
.lead{margin-top:18px;font-size:1.1rem;color:var(--mist);max-width:58ch}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}
.layers{height:10px;margin-top:40px;border-radius:5px;background:linear-gradient(90deg,var(--gold) 0 34%,var(--jade) 34% 67%,var(--plum) 67% 100%)}
.layers.slim{height:6px;margin-top:22px}
main{max-width:1080px;margin:0 auto;padding:10px 20px 56px}
.pagehead{padding:40px 0 4px}
.pagehead h1{max-width:26ch}
section.cat{padding:38px 0 6px}
section.cat h2{font-family:var(--serif);font-size:1.7rem;color:var(--ube);border-bottom:3px solid var(--gold);display:inline-block;padding-bottom:4px;margin-bottom:14px}
.seclead{color:var(--mist);margin-bottom:12px;max-width:60ch}
ul.items{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:10px 34px}
ul.items li{padding:11px 0 11px 16px;border-left:3px solid var(--line)}
ul.items li:nth-child(3n+1){border-left-color:var(--gold)}
ul.items li:nth-child(3n+2){border-left-color:var(--jade)}
ul.items li:nth-child(3n+3){border-left-color:var(--plum)}
ul.items li b{font-family:var(--serif);font-size:1.12rem;color:var(--ink);display:block}
ul.items li span{display:block;color:var(--mist);font-size:.97rem;margin-top:2px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;padding:22px 0 6px}
.card{background:var(--panel);border:1px solid var(--line);border-top:5px solid var(--gold);border-radius:12px;padding:20px 18px}
.card:nth-child(3n+2){border-top-color:var(--jade)}
.card:nth-child(3n+3){border-top-color:var(--plum)}
.card h3{font-family:var(--serif);font-size:1.25rem;color:var(--ube);margin-bottom:8px}
.card p{color:var(--mist);font-size:.97rem}
.card a{font-weight:600}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:28px 24px;margin-top:34px}
.panel h2{font-family:var(--serif);font-size:1.5rem;color:var(--ube);margin-bottom:12px}
.address{font-size:1.05rem}
.address strong{font-family:var(--serif);font-size:1.15rem;color:var(--ube);display:block;margin-bottom:4px}
table.hours{border-collapse:collapse;margin-top:14px;width:100%;max-width:420px}
table.hours th{text-align:left;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);padding:6px 0}
table.hours td{padding:7px 0;border-bottom:1px solid var(--line);font-size:.98rem;color:var(--mist)}
table.hours tr th{color:var(--ink);font-family:var(--serif);font-size:1rem;text-transform:none;letter-spacing:0;width:9.5em}
blockquote{font-family:var(--serif);font-size:1.2rem;line-height:1.5;color:var(--ube);border-left:4px solid var(--gold);padding:6px 0 6px 20px;margin:22px 0}
blockquote p{margin-bottom:10px}
.byline{font-family:var(--sans);font-size:.9rem;color:var(--mist);letter-spacing:.06em}
.mapwrap{margin-top:26px}
.mapwrap iframe{width:100%;height:340px;border:1px solid var(--line);border-radius:12px;display:block;background:var(--panel)}
form.contact{display:grid;gap:14px;margin-top:14px;max-width:560px}
form.contact label{font-weight:600;font-size:.94rem;display:grid;gap:5px}
form.contact input,form.contact textarea{font:inherit;padding:11px 12px;border:1px solid var(--line);border-radius:8px;background:#fff;color:var(--ink);width:100%}
form.contact textarea{min-height:130px;resize:vertical}
form.contact button{justify-self:start}
.links-two{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;margin-top:18px}
.links-two a{font-weight:600}
.privacy p{margin-bottom:14px;max-width:70ch}
footer.foot{background:var(--ube);color:#f3e9ef;margin-top:30px}
.footgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:22px;max-width:1080px;margin:0 auto;padding:34px 20px 18px}
.footcol p{font-size:.95rem;line-height:1.6}
.fbrand{font-family:var(--serif);font-size:1.25rem;color:#fff;margin-bottom:6px}
.fcap{font-size:.76rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:8px;font-weight:700}
.footcol a{color:#f3e9ef;text-decoration:underline;text-underline-offset:3px}
.footcol a:hover{color:#fff}
.footline{border-top:1px solid rgba(255,255,255,.18);max-width:1080px;margin:0 auto;padding:14px 20px 26px;font-size:.84rem;color:#cdbcd0}
.err404 h1{font-size:clamp(2.2rem,7vw,3.6rem)}
@media (min-width:900px){
  .navbtn{display:none}
  .navtoggle{display:none}
  nav.links{display:flex;flex-direction:row;gap:4px;width:auto;margin-left:auto}
  .hero{padding-top:64px}
  .panel{padding:38px 36px}
  .split{display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:start}
  .split .mapwrap{margin-top:0}
}
'''

# ============ pages ============
PAGES = {}

# home
home_ld = ld_home()
PAGES['index.html'] = (head(f'{BRAND} — Filipino Bakeshop in {CITY}',
    f'Traditional Filipino baked goods — pandesal, ensaymada, sapin-sapin, bibingka, ube cakes and empanadas — now baking at 101 West Street, Vernon, CT {ZIP}.',
    '/') + NAV + '<main id="main">' +
hero(f'Vernon, Connecticut · Now Open',
     'Pandesal at dawn,<br><em>kakanin to remember.</em>',
     f'Traditional Filipino baked goods, cakes, cookies, savory pastries and desserts — flavors and recipes rooted in Filipino cuisine, baked at 101 West Street in {CITY}.',
     '') +
f'''<section class="cat">
  <h2>Fresh Every Morning</h2>
  <p class="seclead">The bread case opens early: airy pandesal coated in breadcrumbs, ensaymada crowned with butter and cheese, and rolls filled with ube, coconut and mung bean.</p>
  <div class="cards">
    <div class="card"><h3>Pandesal</h3><p>Classic, moringa, and ube-cheese rolls — the heart of a Filipino breakfast.</p><p><a href="/breads">All the breads →</a></p></div>
    <div class="card"><h3>Kakanin</h3><p>Sapin-sapin, bibingka, biko, kutsinta and more traditional rice cakes and desserts.</p><p><a href="/kakanin">All the kakanin →</a></p></div>
    <div class="card"><h3>Cakes &amp; Empanadas</h3><p>Ube cake roll, ube flan cake, and flaky chicken and pork empanadas.</p><p><a href="/menu">Full menu →</a></p></div>
  </div>
</section>
<section class="panel">
  <div class="split">
    <div>
      <h2>Come Say Hello</h2>
      <p class="address"><strong>{BRAND}</strong>{STREET}<br>Vernon, CT {ZIP}<br><a href="tel:{PHONE_T}">{PHONE_D}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <table class="hours" aria-label="Hours of operation">
        <tr><th scope="col">Day</th><th scope="col">Hours</th></tr>
''' + '\n'.join(f'        <tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in HOURS_ROWS) + f'''      </table>
      <p style="margin-top:16px"><a class="btn" href="{MAPQ}" rel="noopener">Get Directions</a> <a class="btn btn-ghost" href="/contact">Contact Us</a></p>
    </div>
    <div class="mapwrap"><iframe title="Map to {BRAND}, {STREET}, Vernon, CT" src="{EMBED}" loading="lazy"></iframe></div>
  </div>
</section>
</main>''' + FOOTER +
f'''<script type="application/ld+json">{home_ld[0]}</script>
<script type="application/ld+json">{home_ld[1]}</script>
</body></html>''')

# menu hub
PAGES['menu.html'] = (head(f'Menu — {BRAND}, {CITY}',
    'The full Man Yaman Bake Shop menu: pandesal, ensaymada, ube cakes, empanadas, cookies, and kakanin including sapin-sapin, bibingka, biko and leche flan. Vernon, CT.',
    '/menu') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">The Case &amp; The Cooler</p>
<h1>Everything we<br><em>bake for you.</em></h1>
<p class="lead">Breads and sweets, savory pastries and traditional kakanin — ask at the counter for the day&rsquo;s freshest trays.</p>
<p class="cta"><a class="btn btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a> <a class="btn btn-ghost btn-big" href="{MAPQ}" rel="noopener">Get&nbsp;Directions</a></p>
</div>''' + strip() +
sec('Baked Goods', BREADS) +
sec('Cakes and Sweets', CAKES) +
sec('Cookies', COOKIES) +
sec('Savory Goods', SAVORY) +
sec('Traditional Filipino Desserts (Kakanin)', KAKANIN, cls='last') +
'</main>' + FOOTER +
f'''<script type="application/ld+json">{breadcrumbs("Menu", "/menu")}</script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BakeryMenu","name":BRAND + " menu","inLanguage":"en","hasMenuSection":menu_ld()}, ensure_ascii=False)}</script>
</body></html>''')

# breads detail
breads_ld = ld_page('Breads &amp; Empanadas', '/breads',
    'Pandesal, ensaymada, Spanish bread, pan de coco and Filipino empanadas baked daily at Man Yaman Bake Shop in Vernon, CT.',
    'Filipino Breads & Savory Pastries')
PAGES['breads.html'] = (head(f'Pandesal, Ensaymada &amp; Baked Breads — {BRAND}, {CITY}',
    'Pandesal (classic, moringa, ube-cheese), Filipino cheese bread, Spanish bread, pan de coco, ensaymada, empanadas and cookies — baked daily in Vernon, CT.',
    '/breads') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">The Bread Case</p>
<h1>Pandesal, ensaymada<br>&amp; <em>the good rolls.</em></h1>
<p class="lead">Soft, sweet-savory Filipino breads baked through the morning — plus flaky empanadas and cookies for the box on the way home.</p>
<p class="cta"><a class="btn btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a> <a class="btn btn-ghost btn-big" href="/kakanin">Kakanin&nbsp;→</a></p>
</div>''' + strip() +
sec('Baked Goods', BREADS) +
sec('Savory Goods', SAVORY) +
sec('Cookies', COOKIES, cls='last') +
'</main>' + FOOTER +
f'''<script type="application/ld+json">{breads_ld[0]}</script>
<script type="application/ld+json">{breads_ld[1]}</script>
</body></html>''')

# kakanin detail
kakanin_ld = ld_page('Kakanin &amp; Cakes', '/kakanin',
    'Sapin-sapin, bibingka, biko, kutsinta, puto cheese, cassava cake, maja blanca, leche flan and ube cakes at Man Yaman Bake Shop, Vernon, CT.',
    'Traditional Filipino Kakanin & Cakes')
PAGES['kakanin.html'] = (head(f'Kakanin — Sapin-Sapin, Bibingka &amp; Ube Biko — {BRAND}, {CITY}',
    'Traditional Filipino rice cakes and desserts: sapin-sapin, bibingka, biko, kutsinta, cassava cake, maja blanca, leche flan, plus ube cake and ube flan cake. Vernon, CT.',
    '/kakanin') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">The Kakanin Counter</p>
<h1>Sapin-sapin, bibingka<br>&amp; <em>ube everything.</em></h1>
<p class="lead">Kakanin — the traditional rice cakes and coconut desserts of the Philippines — made the long way, alongside ube cakes for every celebration.</p>
<p class="cta"><a class="btn btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a> <a class="btn btn-ghost btn-big" href="/breads">Breads&nbsp;→</a></p>
</div>''' + strip() +
sec('Cakes and Sweets', CAKES) +
sec('Traditional Filipino Desserts (Kakanin)', KAKANIN, cls='last') +
'</main>' + FOOTER +
f'''<script type="application/ld+json">{kakanin_ld[0]}</script>
<script type="application/ld+json">{kakanin_ld[1]}</script>
</body></html>''')

# about
PAGES['about.html'] = (head(f'Our Story — {BRAND}, {CITY}',
    'Man Yaman Bake Shop opened in November 2026 at 101 West Street in Vernon, CT with traditional Filipino baked goods, cakes and kakanin.',
    '/about') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">Our Story</p>
<h1>A Filipino bake shop<br><em>lands in Vernon.</em></h1>
<p class="lead">Man Yaman Bake Shop opened in November 2026 at 101 West Street, bringing traditional Filipino baked goods, cakes, cookies, savory pastries and desserts — flavors and recipes rooted in Filipino cuisine — to {CITY}.</p>
<p class="cta"><a class="btn btn-big" href="/menu">See&nbsp;the&nbsp;Menu</a> <a class="btn btn-ghost btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a></p>
</div>''' + strip() + f'''
<section class="panel">
  <h2>To the Neighbors Who Waited</h2>
  <blockquote>
    <p>&ldquo;Thank you for choosing us, for waiting for us, and for showing us more love than we could have ever imagined. We see you. We appreciate you. And we are truly grateful for you.&rdquo;</p>
    <p class="byline">— Your ManYaman Family, in a letter to the community after opening week</p>
  </blockquote>
  <p>The welcome was overwhelming from the very first morning — lines formed, trays emptied, and the shop answered with a thank-you letter to the neighborhood. The baking stays the same: pandesal at dawn, kakanin made properly, and cakes for the moments that matter.</p>
  <p style="margin-top:14px">Find us at {STREET}, Vernon, CT {ZIP}, or follow along for the day&rsquo;s trays:</p>
  <div class="links-two">
    <p><a href="{FB}" rel="noopener">Facebook — manyamanbakeshop</a></p>
    <p><a href="{IG}" rel="noopener">Instagram — @manyamanbakeshop</a></p>
  </div>
</section>
</main>''' + FOOTER + f'''<script type="application/ld+json">{breadcrumbs("Our Story", "/about")}</script>
</body></html>''')

# contact
PAGES['contact.html'] = (head(f'Contact &amp; Directions — {BRAND}, {CITY}',
    f'Visit Man Yaman Bake Shop at 101 West Street, Unit B, Vernon, CT {ZIP}. Call {PHONE_D} or send a message — Tue–Fri 7–12 & 2–6, Sat 7–12 & 2–5, Sun 6–9 & 2–5.',
    '/contact') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">Visit &amp; Contact</p>
<h1>101 West Street,<br><em>Vernon, Connecticut.</em></h1>
<p class="lead">Call ahead, send a note, or come by during opening hours — the counter is at {STREET}.</p>
<p class="cta"><a class="btn btn-big" href="tel:{PHONE_T}">Call&nbsp;{PHONE_D}</a> <a class="btn btn-ghost btn-big" href="{MAPQ}" rel="noopener">Get&nbsp;Directions</a></p>
</div>''' + strip() + f'''
<section class="panel">
  <div class="split">
    <div>
      <h2>The Shop</h2>
      <p class="address"><strong>{BRAND}</strong>{STREET}<br>Vernon, CT {ZIP}</p>
      <p style="margin-top:10px"><a href="tel:{PHONE_T}">{PHONE_D}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <table class="hours" aria-label="Hours of operation">
        <tr><th scope="col">Day</th><th scope="col">Hours</th></tr>
''' + '\n'.join(f'        <tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in HOURS_ROWS) + f'''      </table>
      <div class="links-two">
        <p><a href="{FB}" rel="noopener">Facebook</a></p>
        <p><a href="{IG}" rel="noopener">Instagram</a></p>
      </div>
    </div>
    <div>
      <h2>Send a Message</h2>
      <form class="contact" method="POST" action="/contact">
        <label>Your name <input type="text" name="name" maxlength="120" autocomplete="name"></label>
        <label>Phone <input type="tel" name="phone" maxlength="60" autocomplete="tel"></label>
        <label>Email <input type="email" name="email" maxlength="120" autocomplete="email"></label>
        <label>Message <textarea name="message" maxlength="4000"></textarea></label>
        <button class="btn btn-big" type="submit">Send&nbsp;Message</button>
      </form>
    </div>
  </div>
  <div class="mapwrap"><iframe title="Map to {BRAND}, {STREET}, Vernon, CT" src="{EMBED}" loading="lazy"></iframe></div>
</section>
</main>''' + FOOTER + f'''<script type="application/ld+json">{breadcrumbs("Contact & Directions", "/contact")}</script>
</body></html>''')

# privacy
PAGES['privacy.html'] = (head(f'Privacy Policy — {BRAND}, {CITY}',
    'How Man Yaman Bake Shop handles the information you send through this site: name, phone, email and message are used only to reply.',
    '/privacy') + NAV + '<main id="main">' +
f'''<div class="pagehead"><p class="kicker">Privacy</p>
<h1>Simple baking,<br><em>simple privacy.</em></h1>
<p class="cta" style="margin-top:18px"><a class="btn btn-big" href="/menu">See&nbsp;the&nbsp;Menu</a> <a class="btn btn-ghost btn-big" href="/contact">Contact&nbsp;Us</a></p>
</div>''' + strip() + f'''
<section class="panel privacy">
  <h2>What This Site Collects</h2>
  <p>This site has one form. When you send a message, the name, phone number, email address and message you type are delivered to {BRAND} so we can get back to you. That is the only personal information this site handles.</p>
  <h2>What Happens to It</h2>
  <p>Messages are used to answer your question — about orders, the menu, hours, or anything else. We do not sell or rent the information you send. We do not run advertising trackers on this site.</p>
  <h2>Questions</h2>
  <p>Reach us at {PHONE_D} or <a href="mailto:{EMAIL}">{EMAIL}</a>, or stop by the shop at {FULL_ADDR}.</p>
</section>
</main>''' + FOOTER + f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy","url":"{ORIGIN}/privacy","about":{{"@type":"Bakery","name":"{BRAND}"}}}}</script>
</body></html>''')

# 404
PAGES['404.html'] = (head(f'Page not found — {BRAND}',
    'That page is not here. See the menu, the breads, the kakanin, or contact Man Yaman Bake Shop in Vernon, CT.',
    '/404') + NAV + '<main id="main">' +
f'''<section class="panel err404" style="margin-top:48px">
  <p class="kicker">404</p>
  <h1>Not on this<br><em>tray.</em></h1>
  <p class="lead">The page you were looking for is not here — the counter is.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See&nbsp;the&nbsp;Menu</a> <a class="btn btn-ghost btn-big" href="/">Go&nbsp;Home</a></p>
  <div class="links-two">
    <p><a href="/breads">Breads &amp; empanadas</a></p>
    <p><a href="/kakanin">Kakanin &amp; cakes</a></p>
  </div>
</section>
</main>''' + FOOTER + '</body></html>')

# thanks
PAGES['thanks.html'] = (head(f'Message sent — {BRAND}',
    'Your message is on its way to Man Yaman Bake Shop. We will get back to you — or call (860) 281-4546.',
    '/thanks') + NAV + '<main id="main">' +
f'''<section class="panel" style="margin-top:48px">
  <p class="kicker">Sent</p>
  <h1>Message<br><em>on its way.</em></h1>
  <p class="lead">Thank you for writing — we will get back to you soon. Need an answer right now? Call {PHONE_D}.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See&nbsp;the&nbsp;Menu</a> <a class="btn btn-ghost btn-big" href="/">Go&nbsp;Home</a></p>
</section>
</main>''' + FOOTER + '</body></html>')

# sitemap locs: exclude 404/thanks utility pages
SITEMAP_PATHS = ['/', '/menu', '/breads', '/kakanin', '/about', '/contact', '/privacy']

def page_body_pairs(h, body):
    return h + '\n' + body

for fname, full in PAGES.items():
    with open(os.path.join(PUB, fname), 'w') as f:
        f.write(full)

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for pth in SITEMAP_PATHS:
    sitemap += f'<url><loc>{ORIGIN}{pth}</loc><lastmod>2026-11-24</lastmod></url>\n'
sitemap += '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(
    'User-agent: *\nAllow: /\n\nSitemap: ' + ORIGIN + '/sitemap.xml\n')
open(os.path.join(PUB, 'style.css'), 'w').write(STYLE)

favicon = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#46194a"/><rect x="0" y="52" width="64" height="5" fill="#d29a2f"/><text x="32" y="41" font-family="Palatino, Georgia, serif" font-size="27" fill="#fbf3e6" text-anchor="middle">MY</text></svg>'''
open(os.path.join(PUB, 'favicon.svg'), 'w').write(favicon)

print('PAGES:', len([f for f in PAGES if f.endswith('.html')]))
for fname in sorted(os.listdir(PUB)):
    print(fname, os.path.getsize(os.path.join(PUB, fname)))

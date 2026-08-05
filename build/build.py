#!/usr/bin/env python3
"""Erzeugt index.html (de), en/index.html und th/index.html aus einer gemeinsamen Vorlage."""
import io, re, os, json

ROOT = '/Users/lukas/Desktop/Claude/lukaswagner-coming-soon'
os.chdir(ROOT)

CSS = io.open('build/style.css', encoding='utf-8').read()
CSS_REL = CSS.replace("url('/assets/", "url('assets/")

THAI_FACES = """    @font-face{font-family:'Noto Sans Thai';font-style:normal;font-weight:400 600;font-display:swap;
      src:url('/assets/fonts/noto-sans-thai-thai.woff2') format('woff2');unicode-range:U+0E01-0E5B, U+200C-200D, U+25CC}
    @font-face{font-family:'Noto Serif Thai';font-style:normal;font-weight:400 600;font-display:swap;
      src:url('/assets/fonts/noto-serif-thai-thai.woff2') format('woff2');unicode-range:U+0E01-0E5B, U+200C-200D, U+25CC}"""

MAIL = "kontakt@lukaswagner.at"

def mailto(subject, fields):
    body = "%0A".join(f + "%3A" for f in fields) + "%0A"
    return f"mailto:{MAIL}?subject={subject}&amp;body={body}"

# ---------------------------------------------------------------- Inhalte
L = {}

L['de'] = dict(
    lang='de', dir_='', label='Deutsch',
    title='Lukas Wagner | KI-Keynote-Speaker für Unternehmen, Städte &amp; Regionen',
    desc='KI-Keynote-Speaker Lukas Wagner macht Künstliche Intelligenz verständlich und live erlebbar: Keynotes, Workshops und ahead x Live-Formate für Unternehmen, Städte und Regionen.',
    og_title='Lukas Wagner | KI-Keynote-Speaker',
    og_desc='Je digitaler die Welt wird, desto mehr zählt der Raum, in dem Menschen zusammenkommen.',
    schema_desc='Österreichischer KI-Keynote-Speaker, Unternehmer und Gründer von ahead x. Macht Künstliche Intelligenz verständlich und live erlebbar, für Unternehmen, Städte und Regionen.',
    nav=['Erlebnis','Formate','Warum Lukas','ahead x','Stimmen'],
    cta_keynote='Keynote anfragen', cta_reel='Auftritte auf YouTube ansehen',
    menu_open='Menü öffnen', menu_close='Menü schließen', skip='Zum Inhalt springen',
    subj_keynote='Keynote-Anfrage%20Lukas%20Wagner',
    subj_workshop='Workshop-Anfrage%20Lukas%20Wagner',
    subj_region='Regionalformat%20%2F%20ahead%20x%20anfragen',
    f_keynote=['Datum','Ort','Zielgruppe','Anlass'],
    f_region=['Stadt%2FRegion','Zeitraum','Zielgruppe','Anlass'],
    scr=['Mehr Werkzeuge.', 'Mehr Inhalte.', 'Mehr Feeds.', 'Mehr Antworten.', 'Mehr Bildschirme.'],
    scr_turn='Und immer weniger Raum, um gemeinsam zu denken.',
    scr_close='Die Zukunft braucht keinen weiteren Feed. <em>Sie braucht einen Raum.</em>',
    scr_lukas='Lukas Wagner bringt Künstliche Intelligenz in genau diesen Raum.',
    scr_label='Warum echte Räume wichtiger werden',
    scr_alt='Voller Saal bei einem ahead x Format, Menschen hören gemeinsam zu',
    hero_kicker='KI-Keynote-Speaker · Gründer von ahead x · Formatentwickler',
    hero_lead='',
    h1=['Zukunft','entsteht','im Raum'], em_i=2,
    hero_sub='Lukas Wagner holt Künstliche Intelligenz aus dem Bildschirm auf die Bühne. Damit Unternehmen, Städte und Regionen gemeinsam verstehen, was als Nächstes kommt.',
    trust=[('500+','Auftritte auf Bühnen'),('1.700+','Teilnahmen bei ahead x'),('8 Städte','mit eigenen Live-Formaten')],
    hero_alt='Lukas Wagner steht lächelnd im leeren Theatersaal zwischen roten Sitzreihen unter warmem Bühnenlicht',
    hero_cap='Vom Poetry-Slam zur KI-Keynote',
    proof_label='Reichweite und Partner', proof_n='1.700+',
    proof_text='Teilnahmen bei ahead x Live-Formaten in 8 Städten. Gegründet, kuratiert und moderiert von Lukas Wagner.',
    partners='Medien- &amp; Netzwerkpartner von ahead x',
    xp_kicker='Was im Raum passiert', xp_h2='Keine Vorlesung über KI. <br /> Ein Moment mit ihr.',
    xp_lead='KI liefert Antworten. Ein Raum schafft Verständnis. Eine Keynote von Lukas Wagner ist in fünf Akten gebaut, wie ein guter Abend im Theater.',
    act_word='Akt',
    acts=[('Ankommen','Menschen kommen mit Fragen, Halbwissen und Skepsis. Genau richtig.'),
          ('Verstehen','Was ist relevant, was bleibt Hype. Klare Sprache statt Fachjargon.'),
          ('Erleben','Das Publikum gibt Input, die KI liefert live. Staunen, Lachen, Diskussion.'),
          ('Einordnen','Chancen und Grenzen, ohne Alarmismus und ohne Verklärung.'),
          ('Handeln','Aus dem Moment wird Richtung: konkrete nächste Schritte.')],
    wide_alt='Publikum verfolgt gespannt eine Fragerunde bei einem ahead x Workshop, Lukas Wagner steht an der Leinwand',
    wide_cap='ahead x live: Aus Publikumsfragen werden Demos',
    keep_kicker='Was bleibt', keep_h2='Menschen kommen mit Fragen. <br /> Sie gehen mit einer Richtung.',
    keeps=[('Eine gemeinsame Sprache für KI','Team und Führung reden danach über dasselbe, nicht über zehn verschiedene Buzzwords.'),
           ('Realistische Orientierung','Was KI heute wirklich kann, was nicht, und was das für die eigene Arbeit heißt.'),
           ('Konkrete nächste Schritte','Ideen, die sich am nächsten Arbeitstag ausprobieren lassen. Ohne neue Einkaufsliste.')],
    keep_note='Keine Transformation über Nacht. Aber ein gemeinsamer Startpunkt, der trägt.',
    fmt_kicker='Formate', fmt_h2='Ein Erlebnis. Drei Bühnen.',
    f1_label='Format 01 · Hauptbühne', f1_h3='Die KI-Keynote',
    f1_alt='Lukas Wagner lächelt vor der Leinwand, während er eine Live-Demo zeigt',
    f1_meta=[('Für wen','Konferenzen, Firmenevents, Stadt- und Zukunftsveranstaltungen, Medienformate'),
             ('Situation','Alle reden über KI, aber im Saal sitzt vom Vorstand bis zum Lehrling jede Wissensstufe'),
             ('Was passiert','Einordnung, Live-Demos mit Publikumsinput, Dramaturgie statt Folienschlacht')],
    f2_label='Format 02 · Hands-on', f2_h3='Der Workshop',
    f2_text='Für Teams, KMU und Organisationen, die nach dem Staunen ins Ausprobieren kommen wollen. KI-Werkzeuge am eigenen Arbeitsalltag getestet, begleitet und eingeordnet.',
    f2_alt='Teilnehmerin arbeitet bei einem ahead x Workshop konzentriert an ihrem Laptop',
    f2_cap='Hands-on bei einem ahead x Workshop', f2_cta='Workshop anfragen',
    f3_label='Format 03 · ahead x', f3_h3='Das Regionalformat',
    f3_text='Für Städte, Regionen und Partner, die KI öffentlich erlebbar machen wollen. Kuratiert mit lokalen Partnern aus Medien, Wirtschaft und Bildung.',
    fam=[('city','öffentliches Stadt-Event, regional und niederschwellig'),
         ('labs','Workshop-Format für Unternehmen und Einsteiger:innen'),
         ('mastermind','Format für Entscheider:innen, in Vorbereitung'),
         ('future','Flaggschiff aus Award Show und Future Day')],
    f3_cta='Regionalformat anfragen',
    why_kicker='Warum Lukas',
    why_open='Bevor <em>Künstliche Intelligenz</em> sein Thema wurde, war <em>menschliche Aufmerksamkeit</em> längst sein Handwerk.',
    layers=[('Der Speaker','Jahre auf Bühnen, auf denen es nur funktioniert, wenn der Raum mitgeht.'),
            ('Der Übersetzer','Komplexe Themen, verdichtet in Sätze, die im Raum hängen bleiben.'),
            ('Der Formatentwickler','Baut Abende, nicht Folien. Dramaturgie, Beteiligung, Atmosphäre.'),
            ('Der Gründer','Mit ahead x lokale Räume gebaut, in denen Menschen KI gemeinsam verstehen.')],
    origin=['<b>Slam-Poet, Autor, Songwriter</b>: die erste Bühne',
            '<b>100+</b> Literatur- &amp; Kulturveranstaltungen organisiert',
            '<b>2017</b> Förderpreis für Kunst und Kultur',
            '<b>TEDxSalzburg</b> Speaker-Coach'],
    why_close='Technologie verändert sich. Das Bedürfnis, gemeinsam zu verstehen, nicht.',
    case_kicker='Case Study', case_h2='ahead x: Räume, in denen eine Region gemeinsam versteht.',
    case_lead='Lukas spricht nicht nur darüber, wie man Menschen für KI erreicht. Er baut die Räume dafür.',
    case=[('Ein Raum','Ein Abend, ein voller Saal, ein Thema. Der Anfang.'),
          ('Eine Stadt','Lokale Partner aus Medien, Wirtschaft und Bildung machen daraus ein Stadtformat.'),
          ('Acht Städte','Dasselbe Prinzip, andere Region. Das Format reist, die Verbindung bleibt lokal.'),
          ('Eine Plattform','Aus einzelnen Abenden wird eine wachsende Plattform mit Publikum von 16 bis 80.')],
    case_close='KI ist global. Verständnis beginnt lokal.',
    stats=[('9','Editionen'),('8','Städte'),('92&nbsp;%','geben 4 oder 5 von 5 Punkten')],
    case_cta1='ahead x entdecken', case_cta2='Partner werden',
    case_src='Zahlen: ahead x, Stand April 2026',
    voices_kicker='Stimmen',
    quote_hero=('Alle im Raum können nicht anders, als an seinen Lippen zu hängen.','Romy Sigl','CEO CoworkingSalzburg'),
    quotes=[('Seine Fähigkeit, komplexe KI-Konzepte verständlich und anschaulich zu vermitteln, macht ihn zu einem herausragenden Sprecher.','Stefan König','Finanzstratege'),
            ('Lukas übersetzt die Komplexität des Themas meisterhaft, ohne dabei an Tiefe zu verlieren.','Oliver Carl Drewo','Webdesign &amp; SEO'),
            ('Willst du deinen Talk auf den Punkt bringen? Frag Lukas.','Andreas Gruber','Speaker, TEDxSalzburg')],
    voices_link='Alle Empfehlungen auf LinkedIn lesen',
    book_kicker='Anfrage', book_h2='Bringt die Zukunft <br /> in euren Raum.',
    book_sub='Schickt mir Datum, Ort, Zielgruppe und Anlass. Ihr bekommt eine ehrliche Einschätzung, welches Format passt. Und welches nicht.',
    book_mail_pre='Direkt:', book_mail_post='auch für Presse &amp; Interviews',
    faq_kicker='FAQ', faq_h2='Kurz beantwortet.',
    faq=[('Für welche Veranstaltungen kann man Lukas Wagner buchen?','Für Konferenzen, Firmenevents, Stadt- und Regionalveranstaltungen, Verbände und Bildungseinrichtungen, als Keynote, Workshop oder Moderation rund um Künstliche Intelligenz.'),
         ('Ist die Keynote auch für Einsteiger:innen geeignet?','Ja. KI wird ohne Fachjargon verständlich gemacht. Tiefe und Inhalt richten sich nach der Zielgruppe.'),
         ('Bietet Lukas Wagner auch KI-Workshops an?','Ja: Hands-on-Workshops und Impulstage für Teams, KMU, Organisationen und öffentliche Einrichtungen.'),
         ('Wie läuft eine Anfrage ab?','Kurze E-Mail mit Datum, Ort, Zielgruppe und Anlass, dann folgt eine ehrliche Einschätzung, welches Format passt.')],
    foot_nav=['Erlebnis','Formate','Warum Lukas','ahead x','Anfrage'],
    legal_h=['Anbieter','Rechtsform &amp; Register','Kontakt'],
    legal_form='Florida Limited Liability Company<br />Reg.-Nr. L24000079118, Bundesstaat Florida<br />Vertreten durch Lukas M. Wagner',
    privacy='Datenschutzerklärung', privacy_url='/datenschutz.html',
    purpose='Unternehmensgegenstand: Keynotes, Workshops und Live-Formate zum Thema Künstliche Intelligenz.',
    photo_credit='Eventfotos © Nussbaumer Photography',
)

L['en'] = dict(
    lang='en', dir_='en/', label='English',
    title='Lukas Wagner | AI Keynote Speaker for Companies, Cities &amp; Regions',
    desc='AI keynote speaker Lukas Wagner makes artificial intelligence understandable and tangible on stage: keynotes, workshops and ahead x live formats for companies, cities and regions.',
    og_title='Lukas Wagner | AI Keynote Speaker',
    og_desc='The more digital the world becomes, the more valuable real rooms become.',
    schema_desc='Austrian AI keynote speaker, entrepreneur and founder of ahead x. Makes artificial intelligence understandable and tangible on stage, for companies, cities and regions.',
    nav=['Experience','Formats','Why Lukas','ahead x','Voices'],
    cta_keynote='Request a keynote', cta_reel='Watch talks on YouTube',
    menu_open='Open menu', menu_close='Close menu', skip='Skip to content',
    subj_keynote='Keynote%20enquiry%20Lukas%20Wagner',
    subj_workshop='Workshop%20enquiry%20Lukas%20Wagner',
    subj_region='Regional%20format%20%2F%20ahead%20x%20enquiry',
    f_keynote=['Date','Location','Audience','Occasion'],
    f_region=['City%2FRegion','Timeframe','Audience','Occasion'],
    scr=['More tools.', 'More content.', 'More feeds.', 'More answers.', 'More screens.'],
    scr_turn='And less room to think together.',
    scr_close='The future does not need another feed. <em>It needs a room.</em>',
    scr_lukas='Lukas Wagner brings artificial intelligence into that room.',
    scr_label='Why real rooms matter more',
    scr_alt='A full room at an ahead x format, people listening together',
    hero_kicker='AI Keynote Speaker · Founder of ahead x · Format Developer',
    hero_lead='',
    h1=['The future','happens','in the room'], em_i=2,
    hero_sub='Lukas Wagner brings artificial intelligence out of the screen and onto the stage. So companies, cities and regions can understand together what comes next.',
    trust=[('500+','stage appearances'),('1,700+','attendances at ahead x'),('8 cities','with their own live formats')],
    hero_alt='Lukas Wagner stands smiling in an empty theatre between rows of red seats under warm stage light',
    hero_cap='From poetry slam to AI keynote',
    proof_label='Reach and partners', proof_n='1,700+',
    proof_text='Attendances at ahead x live formats across 8 cities. Founded, curated and hosted by Lukas Wagner.',
    partners='Media &amp; network partners of ahead x',
    xp_kicker='What happens in the room', xp_h2='Not a lecture about AI. <br /> A moment with it.',
    xp_lead='AI generates answers. A room creates understanding. A keynote by Lukas Wagner is built in five acts, like a good evening at the theatre.',
    act_word='Act',
    acts=[('Arrival','People arrive with questions, half-knowledge and healthy scepticism. Exactly right.'),
          ('Understanding','What is relevant, what stays hype. Plain language instead of jargon.'),
          ('Experience','The audience gives input, the AI delivers live. Amazement, laughter, debate.'),
          ('Perspective','Opportunities and limits, without alarmism and without glorification.'),
          ('Action','The moment turns into direction: concrete next steps.')],
    wide_alt='Audience follows a question round at an ahead x workshop, Lukas Wagner stands at the screen',
    wide_cap='ahead x live: audience questions become demos',
    keep_kicker='What stays', keep_h2='People arrive with questions. <br /> They leave with a direction.',
    keeps=[('A shared language for AI','Teams and leadership talk about the same thing afterwards, not about ten different buzzwords.'),
           ('Realistic perspective','What AI can really do today, what it cannot, and what that means for your own work.'),
           ('Concrete next steps','Ideas you can try on the next working day. Without a new shopping list.')],
    keep_note='No transformation overnight. But a shared starting point that holds.',
    fmt_kicker='Formats', fmt_h2='One experience. Three stages.',
    f1_label='Format 01 · Main stage', f1_h3='The AI keynote',
    f1_alt='Lukas Wagner smiles in front of the screen while showing a live demo',
    f1_meta=[('For whom','Conferences, corporate events, city and future events, media formats'),
             ('Situation','Everyone talks about AI, but the room holds every level of knowledge, from the board to the apprentice'),
             ('What happens','Perspective, live demos with audience input, dramaturgy instead of slide decks')],
    f2_label='Format 02 · Hands-on', f2_h3='The workshop',
    f2_text='For teams, SMEs and organisations that want to move from amazement to trying things out. AI tools tested on your own working day, guided and put in context.',
    f2_alt='A participant works focused on her laptop at an ahead x workshop',
    f2_cap='Hands-on at an ahead x workshop', f2_cta='Request a workshop',
    f3_label='Format 03 · ahead x', f3_h3='The regional format',
    f3_text='For cities, regions and partners who want to make AI publicly tangible. Curated with local partners from media, business and education.',
    fam=[('city','public city event, regional and low-threshold'),
         ('labs','workshop format for companies and beginners'),
         ('mastermind','format for decision-makers, in preparation'),
         ('future','flagship of award show and future day')],
    f3_cta='Request a regional format',
    why_kicker='Why Lukas',
    why_open='Before <em>artificial intelligence</em> became his subject, <em>human attention</em> was already his craft.',
    layers=[('The speaker','Years on stages where it only works if the room comes along.'),
            ('The translator','Complex topics, condensed into sentences that stay in the room.'),
            ('The format developer','Builds evenings, not slides. Dramaturgy, participation, atmosphere.'),
            ('The founder','Built local rooms with ahead x where people understand AI together.')],
    origin=['<b>Slam poet, author, songwriter</b>: the first stage',
            '<b>100+</b> literature and culture events organised',
            '<b>2017</b> arts and culture grant award (Förderpreis)',
            '<b>TEDxSalzburg</b> speaker coach'],
    why_close='Technology changes. The need to understand together does not.',
    case_kicker='Case study', case_h2='ahead x: rooms where a region understands together.',
    case_lead='Lukas does not just talk about how to reach people with AI. He builds the rooms for it.',
    case=[('One room','One evening, one full hall, one topic. The beginning.'),
          ('One city','Local partners from media, business and education turn it into a city format.'),
          ('Eight cities','Same principle, different region. The format travels, the connection stays local.'),
          ('One platform','Single evenings grow into a platform with an audience aged 16 to 80.')],
    case_close='AI is global. Understanding begins locally.',
    stats=[('9','editions'),('8','cities'),('92&nbsp;%','rate it 4 or 5 out of 5')],
    case_cta1='Explore ahead x', case_cta2='Become a partner',
    case_src='Figures: ahead x, as of April 2026',
    voices_kicker='Voices',
    quote_hero=('Nobody in the room can help hanging on his every word.','Romy Sigl','CEO CoworkingSalzburg'),
    quotes=[('His ability to convey complex AI concepts clearly and vividly makes him an outstanding speaker.','Stefan König','financial strategist'),
            ('Lukas translates the complexity of the topic masterfully, without losing depth.','Oliver Carl Drewo','web design &amp; SEO'),
            ('Want to get your talk to the point? Ask Lukas.','Andreas Gruber','speaker, TEDxSalzburg')],
    voices_link='Read all recommendations on LinkedIn',
    book_kicker='Enquiry', book_h2='Bring the future <br /> into your room.',
    book_sub='Send me the date, location, audience and occasion. You get an honest assessment of which format fits. And which does not.',
    book_mail_pre='Direct:', book_mail_post='also for press &amp; interviews',
    faq_kicker='FAQ', faq_h2='Answered briefly.',
    faq=[('What kind of events can Lukas Wagner be booked for?','Conferences, corporate events, city and regional events, associations and educational institutions, as a keynote, workshop or moderation around artificial intelligence.'),
         ('Is the keynote suitable for beginners too?','Yes. AI is explained without jargon. Depth and content are matched to the audience.'),
         ('Does Lukas Wagner also offer AI workshops?','Yes: hands-on workshops and impulse days for teams, SMEs, organisations and public institutions.'),
         ('How does an enquiry work?','A short email with date, location, audience and occasion, followed by an honest assessment of which format fits.')],
    foot_nav=['Experience','Formats','Why Lukas','ahead x','Enquiry'],
    legal_h=['Provider','Legal form &amp; registry','Contact'],
    legal_form='Florida Limited Liability Company<br />Reg. no. L24000079118, State of Florida<br />Represented by Lukas M. Wagner',
    privacy='Privacy policy', privacy_url='/en/privacy.html',
    purpose='Business purpose: keynotes, workshops and live formats on artificial intelligence.',
    photo_credit='Event photos © Nussbaumer Photography',
)

L['th'] = dict(
    lang='th', dir_='th/', label='ไทย',
    title='Lukas Wagner | วิทยากรคีย์โน้ต AI สำหรับองค์กร เมือง และภูมิภาค',
    desc='Lukas Wagner วิทยากรคีย์โน้ตด้าน AI ทำให้ปัญญาประดิษฐ์เข้าใจง่ายและสัมผัสได้จริงบนเวที ทั้งคีย์โน้ต เวิร์กช็อป และงานสดของ ahead x สำหรับองค์กร เมือง และภูมิภาค',
    og_title='Lukas Wagner | วิทยากรคีย์โน้ต AI',
    og_desc='ยิ่งโลกเป็นดิจิทัลมากเท่าไร พื้นที่จริงที่ผู้คนมาพบกันยิ่งมีค่ามากขึ้นเท่านั้น',
    schema_desc='วิทยากรคีย์โน้ตด้าน AI ชาวออสเตรีย ผู้ประกอบการ และผู้ก่อตั้ง ahead x ทำให้ปัญญาประดิษฐ์เข้าใจง่ายและสัมผัสได้จริง สำหรับองค์กร เมือง และภูมิภาค',
    nav=['ประสบการณ์','รูปแบบงาน','ทำไมต้อง Lukas','ahead x','เสียงตอบรับ'],
    cta_keynote='ขอข้อมูลคีย์โน้ต', cta_reel='ดูการบรรยายบน YouTube',
    menu_open='เปิดเมนู', menu_close='ปิดเมนู', skip='ข้ามไปยังเนื้อหา',
    subj_keynote='Keynote%20enquiry%20Lukas%20Wagner',
    subj_workshop='Workshop%20enquiry%20Lukas%20Wagner',
    subj_region='Regional%20format%20%2F%20ahead%20x%20enquiry',
    f_keynote=['Date','Location','Audience','Occasion'],
    f_region=['City%2FRegion','Timeframe','Audience','Occasion'],
    scr=['เครื่องมือมากขึ้น', 'เนื้อหามากขึ้น', 'ฟีดมากขึ้น', 'คำตอบมากขึ้น', 'หน้าจอมากขึ้น'],
    scr_turn='แต่พื้นที่สำหรับคิดร่วมกันกลับน้อยลง',
    scr_close='อนาคตไม่ได้ต้องการฟีดเพิ่มอีกหนึ่งอัน <em>แต่ต้องการพื้นที่จริง</em>',
    scr_lukas='Lukas Wagner นำปัญญาประดิษฐ์เข้าสู่พื้นที่นั้น',
    scr_label='ทำไมพื้นที่จริงจึงสำคัญขึ้น',
    scr_alt='ห้องที่เต็มไปด้วยผู้คนในงานของ ahead x กำลังรับฟังร่วมกัน',
    hero_kicker='วิทยากรคีย์โน้ต AI · ผู้ก่อตั้ง ahead x · นักออกแบบรูปแบบงาน',
    hero_lead='',
    h1=['อนาคต','เกิดขึ้น','ในพื้นที่จริง'], em_i=2,
    hero_sub='Lukas Wagner นำปัญญาประดิษฐ์ออกจากหน้าจอขึ้นสู่เวที เพื่อให้องค์กร เมือง และภูมิภาคเข้าใจร่วมกันว่าอะไรกำลังจะมาถึง',
    trust=[('500+','ครั้งบนเวที'),('1,700+','การเข้าร่วมงาน ahead x'),('8 เมือง','ที่มีงานสดของตัวเอง')],
    hero_alt='Lukas Wagner ยืนยิ้มอยู่ในโรงละครที่ว่างเปล่า ท่ามกลางแถวเก้าอี้สีแดงใต้แสงไฟเวทีอบอุ่น',
    hero_cap='จากเวที Poetry Slam สู่คีย์โน้ต AI',
    proof_label='การเข้าถึงและพันธมิตร', proof_n='1,700+',
    proof_text='การเข้าร่วมงานสดของ ahead x ใน 8 เมือง ก่อตั้ง คัดสรร และดำเนินรายการโดย Lukas Wagner',
    partners='พันธมิตรด้านสื่อและเครือข่ายของ ahead x',
    xp_kicker='สิ่งที่เกิดขึ้นในห้อง', xp_h2='ไม่ใช่การบรรยายเรื่อง AI <br /> แต่เป็นช่วงเวลาที่ได้อยู่กับมัน',
    xp_lead='AI ให้คำตอบ แต่พื้นที่จริงสร้างความเข้าใจ คีย์โน้ตของ Lukas Wagner ถูกออกแบบเป็นห้าองก์ เหมือนค่ำคืนดี ๆ ในโรงละคร',
    act_word='องก์ที่',
    acts=[('การมาถึง','ผู้คนมาพร้อมคำถาม ความรู้ครึ่ง ๆ กลาง ๆ และความสงสัย ซึ่งถูกต้องแล้ว'),
          ('ความเข้าใจ','อะไรสำคัญจริง อะไรเป็นเพียงกระแส ด้วยภาษาที่ชัดเจน ไม่ใช่ศัพท์เทคนิค'),
          ('การสัมผัส','ผู้ฟังให้โจทย์ AI ตอบสดตรงหน้า ทั้งความทึ่ง เสียงหัวเราะ และการถกเถียง'),
          ('การจัดวาง','ทั้งโอกาสและข้อจำกัด ไม่ตื่นตระหนก และไม่เชิดชูเกินจริง'),
          ('การลงมือ','จากช่วงเวลานั้นกลายเป็นทิศทาง คือก้าวถัดไปที่ทำได้จริง')],
    wide_alt='ผู้ฟังตั้งใจฟังช่วงถามตอบในเวิร์กช็อปของ ahead x โดยมี Lukas Wagner ยืนอยู่หน้าจอ',
    wide_cap='ahead x สด: คำถามจากผู้ฟังกลายเป็นการสาธิต',
    keep_kicker='สิ่งที่เหลืออยู่', keep_h2='ผู้คนมาพร้อมคำถาม <br /> และกลับไปพร้อมทิศทาง',
    keeps=[('ภาษากลางสำหรับเรื่อง AI','ทีมและผู้บริหารพูดถึงสิ่งเดียวกัน ไม่ใช่คนละสิบคำศัพท์'),
           ('มุมมองที่เป็นจริง','วันนี้ AI ทำอะไรได้จริง ทำอะไรไม่ได้ และนั่นหมายความว่าอย่างไรกับงานของเรา'),
           ('ก้าวถัดไปที่ชัดเจน','ไอเดียที่เริ่มลองได้ในวันทำงานถัดไป โดยไม่ต้องซื้อเครื่องมือใหม่')],
    keep_note='ไม่ใช่การเปลี่ยนแปลงข้ามคืน แต่เป็นจุดเริ่มต้นร่วมกันที่ตั้งอยู่ได้',
    fmt_kicker='รูปแบบงาน', fmt_h2='หนึ่งประสบการณ์ สามเวที',
    f1_label='รูปแบบที่ 01 · เวทีหลัก', f1_h3='คีย์โน้ต AI',
    f1_alt='Lukas Wagner ยิ้มอยู่หน้าจอขณะสาธิตการใช้งานสด',
    f1_meta=[('เหมาะกับใคร','งานประชุม งานองค์กร งานของเมืองและงานด้านอนาคต รวมถึงรายการสื่อ'),
             ('สถานการณ์','ทุกคนพูดถึง AI แต่ในห้องมีทุกระดับความรู้ ตั้งแต่ผู้บริหารจนถึงพนักงานฝึกหัด'),
             ('สิ่งที่เกิดขึ้น','การจัดวางภาพรวม การสาธิตสดที่ผู้ฟังมีส่วนร่วม และการเล่าเรื่องแทนการไล่สไลด์')],
    f2_label='รูปแบบที่ 02 · ลงมือทำ', f2_h3='เวิร์กช็อป',
    f2_text='สำหรับทีม ธุรกิจขนาดกลางและเล็ก และองค์กรที่อยากก้าวจากความทึ่งไปสู่การลงมือลอง ทดลองใช้เครื่องมือ AI กับงานจริงของตัวเอง โดยมีคนคอยแนะนำและช่วยจัดวาง',
    f2_alt='ผู้เข้าร่วมกำลังตั้งใจทำงานบนแล็ปท็อปในเวิร์กช็อปของ ahead x',
    f2_cap='ลงมือทำในเวิร์กช็อปของ ahead x', f2_cta='ขอข้อมูลเวิร์กช็อป',
    f3_label='รูปแบบที่ 03 · ahead x', f3_h3='รูปแบบงานระดับภูมิภาค',
    f3_text='สำหรับเมือง ภูมิภาค และพันธมิตรที่อยากทำให้ AI จับต้องได้ในพื้นที่สาธารณะ คัดสรรร่วมกับพันธมิตรท้องถิ่นจากสื่อ ภาคธุรกิจ และการศึกษา',
    fam=[('city','งานสาธารณะระดับเมือง เข้าถึงง่าย'),
         ('labs','เวิร์กช็อปสำหรับองค์กรและผู้เริ่มต้น'),
         ('mastermind','รูปแบบสำหรับผู้ตัดสินใจ อยู่ระหว่างเตรียมการ'),
         ('future','งานเรือธง ประกอบด้วย Award Show และ Future Day')],
    f3_cta='ขอข้อมูลรูปแบบงานระดับภูมิภาค',
    why_kicker='ทำไมต้อง Lukas',
    why_open='ก่อนที่ <em>ปัญญาประดิษฐ์</em> จะกลายเป็นหัวข้อของเขา <em>ความสนใจของผู้คน</em> คือทักษะที่เขาฝึกมาก่อนแล้ว',
    layers=[('นักพูด','หลายปีบนเวทีที่จะสำเร็จได้ก็ต่อเมื่อคนทั้งห้องไปด้วยกัน'),
            ('นักแปลความ','เรื่องซับซ้อน กลั่นเป็นประโยคที่ยังค้างอยู่ในห้องหลังจบงาน'),
            ('นักออกแบบรูปแบบงาน','สร้างค่ำคืน ไม่ใช่สไลด์ ทั้งจังหวะการเล่า การมีส่วนร่วม และบรรยากาศ'),
            ('ผู้ก่อตั้ง','สร้างพื้นที่ท้องถิ่นด้วย ahead x ที่ผู้คนได้เข้าใจ AI ร่วมกัน')],
    origin=['<b>กวี Slam นักเขียน นักแต่งเพลง</b>: เวทีแรก',
            'จัดงานวรรณกรรมและวัฒนธรรมมากกว่า <b>100</b> งาน',
            '<b>ปี 2017</b> รางวัลสนับสนุนด้านศิลปะและวัฒนธรรม',
            'โค้ชนักพูดของ <b>TEDxSalzburg</b>'],
    why_close='เทคโนโลยีเปลี่ยนไป แต่ความต้องการที่จะเข้าใจร่วมกันไม่เคยเปลี่ยน',
    case_kicker='กรณีศึกษา', case_h2='ahead x: พื้นที่ที่ทั้งภูมิภาคได้เข้าใจร่วมกัน',
    case_lead='Lukas ไม่ได้แค่พูดว่าจะเข้าถึงผู้คนด้วยเรื่อง AI อย่างไร เขาสร้างพื้นที่สำหรับสิ่งนั้นขึ้นมาเอง',
    case=[('หนึ่งพื้นที่','หนึ่งค่ำคืน หนึ่งห้องที่เต็ม หนึ่งหัวข้อ นั่นคือจุดเริ่มต้น'),
          ('หนึ่งเมือง','พันธมิตรท้องถิ่นจากสื่อ ภาคธุรกิจ และการศึกษา ทำให้กลายเป็นงานระดับเมือง'),
          ('แปดเมือง','หลักการเดียวกัน คนละภูมิภาค รูปแบบงานเดินทางไป แต่ความเชื่อมโยงยังเป็นของท้องถิ่น'),
          ('หนึ่งแพลตฟอร์ม','จากค่ำคืนเดี่ยว ๆ เติบโตเป็นแพลตฟอร์มที่มีผู้ฟังตั้งแต่อายุ 16 ถึง 80 ปี')],
    case_close='AI เป็นเรื่องระดับโลก แต่ความเข้าใจเริ่มต้นที่ท้องถิ่น',
    stats=[('9','ครั้ง'),('8','เมือง'),('92&nbsp;%','ให้คะแนน 4 หรือ 5 จาก 5')],
    case_cta1='ดู ahead x', case_cta2='ร่วมเป็นพันธมิตร',
    case_src='ตัวเลข: ahead x ข้อมูล ณ เดือนเมษายน 2026',
    voices_kicker='เสียงตอบรับ',
    quote_hero=('ทุกคนในห้องอดไม่ได้ที่จะตั้งใจฟังทุกคำของเขา','Romy Sigl','CEO CoworkingSalzburg'),
    quotes=[('ความสามารถในการอธิบายแนวคิด AI ที่ซับซ้อนให้เข้าใจง่ายและเห็นภาพ ทำให้เขาเป็นนักพูดที่โดดเด่น','Stefan König','นักกลยุทธ์การเงิน'),
            ('Lukas ถ่ายทอดความซับซ้อนของหัวข้อได้อย่างเชี่ยวชาญ โดยไม่สูญเสียความลึก','Oliver Carl Drewo','เว็บดีไซน์ &amp; SEO'),
            ('อยากให้ทอล์กของคุณเข้าเป้าใช่ไหม ถาม Lukas','Andreas Gruber','นักพูด, TEDxSalzburg')],
    voices_link='อ่านคำแนะนำทั้งหมดบน LinkedIn',
    book_kicker='ติดต่อ', book_h2='นำอนาคต <br /> เข้าสู่พื้นที่ของคุณ',
    book_sub='ส่งวันที่ สถานที่ กลุ่มผู้ฟัง และโอกาสของงานมา แล้วคุณจะได้คำแนะนำตรงไปตรงมาว่ารูปแบบไหนเหมาะ และรูปแบบไหนไม่เหมาะ',
    book_mail_pre='ติดต่อโดยตรง:', book_mail_post='สำหรับสื่อและการสัมภาษณ์ด้วย',
    faq_kicker='คำถามที่พบบ่อย', faq_h2='ตอบสั้น ๆ',
    faq=[('จอง Lukas Wagner ไปพูดในงานแบบไหนได้บ้าง','งานประชุม งานองค์กร งานของเมืองและภูมิภาค สมาคม และสถาบันการศึกษา ทั้งในรูปแบบคีย์โน้ต เวิร์กช็อป หรือการดำเนินรายการในหัวข้อปัญญาประดิษฐ์'),
         ('คีย์โน้ตนี้เหมาะกับผู้เริ่มต้นด้วยหรือไม่','เหมาะ เนื้อหาอธิบายโดยไม่ใช้ศัพท์เทคนิค ความลึกและรายละเอียดปรับตามกลุ่มผู้ฟัง'),
         ('มีเวิร์กช็อป AI ด้วยหรือไม่','มี ทั้งเวิร์กช็อปแบบลงมือทำและวันอบรมสำหรับทีม ธุรกิจขนาดกลางและเล็ก องค์กร และหน่วยงานภาครัฐ'),
         ('ขั้นตอนการติดต่อเป็นอย่างไร','ส่งอีเมลสั้น ๆ พร้อมวันที่ สถานที่ กลุ่มผู้ฟัง และโอกาสของงาน จากนั้นจะได้รับคำแนะนำตรงไปตรงมาว่ารูปแบบไหนเหมาะที่สุด')],
    foot_nav=['ประสบการณ์','รูปแบบงาน','ทำไมต้อง Lukas','ahead x','ติดต่อ'],
    legal_h=['ผู้ให้บริการ','รูปแบบทางกฎหมายและทะเบียน','ติดต่อ'],
    legal_form='Florida Limited Liability Company<br />ทะเบียนเลขที่ L24000079118 รัฐฟลอริดา<br />ดำเนินการโดย Lukas M. Wagner',
    privacy='นโยบายความเป็นส่วนตัว', privacy_url='/th/privacy.html',
    purpose='วัตถุประสงค์ของธุรกิจ: คีย์โน้ต เวิร์กช็อป และงานสดในหัวข้อปัญญาประดิษฐ์',
    photo_credit='ภาพงาน © Nussbaumer Photography',
)

ORDER = ['de','en','th']
CODE = {'de':'DE','en':'EN','th':'TH'}
URLS = {'de':'/','en':'/en/','th':'/th/'}

def langs(cur):
    out=[]
    for i,k in enumerate(ORDER):
        if i: out.append('<span aria-hidden="true">·</span>')
        cu = ' aria-current="page"' if k==cur else ''
        out.append(f'<a href="{URLS[k]}" hreflang="{k}" lang="{k}"{cu}>{CODE[k]}</a>')
    return '<span class="langs" role="group" aria-label="Sprache / Language">' + ''.join(out) + '</span>'

def build(k):
    d = L[k]
    A = '/assets/' if d['dir_'] else 'assets/'
    css = CSS if d['dir_'] else CSS_REL
    if k == 'th':
        css = (THAI_FACES + "\n" + css
               + "\n    /* Thai: Fallback-Schriften und mehr Zeilenhoehe fuer Ober- und Unterlaengen */\n"
               + '    :root{--serif:"Fraunces","Noto Serif Thai",Georgia,serif;--sans:"Inter","Noto Sans Thai",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}\n'
               + "    h1{line-height:1.16}\n    h2,.act h3,.layer h3,.case-steps h3,.quote-hero blockquote p{line-height:1.35}\n"
               + "    .kicker,.proof-partners .t,.origin .t{letter-spacing:normal}\n    .fam li{grid-template-columns:8rem 1fr}\n"
               + "    .scr{line-height:1.5}\n    .scr-turn,.scr-close{line-height:1.55}\n")
    mk = mailto(d['subj_keynote'], d['f_keynote'])
    mw = mailto(d['subj_workshop'], d['f_keynote'])
    mr = mailto(d['subj_region'], d['f_region'])
    ids = ['erlebnis','formate','warum','aheadx','stimmen']

    alt = "\n".join(f'  <link rel="alternate" hreflang="{x}" href="https://lukaswagner.at{URLS[x]}" />' for x in ORDER)
    alt += '\n  <link rel="alternate" hreflang="x-default" href="https://lukaswagner.at/" />'

    faq_ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":re.sub('&amp;','&',q),"acceptedAnswer":{"@type":"Answer","text":re.sub('&amp;','&',a)}}
        for q,a in d['faq']]}, ensure_ascii=False)

    acts = "\n".join(
        f'          <li class="act reveal"><span class="no">{d["act_word"]} 0{i+1}</span><h3>{t}</h3><p>{p}</p></li>'
        for i,(t,p) in enumerate(d['acts']))
    keeps = "\n".join(
        f'          <div class="result reveal"><h3>{t}</h3><p>{p}</p></div>' for t,p in d['keeps'])
    f1meta = "\n".join(
        f'              <div><dt>{t}</dt><dd>{v}</dd></div>' for t,v in d['f1_meta'])
    fam = "\n".join(
        f'              <li><b>{n}</b><span>{v}</span></li>' for n,v in d['fam'])
    layers = "\n".join(
        f'          <div class="layer reveal"><h3>{t}</h3><p>{p}</p></div>' for t,p in d['layers'])
    origin = "\n".join(f'            <span>{o}</span>' for o in d['origin'])
    case = "\n".join(
        f'          <li class="reveal"><h3>{t}</h3><p>{p}</p></li>' for t,p in d['case'])
    stats = "\n".join(
        f'            <div class="cs"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in d['stats'])
    quotes = "\n".join(
        f'          <figure class="reveal">\n            <p>{q}</p>\n            <figcaption><b>{n}</b> · {r}</figcaption>\n          </figure>'
        for q,n,r in d['quotes'])
    faq_html = "\n".join(
        f'          <details><summary>{q}</summary><p>{a}</p></details>' for q,a in d['faq'])
    em_i = d.get('em_i', 1)
    # Die drei Zeilen bilden einen Satz: nur die letzte bekommt den Punkt.
    # Thai setzt keinen Satzpunkt, dort entfaellt er ganz.
    stop = '' if d['lang']=='th' else '.'
    last = len(d['h1']) - 1
    h1_html = "\n".join(
        '            <span class="hl">{}{}{}{}</span>'.format(
            '<em>' if i==em_i else '', t, '</em>' if i==em_i else '',
            f'<span class="stop">{stop}</span>' if (i==last and stop) else '')
        for i,t in enumerate(d['h1']))
    lead_html = (f'<p class="hero-lead">{d["hero_lead"]}</p>\n          ' if d.get('hero_lead') else '')
    scr_html = "\n".join(
        f'          <p class="scr scr-{i+1}">{t}</p>' for i,t in enumerate(d['scr']))
    case_close_html = (f'        <p class="case-close reveal">{d["case_close"]}</p>' if d.get('case_close') else '')
    navl = "\n".join(f'        <a href="#{i}">{t}</a>' for i,t in zip(ids, d['nav']))
    footnav = "".join(f'<a href="#{i}">{t}</a>' for i,t in zip(ids[:4]+['kontakt'], d['foot_nav']))

    return f'''<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}" />

  <link rel="canonical" href="https://lukaswagner.at{URLS[k]}" />
{alt}
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{ {'de':'de_AT','en':'en_US','th':'th_TH'}[k] }" />
  <meta property="og:title" content="{d['og_title']}" />
  <meta property="og:description" content="{d['og_desc']}" />
  <meta property="og:url" content="https://lukaswagner.at{URLS[k]}" />
  <meta property="og:image" content="https://lukaswagner.at/assets/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#141110" />
  <link rel="icon" href="data:image/svg+xml,&lt;svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'&gt;&lt;rect width='100' height='100' rx='22' fill='%23141110'/&gt;&lt;text x='50' y='68' font-size='52' font-family='Georgia' font-weight='bold' text-anchor='middle' fill='%23e2a45c'&gt;LW&lt;/text&gt;&lt;/svg&gt;" />

  <!-- Schriften liegen lokal. Kein Aufruf an Google, damit keine Besucher-IP an Dritte geht. -->
  <link rel="preload" as="font" type="font/woff2" href="{A}fonts/fraunces-normal-latin.woff2" crossorigin />

  <link rel="preload" as="image" href="{A}lukas-stage.jpg"
        imagesrcset="{A}lukas-stage-800.jpg 533w, {A}lukas-stage.jpg 1066w"
        imagesizes="(max-width:1020px) 92vw, 40vw" fetchpriority="high" />

  <script type="application/ld+json">
  {{ "@context":"https://schema.org","@type":"Person","name":"Lukas Wagner","jobTitle":"{d['hero_kicker'].split('·')[0].strip()}",
    "description":"{d['schema_desc']}",
    "url":"https://lukaswagner.at/","image":"https://lukaswagner.at/assets/lukas-portrait.jpg","nationality":"Österreich",
    "worksFor":{{"@type":"Organization","name":"ahead x","url":"https://aheadx.at"}},
    "sameAs":["https://www.youtube.com/@lukaswagnerai","https://aheadx.at","https://www.linkedin.com/in/lukaswagnerai/"] }}
  </script>
  <!-- FAQ-JSON-LD ist wortgleich zum sichtbaren FAQ. -->
  <script type="application/ld+json">
  {faq_ld}
  </script>

  <style>
{css}
  </style>
</head>
<body>
  <script>document.documentElement.className+=" js";</script>
  <a class="skip" href="#main">{d['skip']}</a>

  <header>
    <div class="wrap nav">
      <a class="brand" href="#top">Lukas Wagner<i>.</i></a>
      <button class="nav-toggle" aria-label="{d['menu_open']}" aria-expanded="false" aria-controls="menu">☰</button>
      <nav class="nav-links" id="menu" aria-label="Navigation">
{navl}
        {langs(k)}
        <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_keynote']}</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <span id="top"></span>

    <section class="hero" aria-label="Intro">
      <div class="hero-glow" aria-hidden="true"></div>
      <div class="hero-inner">
        <div class="hero-copy">
          <p class="kicker">{d['hero_kicker']}</p>
          {lead_html}<h1>
{h1_html}
          </h1>
          <p class="sub">{d['hero_sub']}</p>
          <div class="hero-cta">
            <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_keynote']}</a>
            <a class="btn btn-ghost" data-cta="speaker-reel" href="https://www.youtube.com/@lukaswagnerai" target="_blank" rel="noopener">{d['cta_reel']}&nbsp;↗</a>
          </div>
          <div class="hero-trust">
            <!-- OFFEN: "500+" ist noch nicht oeffentlich belegt, Freigabe durch LW noetig. -->
            <span><b>{d['trust'][0][0]}</b> {d['trust'][0][1]}</span>
            <span><b>{d['trust'][1][0]}</b> {d['trust'][1][1]}</span>
            <span><b>{d['trust'][2][0]}</b> {d['trust'][2][1]}</span>
          </div>
        </div>
        <div class="hero-fig">
          <figure>
            <img src="{A}lukas-stage.jpg"
                 srcset="{A}lukas-stage-800.jpg 533w, {A}lukas-stage.jpg 1066w"
                 sizes="(max-width:1020px) 92vw, 40vw"
                 width="1066" height="1600" fetchpriority="high"
                 alt="{d['hero_alt']}" />
            <figcaption>{d['hero_cap']}</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="proof band" aria-label="{d['proof_label']}">
      <div class="wrap proof-grid">
        <div class="proof-num reveal">
          <div class="n">{d['proof_n']}</div>
          <p class="l">{d['proof_text']}</p>
        </div>
        <div class="proof-partners reveal">
          <p class="t">{d['partners']}</p>
          <div class="logo-row">
            <span class="lg"><img src="{A}logos/dcv.png" alt="Digital Campus Vorarlberg" loading="lazy" width="120" height="32" /></span>
            <span class="lg"><img src="{A}logos/vn.png" alt="Vorarlberger Nachrichten" loading="lazy" width="120" height="32" /></span>
            <span class="lg"><img src="{A}logos/vol.png" alt="VOL.at" loading="lazy" width="120" height="32" /></span>
            <span class="lg"><img src="{A}logos/neue.png" alt="NEUE am Sonntag" loading="lazy" width="120" height="32" /></span>
            <span class="lg"><img src="{A}logos/tt.png" alt="Tiroler Tageszeitung" loading="lazy" width="120" height="32" /></span>
            <span class="lg"><img src="{A}logos/kleine-zeitung.svg" alt="Kleine Zeitung" loading="lazy" width="120" height="32" /></span>
          </div>
        </div>
      </div>
    </section>

    <!-- SIGNATURE: Another screen. Die Zeilen ziehen an, dann Stille, dann die Wende. -->
    <section class="screens" aria-label="{d['scr_label']}">
      <div class="wrap">
        <div class="screens-stack">
{scr_html}
          <div class="scr-pause" aria-hidden="true"></div>
          <p class="scr-turn">{d['scr_turn']}</p>
        </div>
        <figure class="screens-fig reveal">
          <img src="{A}aheadx-audience.jpg"
               srcset="{A}aheadx-audience-900.jpg 900w, {A}aheadx-audience.jpg 1500w"
               sizes="(max-width:1020px) 92vw, 1120px"
               width="1500" height="1000" loading="lazy"
               alt="{d['scr_alt']}" />
        </figure>
        <p class="scr-close reveal">{d['scr_close']}</p>
        <p class="scr-lukas reveal">{d['scr_lukas']}</p>
      </div>
    </section>

    <section id="erlebnis" aria-label="{d['xp_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['xp_kicker']}</p>
          <h2>{d['xp_h2']}</h2>
          <p class="lead-in">{d['xp_lead']}</p>
        </div>
        <ol class="acts">
{acts}
        </ol>
      </div>
    </section>

    <section id="wirkung" class="on-paper" style="padding-bottom:clamp(1.4rem,2.5vw,2rem)" aria-label="{d['keep_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['keep_kicker']}</p>
          <h2>{d['keep_h2']}</h2>
        </div>
        <div class="results">
{keeps}
        </div>
        <p class="results-note reveal">{d['keep_note']}</p>
      </div>
    </section>

    <section id="formate" class="on-paper" style="padding-top:clamp(1.4rem,2.5vw,2rem)" aria-label="{d['fmt_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['fmt_kicker']}</p>
          <h2>{d['fmt_h2']}</h2>
        </div>

        <article class="fmt-feature reveal">
          <figure>
            <img src="{A}speaker-reel-thumb.jpg"
                 srcset="{A}speaker-reel-thumb-900.jpg 900w, {A}speaker-reel-thumb.jpg 1500w"
                 sizes="(max-width:1020px) 92vw, 48vw"
                 width="1500" height="1000" loading="lazy"
                 alt="{d['f1_alt']}" />
          </figure>
          <div>
            <p class="fmt-label">{d['f1_label']}</p>
            <h3>{d['f1_h3']}</h3>
            <dl class="fmt-meta">
{f1meta}
            </dl>
            <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_keynote']}</a>
          </div>
        </article>

        <div class="fmt-duo">
          <article class="reveal">
            <div>
              <p class="fmt-label">{d['f2_label']}</p>
              <h3>{d['f2_h3']}</h3>
              <p>{d['f2_text']}</p>
            </div>
            <figure>
              <img src="{A}aheadx-demo.jpg"
                   srcset="{A}aheadx-demo-800.jpg 533w, {A}aheadx-demo.jpg 866w"
                   sizes="(max-width:820px) 92vw, 44vw"
                   width="866" height="1300" loading="lazy"
                   alt="{d['f2_alt']}" />
              <figcaption>{d['f2_cap']}</figcaption>
            </figure>
            <div class="fmt-foot">
              <a class="tlink" data-cta="workshop" href="{mw}">{d['f2_cta']} →</a>
            </div>
          </article>
          <article class="reveal">
            <div>
              <p class="fmt-label">{d['f3_label']}</p>
              <h3>{d['f3_h3']}</h3>
              <p>{d['f3_text']}</p>
            </div>
            <ul class="fam">
{fam}
            </ul>
            <div class="fmt-foot">
              <a class="tlink" data-cta="aheadx" href="{mr}">{d['f3_cta']} →</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section id="warum" aria-label="{d['why_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal" style="max-width:none">
          <p class="kicker">{d['why_kicker']}</p>
          <h2 class="why-open">{d['why_open']}</h2>
        </div>
        <div class="layers">
{layers}
        </div>
        <div class="origin reveal">
          <div class="origin-facts">
            <!-- OFFEN: biografische Angaben stammen aus dem Briefing von LW, extern noch nicht belegt. -->
{origin}
          </div>
          <p class="why-close">{d['why_close']}</p>
        </div>
      </div>
    </section>

    <section id="aheadx" class="band" aria-label="{d['case_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['case_kicker']}</p>
          <h2>{d['case_h2']}</h2>
          <p class="lead-in">{d['case_lead']}</p>
        </div>
        <ol class="case-steps">
{case}
        </ol>
        <!-- Zahlen belegt auf aheadx.at, Stand 30.04.2026. -->
        <div class="case-foot reveal">
          <div class="case-stats">
{stats}
          </div>
          <div class="case-cta">
            <a class="btn btn-ghost" data-cta="aheadx" href="https://aheadx.at" target="_blank" rel="noopener">{d['case_cta1']}&nbsp;↗</a>
            <a class="tlink" data-cta="aheadx" href="{mr}">{d['case_cta2']} →</a>
          </div>
        </div>
{case_close_html}
        <p class="case-src reveal">{d['case_src']}</p>
      </div>
    </section>

    <section id="stimmen" class="on-paper" aria-label="{d['voices_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal" style="margin-bottom:1.2rem">
          <h2 class="kicker">{d['voices_kicker']}</h2>
        </div>
        <!-- OFFEN: Freigabe von Wortlaut und Rolle der zitierten Personen. -->
        <figure class="quote-hero reveal">
          <blockquote><p>{d['quote_hero'][0]}</p></blockquote>
          <figcaption><b>{d['quote_hero'][1]}</b> · {d['quote_hero'][2]}</figcaption>
        </figure>
        <div class="quote-row">
{quotes}
        </div>
        <p class="quote-src reveal"><a class="tlink" href="https://www.linkedin.com/in/lukaswagnerai/details/recommendations/" target="_blank" rel="noopener">{d['voices_link']} →</a></p>
      </div>
    </section>

    <section id="kontakt" class="book" aria-label="{d['book_kicker']}">
      <div class="book-glow" aria-hidden="true"></div>
      <div class="wrap book-inner">
        <p class="kicker reveal" style="justify-content:center">{d['book_kicker']}</p>
        <h2 class="reveal">{d['book_h2']}</h2>
        <p class="sub reveal">{d['book_sub']}</p>
        <div class="hero-cta reveal">
          <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_keynote']}</a>
          <a class="btn btn-ghost" data-cta="speaker-reel" href="https://www.youtube.com/@lukaswagnerai" target="_blank" rel="noopener">{d['cta_reel']}&nbsp;↗</a>
        </div>
        <p class="book-mail reveal">{d['book_mail_pre']} <a href="mailto:{MAIL}">{MAIL}</a> · {d['book_mail_post']}</p>
      </div>
    </section>

    <section id="faq" class="band" style="padding-top:clamp(2.4rem,4.5vw,3.4rem);padding-bottom:clamp(2.4rem,4.5vw,3.4rem)" aria-label="{d['faq_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['faq_kicker']}</p>
          <h2>{d['faq_h2']}</h2>
        </div>
        <div class="faq reveal">
{faq_html}
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap">
      <div class="foot-top">
        <span class="brand">Lukas Wagner<i>.</i></span>
        <nav class="foot-links" aria-label="Footer">
          {footnav}<a href="https://www.youtube.com/@lukaswagnerai" target="_blank" rel="noopener">YouTube</a><a href="https://aheadx.at" target="_blank" rel="noopener">aheadx.at</a>
        </nav>
      </div>
      <div class="legal">
        <!-- OFFEN: Urheber-Credit fuer das Theaterfoto im Hero fehlt noch. -->
        <div class="legal-grid">
          <div><b>{d['legal_h'][0]}</b>SHINK BIG LLC<br />7901 4th St N, Ste 300<br />St. Petersburg, FL 33702, USA</div>
          <div><b>{d['legal_h'][1]}</b>{d['legal_form']}</div>
          <div><b>{d['legal_h'][2]}</b><a href="mailto:{MAIL}">{MAIL}</a><br /><a href="{d['privacy_url']}">{d['privacy']}</a></div>
        </div>
        <p class="legal-foot">{d['purpose']} © <span id="year">2026</span> SHINK BIG LLC · {d['photo_credit']}</p>
      </div>
    </div>
  </footer>

  <a class="sticky-cta" data-cta="keynote" href="{mk}"><span class="btn btn-primary">{d['cta_keynote']}</span></a>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    var t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');
    if(t){{t.addEventListener('click',function(){{var o=m.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');t.setAttribute('aria-label',o?'{d['menu_close']}':'{d['menu_open']}');}});
      m.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{m.classList.remove('open');t.setAttribute('aria-expanded','false');}});}});}}
    var sticky=document.querySelector('.sticky-cta'),hero=document.querySelector('.hero');
    if(sticky&&hero&&'IntersectionObserver' in window){{
      new IntersectionObserver(function(es){{es.forEach(function(e){{sticky.classList.toggle('show',!e.isIntersecting);}});}},{{rootMargin:'-80px 0px 0px 0px'}}).observe(hero);
    }}
    /* Signature-Sequenz startet einmalig, wenn der Abschnitt sichtbar wird. Kein Scroll-Hijacking. */
    var scr=document.querySelector('.screens');
    if(scr){{
      var lite=function(){{ if(!scr.classList.contains('lit')&&scr.getBoundingClientRect().top<window.innerHeight*.85){{
        scr.classList.add('lit'); window.removeEventListener('scroll',lite); }} }};
      if('IntersectionObserver' in window){{
        new IntersectionObserver(function(es,o){{es.forEach(function(e){{if(e.isIntersecting){{scr.classList.add('lit');o.disconnect();window.removeEventListener('scroll',lite);}}}});}},{{threshold:.2}}).observe(scr);
      }}
      /* Rueckfallebene 1: Scroll, greift auch wenn der Observer nie feuert. */
      window.addEventListener('scroll',lite,{{passive:true}}); lite();
      /* Rueckfallebene 2: Nach 6s wird der Abschnitt in jedem Fall sichtbar.
         Lieber die Sequenz verpassen als einen leeren Abschnitt zeigen. */
      setTimeout(function(){{ scr.classList.add('lit'); }},6000);
    }}
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(!reduced && 'IntersectionObserver' in window){{
      var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.12}});
      document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el);}});
    }} else {{ document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}}); }}
    setTimeout(function(){{ if(!document.querySelector('.reveal.in')){{ document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}}); }}
      if(scr&&!scr.classList.contains('lit')&&scr.getBoundingClientRect().top<window.innerHeight){{ scr.classList.add('lit'); }} }},2000);
  </script>
</body>
</html>
'''

for k in ORDER:
    d = L[k]
    path = (d['dir_'] + 'index.html') if d['dir_'] else 'index.html'
    if d['dir_']: os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path,'w',encoding='utf-8').write(build(k))
    print(f"{path:20} {os.path.getsize(path)/1024:6.1f} KB")

# /de/ ist der Spiegel der deutschen Seite mit absoluten Assetpfaden.
# Faengt alte Weiterleitungen aus der aheadx-Zeit ab, canonical zeigt auf /.
de = io.open('index.html', encoding='utf-8').read()
for a,b in [('src="assets/','src="/assets/'),('srcset="assets/','srcset="/assets/'),
            ('imagesrcset="assets/','imagesrcset="/assets/'),("url('assets/","url('/assets/"),
            (', assets/',', /assets/'),('href="assets/','href="/assets/')]:
    de = de.replace(a,b)
os.makedirs('de', exist_ok=True)
io.open('de/index.html','w',encoding='utf-8').write(de)
print(f"{'de/index.html':20} {os.path.getsize('de/index.html')/1024:6.1f} KB")

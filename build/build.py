#!/usr/bin/env python3
"""Erzeugt index.html (de), de/, en/ und th/ aus einer gemeinsamen Vorlage.

Sechs Kapitel: Hero, Haltung, Keynote, Warum Lukas, Beweis, Buchung.
Inhalte je Sprache im Dictionary L, Designsystem in build/style.css.
Die HTML-Dateien im Wurzelverzeichnis sind Build-Ergebnisse, nicht von Hand editieren.
"""
import io, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CSS = io.open('build/style.css', encoding='utf-8').read()
CSS_REL = CSS.replace("url('/assets/", "url('assets/")

THAI_FACES = """    @font-face{font-family:'Noto Sans Thai';font-style:normal;font-weight:400 600;font-display:swap;
      src:url('/assets/fonts/noto-sans-thai-thai.woff2') format('woff2');unicode-range:U+0E01-0E5B, U+200C-200D, U+25CC}
    @font-face{font-family:'Noto Serif Thai';font-style:normal;font-weight:400 600;font-display:swap;
      src:url('/assets/fonts/noto-serif-thai-thai.woff2') format('woff2');unicode-range:U+0E01-0E5B, U+200C-200D, U+25CC}"""

MAIL = "kontakt@lukaswagner.at"


def mailto(subject, fields):
    return f"mailto:{MAIL}?subject={subject}&amp;body=" + "%0A".join(f + "%3A" for f in fields) + "%0A"


L = {}

L['de'] = dict(
    lang='de', dir_='', locale='de_AT',
    title='Lukas Wagner | KI-Keynote-Speaker für Unternehmen, Städte &amp; Regionen',
    desc='Live-Keynotes, die künstliche Intelligenz verständlich, überraschend und gemeinsam erlebbar machen. Für Unternehmen, Konferenzen, Städte und Regionen.',
    og_title='Lukas Wagner | KI-Keynote-Speaker', og_desc='Die Zukunft passiert im Raum.',
    schema_desc='Österreichischer KI-Keynote-Speaker, Unternehmer und Gründer von ahead x. Macht künstliche Intelligenz verständlich und live erlebbar, für Unternehmen, Städte und Regionen.',
    job='KI-Keynote-Speaker',
    nav=[('keynote', 'Keynote'), ('warum', 'Warum Lukas'), ('aheadx', 'ahead x'), ('stimmen', 'Stimmen')],
    cta_main='KI-Keynote anfragen', cta_stage='Lukas auf die Bühne holen', cta_reel='Auftritte ansehen',
    menu_open='Menü öffnen', menu_close='Menü schließen', skip='Zum Inhalt springen',
    subj_keynote='Keynote-Anfrage%20Lukas%20Wagner', subj_workshop='Workshop-Anfrage%20Lukas%20Wagner',
    subj_region='Regionalformat%20%2F%20ahead%20x%20anfragen',
    f_key=['Datum', 'Ort', 'Zielgruppe', 'Anlass'], f_reg=['Stadt%2FRegion', 'Zeitraum', 'Zielgruppe', 'Anlass'],

    hero_micro='Lukas Wagner · KI-Keynote-Speaker',
    hero_pre='Die Zukunft ist kein weiterer Bildschirm.',
    hero_h1=['Die Zukunft passiert', 'im Raum.'],
    hero_sub='Live-Keynotes, die künstliche Intelligenz verständlich, überraschend und gemeinsam erlebbar machen. Für Unternehmen, Konferenzen, Städte und Regionen.',
    hero_alt='Lukas Wagner steht lächelnd im Theatersaal zwischen roten Sitzreihen unter warmem Bühnenlicht',

    hal_kicker='Die Haltung',
    hal_lines=['Mehr Werkzeuge.', 'Mehr Inhalte.', 'Mehr Antworten.'],
    hal_turn='Aber immer weniger Raum, um gemeinsam zu verstehen.',
    hal_close='Genau deshalb bringt Lukas Wagner künstliche Intelligenz aus dem Bildschirm in den Raum.',
    hal_alt='Voller Raum bei einem ahead x Format, Menschen hören gemeinsam zu',
    hal_cap='ahead x live, Fragerunde im vollen Raum',

    key_kicker='Die Keynote', key_h2='Verstehen. Erleben. Handeln.',
    scenes=[('Verstehen', 'Was ist relevant, und was nur Hype? KI wird eingeordnet, in klarer Sprache statt Fachjargon.', 'Eine gemeinsame Sprache für KI.'),
            ('Erleben', 'Live-Demos mit Fragen und Input aus dem Publikum. Was passiert, sieht der Saal in Echtzeit.', 'Eine realistische Vorstellung von Möglichkeiten und Grenzen.'),
            ('Handeln', 'Aus dem gemeinsamen Moment entstehen konkrete nächste Schritte, passend zur Organisation.', 'Ideen, die am nächsten Arbeitstag ausprobiert werden können.')],
    res_label='Was bleibt',
    scene2_alt='Lukas Wagner lächelt vor der Leinwand, während er eine Live-Demo zeigt',
    scene2_cap='Live-Demo vor Publikum',
    scene3_alt='Teilnehmerin arbeitet bei einem ahead x Workshop konzentriert an ihrem Laptop',
    scene3_cap='Hands-on nach der Keynote',

    fmt_kicker='Formate', fmt_h1='Die KI-Keynote',
    fmt_meta=[('Geeignet für', 'Konferenzen, Firmenevents, Führungstage sowie Stadt- und Zukunftsveranstaltungen.'),
              ('Das passiert', 'Einordnung, Live-Demos, Publikumsbeteiligung und konkreter Transfer.'),
              ('Das bleibt', 'Orientierung, Gesprächsstoff und nächste Schritte.')],
    fmt_small=[('Workshop', 'Für Teams, KMU und Organisationen.', 'KI-Werkzeuge am eigenen Arbeitsalltag getestet, begleitet und eingeordnet.', 'Workshop anfragen'),
               ('Regionalformat', 'Für Städte, Regionen und Partner.', 'Ein kuratiertes Live-Event mit lokalen Partnern aus Medien, Wirtschaft und Bildung.', 'Regionalformat anfragen')],

    why_kicker='Warum Lukas', why_h2='Bühne. Sprache. Format.',
    why_alt='Porträt von Lukas Wagner im Theatersaal',
    strengths=[('Bühne', 'Jahre auf Bühnen, auf denen Aufmerksamkeit unmittelbar gewonnen werden muss.'),
               ('Sprache', 'Komplexe Gedanken so verdichten, dass Menschen sie verstehen und erinnern.'),
               ('Format', 'Nicht nur Vorträge halten, sondern ganze Erlebnisse und Veranstaltungsreihen entwickeln.')],
    why_facts='Slam-Poet · 100+ Kulturveranstaltungen · Förderpreis 2017 · TEDxSalzburg Speaker-Coach · Gründer von ahead x',
    why_close='KI ist sein Thema. <em>Aufmerksamkeit ist sein Handwerk.</em>',

    pf_kicker='Der Beweis', pf_h2='Aus einem Raum wurden acht Städte.',
    pf_lead='Mit ahead x baut Lukas Wagner die Räume, über die er auf der Bühne spricht.',
    pf_steps=['Ein Abend', 'eine Stadt', 'acht Städte', 'eine Plattform'],
    pf_nums=[('9', 'Editionen'), ('8', 'Städte'), ('1.700+', 'Teilnahmen'), ('92 %', 'geben 4 oder 5 von 5')],
    pf_src='Zahlen: ahead x, Stand April 2026',
    pf_partners='Medien- &amp; Netzwerkpartner von ahead x', pf_cta='ahead x ansehen',
    quote_main=('Alle im Raum können nicht anders, als an seinen Lippen zu hängen.', 'Romy Sigl', 'CEO CoworkingSalzburg'),
    quotes=[('Seine Fähigkeit, komplexe KI-Konzepte verständlich und anschaulich zu vermitteln, macht ihn zu einem herausragenden Sprecher.', 'Stefan König', 'Finanzstratege'),
            ('Lukas übersetzt die Komplexität des Themas meisterhaft, ohne dabei an Tiefe zu verlieren.', 'Oliver Carl Drewo', 'Webdesign &amp; SEO')],
    quotes_link='Alle Empfehlungen auf LinkedIn',

    book_kicker='Anfrage', book_h2=['Ihr habt den Raum.', 'Lukas bringt die Zukunft.'],
    book_sub='Datum. Ort. Zielgruppe. Anlass. Mehr braucht es für den ersten Schritt nicht.',
    book_mail_pre='Direkt:', book_mail_post='auch für Presse &amp; Interviews',
    book_aside='Keine 87 Folien. Versprochen.',

    faq_kicker='FAQ', faq_h2='Kurz beantwortet.',
    faq=[('Für welche Veranstaltungen kann man Lukas Wagner buchen?', 'Für Konferenzen, Firmenevents, Stadt- und Regionalveranstaltungen, Verbände und Bildungseinrichtungen, als Keynote, Workshop oder Moderation rund um künstliche Intelligenz.'),
         ('Ist die Keynote auch für Einsteiger:innen geeignet?', 'Ja. KI wird ohne Fachjargon verständlich gemacht. Tiefe und Inhalt richten sich nach der Zielgruppe.'),
         ('Wie läuft eine Anfrage ab?', 'Kurze E-Mail mit Datum, Ort, Zielgruppe und Anlass, dann folgt eine ehrliche Einschätzung, welches Format passt.')],

    foot_nav=[('keynote', 'Keynote'), ('warum', 'Warum Lukas'), ('aheadx', 'ahead x'), ('kontakt', 'Anfrage')],
    legal_h=['Anbieter', 'Rechtsform &amp; Register', 'Kontakt'],
    legal_form='Florida Limited Liability Company<br />Reg.-Nr. L24000079118, Bundesstaat Florida<br />Vertreten durch Lukas M. Wagner',
    privacy='Datenschutzerklärung', privacy_url='/datenschutz.html',
    purpose='Unternehmensgegenstand: Keynotes, Workshops und Live-Formate zum Thema künstliche Intelligenz.',
    photo_credit='Eventfotos © Nussbaumer Photography',
)

L['en'] = dict(
    lang='en', dir_='en/', locale='en_US',
    title='Lukas Wagner | AI Keynote Speaker for Companies, Cities &amp; Regions',
    desc='Live keynotes that make artificial intelligence understandable, surprising and shared. For companies, conferences, cities and regions.',
    og_title='Lukas Wagner | AI Keynote Speaker', og_desc='The future happens in the room.',
    schema_desc='Austrian AI keynote speaker, entrepreneur and founder of ahead x. Makes artificial intelligence understandable and tangible on stage, for companies, cities and regions.',
    job='AI Keynote Speaker',
    nav=[('keynote', 'Keynote'), ('warum', 'Why Lukas'), ('aheadx', 'ahead x'), ('stimmen', 'Voices')],
    cta_main='Request a keynote', cta_stage='Bring Lukas to your stage', cta_reel='Watch talks',
    menu_open='Open menu', menu_close='Close menu', skip='Skip to content',
    subj_keynote='Keynote%20enquiry%20Lukas%20Wagner', subj_workshop='Workshop%20enquiry%20Lukas%20Wagner',
    subj_region='Regional%20format%20%2F%20ahead%20x%20enquiry',
    f_key=['Date', 'Location', 'Audience', 'Occasion'], f_reg=['City%2FRegion', 'Timeframe', 'Audience', 'Occasion'],

    hero_micro='Lukas Wagner · AI Keynote Speaker',
    hero_pre='The future is not another screen.',
    hero_h1=['The future happens', 'in the room.'],
    hero_sub='Live keynotes that make artificial intelligence understandable, surprising and shared. For companies, conferences, cities and regions.',
    hero_alt='Lukas Wagner stands smiling in a theatre between rows of red seats under warm stage light',

    hal_kicker='The belief',
    hal_lines=['More tools.', 'More content.', 'More answers.'],
    hal_turn='And less room to understand together.',
    hal_close='That is why Lukas Wagner brings artificial intelligence out of the screen and into the room.',
    hal_alt='A full room at an ahead x format, people listening together',
    hal_cap='ahead x live, question round in a full room',

    key_kicker='The keynote', key_h2='Understand. Experience. Act.',
    scenes=[('Understand', 'What is relevant, and what is only hype? AI is put in context, in plain language instead of jargon.', 'A shared language for AI.'),
            ('Experience', 'Live demos with questions and input from the audience. The room sees what happens in real time.', 'A realistic sense of what is possible and what is not.'),
            ('Act', 'The shared moment turns into concrete next steps, matched to the organisation.', 'Ideas you can try on the next working day.')],
    res_label='What stays',
    scene2_alt='Lukas Wagner smiles in front of the screen while showing a live demo',
    scene2_cap='Live demo in front of an audience',
    scene3_alt='A participant works focused on her laptop at an ahead x workshop',
    scene3_cap='Hands-on after the keynote',

    fmt_kicker='Formats', fmt_h1='The AI keynote',
    fmt_meta=[('Suited for', 'Conferences, corporate events, leadership days as well as city and future events.'),
              ('What happens', 'Context, live demos, audience participation and concrete transfer.'),
              ('What stays', 'Orientation, conversation and next steps.')],
    fmt_small=[('Workshop', 'For teams, SMEs and organisations.', 'AI tools tested on your own working day, guided and put in context.', 'Request a workshop'),
               ('Regional format', 'For cities, regions and partners.', 'A curated live event with local partners from media, business and education.', 'Request a regional format')],

    why_kicker='Why Lukas', why_h2='Stage. Language. Format.',
    why_alt='Portrait of Lukas Wagner in a theatre',
    strengths=[('Stage', 'Years on stages where attention has to be won immediately.'),
               ('Language', 'Condensing complex thoughts so people understand and remember them.'),
               ('Format', 'Not just giving talks, but building whole experiences and event series.')],
    why_facts='Slam poet · 100+ culture events · 2017 arts grant award · TEDxSalzburg speaker coach · Founder of ahead x',
    why_close='AI is his subject. <em>Attention is his craft.</em>',

    pf_kicker='The proof', pf_h2='One room became eight cities.',
    pf_lead='With ahead x, Lukas Wagner builds the rooms he talks about on stage.',
    pf_steps=['One evening', 'one city', 'eight cities', 'one platform'],
    pf_nums=[('9', 'editions'), ('8', 'cities'), ('1,700+', 'attendances'), ('92 %', 'rate it 4 or 5 out of 5')],
    pf_src='Figures: ahead x, as of April 2026',
    pf_partners='Media &amp; network partners of ahead x', pf_cta='See ahead x',
    quote_main=('Nobody in the room can help hanging on his every word.', 'Romy Sigl', 'CEO CoworkingSalzburg'),
    quotes=[('His ability to convey complex AI concepts clearly and vividly makes him an outstanding speaker.', 'Stefan König', 'financial strategist'),
            ('Lukas translates the complexity of the topic masterfully, without losing depth.', 'Oliver Carl Drewo', 'web design &amp; SEO')],
    quotes_link='All recommendations on LinkedIn',

    book_kicker='Enquiry', book_h2=['You have the room.', 'Lukas brings the future.'],
    book_sub='Date. Location. Audience. Occasion. That is all it takes for the first step.',
    book_mail_pre='Direct:', book_mail_post='also for press &amp; interviews',
    book_aside='No 87 slides. Promised.',

    faq_kicker='FAQ', faq_h2='Answered briefly.',
    faq=[('What kind of events can Lukas Wagner be booked for?', 'Conferences, corporate events, city and regional events, associations and educational institutions, as a keynote, workshop or moderation around artificial intelligence.'),
         ('Is the keynote suitable for beginners too?', 'Yes. AI is explained without jargon. Depth and content are matched to the audience.'),
         ('How does an enquiry work?', 'A short email with date, location, audience and occasion, followed by an honest assessment of which format fits.')],

    foot_nav=[('keynote', 'Keynote'), ('warum', 'Why Lukas'), ('aheadx', 'ahead x'), ('kontakt', 'Enquiry')],
    legal_h=['Provider', 'Legal form &amp; registry', 'Contact'],
    legal_form='Florida Limited Liability Company<br />Reg. no. L24000079118, State of Florida<br />Represented by Lukas M. Wagner',
    privacy='Privacy policy', privacy_url='/en/privacy.html',
    purpose='Business purpose: keynotes, workshops and live formats on artificial intelligence.',
    photo_credit='Event photos © Nussbaumer Photography',
)

L['th'] = dict(
    lang='th', dir_='th/', locale='th_TH',
    title='Lukas Wagner | วิทยากรคีย์โน้ต AI สำหรับองค์กร เมือง และภูมิภาค',
    desc='คีย์โน้ตสดที่ทำให้ปัญญาประดิษฐ์เข้าใจง่าย เหนือความคาดหมาย และสัมผัสได้ร่วมกัน สำหรับองค์กร งานประชุม เมือง และภูมิภาค',
    og_title='Lukas Wagner | วิทยากรคีย์โน้ต AI', og_desc='อนาคตเกิดขึ้นในพื้นที่จริง',
    schema_desc='วิทยากรคีย์โน้ตด้าน AI ชาวออสเตรีย ผู้ประกอบการ และผู้ก่อตั้ง ahead x ทำให้ปัญญาประดิษฐ์เข้าใจง่ายและสัมผัสได้จริงบนเวที สำหรับองค์กร เมือง และภูมิภาค',
    job='วิทยากรคีย์โน้ต AI',
    nav=[('keynote', 'คีย์โน้ต'), ('warum', 'ทำไมต้อง Lukas'), ('aheadx', 'ahead x'), ('stimmen', 'เสียงตอบรับ')],
    cta_main='ขอข้อมูลคีย์โน้ต AI', cta_stage='เชิญ Lukas ขึ้นเวทีของคุณ', cta_reel='ดูการบรรยาย',
    menu_open='เปิดเมนู', menu_close='ปิดเมนู', skip='ข้ามไปยังเนื้อหา',
    subj_keynote='Keynote%20enquiry%20Lukas%20Wagner', subj_workshop='Workshop%20enquiry%20Lukas%20Wagner',
    subj_region='Regional%20format%20%2F%20ahead%20x%20enquiry',
    f_key=['Date', 'Location', 'Audience', 'Occasion'], f_reg=['City%2FRegion', 'Timeframe', 'Audience', 'Occasion'],

    hero_micro='Lukas Wagner · วิทยากรคีย์โน้ต AI',
    hero_pre='อนาคตไม่ใช่หน้าจออีกอันหนึ่ง',
    hero_h1=['อนาคตเกิดขึ้น', 'ในพื้นที่จริง'],
    hero_sub='คีย์โน้ตสดที่ทำให้ปัญญาประดิษฐ์เข้าใจง่าย เหนือความคาดหมาย และสัมผัสได้ร่วมกัน สำหรับองค์กร งานประชุม เมือง และภูมิภาค',
    hero_alt='Lukas Wagner ยืนยิ้มอยู่ในโรงละคร ท่ามกลางแถวเก้าอี้สีแดงใต้แสงไฟเวทีอบอุ่น',

    hal_kicker='ความเชื่อ',
    hal_lines=['เครื่องมือมากขึ้น', 'เนื้อหามากขึ้น', 'คำตอบมากขึ้น'],
    hal_turn='แต่พื้นที่สำหรับทำความเข้าใจร่วมกันกลับน้อยลง',
    hal_close='ด้วยเหตุนี้ Lukas Wagner จึงนำปัญญาประดิษฐ์ออกจากหน้าจอเข้าสู่พื้นที่จริง',
    hal_alt='ห้องที่เต็มไปด้วยผู้คนในงานของ ahead x กำลังรับฟังร่วมกัน',
    hal_cap='ahead x สด ช่วงถามตอบในห้องที่เต็ม',

    key_kicker='คีย์โน้ต', key_h2='เข้าใจ สัมผัส ลงมือ',
    scenes=[('เข้าใจ', 'อะไรสำคัญจริง และอะไรเป็นเพียงกระแส AI ถูกจัดวางด้วยภาษาที่ชัดเจน ไม่ใช่ศัพท์เทคนิค', 'ภาษากลางสำหรับเรื่อง AI'),
            ('สัมผัส', 'การสาธิตสดพร้อมคำถามและโจทย์จากผู้ฟัง ทั้งห้องเห็นสิ่งที่เกิดขึ้นแบบเรียลไทม์', 'ภาพที่เป็นจริงว่าอะไรทำได้และอะไรทำไม่ได้'),
            ('ลงมือ', 'จากช่วงเวลาร่วมกันกลายเป็นก้าวถัดไปที่ชัดเจน เหมาะกับองค์กรนั้น ๆ', 'ไอเดียที่เริ่มลองได้ในวันทำงานถัดไป')],
    res_label='สิ่งที่เหลืออยู่',
    scene2_alt='Lukas Wagner ยิ้มอยู่หน้าจอขณะสาธิตการใช้งานสด',
    scene2_cap='การสาธิตสดต่อหน้าผู้ฟัง',
    scene3_alt='ผู้เข้าร่วมกำลังตั้งใจทำงานบนแล็ปท็อปในเวิร์กช็อปของ ahead x',
    scene3_cap='ลงมือทำหลังคีย์โน้ต',

    fmt_kicker='รูปแบบงาน', fmt_h1='คีย์โน้ต AI',
    fmt_meta=[('เหมาะกับ', 'งานประชุม งานองค์กร วันผู้บริหาร รวมถึงงานของเมืองและงานด้านอนาคต'),
              ('สิ่งที่เกิดขึ้น', 'การจัดวางภาพรวม การสาธิตสด การมีส่วนร่วมของผู้ฟัง และการนำไปใช้จริง'),
              ('สิ่งที่เหลืออยู่', 'ทิศทาง บทสนทนา และก้าวถัดไป')],
    fmt_small=[('เวิร์กช็อป', 'สำหรับทีม ธุรกิจขนาดกลางและเล็ก และองค์กร', 'ทดลองใช้เครื่องมือ AI กับงานจริง โดยมีคนแนะนำและช่วยจัดวาง', 'ขอข้อมูลเวิร์กช็อป'),
               ('รูปแบบงานระดับภูมิภาค', 'สำหรับเมือง ภูมิภาค และพันธมิตร', 'งานสดที่คัดสรรร่วมกับพันธมิตรท้องถิ่นจากสื่อ ภาคธุรกิจ และการศึกษา', 'ขอข้อมูลรูปแบบงานระดับภูมิภาค')],

    why_kicker='ทำไมต้อง Lukas', why_h2='เวที ภาษา รูปแบบงาน',
    why_alt='ภาพพอร์เทรตของ Lukas Wagner ในโรงละคร',
    strengths=[('เวที', 'หลายปีบนเวทีที่ต้องเรียกความสนใจให้ได้ทันที'),
               ('ภาษา', 'กลั่นความคิดที่ซับซ้อนให้ผู้คนเข้าใจและจดจำได้'),
               ('รูปแบบงาน', 'ไม่ใช่แค่บรรยาย แต่สร้างประสบการณ์และซีรีส์งานทั้งชุด')],
    why_facts='กวี Slam · จัดงานวัฒนธรรมกว่า 100 งาน · รางวัลสนับสนุนศิลปะ ปี 2017 · โค้ชนักพูด TEDxSalzburg · ผู้ก่อตั้ง ahead x',
    why_close='AI คือหัวข้อของเขา <em>ความสนใจของผู้คนคือทักษะของเขา</em>',

    pf_kicker='ข้อพิสูจน์', pf_h2='จากหนึ่งพื้นที่ กลายเป็นแปดเมือง',
    pf_lead='ด้วย ahead x Lukas Wagner สร้างพื้นที่ที่เขาพูดถึงบนเวทีขึ้นมาจริง',
    pf_steps=['หนึ่งค่ำคืน', 'หนึ่งเมือง', 'แปดเมือง', 'หนึ่งแพลตฟอร์ม'],
    pf_nums=[('9', 'ครั้ง'), ('8', 'เมือง'), ('1,700+', 'การเข้าร่วม'), ('92 %', 'ให้คะแนน 4 หรือ 5 จาก 5')],
    pf_src='ตัวเลข: ahead x ข้อมูล ณ เดือนเมษายน 2026',
    pf_partners='พันธมิตรด้านสื่อและเครือข่ายของ ahead x', pf_cta='ดู ahead x',
    quote_main=('ทุกคนในห้องอดไม่ได้ที่จะตั้งใจฟังทุกคำของเขา', 'Romy Sigl', 'CEO CoworkingSalzburg'),
    quotes=[('ความสามารถในการอธิบายแนวคิด AI ที่ซับซ้อนให้เข้าใจง่ายและเห็นภาพ ทำให้เขาเป็นนักพูดที่โดดเด่น', 'Stefan König', 'นักกลยุทธ์การเงิน'),
            ('Lukas ถ่ายทอดความซับซ้อนของหัวข้อได้อย่างเชี่ยวชาญ โดยไม่สูญเสียความลึก', 'Oliver Carl Drewo', 'เว็บดีไซน์ &amp; SEO')],
    quotes_link='อ่านคำแนะนำทั้งหมดบน LinkedIn',

    book_kicker='ติดต่อ', book_h2=['พื้นที่เป็นของคุณ', 'Lukas นำอนาคตมาให้'],
    book_sub='วันที่ สถานที่ กลุ่มผู้ฟัง และโอกาสของงาน แค่นี้ก็เริ่มต้นได้แล้ว',
    book_mail_pre='ติดต่อโดยตรง:', book_mail_post='สำหรับสื่อและการสัมภาษณ์ด้วย',
    book_aside='ไม่มีสไลด์ 87 แผ่น รับรอง',

    faq_kicker='คำถามที่พบบ่อย', faq_h2='ตอบสั้น ๆ',
    faq=[('จอง Lukas Wagner ไปพูดในงานแบบไหนได้บ้าง', 'งานประชุม งานองค์กร งานของเมืองและภูมิภาค สมาคม และสถาบันการศึกษา ทั้งในรูปแบบคีย์โน้ต เวิร์กช็อป หรือการดำเนินรายการในหัวข้อปัญญาประดิษฐ์'),
         ('คีย์โน้ตนี้เหมาะกับผู้เริ่มต้นด้วยหรือไม่', 'เหมาะ เนื้อหาอธิบายโดยไม่ใช้ศัพท์เทคนิค ความลึกและรายละเอียดปรับตามกลุ่มผู้ฟัง'),
         ('ขั้นตอนการติดต่อเป็นอย่างไร', 'ส่งอีเมลสั้น ๆ พร้อมวันที่ สถานที่ กลุ่มผู้ฟัง และโอกาสของงาน จากนั้นจะได้รับคำแนะนำตรงไปตรงมาว่ารูปแบบไหนเหมาะที่สุด')],

    foot_nav=[('keynote', 'คีย์โน้ต'), ('warum', 'ทำไมต้อง Lukas'), ('aheadx', 'ahead x'), ('kontakt', 'ติดต่อ')],
    legal_h=['ผู้ให้บริการ', 'รูปแบบทางกฎหมายและทะเบียน', 'ติดต่อ'],
    legal_form='Florida Limited Liability Company<br />ทะเบียนเลขที่ L24000079118 รัฐฟลอริดา<br />ดำเนินการโดย Lukas M. Wagner',
    privacy='นโยบายความเป็นส่วนตัว', privacy_url='/th/privacy.html',
    purpose='วัตถุประสงค์ของธุรกิจ: คีย์โน้ต เวิร์กช็อป และงานสดในหัวข้อปัญญาประดิษฐ์',
    photo_credit='ภาพงาน © Nussbaumer Photography',
)

ORDER = ['de', 'en', 'th']
CODE = {'de': 'DE', 'en': 'EN', 'th': 'TH'}
URLS = {'de': '/', 'en': '/en/', 'th': '/th/'}


def langs(cur):
    out = []
    for i, k in enumerate(ORDER):
        if i:
            out.append('<span aria-hidden="true">·</span>')
        cu = ' aria-current="page"' if k == cur else ''
        out.append(f'<a href="{URLS[k]}" hreflang="{k}" lang="{k}"{cu}>{CODE[k]}</a>')
    return '<span class="langs" role="group" aria-label="Sprache / Language">' + ''.join(out) + '</span>'


def build(k):
    d = L[k]
    A = '/assets/' if d['dir_'] else 'assets/'
    css = CSS if d['dir_'] else CSS_REL
    if k == 'th':
        css = (THAI_FACES + "\n" + css
               + "\n    /* Thai: Fallback-Schriften, mehr Zeilenhoehe, kein Buchstabenabstand */\n"
               + '    :root{--serif:"Fraunces","Noto Serif Thai",Georgia,serif;--sans:"Inter","Noto Sans Thai",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}\n'
               + "    h1{line-height:1.2}\n    h2,.scene h3,.str h3,.quote-main blockquote p,.hal-turn{line-height:1.42}\n"
               + "    .kicker,.hero-micro,.pf-num span,.res-label,.legal-grid b{letter-spacing:normal}\n")

    mk = mailto(d['subj_keynote'], d['f_key'])
    mw = mailto(d['subj_workshop'], d['f_key'])
    mr = mailto(d['subj_region'], d['f_reg'])

    alt = "\n".join(f'  <link rel="alternate" hreflang="{x}" href="https://lukaswagner.at{URLS[x]}" />' for x in ORDER)
    alt += '\n  <link rel="alternate" hreflang="x-default" href="https://lukaswagner.at/" />'

    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q.replace('&amp;', '&'),
         "acceptedAnswer": {"@type": "Answer", "text": a.replace('&amp;', '&')}}
        for q, a in d['faq']]}, ensure_ascii=False)

    navl = "\n".join(f'        <a href="#{i}">{t}</a>' for i, t in d['nav'])
    footnav = "".join(f'<a href="#{i}">{t}</a>' for i, t in d['foot_nav'])
    hal = "\n".join(f'          <p class="hal-line hal-{i+1}">{t}</p>' for i, t in enumerate(d['hal_lines']))
    h1 = f'<span class="hl">{d["hero_h1"][0]}</span> <em>{d["hero_h1"][1]}</em>'

    # Szene 01 traegt bewusst keine Fotografie: es gibt nur vier echte Bilder und
    # jedes hat bereits eine eigene Aufgabe. Wiederholung waere schwaecher als Weissraum.
    figs = [None,
            (f'{A}speaker-reel-thumb.jpg', f'{A}speaker-reel-thumb-900.jpg 900w, {A}speaker-reel-thumb.jpg 1500w',
             1500, 1000, d['scene2_alt'], d['scene2_cap']),
            (f'{A}aheadx-demo.jpg', f'{A}aheadx-demo-800.jpg 533w, {A}aheadx-demo.jpg 866w',
             866, 1300, d['scene3_alt'], d['scene3_cap'])]
    scenes = []
    for i, (t, p_, res) in enumerate(d['scenes']):
        f = figs[i]
        fig = ''
        if f:
            fig = (f'\n            <figure class="scene-fig">\n'
                   f'              <img src="{f[0]}" srcset="{f[1]}" sizes="(max-width:820px) 92vw, 44vw"\n'
                   f'                   width="{f[2]}" height="{f[3]}" loading="lazy" alt="{f[4]}" />\n'
                   f'              <figcaption>{f[5]}</figcaption>\n            </figure>')
        scenes.append(
            f'          <article class="scene scene-{i+1} reveal">\n'
            f'            <div class="scene-copy">\n'
            f'              <span class="scene-no">0{i+1}</span>\n'
            f'              <h3>{t}</h3>\n'
            f'              <p>{p_}</p>\n'
            f'              <p class="scene-res"><span class="res-label">{d["res_label"]}</span> {res}</p>\n'
            f'            </div>{fig}\n'
            f'          </article>')
    scenes = "\n".join(scenes)

    fmt_meta = "\n".join(f'              <div><dt>{t}</dt><dd>{v}</dd></div>' for t, v in d['fmt_meta'])
    fmt_small = "\n".join(
        f'          <article class="fmt-s reveal"><h3>{t}</h3><p class="fmt-who">{who}</p><p>{p_}</p>'
        f'<a class="tlink" data-cta="{"workshop" if i == 0 else "aheadx"}" href="{mw if i == 0 else mr}">{cta} →</a></article>'
        for i, (t, who, p_, cta) in enumerate(d['fmt_small']))
    strengths = "\n".join(
        f'            <div class="str reveal"><h3>{t}</h3><p>{p_}</p></div>'
        for t, p_ in d['strengths'])
    steps = '<span class="pf-arrow" aria-hidden="true">→</span>'.join(
        f'<span class="pf-step">{t}</span>' for t in d['pf_steps'])
    nums = "\n".join(
        f'          <div class="pf-num"><b>{n}</b><span>{l}</span></div>' for n, l in d['pf_nums'])
    quotes = "\n".join(
        f'          <figure class="reveal"><p>{q}</p><figcaption><b>{n}</b> · {r}</figcaption></figure>'
        for q, n, r in d['quotes'])
    faq_html = "\n".join(f'          <details><summary>{q}</summary><p>{a}</p></details>' for q, a in d['faq'])
    book_h2 = f'{d["book_h2"][0]}<br /><em>{d["book_h2"][1]}</em>'

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
  <meta property="og:locale" content="{d['locale']}" />
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
        imagesizes="(max-width:820px) 100vw, 56vw" fetchpriority="high" />

  <script type="application/ld+json">
  {{ "@context":"https://schema.org","@type":"Person","name":"Lukas Wagner","jobTitle":"{d['job']}",
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
        <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_main']}</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <span id="top"></span>

    <!-- 01 HERO. Das Theaterfoto traegt die Flaeche, die Schrift bleibt ruhig. -->
    <section class="hero" aria-label="Intro">
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="hero-micro">{d['hero_micro']}</p>
          <p class="hero-pre">{d['hero_pre']}</p>
          <h1>{h1}</h1>
          <p class="sub">{d['hero_sub']}</p>
          <div class="hero-cta">
            <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_main']}</a>
            <a class="btn btn-ghost" data-cta="speaker-reel" href="https://www.youtube.com/@lukaswagnerai" target="_blank" rel="noopener">{d['cta_reel']}&nbsp;↗</a>
          </div>
        </div>
        <figure class="hero-fig">
          <img src="{A}lukas-stage.jpg"
               srcset="{A}lukas-stage-800.jpg 533w, {A}lukas-stage.jpg 1066w"
               sizes="(max-width:820px) 100vw, 56vw"
               width="1066" height="1600" fetchpriority="high" alt="{d['hero_alt']}" />
          <span class="hero-spot" aria-hidden="true"></span>
        </figure>
      </div>
    </section>

    <!-- 02 DIE HALTUNG. Verdichtung, Stille, dann oeffnet sich der Raum. -->
    <section id="haltung" class="haltung" aria-label="{d['hal_kicker']}">
      <div class="wrap">
        <p class="kicker">{d['hal_kicker']}</p>
        <div class="hal-stack">
{hal}
          <div class="hal-pause" aria-hidden="true"></div>
          <p class="hal-turn">{d['hal_turn']}</p>
        </div>
      </div>
      <figure class="hal-fig">
        <img src="{A}aheadx-audience.jpg"
             srcset="{A}aheadx-audience-900.jpg 900w, {A}aheadx-audience.jpg 1500w"
             sizes="100vw" width="1500" height="1000" loading="lazy" alt="{d['hal_alt']}" />
        <figcaption>{d['hal_cap']}</figcaption>
      </figure>
      <div class="wrap">
        <p class="hal-close reveal">{d['hal_close']}</p>
      </div>
    </section>

    <!-- 03 DIE KEYNOTE. Drei Szenen statt fuenf Akten plus separatem Ergebnisblock. -->
    <section id="keynote" class="on-paper" aria-label="{d['key_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['key_kicker']}</p>
          <h2>{d['key_h2']}</h2>
        </div>
        <div class="scenes">
{scenes}
        </div>

        <article class="fmt-main reveal">
          <p class="kicker">{d['fmt_kicker']}</p>
          <h3>{d['fmt_h1']}</h3>
          <dl class="fmt-meta">
{fmt_meta}
          </dl>
          <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_main']}</a>
        </article>
        <div class="fmt-row">
{fmt_small}
        </div>
      </div>
    </section>

    <!-- 04 WARUM LUKAS. Drei Staerken statt fuenf Rollen. -->
    <section id="warum" aria-label="{d['why_kicker']}">
      <div class="wrap why-grid">
        <figure class="why-fig reveal">
          <img src="{A}lukas-stage.jpg"
               srcset="{A}lukas-stage-800.jpg 533w, {A}lukas-stage.jpg 1066w"
               sizes="(max-width:820px) 92vw, 32vw"
               width="1066" height="1600" loading="lazy" alt="{d['why_alt']}" />
        </figure>
        <div class="why-copy">
          <div class="sec-head reveal">
            <p class="kicker">{d['why_kicker']}</p>
            <h2>{d['why_h2']}</h2>
          </div>
          <div class="strengths">
{strengths}
          </div>
          <!-- OFFEN: biografische Angaben stammen aus dem Briefing von LW, extern noch nicht belegt. -->
          <p class="why-facts reveal">{d['why_facts']}</p>
          <p class="why-close reveal">{d['why_close']}</p>
        </div>
      </div>
    </section>

    <!-- 05 DER BEWEIS. ahead x, Zahlen, Partner und Stimmen in einem Kapitel. -->
    <section id="aheadx" class="band" aria-label="{d['pf_kicker']}">
      <div class="wrap">
        <div class="sec-head reveal">
          <p class="kicker">{d['pf_kicker']}</p>
          <h2>{d['pf_h2']}</h2>
          <p class="lead-in">{d['pf_lead']}</p>
        </div>
        <p class="pf-path reveal">{steps}</p>
        <!-- Zahlen belegt auf aheadx.at, Stand 30.04.2026. -->
        <div class="pf-nums reveal">
{nums}
        </div>
        <p class="pf-src reveal">{d['pf_src']}</p>

        <p class="pf-partners-t reveal">{d['pf_partners']}</p>
        <div class="logo-row reveal">
          <span class="lg"><img src="{A}logos/dcv.png" alt="Digital Campus Vorarlberg" loading="lazy" width="120" height="32" /></span>
          <span class="lg"><img src="{A}logos/vn.png" alt="Vorarlberger Nachrichten" loading="lazy" width="120" height="32" /></span>
          <span class="lg"><img src="{A}logos/vol.png" alt="VOL.at" loading="lazy" width="120" height="32" /></span>
          <span class="lg"><img src="{A}logos/neue.png" alt="NEUE am Sonntag" loading="lazy" width="120" height="32" /></span>
          <span class="lg"><img src="{A}logos/tt.png" alt="Tiroler Tageszeitung" loading="lazy" width="120" height="32" /></span>
          <span class="lg"><img src="{A}logos/kleine-zeitung.svg" alt="Kleine Zeitung" loading="lazy" width="120" height="32" /></span>
        </div>
        <p class="pf-cta reveal"><a class="tlink" data-cta="aheadx" href="https://aheadx.at" target="_blank" rel="noopener">{d['pf_cta']}&nbsp;↗</a></p>
      </div>

      <div id="stimmen" class="wrap quotes">
        <!-- OFFEN: Freigabe von Wortlaut und Rolle der zitierten Personen. -->
        <figure class="quote-main reveal">
          <blockquote><p>{d['quote_main'][0]}</p></blockquote>
          <figcaption><b>{d['quote_main'][1]}</b> · {d['quote_main'][2]}</figcaption>
        </figure>
        <div class="quote-row">
{quotes}
        </div>
        <p class="quote-src reveal"><a class="tlink" href="https://www.linkedin.com/in/lukaswagnerai/details/recommendations/" target="_blank" rel="noopener">{d['quotes_link']} →</a></p>
      </div>
    </section>

    <!-- 06 BUCHUNG -->
    <section id="kontakt" class="book" aria-label="{d['book_kicker']}">
      <div class="book-beam" aria-hidden="true"></div>
      <div class="wrap book-inner">
        <p class="kicker reveal">{d['book_kicker']}</p>
        <h2 class="reveal">{book_h2}</h2>
        <p class="sub reveal">{d['book_sub']}</p>
        <div class="hero-cta reveal">
          <a class="btn btn-primary" data-cta="keynote" href="{mk}">{d['cta_stage']}</a>
          <a class="btn btn-ghost" data-cta="speaker-reel" href="https://www.youtube.com/@lukaswagnerai" target="_blank" rel="noopener">{d['cta_reel']}&nbsp;↗</a>
        </div>
        <p class="book-mail reveal">{d['book_mail_pre']} <a href="mailto:{MAIL}">{MAIL}</a> · {d['book_mail_post']}</p>
        <p class="aside reveal">{d['book_aside']}</p>
      </div>
    </section>

    <section id="faq" class="band faq-sec" aria-label="{d['faq_kicker']}">
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
        <!-- OFFEN: Urheber-Credit fuer das Theaterfoto fehlt noch. -->
        <div class="legal-grid">
          <div><b>{d['legal_h'][0]}</b>SHINK BIG LLC<br />7901 4th St N, Ste 300<br />St. Petersburg, FL 33702, USA</div>
          <div><b>{d['legal_h'][1]}</b>{d['legal_form']}</div>
          <div><b>{d['legal_h'][2]}</b><a href="mailto:{MAIL}">{MAIL}</a><br /><a href="{d['privacy_url']}">{d['privacy']}</a></div>
        </div>
        <p class="legal-foot">{d['purpose']} © <span id="year">2026</span> SHINK BIG LLC · {d['photo_credit']}</p>
      </div>
    </div>
  </footer>

  <a class="sticky-cta" data-cta="keynote" href="{mk}"><span class="btn btn-primary">{d['cta_main']}</span></a>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    var t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');
    if(t){{t.addEventListener('click',function(){{var o=m.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');t.setAttribute('aria-label',o?'{d['menu_close']}':'{d['menu_open']}');}});
      m.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{m.classList.remove('open');t.setAttribute('aria-expanded','false');}});}});}}
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    /* Sticky-CTA erscheint erst, wenn der Hero aus dem Blick ist. */
    var sticky=document.querySelector('.sticky-cta'),hero=document.querySelector('.hero');
    if(sticky&&hero&&'IntersectionObserver' in window){{
      new IntersectionObserver(function(es){{es.forEach(function(e){{sticky.classList.toggle('show',!e.isIntersecting);}});}},{{rootMargin:'-80px 0px 0px 0px'}}).observe(hero);
    }}
    /* Zurueckhaltender Scheinwerfer, nur bei Maus und nur per transform. */
    var spot=document.querySelector('.hero-spot'),hfig=document.querySelector('.hero-fig');
    if(spot&&hfig&&!reduced&&window.matchMedia('(pointer:fine)').matches){{
      var pend=null;
      hfig.addEventListener('pointermove',function(e){{
        if(pend)return;
        pend=requestAnimationFrame(function(){{
          var r=hfig.getBoundingClientRect();
          spot.style.transform='translate3d('+(e.clientX-r.left)+'px,'+(e.clientY-r.top)+'px,0)';
          pend=null;}});
      }},{{passive:true}});
    }}
    /* Die Haltungs-Sequenz laeuft einmal. Drei Wege, damit nie ein leerer Abschnitt entsteht. */
    var hal=document.querySelector('.haltung');
    if(hal){{
      var lite=function(){{ if(!hal.classList.contains('lit')&&hal.getBoundingClientRect().top<window.innerHeight*.8){{
        hal.classList.add('lit'); window.removeEventListener('scroll',lite); }} }};
      if('IntersectionObserver' in window){{
        new IntersectionObserver(function(es,o){{es.forEach(function(e){{if(e.isIntersecting){{hal.classList.add('lit');o.disconnect();}}}});}},{{threshold:.2}}).observe(hal);
      }}
      window.addEventListener('scroll',lite,{{passive:true}}); lite();
      setTimeout(function(){{hal.classList.add('lit');}},6000);
    }}
    if(!reduced && 'IntersectionObserver' in window){{
      var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.12}});
      document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el);}});
    }} else {{ document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}}); }}
    setTimeout(function(){{ if(!document.querySelector('.reveal.in')){{ document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}}); }} }},2000);
  </script>
</body>
</html>
'''


for k in ORDER:
    d = L[k]
    path = (d['dir_'] + 'index.html') if d['dir_'] else 'index.html'
    if d['dir_']:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8').write(build(k))
    print(f"{path:20} {os.path.getsize(path)/1024:6.1f} KB")

# /de/ spiegelt die deutsche Seite mit absoluten Assetpfaden und faengt alte
# Weiterleitungen aus der aheadx-Zeit ab. Canonical zeigt auf /.
de = io.open('index.html', encoding='utf-8').read()
for a, b in [('src="assets/', 'src="/assets/'), ('srcset="assets/', 'srcset="/assets/'),
             ('imagesrcset="assets/', 'imagesrcset="/assets/'), ("url('assets/", "url('/assets/"),
             (', assets/', ', /assets/'), ('href="assets/', 'href="/assets/')]:
    de = de.replace(a, b)
os.makedirs('de', exist_ok=True)
io.open('de/index.html', 'w', encoding='utf-8').write(de)
print(f"{'de/index.html':20} {os.path.getsize('de/index.html')/1024:6.1f} KB")

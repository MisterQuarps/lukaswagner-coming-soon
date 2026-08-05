# lukaswagner.at · Markenthese, Asset-Brief, Claim-Verifikation und offene Punkte

## 0. Zentrale Markenthese

**Zukunft entsteht im Raum.** (EN: The future happens in the room.)

Je digitaler die Welt wird, desto mehr zaehlt der Raum, in dem Menschen zusammenkommen.
Das ist ausdruecklich **keine** technikfeindliche Haltung: Die Zukunft wird digital sein.
Was sie bedeutsam macht, entsteht in echten Raeumen. KI skaliert Information,
aber Vertrauen, Zugehoerigkeit, gemeinsame Aufmerksamkeit und der Mut zur Veraenderung
entstehen dort, wo Menschen physisch zusammen sind.

Die These traegt die Seite, wird aber nicht in jedem Abschnitt wiederholt.
Sie ist verankert in: Hero, Signature-Abschnitt "Another screen", Erlebnis-Einleitung
("KI liefert Antworten. Ein Raum schafft Verstaendnis."), ahead-x-Case
("KI ist global. Verstaendnis beginnt lokal.") und Warum-Lukas
("Technologie veraendert sich. Das Beduerfnis, gemeinsam zu verstehen, nicht.").

Verboten sind Aussagen wie "digital ist schlecht", "zurueck ins Analoge" oder
"KI zerstoert Beziehungen". Die kommerzielle Hauptleistung bleibt unveraendert:
KI-Keynote-Speaker fuer Unternehmen, Staedte und Regionen.


Stand: 04.08.2026 · gilt für `index.html` und den Spiegel `de/index.html`

Diese Datei ersetzt die früher sichtbaren Asset-Slot-Boxen auf der Website.
Auf der Seite selbst stehen keine Dateinamen, Auflösungen oder Produktionshinweise mehr.
An jeder späteren Einfügestelle liegt zusätzlich ein kurzer HTML-Kommentar.

---

## 1. Status Livegang

Die Seite ist seit 05.08.2026 live und indexierbar. `noindex, nofollow` und `Disallow: /` sind entfernt.

Betreiberin ist **SHINK BIG LLC** (Florida, Reg.-Nr. L24000079118), Lukas Wagner hat keinen festen
Wohnsitz und haelt sich hoechstens vier Monate im Jahr in Oesterreich auf. Die oesterreichischen
Offenlegungspflichten nach ECG und MedienG knuepfen an Niederlassung beziehungsweise Sitz oder
Wohnsitz an und greifen in dieser Konstellation sehr wahrscheinlich nicht. Im Footer steht deshalb
eine freiwillige Anbieterkennzeichnung, nicht ein Impressum nach oesterreichischem Recht.
Die DSGVO gilt dagegen ueber das Marktortprinzip, weil sich das Angebot an Menschen im EWR richtet.

### Noch offen

| # | Punkt | Wo | Verantwortlich |
|---|---|---|---|
| 1 | **Urheber-Credit fuer das Theaterfoto** im Hero. Der bestehende Credit deckt nur die Eventfotos ab. | Footer `.legal-foot` | Lukas Wagner |
| 2 | **Claim "500+ Auftritte auf Buehnen"** bestaetigen oder entfernen. Einzige Zahl der Seite ohne oeffentlichen Beleg. | Hero `.hero-trust` | Lukas Wagner |
| 3 | **Biografische Angaben** bestaetigen (100+ Veranstaltungen, Foerderpreis 2017, TEDxSalzburg). | `#warum` | Lukas Wagner |
| 4 | **Testimonials**: Wortlaut und Einverstaendnis der vier Personen. Die Zitate waren bereits vor diesem Livegang oeffentlich, das Thema ist damit nicht neu, aber weiter offen. | `#stimmen` | Lukas Wagner |
| 5 | **Anwaltliche Durchsicht der Datenschutzerklaerung**, insbesondere die Frage eines EU-Vertreters nach Art. 27 DSGVO fuer Verantwortliche ausserhalb der EU. Fuer eine reine Broschuerenseite greift moeglicherweise die Ausnahme, das sollte jemand mit Zulassung beurteilen. | `datenschutz.html` | Lukas Wagner |
| 6 | **Steuerliche Einordnung** der Konstellation US-LLC plus Events in acht oesterreichischen Staedten (Betriebsstaette, Ort der Geschaeftsleitung). Kein Website-Thema, aber vermutlich das gewichtigere. | extern | Steuerberater |

## 1b. Sprachversionen

| Sprache | URL | Datenschutz |
|---|---|---|
| Deutsch (Standard) | `/` | `/datenschutz.html` |
| Englisch | `/en/` | `/en/privacy.html` |
| Thai | `/th/` | `/th/privacy.html` |

`/de/` bleibt als Spiegel der deutschen Seite bestehen und faengt alte Weiterleitungen aus der
aheadx-Zeit ab. Er zeigt per canonical auf `/`.

**Build:** Alle vier Seiten (`index.html`, `de/`, `en/`, `th/`) werden erzeugt mit

    python3 build/build.py

Inhalte liegen als Dictionary je Sprache in `build/build.py`, das Designsystem in
`build/style.css`. Wer Inhalte oder Styles aendert, aendert sie dort und generiert neu.
Die HTML-Dateien im Wurzelverzeichnis sind Build-Ergebnisse und werden nicht von Hand editiert.

Thai nutzt zusaetzlich Noto Sans Thai und Noto Serif Thai als Fallback. Latein bleibt
Fraunces und Inter, die Umschaltung passiert automatisch ueber `unicode-range`.

**Offen:** Die thailändische Uebersetzung stammt von Claude und sollte vor ernsthaftem
Vertriebseinsatz von einer thailaendischen Muttersprachlerin gegengelesen werden.
Die englischen Testimonials sind Uebersetzungen der deutschen Originalzitate.

## 2. Fehlende Medien nach Priorität

Die Seite funktioniert ohne diese Assets vollständig. Kein Platzhalter, keine Lücke.
Jedes neue Asset ist ein Upgrade, keine Reparatur.

### Priorität 1 · Speaker-Reel (größter Hebel)

| Feld | Vorgabe |
|---|---|
| Datei | `assets/speaker-reel.mp4` + `assets/speaker-reel-poster.jpg` |
| Inhalt | 60 bis 90 Sekunden aus echten Auftritten: Bühne, Publikumsreaktion, Live-Demo, Transfer |
| Format | 16:9, min. 1920 × 1080 px, Poster in gleicher Größe |
| Einbettung | lokal gehostet oder datenschutzfreundlicher Embed |
| Regeln | kein Autoplay mit Ton, Laufzeit erst anzeigen, wenn der Schnitt final ist |
| Einsatzort | Hero als sekundäre Aktion und im Abschnitt `#erlebnis` |
| Bis dahin | ehrlicher Link „Auftritte auf YouTube ansehen" ohne simulierte Laufzeit. Bereits umgesetzt. |

### Priorität 2 · Live-Aufnahme von Lukas vor Publikum

| Feld | Vorgabe |
|---|---|
| Datei | `assets/lukas-live.jpg` |
| Motiv | Lukas auf der Bühne, Publikum im Bild, Blick oder Geste ins Publikum, echte Veranstaltung |
| Ausschnitt | Halbtotale, Lukas nicht kleiner als ein Drittel der Bildhöhe |
| Format | 3:2 quer, min. 2000 × 1333 px |
| Mobil-Crop | 4:3, Lukas mittig |
| Alt-Text | „Lukas Wagner spricht auf einer Bühne vor vollem Publikum" |
| Einsatzort | zweite Beweisebene im Hero, alternativ als Breitband in `#erlebnis` |
| Warum wichtig | Das Theaterfoto im Hero ist ein Porträt im leeren Saal. Es zeigt Persönlichkeit, aber keinen Auftritt. |

### Priorität 3 · Nahes Portrait

| Feld | Vorgabe |
|---|---|
| Datei | `assets/lukas-portrait-close.jpg` |
| Motiv | ruhiger menschlicher Moment, Blickkontakt, warmes Licht, kein Studio-Freisteller |
| Format | 4:5 hoch, min. 1200 × 1500 px |
| Alt-Text | „Porträt von Lukas Wagner" |
| Einsatzort | optional in `#warum`, links neben den vier Ebenen |
| Hinweis | Der Abschnitt ist bewusst so gebaut, dass er ohne Bild funktioniert. Ein Portrait ist eine Verbesserung, keine Voraussetzung. |

### Priorität 4 · ahead-x-Event mit Lukas und Publikum

| Feld | Vorgabe |
|---|---|
| Datei | `assets/aheadx-event.jpg` |
| Motiv | Lukas moderiert oder spricht bei einem ahead x Event, Publikum sichtbar, Raumgefühl |
| Format | 4:5 hoch, min. 1000 × 1250 px |
| Alt-Text | „Lukas Wagner moderiert ein ahead x Event vor vollem Saal" |
| Einsatzort | `#aheadx`, rechte Spalte neben der Case-Logik |
| Ersetzt | `assets/aheadx-tour.jpg`. Dieses Foto zeigt einen anderen Speaker und wird deshalb nicht verwendet. Die Datei bleibt im Repo, ist aber nirgends eingebunden. |

### Priorität 5 · Workshop-Situation mit Lukas

| Feld | Vorgabe |
|---|---|
| Datei | `assets/workshop-hands-on.jpg` |
| Motiv | Lukas im Gespräch am Tisch, offene Laptops, echte Arbeitssituation, keine gestellte Pose |
| Format | 16:10 quer, min. 1600 × 1000 px |
| Mobil-Crop | 4:3, zwei Personen mittig |
| Alt-Text | „Lukas Wagner begleitet Teilnehmende beim Ausprobieren von KI-Werkzeugen" |
| Einsatzort | `#formate`, Format 02 |
| Bis dahin | `assets/aheadx-demo.jpg` ist im Einsatz. Es dokumentiert eine echte Hands-on-Situation aus Teilnehmendenperspektive. Die Bildunterschrift „Hands-on bei einem ahead x Workshop" benennt genau das und behauptet nicht, Lukas sei abgebildet. |

---

## 3. Aktuell verwendete Bilder

| Datei | Maße | Varianten | Einsatz |
|---|---|---|---|
| `lukas-stage.jpg` | 1066 × 1600 | `lukas-stage-800.jpg` (533 × 800) | Hero, preloaded |
| `aheadx-audience.jpg` | 1500 × 1000 | `aheadx-audience-900.jpg` (900 × 600) | Breitband in `#erlebnis` |
| `speaker-reel-thumb.jpg` | 1500 × 1000 | `speaker-reel-thumb-900.jpg` (900 × 600) | Keynote-Feature in `#formate` |
| `aheadx-demo.jpg` | 866 × 1300 | `aheadx-demo-800.jpg` (533 × 800) | Workshop in `#formate` |
| `logos/*.png,svg` | div. | keine | Partnerzeile im Proof-Strip |
| `og-image.jpg` | 1200 × 630 | keine | Open Graph |
| `lukas-portrait.jpg` | 733 × 1100 | keine | nur Person-Schema. **Identisch mit `lukas-stage.jpg`**, nur kleiner. |
| `aheadx-tour.jpg` | 1000 × 1500 | keine | **nicht eingebunden**, zeigt einen fremden Speaker |

Hinweis zu `srcset`: Die Breitenangaben entsprechen den tatsächlichen Pixelbreiten.
`aheadx-demo-800.jpg` ist 533 px breit und wird korrekt als `533w` deklariert, nicht als `800w`.

---

## 4. Claim-Verifikation

Quelle „aheadx.at" = öffentlich auf der Startseite von aheadx.at, abgerufen am 04.08.2026, dort mit „Stand 30.04.2026" ausgewiesen.

| Sichtbare Aussage | Quelle | Genaue Definition | Status | Fundstelle |
|---|---|---|---|---|
| „1.700+ Teilnahmen bei ahead x" | aheadx.at | Originalwortlaut: „1 702+ Teilnahmen bei allen bisherigen ahead x Formaten". **Teilnahmen, nicht Personen.** Eine Person, die dreimal kommt, zählt dreifach. | **verifiziert** | Hero, Proof-Strip |
| „8 Städte mit eigenen Live-Formaten" | aheadx.at | Originalwortlaut: „1 702+ Menschen in 8 Städten" | **verifiziert** | Hero, Proof-Strip, Case |
| „9 Editionen" | aheadx.at | 9 bisher durchgeführte ahead x Editionen | **verifiziert** | Case `#aheadx` |
| „92 % geben 4 oder 5 von 5 Punkten" | aheadx.at | Originalwortlaut: „92% geben 4 oder 5 von 5". **Anteil der Top-2-Bewertungen, nicht allgemeine Zufriedenheit.** Stichprobengröße und exakte Fragestellung sind nicht veröffentlicht und sollten intern ergänzt werden. | **verifiziert, Metrik präzisiert** | Case `#aheadx` |
| Formatfamilie city / labs / mastermind / future | aheadx.at | mastermind ist dort als „in Vorbereitung" ausgewiesen, das ist auf der Seite so benannt | **verifiziert** | `#formate`, Format 03 |
| Partnerlogos (Digital Campus Vorarlberg, VN, VOL.at, NEUE, Tiroler Tageszeitung, Kleine Zeitung) | aheadx.at | dort als Medien- und Netzwerkpartner gelistet | **verifiziert**; Nutzungsrecht der Logos auf lukaswagner.at separat klären | Proof-Strip |
| „500+ Auftritte auf Bühnen" | Briefing Lukas Wagner | Definition offen: zählt Slam-Auftritte, Moderationen und Keynotes zusammen | **unklar, Freigabe nötig** | Hero `.hero-trust` |
| „100+ Literatur- & Kulturveranstaltungen organisiert" | Briefing Lukas Wagner | selbst organisierte Veranstaltungen | **unklar, Freigabe nötig** | `#warum` |
| „2017 Förderpreis für Kunst und Kultur" | Briefing Lukas Wagner | vergebende Stelle nicht benannt | **unklar, Freigabe nötig**; aus dem Person-Schema entfernt | `#warum` |
| „TEDxSalzburg Speaker-Coach" | Briefing Lukas Wagner | Rolle und Zeitraum nicht spezifiziert | **unklar, Freigabe nötig** | `#warum` |
| 28-Stunden-Poetry-Slam-Weltrekord | Briefing Lukas Wagner | „beteiligt am" war unscharf, kein Beleg auffindbar | **entfernt** | war in `#warum` |
| „Zufriedenheit im Teilnehmer:innen-Feedback" als Label für 92 % | frühere Fassung | war eine erfundene Umschreibung der Metrik | **entfernt und durch den Originalwortlaut ersetzt** | war in `#aheadx` |
| „1.700+ Menschen live erreicht" | frühere Fassung | legte nahe, es sei Lukas' gesamte persönliche Reichweite | **entfernt und präzisiert zu „Teilnahmen bei ahead x"** | war im Hero |
| Testimonials Romy Sigl, Stefan König, Oliver Carl Drewo, Andreas Gruber | LinkedIn-Empfehlungen | Profil ist nicht öffentlich abrufbar, Wortlaut stammt aus einer früheren Session | **unklar, Freigabe nötig** | `#stimmen` |
| „Publikum von 16 bis 80" | Briefing / ahead x | Altersspanne des Publikums | **unklar, Freigabe nötig** | Case `#aheadx` |

Regel für alle offenen Punkte: nicht durch plausibel klingende Formulierungen ersetzen.
Entweder belegen oder streichen.

---

## 5. Verbleibende TODOs

1. Impressum ergänzen (Launch-Blocker 1)
2. Theaterfoto-Credit ergänzen (Launch-Blocker 2)
3. „500+ Auftritte" bestätigen oder streichen (Launch-Blocker 3)
4. Biografische Angaben bestätigen (Launch-Blocker 4)
5. Testimonials freigeben lassen (Launch-Blocker 5)
6. Stichprobengröße und Fragestellung hinter den 92 % intern dokumentieren
7. Nutzungsrecht der Partnerlogos für lukaswagner.at klären, MeinBezirk fehlt als Logo
8. Speaker-Reel produzieren (Priorität 1)
9. Live-Foto vor Publikum beschaffen (Priorität 2)
10. ~~Livegang: `noindex` und `Disallow: /` entfernen~~ erledigt am 05.08.2026
11. ~~Google Fonts selbst hosten~~ erledigt, Latin-Subsets liegen unter `assets/fonts/`
12. Optional: EN-Version unter `/en/`
13. Nach dem Livegang: Google Search Console einrichten und `sitemap.xml` einreichen

---

## 6. Redaktionelle Regeln für diese Seite

- Keine Gedankenstriche im sichtbaren Text. Stattdessen Komma, Doppelpunkt oder Punkt.
- Keine erfundenen Belege, keine simulierten Zeitmarken, keine Fake-UI.
- Kein Foto einsetzen, das eine andere Person als Hauptmotiv zeigt und dabei wie Lukas wirkt.
- Zahlen nur mit Quelle und exakter Metrik.
- `de/index.html` ist ein reiner Spiegel von `index.html` mit absoluten `/assets/`-Pfaden und wird per sed erzeugt, nicht von Hand gepflegt.

# lukaswagner.at auf Hostinger deployen (hPanel)

Statische Seite, kein Build. Ziel: **eigener, isolierter Webspace** für lukaswagner.at
im selben Hostinger-Account wie aheadx.at — sauber getrennt durch einen **eigenen Docroot**.

> Hintergrund: Der Vorfall vom 22.06.2026 entstand, weil lukaswagner.at auf den
> **Docroot/Redirect von aheadx** zeigte. Nicht „derselbe Account" ist das Problem,
> sondern ein gemeinsamer Ordner / eine alte Weiterleitung. Die Schritte unten
> verhindern genau das.

---

## 1. Website mit eigenem Docroot anlegen
1. hPanel → **Websites** → **Website hinzufügen** (bzw. **Domains** → Domain hinzufügen).
2. `lukaswagner.at` als **eigene Website** hinzufügen.
3. Hostinger legt automatisch einen eigenen Ordner an:
   `/domains/lukaswagner.at/public_html/`
4. ⚠️ **Wichtig:** NICHT den aheadx-Ordner auswählen oder wiederverwenden. Eigener Ordner.

## 2. Dateien hochladen
1. hPanel → **Dateien** → **Dateimanager**.
2. In `/domains/lukaswagner.at/public_html/` wechseln und sicherstellen, dass er **leer**
   ist (keine Default- oder aheadx-Dateien, keine alte `index.html`).
3. Diese Inhalte hochladen (am einfachsten als ZIP hochladen + entpacken):
   - `index.html`
   - `404.html`
   - `robots.txt`
   - Ordner `de/`  (enthält `de/index.html`)
   - Ordner `assets/`  (alle Bilder)
4. Endstruktur muss so aussehen:
   ```
   public_html/index.html
   public_html/404.html
   public_html/robots.txt
   public_html/de/index.html
   public_html/assets/…  (lukas-stage.jpg, speaker-reel-thumb.jpg, …)
   ```
   Die `/de`-Seite nutzt absolute Pfade (`/assets/…`), deshalb **müssen** die Bilder
   in `public_html/assets/` liegen (tun sie bei dieser Struktur).
5. Die Datei `CNAME` ist nur für GitHub Pages — auf Hostinger **nicht nötig**
   (kann hochgeladen werden, schadet nicht, oder einfach weglassen).

## 3. Domain-Zuordnung prüfen
1. Unter der Website prüfen, dass `lukaswagner.at` **und** `www.lukaswagner.at`
   auf **diese** Website / diesen Ordner zeigen.
2. Ist die Domain bei Hostinger registriert: passt meist automatisch.
   Ist sie extern: Nameserver bzw. A-Record auf Hostinger zeigen lassen.

## 4. Alte Weiterleitungen entfernen (der eigentliche Bug-Verhinderer)
1. hPanel → **Weiterleitungen / Redirects**: sicherstellen, dass es **keine**
   Weiterleitung `lukaswagner.at → aheadx.at` (oder umgekehrt auf denselben Ordner) gibt.
   Falls vorhanden: **löschen**.
2. Im Dateimanager in `public_html/` nach **`.htaccess`** suchen. Wenn dort alte
   `RewriteRule`/`Redirect 301` aus der aheadx-Zeit stehen → entfernen.
3. Falls Hostinger-Cache/CDN aktiv ist: **Cache leeren**.

## 5. SSL & Test
1. hPanel → **SSL** → für `lukaswagner.at` aktivieren (Let's Encrypt, meist automatisch).
2. Aufrufen und prüfen:
   - `https://lukaswagner.at/`
   - `https://lukaswagner.at/de/`
   - Bilder laden? Tour, Partner, Teilnehmerzahl (2.040+) sichtbar?

## 6. ⚠️ Vor dem echten Livegang (noch offen)
Solange Vorschau, bleibt die Seite **unsichtbar für Google**:
- `index.html` (und `de/index.html`) enthalten `<meta name="robots" content="noindex, nofollow">`
- `robots.txt` enthält `Disallow: /`

**Erst entfernen, wenn Impressum + Inhalte final sind.** (Übernehme ich, sobald die
Impressum-Daten da sind.) Das Hochladen zum Testen ist vorher unbedenklich — die Seite
ist durch noindex/Disallow ohnehin nicht indexierbar.

## 7. Kontaktformular (PHP-Mail-Handler)
Wird ergänzt, sobald Hosting fix ist: eine kleine `kontakt.php` in `public_html/`,
auf die das Formular (`action="/kontakt.php"`) postet und an `kontakt@lukaswagner.at`
mailt. Kein externer Dienst nötig. Die Mailto-Karten funktionieren bis dahin sofort.

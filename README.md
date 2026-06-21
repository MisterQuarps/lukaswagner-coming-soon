# lukaswagner.at — Coming-Soon-Seite

Eigenständige, statische „Website folgt"-Seite für **lukaswagner.at**.
Bewusst **getrennt** vom ahead.at/aheadx-Projekt (eigenes Verzeichnis, kein gemeinsamer Build,
kein gemeinsames Hosting). Eine einzelne `index.html` ohne Abhängigkeiten.

## Wichtig
- Diese Seite gehört **NICHT** auf den Hostinger-Account von aheadx.at.
  Genau diese Vermischung war die Ursache des Vorfalls vom 22.06.2026 (lukaswagner.at
  zeigte die aheadx-Seite, weil beide Domains auf denselben Server/Docroot zeigten).
- lukaswagner.at soll **vollständig woanders** liegen → eigenes, isoliertes Hosting.

## Deploy-Optionen (alle kostenlos, unabhängig von Hostinger)

### Cloudflare Pages (empfohlen)
1. cloudflare.com → Workers & Pages → „Create" → „Pages" → „Upload assets".
2. Diesen Ordner hochladen (oder mit einem Git-Repo verbinden).
3. Custom Domain `lukaswagner.at` zuweisen → Cloudflare nennt die DNS-Einträge.
4. DNS von lukaswagner.at auf Cloudflare zeigen.

### Netlify
1. netlify.com → „Add new site" → „Deploy manually" → Ordner per Drag&Drop.
2. „Domain settings" → `lukaswagner.at` hinzufügen → DNS laut Anleitung setzen.

### GitHub Pages
1. Neues Repo, diese Dateien committen.
2. Settings → Pages → Branch `main` / root.
3. „Custom domain" `lukaswagner.at` → DNS (CNAME/A) laut GitHub setzen.

## Vor dem echten Launch
- `robots.txt` (`Disallow: /`) und das `<meta name="robots" content="noindex,nofollow">`
  in `index.html` **entfernen**, sonst bleibt die Seite aus dem Index.
- Kontakt-Adresse in `index.html` prüfen (aktuell `kontakt@lukaswagner.at`).

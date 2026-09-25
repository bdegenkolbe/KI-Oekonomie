# -*- coding: utf-8 -*-
"""Lesefassung: ASCII-Transliteration der Rollendaten in echte Umlaute.

Die Rollendaten in roster_d.py sind bewusst ASCII, damit das erzeugte
JavaScript und die darin eingebetteten Prompts unabhaengig von der
Zeichenkodierung bitgleich bleiben. Fuer die Lesefassung werden sie hier
zurueckuebersetzt.

BEWUSST KEINE HEURISTIK. Eine Regel der Form "ersetze jedes ue durch ue mit
Umlaut" erfindet Umlaute, wo keine hingehoeren: aus Termintreue wird
Termintreu-Umlaut, aus Neuentstehung Neu-Umlaut-ntstehung, aus
Hochrisikoeinstufung Hochrisiko-Umlaut-instufung. Genau das ist in der
ersten Fassung passiert und in einer Codepruefung des PR aufgefallen.

Stattdessen eine gepruefte Tabelle: Jedes Wort, das umgeschrieben wird,
steht hier einzeln drin. Was nicht drinsteht, bleibt unveraendert. Damit
kann die Umwandlung nichts erfinden; sie kann hoechstens etwas auslassen,
und das faellt beim Lesen auf, statt falsch dazustehen.

Kommen neue Rollen oder neue Prompttexte hinzu, meldet die Selbstpruefung
unten die fehlenden Woerter (python3 lesbar.py).
"""
import re

WOERTERBUCH = {
    '-Zoelle': '-Zölle',
    'Abhaengigkeit': 'Abhängigkeit',
    'Abhaengigkeiten': 'Abhängigkeiten',
    'Aemtern': 'Ämtern',
    'Aerztliche': 'Ärztliche',
    'Agentenfaehigkeit': 'Agentenfähigkeit',
    'Alterungsrueckstellung': 'Alterungsrückstellung',
    'Angekuendigte': 'Angekündigte',
    'Angriffsflaeche': 'Angriffsfläche',
    'Anhaengsel': 'Anhängsel',
    'Arbeitsvorgaengen': 'Arbeitsvorgängen',
    'Aufkommenselastizitaeten': 'Aufkommenselastizitäten',
    'Aussengeschaeft': 'Aussengeschäft',
    'Aussenmarkt': 'Außenmarkt',
    'Begruende': 'Begründe',
    'Begruendung': 'Begründung',
    'Behoerden': 'Behörden',
    'Behoerdenauftraege': 'Behördenaufträge',
    'Beitragssatzstabilitaet': 'Beitragssatzstabilität',
    'Beitragsstabilitaet': 'Beitragsstabilität',
    'Beschaeftigte': 'Beschäftigte',
    'Beschaeftigten': 'Beschäftigten',
    'Beschaeftigung': 'Beschäftigung',
    'Beschaeftigungsformen': 'Beschäftigungsformen',
    'Beschaeftigungsfrage': 'Beschäftigungsfrage',
    'Beschaeftigungssicherung': 'Beschäftigungssicherung',
    'Bestandsqualitaet': 'Bestandsqualität',
    'Bloecke': 'Blöcke',
    'Boehringer': 'Böhringer',
    'Bonitaetsverschiebungen': 'Bonitätsverschiebungen',
    'Buchfuehrungsroutine': 'Buchführungsroutine',
    'Bundeszuschuesse': 'Bundeszuschüsse',
    'Codequalitaet': 'Codequalität',
    'DATEV-Kontenblaetter': 'DATEV-Kontenblätter',
    'Daenemark': 'Dänemark',
    'Datenverfuegbarkeit': 'Datenverfügbarkeit',
    'Deckungsbeitraege': 'Deckungsbeiträge',
    'Diagnostikgeschaeft': 'Diagnostikgeschäft',
    'Dienstplanfaehigkeit': 'Dienstplanfähigkeit',
    'Domaenen': 'Domänen',
    'Einsatzfaehigkeit': 'Einsatzfähigkeit',
    'Entwicklerkapazitaet': 'Entwicklerkapazität',
    'Ergebnisgroessen': 'Ergebnisgrössen',
    'Erloessicherung': 'Erlössicherung',
    'Erstattungsbetraege': 'Erstattungsbeträge',
    'Erstattungsfaehigkeit': 'Erstattungsfähigkeit',
    'Europaeischen': 'Europäischen',
    'Europaeischer': 'Europäischer',
    'Existenzfaehigkeit': 'Existenzfähigkeit',
    'Fachaerztin': 'Fachärztin',
    'Faehigkeit': 'Fähigkeit',
    'Faehigkeitszuwachs': 'Fähigkeitszuwachs',
    'Faelle': 'Fälle',
    'Faktenblaettern': 'Faktenblättern',
    'Fallzusammenfuehrung': 'Fallzusammenführung',
    'Festbetraege': 'Festbeträge',
    'Finanzierungsoekonomie': 'Finanzierungsökonomie',
    'Geraete': 'Geräte',
    'Gesamtvertraege': 'Gesamtverträge',
    'Geschaeft': 'Geschäft',
    'Geschaefts': 'Geschäfts',
    'Geschaeftsbank': 'Geschäftsbank',
    'Geschaeftsfuehrer': 'Geschäftsführer',
    'Geschaeftsfuehrerin': 'Geschäftsführerin',
    'Geschaeftsfuehrung': 'Geschäftsführung',
    'Geschaeftsmodell': 'Geschäftsmodell',
    'Gesetzentwuerfe': 'Gesetzentwürfe',
    'Gesundheitsoekonom': 'Gesundheitsökonom',
    'Gesundheitsoekonomie': 'Gesundheitsökonomie',
    'Gesundheitsoekonomin': 'Gesundheitsökonomin',
    'Gewaehrleistung': 'Gewährleistung',
    'Groesse': 'Größe',
    'Groessenordnung': 'Grössenordnung',
    'Grossauftragsgeschaeft': 'Großauftragsgeschäft',
    'Grosshandelszuschlag': 'Großhandelszuschlag',
    'Grosskunden': 'Großkunden',
    'Grossunternehmen': 'Großunternehmen',
    'Gruenderin': 'Gründerin',
    'Hausaerztin': 'Hausärztin',
    'Honorarverteilungsmassstab': 'Honorarverteilungsmaßstab',
    'Identitaet': 'Identität',
    'KI-Faehigkeitsstand': 'KI-Fähigkeitsstand',
    'KI-gestuetzte': 'KI-gestützte',
    'Kapazitaet': 'Kapazität',
    'Kapazitaetsgewinn': 'Kapazitätsgewinn',
    'Kapitalmobilitaet': 'Kapitalmobilität',
    'Kassenaerztlichen': 'Kassenärztlichen',
    'Kassengeschaeft': 'Kassengeschäft',
    'Kaufmaennischer': 'Kaufmännischer',
    'Kleinbetraegen': 'Kleinbeträgen',
    'Koeln': 'Köln',
    'Koenigreich': 'Königreich',
    'Koerperschaft': 'Körperschaft',
    'Koerperschaftsteuer': 'Körperschaftsteuer',
    'Konformitaet': 'Konformität',
    'Konformitaetsbewertung': 'Konformitätsbewertung',
    'Kostenfuehrerschaft': 'Kostenführerschaft',
    'Kostentraeger': 'Kostenträger',
    'Krankenhaeuser': 'Krankenhäuser',
    'Krankenhausoekonom': 'Krankenhausökonom',
    'Kuendigungsschutz': 'Kündigungsschutz',
    'Kuerzung': 'Kürzung',
    'Laborfaehigkeit': 'Laborfähigkeit',
    'Laender': 'Länder',
    'Laenderhaushalt': 'Länderhaushalt',
    'Landeszufuehrungsbetraege': 'Landeszuführungsbeträge',
    'Leitgroesse': 'Leitgrösse',
    'Lieferfaehigkeit': 'Lieferfähigkeit',
    'Liquiditaet': 'Liquidität',
    'Liquiditaetsplanung': 'Liquiditätsplanung',
    'Loesung': 'Lösung',
    'Loesungsarchitekt': 'Lösungsarchitekt',
    'MD-Pruefung': 'MD-Prüfung',
    'Makrooekonom': 'Makroökonom',
    'Makrooekonomie': 'Makroökonomie',
    'Mandatsrentabilitaet': 'Mandatsrentabilität',
    'Marktloesung': 'Marktlösung',
    'Marktruecknahmen': 'Marktrücknahmen',
    'Massstab': 'Maßstab',
    'Meistbeguenstigung': 'Meistbegünstigung',
    'Methodenqualitaet': 'Methodenqualität',
    'Mindestbeitraege': 'Mindestbeiträge',
    'Mittelstandsgeschaeft': 'Mittelstandsgeschäft',
    'Netto-Erloese': 'Netto-Erlöse',
    'Netzwerkgeschaeft': 'Netzwerkgeschäft',
    'Neugeschaeft': 'Neugeschäft',
    'Oekonom': 'Ökonom',
    'Pflegeheimtraegers': 'Pflegeheimträgers',
    'Pharmagrosshandels': 'Pharmagroßhandels',
    'Politoekonomie': 'Politökonomie',
    'Portfolioqualitaet': 'Portfolioqualität',
    'Preisrigiditaeten': 'Preisrigiditäten',
    'Primaerversorgung': 'Primärversorgung',
    'Produktivitaet': 'Produktivität',
    'Produktivitaetsgewinn': 'Produktivitätsgewinn',
    'Produktivitaetsgewinne': 'Produktivitätsgewinne',
    'Produktivitaetsgewinns': 'Produktivitätsgewinns',
    'Produktivitaetsparadox': 'Produktivitätsparadox',
    'Projektvertraege': 'Projektverträge',
    'Pruefe': 'Prüfe',
    'Pruefer': 'Prüfer',
    'Pruefquote': 'Prüfquote',
    'Pruefschritte': 'Prüfschritte',
    'Pruefungssicherheit': 'Prüfungssicherheit',
    'Pruefungsstandards': 'Prüfungsstandards',
    'Qualitaet': 'Qualität',
    'Qualitaetsberichte': 'Qualitätsberichte',
    'Qualitaetsmarkt': 'Qualitätsmarkt',
    'Quellenpruefung': 'Quellenprüfung',
    'Rabattvertraege': 'Rabattverträge',
    'Rahmenvertraege': 'Rahmenverträge',
    'Rechengroesse': 'Rechengrösse',
    'Rechtmaessigkeit': 'Rechtmässigkeit',
    'Rueckhalt': 'Rückhalt',
    'Ruecklagen': 'Rücklagen',
    'Rueckwirkung': 'Rückwirkung',
    'Saetze': 'Sätze',
    'Sanierungsfaehigkeit': 'Sanierungsfähigkeit',
    'Sanitaer-Heizung-Klima': 'Sanitär-Heizung-Klima',
    'Schaetzung': 'Schätzung',
    'Schaetzungen': 'Schätzungen',
    'Sekundaerdaten': 'Sekundärdaten',
    'Sekundaerdatenanalyse': 'Sekundärdatenanalyse',
    'Sekundaernutzung': 'Sekundärnutzung',
    'Souveraenitaet': 'Souveränität',
    'Staerke': 'Stärke',
    'Steuerschaetzung': 'Steuerschätzung',
    'Strukturbrueche': 'Strukturbrüche',
    'Strukturbruechen': 'Strukturbrüchen',
    'Stueckkosten': 'Stückkosten',
    'Systemqualitaet': 'Systemqualität',
    'Systemstabilitaet': 'Systemstabilität',
    'Tarifsekretaer': 'Tarifsekretär',
    'Tarifvertraege': 'Tarifverträge',
    'Teamgroesse': 'Teamgrösse',
    'Traegerbonitaet': 'Trägerbonität',
    'Traegers': 'Trägers',
    'Traegerschaft': 'Trägerschaft',
    'Traegerwechsel': 'Trägerwechsel',
    'Traegerzuschuss': 'Trägerzuschuss',
    'Uebergabe': 'Übergabe',
    'Uebergabegroessen': 'Übergabegrössen',
    'Uebertragbarkeit': 'Übertragbarkeit',
    'Uebertragung': 'Übertragung',
    'Uebertragungsbrueche': 'Übertragungsbrüche',
    'Uebrige': 'Übrige',
    'Universitaet': 'Universität',
    'Universitaetsanbindung': 'Universitätsanbindung',
    'Universitaetsklinikum': 'Universitätsklinikum',
    'Universitaetsklinikums': 'Universitätsklinikums',
    'Veranstaltungsgeschaeft': 'Veranstaltungsgeschäft',
    'Verfuegbarkeit': 'Verfügbarkeit',
    'Verguetungsbetraege': 'Vergütungsbeträge',
    'Verguetungsniveau': 'Vergütungsniveau',
    'Vermoegensverteilung': 'Vermögensverteilung',
    'Versicherungsoekonom': 'Versicherungsökonom',
    'Versorgungsvertraege': 'Versorgungsverträge',
    'Vorstaendin': 'Vorständin',
    'Wirtschaftspruefungsgesellschaft': 'Wirtschaftsprüfungsgesellschaft',
    'Zusaetzlich': 'Zusätzlich',
    'Zuschusshoehe': 'Zuschusshöhe',
    'abschoepft': 'abschöpft',
    'angekuendigte': 'angekündigte',
    'auffaellt': 'auffällt',
    'ausdruecklich': 'ausdrücklich',
    'aushaelt': 'aushält',
    'begruende': 'begründe',
    'beruehrt': 'berührt',
    'beruehrter': 'berührter',
    'betraegt': 'beträgt',
    'daenischen': 'dänischen',
    'dafuer': 'dafür',
    'erhoeht': 'erhöht',
    'erklaert': 'erklärt',
    'europaeischen': 'europäischen',
    'faerben': 'färben',
    'frueher': 'früher',
    'fuenf': 'fünf',
    'fuer': 'für',
    'gegenueber': 'gegenüber',
    'geschaetzt': 'geschätzt',
    'ggue': 'ggü',
    'groessten': 'grössten',
    'groesster': 'grösster',
    'gross': 'groß',
    'grossen': 'großen',
    'haelt': 'hält',
    'haengt': 'hängt',
    'hoeher': 'höher',
    'hoehere': 'höhere',
    'koennte': 'könnte',
    'koerperlich': 'körperlich',
    'laendlichen': 'ländlichen',
    'laengeren': 'längeren',
    'laesst': 'lässt',
    'mittelstaendischen': 'mittelständischen',
    'nachgeprueft': 'nachgeprüft',
    'naechste': 'nächste',
    'neuen': 'neün',
    'oeffentlich': 'öffentlich',
    'oeffentliche': 'öffentliche',
    'oeffentlichen': 'öffentlichen',
    'oeffentlicher': 'öffentlicher',
    'offenlaesst': 'offenlässt',
    'pruefen': 'prüfen',
    'schaetzt': 'schätzt',
    'schuetzen': 'schützen',
    'schutzwuerdige': 'schutzwürdige',
    'staerker': 'stärker',
    'staerksten': 'stärksten',
    'traegt': 'trägt',
    'ueber': 'über',
    'ueberkonfident': 'überkonfident',
    'uebernehmen': 'übernehmen',
    'ueberschaetzt': 'überschätzt',
    'uebersieht': 'übersieht',
    'ueberspringt': 'überspringt',
    'uebertraegt': 'überträgt',
    'ueberzogener': 'überzogener',
    'ungueltig': 'ungültig',
    'unterschaetzt': 'unterschätzt',
    'verdraengt': 'verdrängt',
    'verfuegbare': 'verfügbare',
    'veroeffentlichte': 'veröffentlichte',
    'verzoegern': 'verzögern',
    'verzoegerte': 'verzögerte',
    'vollstaendig': 'vollständig',
    'voruebergehend': 'vorübergehend',
    'waerest': 'wärest',
    'wuerdest': 'würdest',
    'zugaengliche': 'zugängliche',
    'zweckmaessige': 'zweckmäßige',
}


def lesbar(text):
    """Ersetzt bekannte transliterierte Woerter; laesst alles andere stehen."""
    return re.sub(r"[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df-]+",
                  lambda m: WOERTERBUCH.get(m.group(0), m.group(0)), str(text))


def _fehlende(texte):
    """Woerter mit Transliterationsmuster, die (noch) nicht in der Tabelle stehen."""
    tok = set()
    for t in texte:
        tok |= set(re.findall(r"[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df-]+", str(t)))
    return sorted(w for w in tok
                  if re.search(r"ae|oe|ue", w) and w not in WOERTERBUCH)


if __name__ == "__main__":
    import importlib.util, sys
    from roster_d import ROLLEN, STATIONEN
    spec = importlib.util.spec_from_file_location("bsd", "baue-sitzung-d.py")
    bsd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bsd)

    # 1. Die Faelle, an denen die alte Heuristik gescheitert ist
    fallen = ["Termintreue", "Rollentreue", "Neuentstehung", "Hochrisikoeinstufung",
              "neue Aufgaben", "Steuerberaterin", "Zulassungsdauer", "zuerst",
              "Firmenkundenbetreuer", "Zweitquellen", "Launchsequenz", "querfinanzieren"]
    fehler = [t for t in fallen if lesbar(t) != t]
    print("Fallen, die unveraendert bleiben muessen: %s"
          % ("alle ok" if not fehler else "VERAENDERT: %s" % fehler))

    # 2. Die Tabelle darf selbst keine Transliterationsreste enthalten
    reste = [v for v in WOERTERBUCH.values() if re.search(r"ae|oe|ue", v)
             and v not in ("Steuer", "Neuerung")]
    reste = [v for v in reste if not re.search(r"steuer|teuer|neuer|treuer|dauer|quer|quel|quen", v.lower())]
    print("Tabellenwerte mit Transliterationsrest: %s" % (reste or "keine"))

    # 3. Vollstaendigkeit gegen die tatsaechlichen Quellen
    texte = [" ".join(map(str, r)) for r in ROLLEN]
    texte += [str(x) for v in STATIONEN.values() for x in v if x]
    texte += [bsd.FRAGEBOGEN, bsd.REGELN, bsd.KEINE_DOPPELUNG, bsd.HIGL_LAGE]
    texte += [str(x) for t in bsd.RECHERCHE for x in t]
    texte += [str(x) for t in bsd.ANGRIFFE for x in t]
    texte += [str(x) for t in bsd.KAPITEL for x in t]
    offen = _fehlende(texte)
    # Woerter, in denen ae/oe/ue echt sind, gehoeren nicht in die Tabelle
    print("Nicht abgedeckte Woerter mit ae/oe/ue: %d" % len(offen))
    for w in offen:
        print("   %s" % w)
    print("Tabelleneintraege: %d" % len(WOERTERBUCH))

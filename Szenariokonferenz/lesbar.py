# -*- coding: utf-8 -*-
"""Lesefassung: ASCII-Transliteration der Rollendaten in echte Umlaute.

Die Rollendaten in roster_d.py sind bewusst ASCII, damit das erzeugte
JavaScript und die darin eingebetteten Prompts unabhaengig von der
Zeichenkodierung bitgleich bleiben. Fuer die Lesefassung werden sie hier
zurueckuebersetzt.

BEWUSST KEINE HEURISTIK. Eine Regel der Form "ersetze jedes ue durch ue mit
Umlaut" erfindet Umlaute, wo keine hingehoeren: aus Termintreue wird
Termintreu-Umlaut, aus neuen ne-Umlaut-n, aus Hochrisikoeinstufung
Hochrisiko-Umlaut-instufung. Das ist in zwei aufeinanderfolgenden Fassungen
passiert — erst mit einer Schutzliste, dann mit einer Tabelle, die aus
derselben Heuristik erzeugt und nur stichprobenartig geprueft war. Beide
Male hat es eine Codepruefung gefunden, nicht die eigene Kontrolle.

Deshalb jetzt zweistufig:

1. Eine Tabelle. Jedes Wort, das umgeschrieben wird, steht einzeln drin.
   Was nicht drinsteht, bleibt unveraendert. Die Umwandlung kann damit
   nichts erfinden; sie kann hoechstens etwas auslassen, und das faellt
   beim Lesen auf, statt falsch dazustehen.

2. Eine Freigabeliste fuer die gefaehrliche Teilmenge. Genau dort, wo die
   umgewandelte Silbe an eine Vokalgrenze stoesst, sitzen die Artefakte.
   Jeder solche Eintrag muss in GEPRUEFT_AN_VOKALGRENZE stehen. Kommt ein
   neuer hinzu, schlaegt die Selbstpruefung fehl, bis ihn jemand angesehen
   und eingetragen hat. Ein vergessener Eintrag ist dann ein lautes
   Versagen und kein stilles.

Selbstpruefung: python3 lesbar.py
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
    'Aussengeschaeft': 'Außengeschäft',
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
    'Ergebnisgroessen': 'Ergebnisgrößen',
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
    'Groessenordnung': 'Größenordnung',
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
    'Leitgroesse': 'Leitgröße',
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
    'Rechengroesse': 'Rechengröße',
    'Rechtmaessigkeit': 'Rechtmäßigkeit',
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
    'Teamgroesse': 'Teamgröße',
    'Traegerbonitaet': 'Trägerbonität',
    'Traegers': 'Trägers',
    'Traegerschaft': 'Trägerschaft',
    'Traegerwechsel': 'Trägerwechsel',
    'Traegerzuschuss': 'Trägerzuschuss',
    'Uebergabe': 'Übergabe',
    'Uebergabegroessen': 'Übergabegrößen',
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
    'groessten': 'größten',
    'groesster': 'größter',
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

# Eintraege, deren umgewandelte Silbe an eine Vokalgrenze stoesst. Jeder hier
# wurde einzeln angesehen. Neue Eintraege dieser Art muessen hier nachgetragen
# werden, sonst schlaegt die Selbstpruefung fehl.
GEPRUEFT_AN_VOKALGRENZE = {
    'Aemtern',
    'Aerztliche',
    'Europaeischen',
    'Europaeischer',
    'Koerperschaftsteuer',
    'Krankenhaeuser',
    'Makrooekonom',
    'Makrooekonomie',
    'Oekonom',
    'Steuerschaetzung',
    'Uebergabe',
    'Uebergabegroessen',
    'Uebertragbarkeit',
    'Uebertragung',
    'Uebertragungsbrueche',
    'Uebrige',
    'europaeischen',
    'ggue',
    'oeffentlich',
    'oeffentliche',
    'oeffentlichen',
    'oeffentlicher',
    'ueber',
    'ueberkonfident',
    'uebernehmen',
    'ueberschaetzt',
    'uebersieht',
    'ueberspringt',
    'uebertraegt',
    'ueberzogener',
}

_WORT = re.compile(r"[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df-]+")


def lesbar(text):
    """Ersetzt bekannte transliterierte Woerter; laesst alles andere stehen."""
    return _WORT.sub(lambda m: WOERTERBUCH.get(m.group(0), m.group(0)), str(text))


def _an_vokalgrenze(wort):
    """Steht eine Transliterationssilbe neben einem Vokal? Dort sitzen die Artefakte."""
    for m in re.finditer(r"[aouAOU]e", wort):
        i = m.start()
        davor = wort[i - 1] if i > 0 else ""
        danach = wort[i + 2] if i + 2 < len(wort) else ""
        if davor.lower() in "aeiou" or danach.lower() in "aeiou":
            return True
    return False


def _falte(wort):
    """Echte Umlaute zurueck nach ASCII — fuer die Rundlaufprobe."""
    for a, b in (("\u00e4", "ae"), ("\u00f6", "oe"), ("\u00fc", "ue"),
                 ("\u00c4", "Ae"), ("\u00d6", "Oe"), ("\u00dc", "Ue"), ("\u00df", "ss")):
        wort = wort.replace(a, b)
    return wort


def pruefe():
    """Gibt die Liste der Beanstandungen zurueck; leer heisst in Ordnung."""
    fehler = []

    # 1. Die Wortformen, an denen die Heuristik gescheitert ist, duerfen nicht
    #    in der Tabelle stehen — auch nicht gebeugt.
    for w in ("neue", "neuen", "neuer", "neues", "Neue", "Neuen",
              "Treue", "Termintreue", "Rollentreue", "Neuentstehung",
              "Hochrisikoeinstufung", "Steuerberaterin", "Zulassungsdauer",
              "zuerst", "Firmenkundenbetreuer", "Zweitquellen", "Launchsequenz",
              "querfinanzieren", "Verfahrensdauer", "Neuerung"):
        if lesbar(w) != w:
            fehler.append("Falle veraendert: %s -> %s" % (w, lesbar(w)))

    # 2. Jeder Eintrag an einer Vokalgrenze braucht eine Freigabe.
    for k in WOERTERBUCH:
        if _an_vokalgrenze(k) and k not in GEPRUEFT_AN_VOKALGRENZE:
            fehler.append("an Vokalgrenze, aber nicht freigegeben: %s -> %s"
                          % (k, WOERTERBUCH[k]))

    # 3. Rundlaufprobe: der Wert muss, zurueckgefaltet, wieder den Schluessel ergeben.
    for k, v in WOERTERBUCH.items():
        if _falte(v) != k:
            fehler.append("Rundlauf gebrochen: %s -> %s -> %s" % (k, v, _falte(v)))

    # 4. Kein Wert darf noch eine Transliteration enthalten, die ein Umlaut sein muesste.
    for k, v in WOERTERBUCH.items():
        if "ss" in v and re.search(r"(gr|Gr)oess|maessig|aussen|Aussen", k):
            fehler.append("scharfes s fehlt: %s -> %s" % (k, v))
    return fehler


if __name__ == "__main__":
    import importlib.util, sys, os
    HIER = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HIER)

    fehler = pruefe()
    print("Tabelleneintraege: %d, davon an einer Vokalgrenze freigegeben: %d"
          % (len(WOERTERBUCH), len(GEPRUEFT_AN_VOKALGRENZE)))
    if fehler:
        print("\nBEANSTANDUNGEN (%d):" % len(fehler))
        for f in fehler:
            print("  " + f)
    else:
        print("Selbstpruefung ohne Beanstandung.")

    # 5. Vollstaendigkeit gegen die tatsaechlichen Quellen
    from roster_d import ROLLEN, STATIONEN
    spec = importlib.util.spec_from_file_location("bsd", os.path.join(HIER, "baue-sitzung-d.py"))
    bsd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bsd)
    texte = [" ".join(map(str, r)) for r in ROLLEN]
    texte += [str(x) for v in STATIONEN.values() for x in v if x]
    texte += [bsd.FRAGEBOGEN, bsd.REGELN, bsd.KEINE_DOPPELUNG, bsd.HIGL_LAGE]
    texte += [str(x) for t in bsd.RECHERCHE for x in t]
    texte += [str(x) for t in bsd.ANGRIFFE for x in t]
    texte += [str(x) for t in bsd.KAPITEL for x in t]
    tok = set()
    for t in texte:
        tok |= set(_WORT.findall(str(t)))
    offen = sorted(w for w in tok if re.search(r"ae|oe|ue", w) and w not in WOERTERBUCH)
    print("\nNicht in der Tabelle, mit ae/oe/ue (dort ist die Folge echt): %d" % len(offen))
    for w in offen:
        print("  %s" % w)
    sys.exit(1 if fehler else 0)

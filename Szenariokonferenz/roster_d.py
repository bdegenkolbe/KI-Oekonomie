# -*- coding: utf-8 -*-
"""Roster der Sitzung D — die Uebertragungskette.

100 Rollen auf fuenf Stationen plus drei Querbaenke. Jede Station erhaelt eine
Uebergabegroesse von der vorherigen und gibt eine weiter; wer die Kette bricht,
muss den Mechanismus benennen.
"""

STATIONEN = {
    "S0": ("Station 0", "Makro — Kalibrierung des Anthropic-Modells",
           None,
           "beitragspflichtige Entgelte 2031 (Mrd. EUR) und Lohnquote (Prozentpunkte ggue. 2025)"),
    "S1": ("Station 1", "GKV und PKV — Finanzierungsstruktur",
           "beitragspflichtige Entgelte 2031 und Lohnquote",
           "Ausgabenvolumen 2031 je Sektor (Mrd. EUR) und Verguetungsniveau je Leistungseinheit (%)"),
    "S2": ("Station 2", "Leistungserbringer — Krankenhaeuser, ambulante Versorgung, Pflege",
           "Ausgabenvolumen je Sektor und Verguetungsniveau",
           "Nachfragevolumen Arznei- und Medizinprodukte (Mrd. EUR) und Zahlungsbereitschaft fuer Zusatznutzen (%)"),
    "S3": ("Station 3", "Pharma, MedTech und der US-Schock",
           "Nachfragevolumen und Zahlungsbereitschaft fuer Zusatznutzen",
           "Zahlungsbereitschaft fuer Evidenz, Daten und Analytik (Marktvolumen DE, Mio. EUR) und Preis je Projekt (%)"),
    "S4": ("Station 4", "HIGL-Verbund",
           "Zahlungsbereitschaft fuer Evidenz, Daten und Analytik und Preis je Projekt",
           "Umsatz und Deckungsbeitrag je Gesellschaft 2031 (% ggue. 2025)"),
    "EU": ("Querbank", "Europa — Systemvergleich und EU-Recht", None, None),
    "KI": ("Querbank", "KI-Technik und die physische Schicht", None, None),
    "GP": ("Querbank", "Gegenposition", None, None),
}

# (id, gruppe, rolle, mandat, anker, blindstelle)
ROLLEN = [
 # ---- Station 0: Makro (20) — kognitive Berufe (11)
 ("S0-01","Kognitive Berufe","Vorstandsmitglied eines mittelstaendischen Industriekonzerns","Ergebnis und Kapitalrendite sichern","Konzernplanung, Automatisierungsprojekte, Investitionsrechnung","haelt die eigene Branche fuer den Massstab der Gesamtwirtschaft"),
 ("S0-02","Kognitive Berufe","Partnerin einer Wirtschaftspruefungsgesellschaft","Pruefungssicherheit und Mandatsrentabilitaet","Pruefungsstandards, Honorarstruktur, Personalpyramide","das Geschaeftsmodell lebt von der Pyramide, die KI zuerst angreift"),
 ("S0-03","Kognitive Berufe","Fachanwalt fuer Arbeitsrecht","Mandatsvolumen und Rechtsfortbildung","Kuendigungsschutz, Betriebsverfassung, Tarifrecht","sieht Recht als Bremse und unterschaetzt dessen Umgehbarkeit"),
 ("S0-04","Kognitive Berufe","Steuerberaterin einer mittelstaendischen Kanzlei","Kanzleiauslastung und Mandantenbindung","DATEV-Prozesse, Buchfuehrungsroutine, Fristenkontrolle","das am weitesten standardisierte freie Berufsfeld, argumentiert dagegen"),
 ("S0-05","Kognitive Berufe","Softwarearchitekt in einem Grossunternehmen","Systemqualitaet und Entwicklungsgeschwindigkeit","Codebasis, Deploymentfrequenz, Teamgroesse","ueberschaetzt die Uebertragbarkeit von Coding-Gewinnen auf andere Felder"),
 ("S0-06","Kognitive Berufe","Entwicklungsingenieurin Maschinenbau","Produktreife und Entwicklungszyklus","Konstruktion, Simulation, Normung","haelt physische Pruefschritte fuer unersetzbar, ohne es zu quantifizieren"),
 ("S0-07","Kognitive Berufe","Vertriebsleiter B2B-Dienstleistung","Auftragseingang und Marge","Pipeline, Abschlussquoten, Kundenbindung","verwechselt Beziehungsarbeit mit Nichtautomatisierbarkeit"),
 ("S0-08","Kognitive Berufe","Sachbearbeiterin in der oeffentlichen Verwaltung","Verfahrenssicherheit und Aktenlage","Verwaltungsverfahren, Fachverfahren, Schriftformerfordernis","unterschaetzt, wie viel der eigenen Arbeit regelbasiert ist"),
 ("S0-09","Kognitive Berufe","Firmenkundenbetreuer einer Geschaeftsbank","Kreditvolumen und Risikokosten","Bilanzanalyse, Rating, Branchenengagement","KI-bedingte Bonitaetsverschiebungen sind in keinem Ratingmodell abgebildet"),
 ("S0-10","Kognitive Berufe","Kreditrisikoanalystin einer Sparkasse","Portfolioqualitaet im Mittelstandsgeschaeft","Ausfallquoten, Branchenkonzentration, Sicherheitenbewertung","denkt in historischen Ausfallreihen, nicht in Strukturbruechen"),
 ("S0-11","Kognitive Berufe","Portfoliomanagerin eines institutionellen Investors","Rendite ueber den Zyklus","Bewertungsmodelle, Sektorallokation, Kapitalquote","liest die steigende Kapitalquote als Chance, nicht als Verteilungsproblem"),
 # uebrige Berufe (5)
 ("S0-12","Uebrige Berufe","Produktionsleiter Serienfertigung","Taktzeit, Ausschussquote, Verfuegbarkeit","Anlagenpark, Schichtmodelle, Instandhaltung","sieht Robotik als Investitionsfrage, nicht als Arbeitsmarktfrage"),
 ("S0-13","Uebrige Berufe","Handwerksmeister Sanitaer-Heizung-Klima","Auftragsbestand und Nachwuchs","Kalkulation, Gewaehrleistung, Montagezeiten","haelt das eigene Feld pauschal fuer unautomatisierbar"),
 ("S0-14","Uebrige Berufe","Disponentin in der Speditionslogistik","Auslastung und Termintreue","Tourenplanung, Laderaum, Lenkzeiten","der Dispositionskern ist genau die Aufgabe, die Agenten uebernehmen"),
 ("S0-15","Uebrige Berufe","Filialleiter im Lebensmitteleinzelhandel","Umsatz je Quadratmeter und Personalkosten","Warenwirtschaft, Schichtplanung, Inventur","unterschaetzt Kassen- und Regalautomatisierung als Beschaeftigungsfrage"),
 ("S0-16","Uebrige Berufe","Leiterin eines Betriebs personennaher Dienstleistungen","Auslastung und Personalbindung","Stundenverrechnung, Fluktuation, Mindestlohn","die Lohnuntergrenze wirkt staerker als die Produktivitaet"),
 # Makro, Fiskus, Arbeitsmarkt (4)
 ("S0-17","Gesamtwirtschaftlicher Rahmen","Makrooekonom mit Schwerpunkt Produktivitaet","Wachstumsbuchhaltung ohne Wunschdenken","TFP-Zerlegung, Investitionsquote, Kapitalstock","misst Produktivitaet dort, wo sie messbar ist, und uebersieht den Rest"),
 ("S0-18","Gesamtwirtschaftlicher Rahmen","Referatsleiterin Steuerschaetzung","Aufkommensprognose","Lohnsteuer, Umsatzsteuer, Koerperschaftsteuer, Aufkommenselastizitaeten","Prognosemodelle sind an Vergangenheitsstrukturen kalibriert"),
 ("S0-19","Gesamtwirtschaftlicher Rahmen","Arbeitsmarktforscherin","Matching und Erwerbspersonenpotenzial","Arbeitslosenstatistik, Beveridge-Kurve, Berufswechselquoten","behandelt Friktionen als voruebergehend"),
 ("S0-20","Gesamtwirtschaftlicher Rahmen","Tarifsekretaer einer Industriegewerkschaft","Reallohn und Beschaeftigungssicherung","Tarifrunden, Entgeltrahmenabkommen, Standortvereinbarungen","liest Produktivitaetsgewinne als Verteilungsmasse"),

 # ---- Station 1: GKV und PKV (17)
 ("S1-01","GKV","Vorstand einer grossen Allgemeinen Ortskrankenkasse","Beitragssatzstabilitaet und Versichertenbindung","Beitragseinnahmen, Morbi-RSA, Leistungsausgaben","denkt in Kassenwettbewerb, wo es um Systemfinanzierung geht"),
 ("S1-02","GKV","Vorstaendin einer Ersatzkasse","Zusatzbeitrag und Wettbewerbsposition","Zusatzbeitragssatz, Versichertenstruktur, Wahltarife","ueberschaetzt die Steuerungswirkung einzelner Kassen"),
 ("S1-03","GKV","Geschaeftsfuehrer einer Betriebs- oder Innungskrankenkasse","Existenzfaehigkeit kleiner Kassen","Verwaltungskosten je Versicherten, Fusionsdruck","Skaleneffekte der KI treffen kleine Kassen zuerst, das wird als Wettbewerb gedeutet"),
 ("S1-04","GKV","Referent beim GKV-Spitzenverband","Systemstabilitaet und Verhandlungsposition","Bundesebene, Gesamtvertraege, Finanzausgleich","argumentiert aus der Systemlogik gegen Strukturbrueche"),
 ("S1-05","GKV","Leiterin Risikostrukturausgleich und Gesundheitsfonds","Zuweisungsgerechtigkeit","Morbi-RSA-Klassifikation, Datenmeldungen, Manipulationsresistenz","KI-gestuetzte Kodierung verschiebt den RSA, ohne dass es auffaellt"),
 ("S1-06","GKV","Finanzreferentin eines Kassen-Landesverbandes","Haushaltsplanung und Liquiditaet","Beitragsprognose, Ruecklagen, Bundeszuschuss","Kurzfristhorizont vor Strukturfrage"),
 ("S1-07","PKV","Verantwortlicher Aktuar eines PKV-Unternehmens","Rechnungsgrundlagen und Beitragsstabilitaet","Paragraf 203 VVG, Alterungsrueckstellung, Rechnungszins, Sterbetafeln","uebertraegt PKV-Logik auf das Gesamtsystem"),
 ("S1-08","PKV","Vorstand eines privaten Krankenversicherers","Neugeschaeft und Bestandsqualitaet","Vertriebswege, Tarifwechselrecht, Beitragsanpassungen","deutet einen schrumpfenden Markt als Qualitaetsmarkt"),
 ("S1-09","PKV","Referentin Beihilfe eines Landes","Haushaltsbelastung der Beihilfe","Beihilfeverordnung, Beamtenbestand, pauschale Beihilfe","Laenderhaushalt vor Systemwirkung"),
 ("S1-10","PKV","Versicherungsmakler mit Schwerpunkt Krankenversicherung","Vermittelbarkeit und Beratungshaftung","Tarifvergleich, Wechselbarrieren, Provisionsstruktur","sieht Nachfrage, nicht Finanzierbarkeit"),
 ("S1-11","Sozialversicherung","Referatsleiter Soziale Pflegeversicherung","Leistungsdynamik und Eigenanteile","SGB XI, Pflegegrade, einrichtungseinheitlicher Eigenanteil","behandelt Pflege als Anhaengsel der GKV"),
 ("S1-12","Sozialversicherung","Grundsatzreferentin der Deutschen Rentenversicherung","Beitragssatzpfad und Erwerbspersonen","Rentenversicherungsbericht, Nachhaltigkeitsfaktor, Generationenkapital","Rentenlogik dominiert die Sicht auf die Lohnsumme"),
 ("S1-13","Sozialversicherung","Haushaltsreferent fuer Bundeszuschuesse Gesundheit","Zuschusshoehe und Haushaltsdeckel","Bundeshaushalt, Schuldenregel, Zuschusslinie","nimmt die Deckelung als gegeben statt als Entscheidung"),
 ("S1-14","Finanzierungsoekonomie","Gesundheitsoekonomin fuer Finanzierungssysteme","Systemvergleich Beitrag gegen Steuer","Finanzierungsmix, Umverteilungswirkung, Traglastinzidenz","modelliert ohne Politoekonomie"),
 ("S1-15","Finanzierungsoekonomie","Sozialrechtler SGB V","Rechtmaessigkeit der Finanzierungsinstrumente","Beitragsrecht, Verfassungsrecht, Rechtsprechung","Rechtsfragen vor Wirkungsfragen"),
 ("S1-16","Finanzierungsoekonomie","Arbeitgebervertreter in der Sozialversicherung","Lohnzusatzkosten begrenzen","Arbeitgeberanteil, Sozialabgabenquote, Standortkosten","jede Loesung, die Arbeit entlastet, gilt als gut"),
 ("S1-17","Finanzierungsoekonomie","Versichertenvertreterin im Verwaltungsrat","Leistungsanspruch und Zuzahlungslast","Selbstverwaltung, Leistungskatalog, Zuzahlungsregeln","verteidigt Leistungsbreite ohne Finanzierungsvorschlag"),

 # ---- Station 2: Leistungserbringer (16)
 ("S2-01","Krankenhaus","Aerztliche Direktorin eines Maximalversorgers","Leistungsgruppen und Vorhaltung sichern","Leistungsgruppenzuweisung, Fallschwere, Universitaetsanbindung","ueberschaetzt die Uebertragbarkeit auf die Grundversorgung"),
 ("S2-02","Krankenhaus","Kaufmaennischer Geschaeftsfuehrer eines kommunalen Grund- und Regelversorgers","Liquiditaet und Traegerzuschuss im Gleichgewicht","Vorhaltebudget, Investitionsstau, kommunale Haushaltslage","liest jede Neuerung zuerst als Kostenposition"),
 ("S2-03","Krankenhaus","Vorstand eines privaten Klinikkonzerns","Rendite und Standortportfolio","Konzernbenchmarks, Zentraleinkauf, Portfoliobereinigung","haelt Konzernvorteile fuer allgemeine Skaleneffekte"),
 ("S2-04","Krankenhaus","Kaufmaennischer Vorstand eines Universitaetsklinikums","Forschung, Lehre und Krankenversorgung querfinanzieren","Landeszufuehrungsbetraege, Drittmittel, Hochschulmedizin","erklaert die eigene Sonderstellung zum Massstab"),
 ("S2-05","Krankenhaus","Leiterin Medizincontrolling","Erloessicherung unter Pruefquote","Kodierrichtlinien, MD-Pruefung, Fallzusammenfuehrung","sieht Versorgung durch die Abrechnungslinse"),
 ("S2-06","Krankenhaus","Pflegedirektor","Dienstplanfaehigkeit und Pflegebudget","PPBV, PpUGV, Paragraf 6a KHEntgG","argumentiert regulatorisch und haelt das fuer physisch"),
 ("S2-07","Krankenhaus","Referent Krankenhausplanung eines Landes","Versorgungsauftrag und Standortstruktur","KHVVG-Umsetzung, Leistungsgruppen, Erreichbarkeit","Landesinteresse vor Systemwirkung"),
 ("S2-08","Ambulant","Hausaerztin im laendlichen Einzelsitz","Sicherstellung ohne Nachfolge","Bedarfsplanung, Hausarztvertrag, Wegezeiten","haelt die eigene Praxisform fuer die schutzwuerdige Norm"),
 ("S2-09","Ambulant","Geschaeftsfuehrer eines investorengetragenen MVZ","Rendite und Standortkonsolidierung","Kaufpreismultiplikatoren, Arztsitzhandel, Prozessstandardisierung","blendet die Versorgungswirkung der Selektion aus"),
 ("S2-10","Ambulant","Vorstand einer Kassenaerztlichen Vereinigung","Sicherstellungsauftrag und Honorarverteilung","Honorarverteilungsmassstab, Bedarfsplanung, Notdienst","verteidigt die Koerperschaft auch dort, wo sie das Hemmnis ist"),
 ("S2-11","Ambulant","Fachaerztin fuer Radiologie im ambulanten Zentrum","Auslastung teurer Geraete","Vorhaltekosten, Befundvolumen, Zuweiserbindung","am staerksten exponiertes Fachgebiet, argumentiert dagegen"),
 ("S2-12","Pflege","Geschaeftsfuehrerin eines Pflegeheimtraegers","Belegung und Eigenanteil","Pflegesatzverhandlung, Personalbemessung, Bauinvestitionen","behandelt Personalmangel als einzige Variable"),
 ("S2-13","Pflege","Leiter eines ambulanten Pflegedienstes","Tourenplanung und Refinanzierung","Leistungskomplexe SGB XI, Wegezeiten, Personalbindung","rechnet Effizienzgewinne, die der Kostentraeger abschoepft"),
 ("S2-14","Klinikfinanzierung","Kreditrisikomanager Healthcare einer Landesbank","Qualitaet des Krankenhauskreditportfolios","Covenants, Insolvenzquoten, Traegerbonitaet","ueberschaetzt den Rueckhalt des Traegers als Sicherheit"),
 ("S2-15","Klinikfinanzierung","Restrukturierungsberater fuer Kliniken","Sanierungsfaehigkeit","Liquiditaetsplanung, Sanierungsgutachten, StaRUG","sieht nur die Faelle, die bereits scheitern"),
 ("S2-16","Klinikfinanzierung","Referentin fuer kommunale Finanzen","Traegerzuschuss im Haushalt","Kommunalhaushalt, Kassenkredite, Haushaltssicherung","behandelt den Defizitausgleich als politische Konstante"),

 # ---- Station 3: Pharma, MedTech, US-Schock (18)
 ("S3-01","Pharma","Deutschlandchef eines forschenden Originators","Marktzugang und Preisniveau halten","AMNOG-Verfahren, Launchsequenz, internationale Preisreferenz","gibt Konzernstrategie als Marktlogik aus"),
 ("S3-02","Pharma","Geschaeftsfuehrerin eines mittelstaendischen Pharmaunternehmens","Portfolio und Liquiditaet","Nischenindikationen, Lohnherstellung, Zulassungskosten","unterschaetzt die eigene Zollbetroffenheit"),
 ("S3-03","Pharma","Vorstand eines Generikaherstellers","Kostenfuehrerschaft und Rabattvertraege","Rabattvertragsausschreibungen, Festbetraege, Wirkstoffbezug","behandelt die Lieferkette als einzige Variable"),
 ("S3-04","Pharma","Gruenderin eines Biotechunternehmens","Finanzierungsrunden und Studienfortschritt","Kapitalmarktfenster, Meilensteine, Auslizenzierung","der US-Kapitalmarkt bestimmt die gesamte Sicht"),
 ("S3-05","Market Access","Leiter Market Access eines Herstellers","Erstattungsbetrag verhandeln","Nutzenbewertung, zweckmaessige Vergleichstherapie, Erstattungsbetragsverhandlung","Verhandlungslogik vor Systemwirkung"),
 ("S3-06","Market Access","Referent des Gemeinsamen Bundesausschusses","Verfahrenssicherheit der Nutzenbewertung","Verfahrensordnung, Beschlusslage, anwendungsbegleitende Datenerhebung","Verfahren vor Wirkung"),
 ("S3-07","Market Access","Wissenschaftlerin am IQWiG","methodische Belastbarkeit der Evidenz","Methodenpapier, Endpunktbewertung, Verzerrungsrisiko","methodische Strenge blendet Zeitkosten aus"),
 ("S3-08","Market Access","Beraterin fuer HEOR und Versorgungsforschung","Auftragsvolumen und Methodenqualitaet","Sekundaerdatenanalyse, Modellierung, Registerdaten","genau das Geschaeft, das KI zuerst verbilligt"),
 ("S3-09","US-Schock","US-Handelsrechtsanwalt fuer Section 232","Zolleinstufung und Ausnahmen","Proklamation vom 2. April 2026, Onshoring-Zusagen, Tarifstufen","Rechtsfrage vor Marktwirkung"),
 ("S3-10","US-Schock","Analystin fuer globale Arzneimittelpreisstrategie","Preisreferenzkaskade","MFN-Vereinbarungen, internationale Referenzpreissysteme, Launchsequenz","rechnet Preise, nicht Versorgungswirkung"),
 ("S3-11","US-Schock","Referent fuer US-Gesundheitspolitik (CMS und CMMI)","Umsetzbarkeit der Erstattungsmodelle","GENEROUS, GLOBE, GUARD, Medicare und Medicaid","US-Binnenlogik, unterschaetzt die Rueckwirkung auf Europa"),
 ("S3-12","MedTech","Geschaeftsfuehrer eines Medizintechnikunternehmens","Zulassung und Erstattung","MDR, NUB-Verfahren, Hilfsmittelverzeichnis","behandelt die MDR als einziges Hemmnis"),
 ("S3-13","MedTech","Leiterin Diagnostikgeschaeft","Testvolumen und Laborpreise","Laborreform, EBM-Kapitel 32, Automatisierungsgrad","liest Preisverfall als Mengenchance"),
 ("S3-14","MedTech","Produktmanager digitale Gesundheitsanwendungen","Erstattungsfaehigkeit und Nutzennachweis","DiGA-Verzeichnis, Erprobungsverfahren, Verguetungsbetraege","behandelt den Nutzennachweis als Formsache"),
 ("S3-15","Lieferkette","Apothekerin einer Offizinapotheke","Arzneimittelversorgung und Fixum","Apothekenbetriebsordnung, E-Rezept, Rabattvertraege","schaetzt den Beratungsanteil hoeher ein, als er abgerechnet wird"),
 ("S3-16","Lieferkette","Geschaeftsfuehrer eines Pharmagrosshandels","Spanne und Logistikkosten","Grosshandelszuschlag, Lieferfaehigkeit, Retouren","die Logistik ist der Hauptkanal der Automatisierung, das bleibt unbenannt"),
 ("S3-17","Lieferkette","Leiter Einkauf Wirkstoffe","Bezugssicherheit und Preis","Wirkstoffherkunft, Zweitquellen, Exportkontrolle","liest Konzentrationsrisiko als Preisrisiko"),
 ("S3-18","Lieferkette","Referentin Arzneimittelversorgung einer Krankenkasse","Ausgabenkontrolle im Arzneimittelbereich","Rabattvertraege, Festbetraege, Arzneimittelausgaben","Ausgabenseite vor Innovationswirkung"),

 # ---- Station 4: HIGL (12)
 ("S4-01","HIGL","Institutsleitung WIG2 (Gesundheitsoekonomie und HEOR)","wissenschaftliche Reputation und Auftragslage","Versorgungsdaten, Modellierung, Pharma- und Behoerdenauftraege","haelt Methodentiefe fuer den Burggraben"),
 ("S4-02","HIGL","Vertriebsverantwortung WIG2 fuer Pharma und Behoerden","Auftragseingang bei Herstellern und Aemtern","Ausschreibungen, Rahmenvertraege, Grossauftragsgeschaeft","verwechselt Kundenbindung mit Unersetzbarkeit"),
 ("S4-03","HIGL","Geschaeftsfuehrung 4K ANALYTICS","Ergebnis und Plattformwachstum","Kassengeschaeft, Lizenzmodell, Produktfahrplan","liest die Konzentration auf zwei Grosskunden als Staerke"),
 ("S4-04","HIGL","Produkt- und Plattformverantwortung 4K ANALYTICS","Produktreife und Skalierung","Datenpipelines, Auswertungslogiken, Releasezyklen","unterschaetzt, wie schnell die Auswertungsschicht zur Ware wird"),
 ("S4-05","HIGL","Geschaeftsfuehrung GREENBAY Software","Auslastung und Stundensatz","Entwicklerkapazitaet, Projektvertraege, interne Verrechnung","das eigene Geschaeftsmodell ist das erste Ziel der Agenten"),
 ("S4-06","HIGL","Entwicklungsleitung GREENBAY Software","Lieferfaehigkeit und Codequalitaet","Teamgroesse, Technologiestack, Wiederverwendung","liest den Produktivitaetsgewinn als Kapazitaetsgewinn statt als Preisverfall"),
 ("S4-07","HIGL","Leitung GREENBAY research (Auftragsforschung)","Studienauslastung und Rekrutierung","DiGA-Studien, Kassenprojekte, Verbundpartner","deutet die Abhaengigkeit von einem Auftraggeber als Partnerschaft"),
 ("S4-08","HIGL","Geschaeftsfuehrung GREENBAY healthcare","Marktzugang und Produktportfolio","Versorgungsvertraege, Kassenkontakte","Markenwirkung vor Zahlungsbereitschaft"),
 ("S4-09","HIGL","Geschaeftsfuehrung CLINIBOTS","Absatz der Klinikdatenauswertung","Paragraf 21 KHEntgG, Qualitaetsberichte, eigene Auswertungssystematik","oeffentlicher Rohstoff, private Auswertung — genau die angreifbare Stelle"),
 ("S4-10","HIGL","Geschaeftsfuehrung INNO3","Veranstaltungs- und Netzwerkgeschaeft","Teilnehmerzahlen, Sponsoring, Kleinbetragsrechnungen","der Netzwerkwert ist schwer bepreisbar und wird ueberschaetzt"),
 ("S4-11","HIGL","Leitung iLoc (Shared Services)","Kostendeckung der Innenverrechnung","Konzernumlage, Verrechnungspreise, Leistungsabgrenzung","ohne Aussenmarkt fehlt jedes Preissignal"),
 ("S4-12","HIGL","Verbundcontrolling HIGL","Ergebnis und Liquiditaet ueber alle Gesellschaften","Buchungsdaten, Deckungsbeitraege, Kundenkonzentration","Zahlenblick ohne Marktblick"),

 # ---- Querbank Europa (8)
 ("EU-01","Europa","Gesundheitssystemforscherin Daenemark","Vergleichbarkeit des daenischen Wegs","Digitalisierungsgrad, zentrale Register, Primaerversorgung","verallgemeinert Kleinstaatvorteile"),
 ("EU-02","Europa","Krankenhausoekonom Frankreich","Klinikfinanzierung unter zentraler Steuerung","Tarification a l activite, ONDAM, oeffentliche Traegerschaft","ueberschaetzt die zentralstaatliche Steuerbarkeit"),
 ("EU-03","Europa","Versicherungsoekonom Niederlande","reguliertes Wettbewerbsmodell","Zorgverzekeringswet, Risikoausgleich, Eigenrisiko","behandelt die Marktloesung als Normalfall"),
 ("EU-04","Europa","Digitalisierungsverantwortliche Estland","staatliche Datenplattform","X-Road, elektronische Patientenakte, digitale Identitaet","ueberspringt die Skalierungsfrage"),
 ("EU-05","Europa","Gesundheitsoekonom Vereinigtes Koenigreich","steuerfinanziertes System unter Budgetdruck","NHS-Budget, Wartelisten, Personalplanung","Budgetrestriktion als einzige Variable"),
 ("EU-06","Europa","Referentin der Europaeischen Kommission fuer den AI Act","Durchsetzung und Hochrisikoeinstufung","VO (EU) 2024/1689, Fristen, Konformitaetsbewertung","Rechtsakt vor Marktwirkung"),
 ("EU-07","Europa","Referent fuer den europaeischen Gesundheitsdatenraum","Sekundaernutzung von Gesundheitsdaten","EHDS, Governance, nationale Zugangsstellen","verwechselt Datenverfuegbarkeit mit Datennutzbarkeit"),
 ("EU-08","Europa","Referentin fuer das EU-Pharmapaket","Versorgungssicherheit und Innovationsanreize","Revision des Arzneimittelrechts, Unterlagenschutz, Anreizsystem","Binnenmarktlogik vor globaler Preiskaskade"),

 # ---- Querbank KI-Technik (6)
 ("KI-01","KI-Technik","Entwicklungsleiterin bei einem Anbieter von Basismodellen","Faehigkeitszuwachs und Sicherheit","Modellgenerationen, Messreihen, Inferenzkosten","verwechselt Laborfaehigkeit mit Einsatzfaehigkeit"),
 ("KI-02","KI-Technik","Loesungsarchitekt fuer Agentensysteme im Unternehmen","Integration in Bestandsprozesse","Systemanbindung, Rechteverwaltung, Fehlertoleranz","unterschaetzt den Integrationsaufwand"),
 ("KI-03","KI-Technik","Robotikingenieurin fuer Service- und Pflegerobotik","technische Reife physischer Systeme","Greifen, Navigation, Sicherheitsnormen","dort, wo das US-Modell endet — neigt zu Optimismus bei den Stueckkosten"),
 ("KI-04","KI-Technik","Leiter Rechenzentrum und Netzanschluss","Kapazitaet, Energie, Latenz","Anschlusswarteschlangen, Strompreis, Auslastung","angekuendigte Kapazitaet ist nicht gebaute Kapazitaet"),
 ("KI-05","KI-Technik","Pruefer einer Benannten Stelle fuer Medizin-KI","Konformitaet und Marktzugang","MDR, Art. 43 VO (EU) 2024/1689, klinische Bewertung","behandelt die Zulassungsdauer als konstante Groesse"),
 ("KI-06","KI-Technik","Informationssicherheitsbeauftragter eines Gesundheitsdienstleisters","Angriffsflaeche und KRITIS-Pflichten","NIS2, KRITIS-Vorgaben, Vorfallmeldung","Sicherheitsbedenken als Universalbremse"),

 # ---- Querbank Gegenposition (3)
 ("GP-01","Gegenposition","Wirtschaftshistoriker der Automatisierungswellen","Widerlegung ueberzogener Erwartungen","Produktivitaetsparadox, Elektrifizierung, Computerisierung","erklaert jede Neuerung zur Wiederholung"),
 ("GP-02","Gegenposition","Oekonom in der Tradition des IW Koeln","Arbeit entlasten statt Kapital belasten","Steuerinzidenz, Kapitalmobilitaet, Standortwettbewerb","Kapitalabfluss als Allzweckargument"),
 ("GP-03","Gegenposition","Verteilungsforscherin","Wer traegt die Anpassungslast","Lohnquote, Vermoegensverteilung, Inzidenzanalyse","die Verteilungsfrage verdraengt die Wachstumsfrage"),
]

def als_dicts():
    return [dict(id=i, gruppe=g, station=i.split("-")[0], rolle=r,
                 mandat=m, anker=a, blindstelle=b)
            for (i, g, r, m, a, b) in ROLLEN]

if __name__ == "__main__":
    import collections, json
    rs = als_dicts()
    assert len(rs) == 100, len(rs)
    assert len({r["id"] for r in rs}) == 100
    c = collections.Counter(r["station"] for r in rs)
    for s in ("S0","S1","S2","S3","S4","EU","KI","GP"):
        print("%-3s %-12s %-52s %3d" % (s, STATIONEN[s][0], STATIONEN[s][1][:52], c[s]))
    print("Summe", sum(c.values()))

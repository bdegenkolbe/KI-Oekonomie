export const meta = {
  name: 'sitzung-a-runde-0-bis-1b',
  description: 'Sitzung A des vollen Laufs: Recherchebank, disjunkte VZAE-Zerlegung, zwei Szenariogerueste, hundert Rollen mit Pflicht-, Markt- und Europagroessen, Modellkontrollarm, Validierung mit gesetzten Fehlern, Streitindex in beiden Varianten',
  phases: [
    { title: 'Recherche', detail: 'Zehn Faktenblaetter der Recherchebank' },
    { title: 'Grundlagen', detail: 'Disjunkte VZAE-Zerlegung ueber hundert Felder und zwei gegensaetzliche Szenariogerueste' },
    { title: 'Runde 1', detail: 'Hundert Rollen isoliert, dazu zehn Rollen doppelt auf einem zweiten Modell' },
    { title: 'Validierung', detail: 'Pruefinstanz je Kartensatz, in zehn Prozent der Karten sind Fehler gesetzt' },
  ],
}

const ROLLEN = [{"id":"A01","bank":"A","bankName":"Stationäre Versorgung","rolle":"Ärztliche Direktorin eines Maximalversorgers","mandat":"Leistungsfähigkeit und Vorhaltung des Hauses sichern","anker":"Leistungsgruppen, Fallschwere, Universitätsanbindung","blindstelle":"überschätzt die Übertragbarkeit ihrer Ausstattung auf die Grundversorgung","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"A02","bank":"A","bankName":"Stationäre Versorgung","rolle":"Kaufmännischer Geschäftsführer eines kommunalen Grund- und Regelversorgers","mandat":"Liquidität und Trägerzuschuss im Gleichgewicht halten","anker":"DRG-Erlöse, Investitionsstau, kommunale Haushaltslage","blindstelle":"liest jede Neuerung zuerst als Kostenposition","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"A03","bank":"A","bankName":"Stationäre Versorgung","rolle":"Chefarzt Innere Medizin","mandat":"ärztliche Therapiehoheit und Weiterbildungsbefugnis","anker":"Leitlinien, Weiterbildungsordnung, Fallzahlen","blindstelle":"unterschätzt, wie viel der eigenen Arbeit Dokumentation ist","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"A04","bank":"A","bankName":"Stationäre Versorgung","rolle":"Leiterin Medizincontrolling","mandat":"Erlössicherung und Prüfquote nach § 275c SGB V","anker":"Kodierrichtlinien, MD-Prüfquoten, Fallzusammenführung","blindstelle":"sieht Versorgung durch die Abrechnungslinse","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"A05","bank":"A","bankName":"Stationäre Versorgung","rolle":"Oberarzt Radiologie","mandat":"Befundqualität bei steigender Untersuchungszahl","anker":"Befundzeiten, CE-zertifizierte Befundungssoftware, Teleradiologie","blindstelle":"am stärksten exponierte Fachrichtung, neigt zur Abwehr","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"A06","bank":"A","bankName":"Stationäre Versorgung","rolle":"Leiter Labormedizin","mandat":"Durchsatz, Akkreditierung, Ringversuche","anker":"Automatisierungsgrad im Labor, DIN EN ISO 15189","blindstelle":"das am weitesten automatisierte Feld hält sich für das Maß aller","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"A07","bank":"A","bankName":"Stationäre Versorgung","rolle":"Geschäftsführerin eines privaten Klinikkonzerns","mandat":"Rendite, Standortportfolio, Skalierung","anker":"Konzern-Benchmarks, Zentraleinkauf, Standortschließungen","blindstelle":"hält Skalierbarkeit für allgemein, wo sie Konzernvorteil ist","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"A08","bank":"A","bankName":"Stationäre Versorgung","rolle":"Pflegedirektor","mandat":"Dienstplanfähigkeit und Pflegebudget","anker":"§ 6a KHEntgG, PpUGV, PPR 2.0, PPBV-Meldung","blindstelle":"argumentiert regulatorisch und hält das für physisch","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"A09","bank":"A","bankName":"Stationäre Versorgung","rolle":"Leiter OP-Management","mandat":"Saalauslastung und Schnitt-Naht-Zeiten","anker":"OP-Statut, Wechselzeiten, Materialverfügbarkeit","blindstelle":"Optimierungsdenken ohne Blick auf die Indikationsstellung","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"A10","bank":"A","bankName":"Stationäre Versorgung","rolle":"Leiterin Zentrale Notaufnahme","mandat":"Triage, Verweildauer, Fehlbelegung","anker":"Ersteinschätzungssysteme, Notfallstufenvergütung","blindstelle":"sieht die Systemlast überproportional, weil sie dort zuerst ankommt","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"B01","bank":"B","bankName":"Ambulante Versorgung","rolle":"Hausärztin im ländlichen Einzelsitz","mandat":"Sicherstellung ohne Nachfolge","anker":"Bedarfsplanung, Hausarztvertrag, Wegezeiten","blindstelle":"hält die eigene Praxisform für die schutzwürdige Norm","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"B02","bank":"B","bankName":"Ambulante Versorgung","rolle":"Hausarzt in einem MVZ-Verbund","mandat":"Arbeitsteilung, Delegation, Anstellungsmodell","anker":"Delegationsvereinbarungen, Terminvergabe, Verbundstrukturen","blindstelle":"unterschätzt die Bindung der Patienten an eine Person","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"B03","bank":"B","bankName":"Ambulante Versorgung","rolle":"Fachärztin für Augenheilkunde","mandat":"Gerätefinanzierung und Leistungsmenge","anker":"EBM-Bewertung, Screeningverfahren, Investitionszyklus","blindstelle":"Fachgebiet mit sehr hoher Automatisierbarkeit, argumentiert dagegen","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"B04","bank":"B","bankName":"Ambulante Versorgung","rolle":"Psychotherapeutin im Richtlinienverfahren","mandat":"Therapieplätze, Wartezeiten, Beziehungsarbeit","anker":"Psychotherapie-Richtlinie, Bedarfsplanung, Gruppenangebote","blindstelle":"sieht Digitalangebote grundsätzlich als Verdrängung","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"B05","bank":"B","bankName":"Ambulante Versorgung","rolle":"Radiologe im ambulanten Zentrum","mandat":"Auslastung teurer Geräte","anker":"Vorhaltekosten, Zuweiserbindung, Befundvolumen","blindstelle":"wirtschaftlicher Druck zur Mengenausweitung bleibt unbenannt","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"B06","bank":"B","bankName":"Ambulante Versorgung","rolle":"Geschäftsführer eines investorengetragenen MVZ","mandat":"Rendite und Standortkonsolidierung","anker":"Kaufpreismultiplikatoren, Arztsitzhandel, Prozessstandardisierung","blindstelle":"blendet die Versorgungswirkung der Selektion aus","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"B07","bank":"B","bankName":"Ambulante Versorgung","rolle":"Kassenärztliche Vereinigung, Sicherstellung","mandat":"Sicherstellungsauftrag und Honorarverteilung","anker":"HVM, Bedarfsplanungs-Richtlinie, Notdienst","blindstelle":"verteidigt die Körperschaft auch dort, wo sie das Hemmnis ist","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"B08","bank":"B","bankName":"Ambulante Versorgung","rolle":"Apothekerin einer Offizinapotheke","mandat":"Arzneimittelversorgung und Beratungsleistung","anker":"Apothekenbetriebsordnung, E-Rezept, Fixum und Rabattverträge","blindstelle":"Beratungsanteil wird höher eingeschätzt, als er abgerechnet wird","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"B09","bank":"B","bankName":"Ambulante Versorgung","rolle":"Leiter eines ambulanten Pflegedienstes","mandat":"Tourenplanung und Refinanzierung","anker":"Leistungskomplexe SGB XI, Wegezeiten, Personalbindung","blindstelle":"rechnet Effizienzgewinne, die der Kostenträger abschöpft","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"B10","bank":"B","bankName":"Ambulante Versorgung","rolle":"Ärztin im Öffentlichen Gesundheitsdienst","mandat":"Bevölkerungsgesundheit und Meldewesen","anker":"IfSG, Gesundheitsberichterstattung, Pakt ÖGD","blindstelle":"chronisch unterbesetzt, neigt zur Überschätzung digitaler Entlastung","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"C01","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Pflegefachkraft Intensivstation","mandat":"Patientensicherheit bei knapper Besetzung","anker":"Verhältniszahlen, Schichtrealität, Übergabeprozess","blindstelle":"verallgemeinert die Intensivsituation auf die Normalstation","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"C02","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Heimleitung einer stationären Pflegeeinrichtung","mandat":"Belegung, Personalschlüssel, Eigenanteil","anker":"§ 113c SGB XI, Landesheimgesetze, Investitionskosten","blindstelle":"sieht Angehörigenerwartungen als konstant an","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"C03","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Pflegedienstleitung ambulant","mandat":"Einsatzplanung und Refinanzierung der Wegezeit","anker":"Leistungskomplexe, Pflegegrade, Angehörigenmitwirkung","blindstelle":"unterschätzt die Grenze der Digitalisierung im Privathaushalt","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"C04","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Berufsverband Pflege","mandat":"Professionalisierung und Vorbehaltsaufgaben","anker":"Pflegeberufegesetz, Vorbehaltsaufgaben § 4 PflBG, Kammerfragen","blindstelle":"liest Delegation grundsätzlich als Abwertung","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"C05","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Pflegewissenschaftlerin","mandat":"Evidenz für Personalbemessung und Outcome","anker":"PPR 2.0, Expertenstandards DNQP, internationale Studien","blindstelle":"Evidenzlage ist dünn, das Urteil trotzdem bestimmt","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"C06","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Pflegende Angehörige","mandat":"Vereinbarkeit, Belastung, Eigenanteil","anker":"Pflegegeld, Verhinderungspflege, Erwerbsminderung durch Pflege","blindstelle":"die größte Leistungsgruppe ohne organisierte Vertretung","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"C07","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Leitung eines Trägers der Freien Wohlfahrtspflege","mandat":"Gemeinnützigkeit und Versorgungsauftrag","anker":"§ 67 AO, Tarifbindung, Refinanzierungslogik","blindstelle":"Steuerbefreiung wird als Schutz gelesen, ist aber auch Abflusskanal","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"C08","bank":"C","bankName":"Pflege und Langzeitversorgung","rolle":"Personalgewinnung Pflege, internationale Anwerbung","mandat":"Besetzung offener Stellen","anker":"Anerkennungsverfahren, Sprachniveau B2, Bindungsquoten","blindstelle":"Anerkennungsdauer wird als lösbar unterstellt","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"D01","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Vorstand einer großen Ersatzkasse","mandat":"Beitragssatzstabilität und Mitgliederbindung","anker":"Verwaltungskosten je Versicherten, Morbi-RSA, § 31a SGB X","blindstelle":"Wettbewerb um gute Risiken bleibt unausgesprochen","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"D02","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Vorstand einer kleinen Betriebskrankenkasse","mandat":"Existenzfähigkeit bei Fixkostendegression","anker":"Skaleneffekte der Verwaltung, Fusionsdruck","blindstelle":"rechnet Digitalisierung als Rettung, nicht als Fusionstreiber","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"D03","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"GKV-Spitzenverband, Grundsatzfragen","mandat":"Systemstabilität und einheitliche Regelsetzung","anker":"Bundesrahmenempfehlungen, Beitragssatzgesetzgebung","blindstelle":"Systemperspektive übersieht die Streuung zwischen Kassen","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"D04","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Medizinischer Dienst, Begutachtung","mandat":"Prüfqualität und Unabhängigkeit","anker":"Prüfquoten § 275c SGB V, Begutachtungsanleitungen","blindstelle":"prüft, was prüfbar ist, nicht was wichtig ist","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"D05","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Aktuar einer privaten Krankenversicherung","mandat":"Kalkulation, Alterungsrückstellung, Beitragsanpassung","anker":"Rechnungsgrundlagen, § 203 VVG, Neugeschäft","blindstelle":"PKV-Logik wird auf das Gesamtsystem übertragen","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"D06","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Pflegekasse, Leistungsrecht","mandat":"Leistungsgewährung und Budgetdisziplin","anker":"Pflegegrade, Begutachtung, Leistungsdynamisierung","blindstelle":"die demografische Kostenwelle dominiert jedes andere Argument","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"D07","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Gemeinsamer Bundesausschuss, Methodenbewertung","mandat":"Nutzenbewertung vor Erstattung","anker":"Verfahrensordnung, Erprobungsregelungen, § 137h SGB V","blindstelle":"Verfahrensdauer wird als Qualitätsgarantie gelesen","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"D08","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Nutzenbewertung (IQWiG-Typ)","mandat":"methodische Strenge der Evidenz","anker":"Studiendesign, Endpunktrelevanz, Verzerrungsrisiko","blindstelle":"verlangt für KI-Verfahren Evidenz, die das Studiendesign nicht liefern kann","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"D09","bank":"D","bankName":"Kostenträger und Selbstverwaltung","rolle":"Deutsche Rentenversicherung, Reha und Erwerbsminderung","mandat":"Erwerbsfähigkeit erhalten","anker":"Reha-Zugänge, EM-Renten, Nahtlosigkeit","blindstelle":"Gesundheitswesen erscheint nur als Zulieferer der Erwerbsfähigkeit","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"E01","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Pharmaunternehmen, Market Access Deutschland","mandat":"Erstattungsbetrag und Marktzugang","anker":"AMNOG, § 130b SGB V, Nutzenbewertung","blindstelle":"Preisbildung wird als Innovationsbedingung dargestellt","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"E02","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Medizintechnikhersteller Bildgebung","mandat":"Gerätezyklen und Serviceerlöse","anker":"MDR-Zertifizierung, Installationsbasis, Wartungsverträge","blindstelle":"Bestandsgeräte sind der Bremsklotz, nicht das Neugeschäft","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"E03","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Anbieter eines Krankenhausinformationssystems","mandat":"Marktanteil und Schnittstellenhoheit","anker":"KIS-Migrationskosten, FHIR-Module, Wechselbarrieren","blindstelle":"die eigene Schnittstellenpolitik ist Teil des Hemmnisses","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"E04","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Health-Tech-Scale-up, Versorgungsprozesse","mandat":"Erstattungstatbestand und Skalierung","anker":"NUB § 6 Abs. 2 KHEntgG, Pilotfinanzierung, Vertriebszyklen","blindstelle":"Vertriebszyklus im Krankenhaus wird chronisch unterschätzt","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"E05","bank":"E","bankName":"Gesundheitsindustrie","rolle":"DiGA-Hersteller","mandat":"Verzeichnisaufnahme und Vergütung","anker":"DiGAV, Erprobungsphase, Verordnungszahlen","blindstelle":"reale Nutzungsraten liegen weit unter den Verordnungen","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"E06","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Labordiagnostik-Konzern","mandat":"Durchsatz und Preisdruck","anker":"EBM-Laborkapitel, Automatisierungsgrad, Skalenlogik","blindstelle":"Vorreiterrolle in der Automatisierung erzeugt Übertragungsoptimismus","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"E07","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Großhandel und Logistik Arzneimittel","mandat":"Lieferfähigkeit und Marge","anker":"Handelsspanne, Engpassmeldungen, Retax-Risiko","blindstelle":"Lieferengpässe werden als Preisproblem gelesen","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"E08","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Hersteller KI-gestützter Befundungssoftware","mandat":"Zulassung und klinische Akzeptanz","anker":"MDR Klasse IIb, AI-Act-Hochrisikoeinstufung, Studienlage","blindstelle":"Zulassung wird mit Einführung verwechselt","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"E09","bank":"E","bankName":"Gesundheitsindustrie","rolle":"Beratungshaus für Krankenhaustransformation","mandat":"Projektvolumen und Folgeaufträge","anker":"Transformationsprogramme, Fördertöpfe, Benchmarking","blindstelle":"Geschäftsmodell lebt vom Umbau, nicht vom Ergebnis","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"F01","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Gewerkschaftssekretärin Gesundheitswesen","mandat":"Entgelt, Besetzung, Beschäftigungssicherung","anker":"TVöD-K, § 87 Abs. 1 Nr. 6 BetrVG, Tarifrunden","blindstelle":"Mitbestimmung verlagert Verdrängung, verhindert sie nicht","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"F02","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Betriebsrat eines Klinikverbunds","mandat":"Mitbestimmung bei technischer Einführung","anker":"Betriebsvereinbarungen, Leistungskontrolle, Dienstplan","blindstelle":"betriebliche Sicht ohne Blick auf die Systemfinanzierung","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"F03","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Ärztliche Interessenvertretung","mandat":"Arbeitszeit, Weiterbildung, ärztliche Vorbehalte","anker":"Arbeitszeitgesetz, Weiterbildungsordnung, Bereitschaftsdienst","blindstelle":"Standeslogik verteidigt auch delegierbare Aufgaben","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"F04","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Assistenzärztin in Weiterbildung","mandat":"Weiterbildungsqualität und Einstiegsposition","anker":"Weiterbildungskataloge, Rotationsplanung, Lernkurve","blindstelle":"ihre Lernstrecke besteht aus genau den automatisierbaren Aufgaben","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"F05","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Medizinische Fachangestellte","mandat":"Aufgabenzuschnitt und Eingruppierung","anker":"Delegationsfähigkeit, Praxisorganisation, MFA-Tarif","blindstelle":"am stärksten betroffene Gruppe mit der schwächsten Vertretung","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"F06","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Hebamme","mandat":"Betreuungsschlüssel und Haftpflicht","anker":"Hebammengesetz, Haftpflichtprämien, Beleghebammenmodell","blindstelle":"kleine Gruppe, argumentiert aus der Ausnahmesituation","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"F07","bank":"F","bankName":"Gesundheitsberufe und Arbeitnehmerseite","rolle":"Notfallsanitäter im Rettungsdienst","mandat":"Kompetenzen und Einsatzaufkommen","anker":"NotSanG, § 2a, Telenotarzt, Landesrettungsdienstgesetze","blindstelle":"Landesrecht ist uneinheitlich, wird aber verallgemeinert","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"G01","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Patientenvertretung im G-BA","mandat":"Mitberatung und Patientensicherheit","anker":"§ 140f SGB V, Beteiligungsrechte ohne Stimmrecht","blindstelle":"Beteiligung ohne Stimmrecht wird als Einfluss gelesen","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"G02","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Sozialverband","mandat":"Zugang und Eigenanteile","anker":"Zuzahlungsregelungen, Härtefälle, Pflegeeigenanteil","blindstelle":"Verteilungsfrage verdrängt die Versorgungsfrage","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"G03","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Selbsthilfeorganisation chronisch Kranker","mandat":"Versorgungskontinuität und Teilhabe","anker":"DMP, Patientenschulung, Selbsthilfeförderung","blindstelle":"die eigene Indikation wird zum Maßstab für alle","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"G04","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Verbraucherschutz Gesundheitsmarkt","mandat":"Transparenz und Irreführungsschutz","anker":"IGeL-Markt, Werbeverbote, Preisvergleichbarkeit","blindstelle":"sieht zuerst Missbrauch, dann Nutzen","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"G05","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Angehörigenvertretung Demenz","mandat":"Betreuung, Entlastung, Würde","anker":"Pflegegrade bei Demenz, Betreuungsrecht, Tagespflege","blindstelle":"Digitalisierung wird pauschal als Entmenschlichung gelesen","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"G06","bank":"G","bankName":"Patienten und Zivilgesellschaft","rolle":"Patientin mit seltener Erkrankung","mandat":"Diagnosestellung und Spezialversorgung","anker":"Zentrenstruktur, Diagnoseodyssee, Orphan Drugs","blindstelle":"genau die Gruppe, die von Mustererkennung am meisten gewänne","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"H01","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Bundesgesundheitsministerium, Grundsatzabteilung","mandat":"Reformfähigkeit und Beitragssatzstabilität","anker":"KHVVG, Finanzierungsreform, Koalitionsbindung","blindstelle":"Gesetzgebungsfähigkeit wird mit Umsetzungsfähigkeit verwechselt","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"H02","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Landesgesundheitsministerium, Krankenhausplanung","mandat":"Versorgungssicherung in der Fläche","anker":"Leistungsgruppen, Investitionsquote, Standortentscheidungen","blindstelle":"Landesinteresse an Standorterhalt prägt jede Zahl","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"H03","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Bundesamt für Soziale Sicherung, Aufsicht","mandat":"Rechtsaufsicht über die Kassen","anker":"§ 31a SGB X, Haushaltsgenehmigung, Prüfberichte","blindstelle":"Aufsicht misst Rechtmäßigkeit, nicht Wirkung","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"H04","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Zulassungsbehörde Medizinprodukte und DiGA","mandat":"Sicherheit und Marktzugang","anker":"MDR, DiGAV, Benannte Stellen, Vigilanz","blindstelle":"Kapazitätsengpass der Benannten Stellen bleibt unterbelichtet","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"H05","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Betreibergesellschaft der Telematikinfrastruktur","mandat":"Interoperabilität und Rollout","anker":"ePA, E-Rezept, Zulassungsverfahren, Konnektoren","blindstelle":"Anschlussquote wird als Nutzung berichtet","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"H06","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Kommunale Gesundheitsplanung","mandat":"wohnortnahe Versorgung und Daseinsvorsorge","anker":"Sicherstellung, kommunale Trägerschaft, ÖGD","blindstelle":"Haushaltslage schlägt jede Versorgungsanalyse","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"H07","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Haushaltspolitikerin, Finanzausschuss","mandat":"Bundeszuschuss und Schuldenbremse","anker":"Bundeshaushalt, Steuerzuschüsse zur GKV, Sozialquote","blindstelle":"Gesundheitsausgaben erscheinen nur als Ausgabenlinie","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"H08","bank":"H","bankName":"Gesundheitspolitik und Aufsicht","rolle":"Public-Health-Institut","mandat":"Bevölkerungsgesundheit und Prävention","anker":"Gesundheitsberichterstattung, Surveillance, Risikofaktoren","blindstelle":"Prävention wird als politisch durchsetzbar unterstellt","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"I01","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Medizinrechtler, Haftung","mandat":"Zurechenbarkeit ärztlicher Entscheidung","anker":"§ 630a ff. BGB, Behandlungsfehlerrecht, Beweislast","blindstelle":"jede Neuerung erscheint zuerst als Haftungsrisiko","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"I02","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Datenschutzbeauftragte eines Krankenhauses","mandat":"Schweigepflicht und Verarbeitungsgrundlage","anker":"§ 203 StGB, § 80 SGB X, DSFA, Auftragsverarbeitung","blindstelle":"Anonymisierung klinischer Freitexte hat keinen anerkannten Standard","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"I03","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Sozialrechtlerin SGB V und XI","mandat":"Leistungsansprüche und Verfahrensrecht","anker":"Leistungsrecht, Widerspruchsverfahren, § 31a SGB X","blindstelle":"Verfahrensrecht wird als unveränderlich behandelt","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"I04","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Medizinethikerin","mandat":"Autonomie, Nichtschaden, Gerechtigkeit","anker":"Ethikkommissionen, Aufklärungsstandards, Priorisierungsdebatte","blindstelle":"ethische Bedenken ohne Kostenseite","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"I05","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Landesdatenschutzaufsicht","mandat":"Aufsichtspraxis und Bußgeldrahmen","anker":"Landeskrankenhausgesetze, Aufsichtsentscheidungen","blindstelle":"Aufsichtspraxis unterscheidet sich je Land erheblich","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"I06","bank":"I","bankName":"Recht, Datenschutz, Ethik","rolle":"Richterin im Arzthaftungsrecht","mandat":"Entscheidbarkeit des Einzelfalls","anker":"Beweisaufnahme, Sachverständigenbeweis, Dokumentationspflicht","blindstelle":"urteilt über Vergangenes, nicht über Einführungsentscheidungen","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"J01","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Makroökonom, Wachstum und Produktivität","mandat":"gesamtwirtschaftliche Wirkung messbar machen","anker":"Produktivitätsstatistik, Wachstumsbuchhaltung, Solow-Residuum","blindstelle":"Aggregate lösen die entscheidenden Verschiebungen nicht auf","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"J02","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Arbeitsmarktökonomin","mandat":"Beschäftigung, Matching, Qualifikation","anker":"Erwerbspersonenpotenzial, Engpassanalyse, Arbeitsmarktprojektion","blindstelle":"Berufswechsel wird als möglich unterstellt, wo er es nicht ist","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"J03","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Finanzwissenschaftlerin, Sozialabgaben","mandat":"Finanzierungsbasis der Sozialversicherung","anker":"Beitragsbemessungsgrenzen, Abgabenkeil, Wertschöpfungsabgabe","blindstelle":"Reformvorschläge ohne politische Durchsetzbarkeitsprüfung","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"J04","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Steuerrechtlerin, Unternehmenssteuerrecht","mandat":"Rechtssicherheit der Besteuerung","anker":"§ 34 AO, § 150 Abs. 7 AO, Gewerbesteuerzerlegung","blindstelle":"Verfahrensrecht als dauerhafter Schutz der eigenen Profession","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"J05","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Demografieforscher","mandat":"Alterung und Erwerbspersonenpotenzial","anker":"Bevölkerungsvorausberechnung, Kohortenanalyse, Wanderung","blindstelle":"demografische Kraft überstrahlt jede andere Ursache","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"J06","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Externe Finanzkontrolle","mandat":"Wirtschaftlichkeit öffentlicher Mittel","anker":"Prüfberichte, Wirtschaftlichkeitsgebot, Fördermittelverwendung","blindstelle":"prüft Verwendung, selten Wirkung","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"J07","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Kommunale Spitzenverbände","mandat":"kommunale Finanzausstattung","anker":"Gewerbesteuerzerlegung, Ergebnisplan, Haushaltssicherung","blindstelle":"kommunale Perspektive auf ein bundesrechtlich geregeltes System","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"J08","bank":"J","bankName":"Gesamtwirtschaft, Fiskus, Demografie","rolle":"Stabilitätsorientierte Institution (Bundesbank-Typ)","mandat":"Tragfähigkeit der öffentlichen Finanzen","anker":"Tragfähigkeitsrechnungen, implizite Staatsschuld, Sozialquote","blindstelle":"langfristige Tragfähigkeit ohne Versorgungsqualität","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"K01","bank":"K","bankName":"Europa und internationale Systeme","rolle":"EU-Kommission, Gesundheitspolitik","mandat":"Europäischer Gesundheitsdatenraum","anker":"EHDS-Verordnung, Sekundärnutzung, grenzüberschreitender Zugang","blindstelle":"Umsetzungsrealität in den Mitgliedstaaten wird unterschätzt","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"K02","bank":"K","bankName":"Europa und internationale Systeme","rolle":"EU-Kommission, Digitalpolitik","mandat":"AI Act und digitale Souveränität","anker":"Hochrisikoeinstufung, Fristen, AI Gigafactories, MFR-Zyklus","blindstelle":"Haushaltszyklus entscheidet mehr als die Politik","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"K03","bank":"K","bankName":"Europa und internationale Systeme","rolle":"Niederländisches Gesundheitssystem","mandat":"reguliertes Wettbewerbsmodell","anker":"Zorgverzekeringswet, Hausarzt als Gatekeeper, Digitalisierungsgrad","blindstelle":"Systemunterschied wird als Vorbild gelesen","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"K04","bank":"K","bankName":"Europa und internationale Systeme","rolle":"Dänisches Gesundheitssystem","mandat":"steuerfinanziert, hochdigitalisiert","anker":"Sundhed.dk, zentrale Register, Regionenstruktur","blindstelle":"kleine, homogene Bevölkerung als Skalierungsvoraussetzung","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"K05","bank":"K","bankName":"Europa und internationale Systeme","rolle":"Französische Krankenversicherung","mandat":"zentralstaatliche Steuerung","anker":"Assurance Maladie, Ségur du numérique, Tarifhoheit","blindstelle":"Zentralsteuerung erscheint als reine Effizienzfrage","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"K06","bank":"K","bankName":"Europa und internationale Systeme","rolle":"Estnisches E-Health-System","mandat":"durchgängige digitale Identität","anker":"X-Road, ePA seit 2008, Bürgerportal","blindstelle":"Vorsprung beruht auf einem Neuaufbau ohne Bestandslast","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"K07","bank":"K","bankName":"Europa und internationale Systeme","rolle":"Internationale Gesundheitsökonomie","mandat":"Systemvergleich und Ergebnisqualität","anker":"OECD Health at a Glance, Ausgabenquoten, Outcome-Indikatoren","blindstelle":"Kennzahlvergleich ohne Systemkontext","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"L01","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"KI-Forscherin, klinische Modelle","mandat":"Modellgüte und Generalisierbarkeit","anker":"Benchmarkergebnisse, Domänenverschiebung, Validierungsstudien","blindstelle":"Benchmarkleistung ist nicht Versorgungswirkung","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"L02","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"ML-Engineer im Krankenhausbetrieb","mandat":"Betrieb, Drift, Integration","anker":"Datenqualität im KIS, Monitoring, Modellpflege","blindstelle":"unterschätzt die Organisations- und Rechtsschicht","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"L03","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"Robotik in Pflege und Chirurgie","mandat":"Assistenzsysteme im physischen Raum","anker":"Sicherheitsnachweis, Performance Level, Zulassung","blindstelle":"Sicherheitsnachweis für lernende Steuerung ist ungelöst","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"L04","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"Rechenzentrums- und Compute-Infrastruktur","mandat":"Kapazität, Standort, Auslastung","anker":"Nennanschlussleistung, Bauleitplanung, Ankermieter","blindstelle":"Kapazitätsankündigung ist nicht Kapazität","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"L05","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"Energie und Netzanschluss","mandat":"Anschlussfähigkeit und Netzentgelte","anker":"Reifegradverfahren, Umspannwerkslieferzeiten, Industriestrompreis","blindstelle":"physikalische Zeitkonstanten dominieren jedes Argument","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"L06","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"Interoperabilität und Standards","mandat":"Datenaustausch über Systemgrenzen","anker":"FHIR, ISiK, Terminologien, Implementierungsleitfäden","blindstelle":"Standard ist nicht Implementierung","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"L07","bank":"L","bankName":"Technik, KI, Infrastruktur","rolle":"IT-Sicherheit im Gesundheitswesen","mandat":"Verfügbarkeit und Angriffsresistenz","anker":"KRITIS-Verordnung, NIS-2, Vorfälle in Kliniken","blindstelle":"Sicherheitsargument blockiert auch nützliche Öffnung","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"M01","bank":"M","bankName":"Geopolitik, Handel, Versorgungssicherheit","rolle":"Lieferketten Arzneimittel und Wirkstoffe","mandat":"Lieferfähigkeit und Diversifizierung","anker":"Wirkstoffherkunft, Engpassliste, Bevorratungspflichten","blindstelle":"Rückverlagerung wird als Preisfrage behandelt","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"M02","bank":"M","bankName":"Geopolitik, Handel, Versorgungssicherheit","rolle":"Handelsökonom, Exportkontrolle","mandat":"Regelkonformität im Außenhandel","anker":"AWG/AWV, EU-Dual-Use-VO, Ausfuhrverantwortlicher","blindstelle":"persönliche Haftung erzeugt Schutz der eigenen Funktion","geruest":"A","anker_reihenfolge":"substitution_zuerst"},{"id":"M03","bank":"M","bankName":"Geopolitik, Handel, Versorgungssicherheit","rolle":"Sicherheitspolitik und Resilienz","mandat":"Krisenfestigkeit kritischer Versorgung","anker":"Zivile Verteidigung, Bevorratung, Szenarien","blindstelle":"Krisenszenarien überzeichnen den Normalbetrieb","geruest":"A","anker_reihenfolge":"gegenevidenz_zuerst"},{"id":"M04","bank":"M","bankName":"Geopolitik, Handel, Versorgungssicherheit","rolle":"Rohstoffe und Medizintechnikimporte","mandat":"Beschaffungssicherheit","anker":"Importabhängigkeiten, Zollfragen, Qualifizierungsdauer","blindstelle":"Lieferantenwechsel wird als kurzfristig möglich unterstellt","geruest":"B","anker_reihenfolge":"substitution_zuerst"},{"id":"N01","bank":"N","bankName":"Der Verfasser","rolle":"Verfasser des Arbeitspapiers","mandat":"die Deutschland-These prüfen lassen, nicht bestätigen","anker":"`KI-Ökonomie.md`, Wertschöpfungsabgabe, Teilhabefonds, Veredelungsstrategie","blindstelle":"verteidigt die eigenen drei Hebel; die Rolle ist ausdrücklich verpflichtet, sie angreifen zu lassen","geruest":"B","anker_reihenfolge":"gegenevidenz_zuerst"}]
const RECH = [{"id":"R01","domaene":"GKV- und SPV-Finanzen","liefergegenstand":"Beitragssatzpfad, Zusatzbeitrag, Rücklagen, Bundeszuschuss, beitragspflichtige Einnahmen je Mitglied, Verwaltungskosten je Versicherten — jeweils Zeitreihe und amtliche Fundstelle","grenze":"keine Fortschreibung über das letzte veröffentlichte Jahr hinaus"},{"id":"R02","domaene":"Versorgungsstrukturen","liefergegenstand":"Betten, Fälle, Leistungsgruppen, Stand der Krankenhausreform je Land, Vorhaltefinanzierung, MVZ-Zahlen, ambulante Sitze","grenze":"Landesrecht ist uneinheitlich; Unterschiede benennen, nicht mitteln"},{"id":"R03","domaene":"Gesundheitspersonal und Bezugsgrößen","liefergegenstand":"Beschäftigte und Vollkräfte nach Berufsgruppe, Ausbildungszahlen, Abbruchquoten, Altersstruktur, Anerkennung ausländischer Abschlüsse, offene Stellen — dazu verbindlich: eine disjunkte Zerlegung der Vollkräfte auf die hundert Felder, je Feld mit Fundstelle und Zuordnungsart `primaer` / `geteilt mit <Feld>` / `unbekannt`, sowie der nicht abgedeckte Rest","grenze":"Vollkräfte und Köpfe nie vermischen; Felder ohne amtliche VZÄ-Zahl als `unbekannt` liefern statt schätzen; bei Überschneidung **entscheiden**, nicht beiden zuschlagen — die Entscheidung ist zu begründen"},{"id":"R04","domaene":"KI in der Versorgung","liefergegenstand":"zugelassene Produkte, DiGA-Verzeichnis, Studienlage zu Wirksamkeit, Erstattungstatbestände, reale Einsatzquoten statt Planwerte","grenze":"Pilotprojekt ist kein Regelbetrieb; beides trennen"},{"id":"R05","domaene":"Recht und Regulierung","liefergegenstand":"SGB V und XI, KHVVG, MDR, EU AI Act mit Fristen, § 203 StGB, § 80 SGB X, Haftungsrecht — jeweils Stand und angekündigte Änderung","grenze":"Gesetzentwürfe als Entwürfe kennzeichnen, Konjunktiv"},{"id":"R06","domaene":"Digitale Infrastruktur","liefergegenstand":"Telematikinfrastruktur, ePA-Nutzung, E-Rezept-Volumen, Interoperabilitätsstandards, KIS-Marktanteile, KRITIS-Vorgaben","grenze":"Anschlussquote ist nicht Nutzungsquote"},{"id":"R07","domaene":"Europäischer Systemvergleich","liefergegenstand":"Niederlande, Dänemark, Frankreich, Estland, Vereinigtes Königreich: Finanzierungsform, Digitalisierungsstand, KI-Einsatz, Personalschlüssel","grenze":"Systemunterschiede vor Kennzahlvergleich; keine Rangliste"},{"id":"R08","domaene":"Makroökonomie, öffentliche Finanzen und Szenariogerüste","liefergegenstand":"BIP, Lohnquote, Abgabenquote, Beitragsbemessungsgrenzen, Steuerquote, Demografieprojektionen, Erwerbspersonenpotenzial — dazu mit R01 und R05 zwei gegensätzliche Szenariogerüste 2031 (A Fortschreibung, B Gegenwelt), je mit BIP-Pfad, Erwerbspersonenpotenzial, Beitragssatzkorridor, Tarifentwicklung, Zinsniveau und Rechtsstand von EU AI Act, MDR, EHDS und Krankenhausreform","grenze":"Projektionen als Projektionen kennzeichnen; beide Gerüste müssen sich in mehreren Größen **gegenläufig** unterscheiden, sonst misst die Gerüstabhängigkeit nichts; beide sind Setzungen und als solche zu kennzeichnen"},{"id":"R09","domaene":"Compute, Energie, Souveränität","liefergegenstand":"Rechenzentrumsleistung, Netzanschlusswarteschlangen, Industriestrompreis, EU-Anteil an Inferenzkapazität, AI Gigafactories","grenze":"angekündigte Kapazität ist nicht gebaute Kapazität"},{"id":"R10","domaene":"Geopolitik und Lieferketten","liefergegenstand":"Wirkstoff- und Medizinprodukteimporte nach Herkunft, Exportkontrolle, Engpassmeldungen, Abhängigkeiten bei KI-Hardware","grenze":"Konzentrationsmaße nennen, nicht Einzelanekdoten"}]
const KONTROLLARM = ['A05', 'B07', 'C04', 'D01', 'E06', 'G03', 'H02', 'J02', 'K01', 'L01']

// Welche Faktenblaetter eine Bank sieht
const BLAETTER = {
  A: ['R02', 'R03', 'R04', 'R06'], B: ['R02', 'R03', 'R04', 'R06'],
  C: ['R02', 'R03', 'R04'],        D: ['R01', 'R03', 'R05'],
  E: ['R04', 'R05', 'R10'],        F: ['R03', 'R05'],
  G: ['R02', 'R04', 'R06'],        H: ['R01', 'R02', 'R05'],
  I: ['R05', 'R06'],               J: ['R01', 'R03', 'R08'],
  K: ['R07', 'R09', 'R05'],        L: ['R04', 'R06', 'R09'],
  M: ['R09', 'R10'],               N: ['R01', 'R08'],
}
const EUROPA = ['K', 'L', 'M']

const ANKER = {
  substitution_zuerst:
    'ANKER: Halten Sie sich zuerst vor Augen, wie weit Sprachmodelle und Automatisierung in Ihrem Feld bereits heute kommen - und erst danach, was sie nicht koennen.',
  gegenevidenz_zuerst:
    'ANKER: Halten Sie sich zuerst vor Augen, was in Ihrem Feld bisher jeder Automatisierung standgehalten hat - und erst danach, wo sie vorangekommen ist.',
}

/* ------------------------------------------------ Runde 0: Recherchebank */

phase('Recherche')

const S_FAKT = {
  type: 'object',
  properties: {
    kennzahlen: {
      type: 'array', minItems: 6, maxItems: 14,
      items: {
        type: 'object',
        properties: {
          groesse: { type: 'string' }, wert: { type: 'string' }, einheit: { type: 'string' },
          stand: { type: 'string' }, quelle: { type: 'string' }, fundstelle: { type: 'string' },
        },
        required: ['groesse', 'wert', 'einheit', 'stand', 'quelle', 'fundstelle'],
      },
    },
    luecken: { type: 'array', items: { type: 'string' }, description: 'Groessen, zu denen keine belastbare Quelle gefunden wurde' },
    hinweis: { type: 'string', description: 'Was beim Lesen dieser Zahlen zu beachten ist' },
  },
  required: ['kennzahlen', 'luecken', 'hinweis'],
}

const faktenblaetter = await pipeline(RECH, (r) => agent(
`Du bist Rechercheur ${r.id} der Szenariokonferenz 2031. Du hast KEINE Interessenlage, keine Meinung und keine Stimme. Du lieferst geprueftes Material, auf dem hundert Rollen anschliessend rechnen.

DEINE DOMAENE: ${r.domaene}
DEIN LIEFERGEGENSTAND: ${r.liefergegenstand}
DEINE AUSDRUECKLICHE GRENZE: ${r.grenze}

Recherchiere und liefere ein kompaktes Kennzahlenblatt: sechs bis vierzehn Groessen, jede mit Wert, Einheit, Stand, tatsaechlich abgerufener Quelle und Fundstelle.

Regeln, die ueber allem stehen:
- Rufe jede Quelle wirklich ab. Erfinde keine Zahl und keine Fundstelle.
- Nenne den Stand (Jahr oder Stichtag) zu JEDER Zahl. Eine Zahl ohne Stand ist wertlos.
- Fortschreibungen ueber das letzte veroeffentlichte Jahr hinaus sind nicht dein Auftrag.
- Was du nicht findest, kommt in "luecken" - nicht in "kennzahlen".
- Beachte deine Grenze oben. Sie ist keine Empfehlung.`,
  { label: `Faktenblatt ${r.id}`, phase: 'Recherche', schema: S_FAKT }
).then(f => ({ id: r.id, domaene: r.domaene, ...f })))

const FB = {}
for (const f of faktenblaetter.filter(Boolean)) FB[f.id] = f
log(`Recherchebank: ${Object.keys(FB).length} von ${RECH.length} Faktenblaettern, ${Object.values(FB).reduce((n, f) => n + f.kennzahlen.length, 0)} Kennzahlen`)

function blatt(id) {
  const f = FB[id]
  if (!f) return ''
  return `FAKTENBLATT ${id} - ${f.domaene}\n` +
    f.kennzahlen.map(k => `  ${k.groesse}: ${k.wert} ${k.einheit} (Stand ${k.stand}) [${k.quelle}, ${k.fundstelle}]`).join('\n') +
    (f.luecken.length ? `\n  LUECKEN: ${f.luecken.join('; ')}` : '') +
    `\n  HINWEIS: ${f.hinweis}`
}

/* ------------------------------------- Runde 0a und 0b: Zerlegung, Gerueste */

phase('Grundlagen')

const S_ZERL = {
  type: 'object',
  properties: {
    felder: {
      type: 'array', minItems: 100, maxItems: 100,
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          bezugsgruppe: { type: 'string', description: 'die Menschen, fuer die diese Rolle spricht' },
          vzae: { type: 'number', description: 'Vollzeitaequivalente; 0 wenn unbekannt' },
          zuordnung: { type: 'string', enum: ['primaer', 'geteilt', 'unbekannt'] },
          geteilt_mit: { type: 'string' },
          quelle: { type: 'string' },
        },
        required: ['id', 'bezugsgruppe', 'vzae', 'zuordnung', 'quelle'],
      },
    },
    rest_vzae: { type: 'number', description: 'Vollkraefte im deutschen Gesundheitswesen, die kein Feld dieses Rosters abdeckt' },
    rest_begruendung: { type: 'string' },
  },
  required: ['felder', 'rest_vzae', 'rest_begruendung'],
}

const S_GER = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    annahmen: {
      type: 'array', minItems: 8, maxItems: 12,
      items: {
        type: 'object',
        properties: { groesse: { type: 'string' }, wert: { type: 'string' }, begruendung: { type: 'string' } },
        required: ['groesse', 'wert', 'begruendung'],
      },
    },
  },
  required: ['name', 'annahmen'],
}

const rollenliste = ROLLEN.map(r => `${r.id} | ${r.rolle} | Bank ${r.bank}: ${r.bankName}`).join('\n')

const [zerlegung, geruestA, geruestB] = await parallel([
  () => agent(
`Du bist R03, Rechercheur fuer Gesundheitspersonal. Dein Auftrag ist die schwierigste Lieferung des ganzen Laufs: eine DISJUNKTE Zerlegung der Vollkraefte auf hundert Felder.

${blatt('R03')}

DIE HUNDERT FELDER:
${rollenliste}

Weise jedem Feld seine Bezugsgruppe in Vollzeitaequivalenten zu. Entscheidend ist die Disjunktheit: JEDE Vollkraft gehoert genau EINEM Feld.

- Wo zwei Felder ueber dieselben Menschen sprechen (etwa eine Klinikleitung und eine Pflegekraft derselben Station, oder ein Verband und seine Mitglieder), weise die Vollkraefte EINEM Feld als "primaer" zu und dem anderen als "geteilt" mit Nennung des Feldes. Nur "primaer" geht spaeter in die Gesamtsumme ein. ENTSCHEIDE - schlage nicht beiden zu.
- Felder, die ueber das gesamte Gesundheitswesen oder die Gesamtwirtschaft sprechen (Bank J, K, M), sind fast immer "geteilt".
- Felder ohne amtliche Zahl: vzae 0 und zuordnung "unbekannt". Schaetze nicht.
- Nenne zu jeder Zahl die Quelle. Vollkraefte und Koepfe nie vermischen.
- Gib am Ende den Rest an: Vollkraefte im deutschen Gesundheitswesen, die KEIN Feld dieses Rosters abdeckt.

Genau hundert Eintraege, einer je Feld-ID.`,
    { label: 'VZAE-Zerlegung', phase: 'Grundlagen', schema: S_ZERL }),

  () => agent(
`Du bist R08 gemeinsam mit R01 und R05. Lege das SZENARIOGERUEST A - FORTSCHREIBUNG fuer das Stichjahr 2031 fest.

${blatt('R08')}

${blatt('R01')}

${blatt('R05')}

Geruest A ist die Welt, in der die amtlichen Projektionen eintreten: Die Krankenhausreform wird wie beschlossen umgesetzt, der Rechtsrahmen gilt zum angekuendigten Termin, keine Rezession.

Acht bis zwoelf Annahmen mit Wert und kurzer Begruendung, mindestens zu: realem BIP-Pfad, Erwerbspersonenpotenzial, allgemeinem GKV-Beitragssatz, Tarifentwicklung im Gesundheitswesen, Zinsniveau, Stand der Krankenhausreform nach KHVVG, Vollzug des EU AI Act, Vollzug der MDR, Stand des EHDS.

Das Geruest ist eine SETZUNG, keine Prognose. Es muss in sich schluessig sein - ein Beitragssatz ohne passende Ausgabenentwicklung ist es nicht.`,
    { label: 'Szenariogeruest A', phase: 'Grundlagen', schema: S_GER }),

  () => agent(
`Du bist R08 gemeinsam mit R01 und R05. Lege das SZENARIOGERUEST B - GEGENWELT fuer das Stichjahr 2031 fest.

${blatt('R08')}

${blatt('R01')}

${blatt('R05')}

Geruest B ist die Gegenwelt zu einer Fortschreibung: schwaecheres Wachstum mit Rezessionsjahren, schnellerer Beitragssatzanstieg mit Leistungskuerzungen in der Debatte, Krankenhausreform in Teilen gescheitert oder landesweise auseinanderlaufend, verzoegerter Vollzug des EU-Rechts, EHDS nicht im Regelbetrieb, hoehere Zinsen.

Acht bis zwoelf Annahmen zu denselben Groessen wie Geruest A, damit beide vergleichbar sind.

ENTSCHEIDEND: B muss sich von A in MEHREREN Groessen GEGENLAEUFIG unterscheiden, nicht nur in einer. Sonst misst die Geruestabhaengigkeit nichts. Auch B muss in sich schluessig sein.`,
    { label: 'Szenariogeruest B', phase: 'Grundlagen', schema: S_GER }),
])

const ZERL = {}
for (const f of (zerlegung?.felder || [])) ZERL[f.id] = f
const gedeckt = Object.values(ZERL).filter(f => f.zuordnung === 'primaer')
log(`Zerlegung: ${Object.keys(ZERL).length} Felder, davon ${gedeckt.length} primaer mit ${gedeckt.reduce((n, f) => n + (f.vzae || 0), 0).toLocaleString('de-DE')} VZAE; nicht abgedeckter Rest ${(zerlegung?.rest_vzae || 0).toLocaleString('de-DE')}`)

function geruesttext(g) {
  if (!g) return '(Geruest fehlt)'
  return `SZENARIOGERUEST ${g.name}\n` + g.annahmen.map(a => `  ${a.groesse}: ${a.wert} - ${a.begruendung}`).join('\n')
}
const GER = { A: geruesttext(geruestA), B: geruesttext(geruestB) }

/* --------------------------------------------------------- Runde 1 */

phase('Runde 1')

const HEMMNISSE = 'Recht und Zulassung | Refinanzierung und Abrechnung | Haftung | Personalbindung und Tarif | Investitionsfaehigkeit | Akzeptanz von Patienten oder Beschaeftigten | Datenverfuegbarkeit'
const ENGPAESSE = 'Technik | Daten | Recht | bedienendes Personal | Entscheidung'
const BESCHAFFUNG = 'frei beschaffbar | Vergaberecht | Auftragsverarbeitung nach § 80 SGB X | Zulassung oder Zertifizierung noetig | Entscheidung der Selbstverwaltung | faktisch nicht beschaffbar'

const S_R1 = {
  type: 'object',
  properties: {
    position: { type: 'string' }, falsifikator: { type: 'string' },
    befunde: {
      type: 'array', minItems: 3, maxItems: 5,
      items: { type: 'object', properties: { aussage: { type: 'string' }, quelle: { type: 'string' }, fundstelle: { type: 'string' } }, required: ['aussage', 'quelle', 'fundstelle'] },
    },
    p1_rechenweg: { type: 'string' }, p1: { type: 'number' }, p1_intervall: { type: 'array', items: { type: 'number' }, minItems: 2, maxItems: 2 },
    p2_rechenweg: { type: 'string' }, p2: { type: 'number' }, p2_hemmnis: { type: 'string' },
    p3_rechenweg: { type: 'string' }, p3: { type: 'number' }, p3_absolut_vzae: { type: 'number' },
    p3_null_rechenweg: { type: 'string' }, p3_null: { type: 'number' },
    p4_ki: { type: 'number' }, p4_demografie: { type: 'number' }, p4_strukturreform: { type: 'number' }, p4_begruendung: { type: 'string' },
    p5_leistungserbringer: { type: 'number' }, p5_preis_beitrag: { type: 'number' }, p5_abfluss_ausland: { type: 'number' }, p5_neue_leistung: { type: 'number' }, p5_begruendung: { type: 'string' },
    a1_beschaffung: { type: 'string' }, a1_norm: { type: 'string' },
    a2_erbringerbudget: { type: 'number' }, a2_verwaltungskosten: { type: 'number' }, a2_erloestatbestand: { type: 'number' }, a2_foerdermittel: { type: 'number' }, a2_kein_topf: { type: 'number' }, a2_begruendung: { type: 'string' },
    a3_engpass: { type: 'string' }, a3_zweitnennung: { type: 'string' }, a3_woran_sichtbar: { type: 'string' },
    e1_jahre: { type: 'number' }, e1_vergleichsstaat: { type: 'string' }, e2_eu_anteil: { type: 'number' }, e3_regelung: { type: 'string' }, e_begruendung: { type: 'string' },
    bezugsgroesse_bestritten: { type: 'string', description: 'leer lassen, wenn die vorgegebene VZAE-Zahl akzeptiert wird; sonst Gegenwert mit Fundstelle' },
    geruest_einwand: { type: 'string' },
  },
  required: ['position', 'falsifikator', 'befunde', 'p1_rechenweg', 'p1', 'p1_intervall', 'p2_rechenweg', 'p2', 'p2_hemmnis',
    'p3_rechenweg', 'p3', 'p3_absolut_vzae', 'p3_null_rechenweg', 'p3_null', 'p4_ki', 'p4_demografie', 'p4_strukturreform', 'p4_begruendung',
    'p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung', 'p5_begruendung',
    'a1_beschaffung', 'a1_norm', 'a2_erbringerbudget', 'a2_verwaltungskosten', 'a2_erloestatbestand', 'a2_foerdermittel', 'a2_kein_topf', 'a2_begruendung',
    'a3_engpass', 'a3_zweitnennung', 'a3_woran_sichtbar', 'bezugsgroesse_bestritten', 'geruest_einwand'],
}

function promptR1(r) {
  const z = ZERL[r.id] || { bezugsgruppe: '(von R03 nicht geliefert)', vzae: 0, zuordnung: 'unbekannt' }
  const blaetter = (BLAETTER[r.bank] || []).map(blatt).filter(Boolean).join('\n\n')
  const eu = EUROPA.includes(r.bank)
  return `Du bist im Rollendossier: ${r.rolle} (${r.id}, Bank ${r.bank}: ${r.bankName}).
MANDAT, das dein Urteil faerben darf und soll: ${r.mandat}
WISSENSANKER: ${r.anker}
BLINDSTELLE, dir mitgeteilt, damit die Auswertung sie pruefen kann - du sollst sie NICHT kompensieren: ${r.blindstelle}

${ANKER[r.anker_reihenfolge]}

DEINE BEZUGSGRUPPE, von R03 vorgegeben: ${z.bezugsgruppe} = ${z.vzae} Vollzeitaequivalente, Zuordnungsart "${z.zuordnung}"${z.geteilt_mit ? ` (geteilt mit ${z.geteilt_mit})` : ''}.
Rechne gegen diese Zahl. Haeltst du sie fuer falsch, nenne im Feld "bezugsgroesse_bestritten" deinen Gegenwert mit Fundstelle - und rechne trotzdem gegen die vorgegebene.

${GER[r.geruest]}

Rechne alle Groessen gegen dieses Geruest. Haeltst du es fuer falsch, sag das in "geruest_einwand" - und rechne trotzdem dagegen.

${blaetter ? `MATERIAL DER RECHERCHEBANK:\n\n${blaetter}\n` : ''}
DIE PFLICHTGROESSEN, Stichjahr 2031. Erst der Rechenweg, dann das Ergebnis. Der Rechenweg muss den Wert aus der Bezugsgruppengroesse reproduzieren - jemand rechnet ihn nach.

P1: Anteil der heute in DEINEM Feld geleisteten Arbeitszeit, der bis 2031 technisch durch KI oder Automatisierung ersetzbar ist, unabhaengig davon ob es geschieht. Prozent 0-100.
P2: Anteil VON P1, der bis 2031 im Regelbetrieb tatsaechlich wirksam wird. Prozent von P1. Nenne das bindende Hemmnis aus: ${HEMMNISSE}
P3: Veraenderung des Personal-BEDARFS bis 2031, in Prozent der VZAE deiner Bezugsgruppe (-100 bis +50) UND in absoluten VZAE. Arbeitszeit, die wegfaellt, ist nicht dasselbe wie Personalbedarf, der wegfaellt.
P3_NULL: dieselbe Groesse unter der Gegenannahme, dass KI und Automatisierung bis 2031 STAGNIEREN - nur Demografie, Recht und Strukturreform wirken.
P4: Ursachenanteil an P3, drei Prozentwerte mit Summe genau 100: KI und Automatisierung / Demografie / Struktur- und Rechtsreform.
P5: Verbleib des Effizienzgewinns, vier Prozentwerte mit Summe genau 100: bleibt beim Leistungserbringer / weitergegeben als Preis oder Beitragssatz / abgeflossen als Lizenz-, Geraete- oder Cloudentgelt ueberwiegend ausserhalb Deutschlands / finanziert zusaetzliche Leistung im eigenen Feld.

Gegenprobe, vor dem Antworten nachrechnen: |P3 - P3_NULL| geteilt durch (|P3 - P3_NULL| + |P3_NULL|) muss zu deinem P4-Wert fuer KI passen, Toleranz 15 Punkte.

DIE MARKTGROESSEN - ob in deinem Feld ueberhaupt ein Markt entsteht:
A1: Darf und kann in deinem Feld 2031 eine Leistung von AUSSEN eingekauft werden? Waehle aus: ${BESCHAFFUNG}. Nenne die konkrete Norm oder Vertragsform.
A2: Aus welchem Topf wuerde sie 2031 bezahlt? Fuenf Prozentwerte mit Summe genau 100: laufendes Budget des Leistungserbringers / Verwaltungskosten des Kostentraegers / gesetzlich gesetzter Erloestatbestand / Foerdermittel oder Projekt / GAR KEIN TOPF. Der letzte Wert ist der wichtigste - rechne ihn nicht klein.
A3: Was ist 2031 in deinem Feld knapper - waehle aus: ${ENGPAESSE}. Erst- und Zweitnennung, dazu woran der Engpass sichtbar wuerde.
${eu ? `
DIE EUROPAEISCHEN VERGLEICHSGROESSEN - nur deine Bank beantwortet sie:
E1: Abstand Deutschlands zum am weitesten fortgeschrittenen der fuenf Vergleichsstaaten (Niederlande, Daenemark, Frankreich, Estland, Vereinigtes Koenigreich) in DEINEM Gegenstand, 2031. Jahre, -8 bis +8, negativ heisst Rueckstand. Nenne den Vergleichsstaat.
E2: Anteil der Wertschoepfung deines Gegenstands, der 2031 INNERHALB der EU entsteht. Prozent.
E3: Welche EU-Regelung wirkt in deinem Gegenstand bis 2031 staerker als jede nationale? EU AI Act / MDR-IVDR / EHDS / DSGVO / Beihilfe- und Vergaberecht / keine.
` : ''}
QUELLENPFLICHT: Drei bis fuenf Befunde, jeder mit einer Quelle, die du tatsaechlich abgerufen hast, samt Fundstelle. Erfinde keine. Findest du nichts, schreibe "keine Quelle gefunden".

Recherchiere zuerst in DEINEM Feld - nicht in der Gesamtwirtschaft. Dann antworte.`
}

const ITEMS = ROLLEN.map(r => ({ r, kontroll: false }))
  .concat(ROLLEN.filter(r => KONTROLLARM.includes(r.id)).map(r => ({ r, kontroll: true })))

const roh = await pipeline(ITEMS, (it) => agent(promptR1(it.r), {
  label: it.kontroll ? `R1 ${it.r.id} (Kontrollarm)` : `R1 ${it.r.id}`,
  phase: 'Runde 1', schema: S_R1, model: it.kontroll ? 'sonnet' : undefined,
}).then(a => ({ ...it, antwort: a })))

const haupt = roh.filter(Boolean).filter(x => !x.kontroll)
const kontroll = roh.filter(Boolean).filter(x => x.kontroll)
const luecken = ITEMS.length - roh.filter(Boolean).length
log(`Runde 1: ${haupt.length} Rollen, ${kontroll.length} Kontrollarm, ${luecken} Ausfaelle`)

/* ---------------------------------------- Gesetzte Fehler und Validierung */

const FREMDQUELLE = 'Bundesagentur fuer Arbeit, Fachkraefteengpassanalyse 2024, S. 17'
const MANDATSBRUCH = ' Dieselbe Einschaetzung gilt unveraendert auch fuer die Zahnmedizin, die Veterinaermedizin und den Rettungsdienst.'

const gesetzt = []
const vorgelegt = haupt.map((x, i) => {
  const a = JSON.parse(JSON.stringify(x.antwort))
  const m = i % 10
  if (m === 0) { a.p1 = Math.round(a.p1 * 3 + 7); gesetzt.push({ rolle: x.r.id, wo: 'p1', art: 'Zahl passt nicht mehr zum Rechenweg' }) }
  if (m === 3) { a.p3_absolut_vzae = Math.round(a.p3_absolut_vzae * 4); gesetzt.push({ rolle: x.r.id, wo: 'p3', art: 'absolute VZAE passen nicht zum Prozentwert' }) }
  if (m === 6 && a.befunde[0]) { a.befunde[0].quelle = FREMDQUELLE; a.befunde[0].fundstelle = 'S. 17'; gesetzt.push({ rolle: x.r.id, wo: 'befund_1', art: 'Quelle deckt die Aussage nicht' }) }
  if (m === 8) { a.position = a.position + MANDATSBRUCH; gesetzt.push({ rolle: x.r.id, wo: 'position', art: 'Rolle spricht ausserhalb ihres Mandats' }) }
  return { r: x.r, a }
})
log(`${gesetzt.length} Fehler in ${new Set(gesetzt.map(g => g.rolle)).size} von ${haupt.length} Kartensaetzen gesetzt`)

phase('Validierung')

const WO = ['position', 'befund_1', 'befund_2', 'befund_3', 'befund_4', 'befund_5', 'p1', 'p2', 'p3', 'p3_null', 'p4', 'p5', 'a1', 'a2', 'a3']
const S_VAL = {
  type: 'object',
  properties: {
    beanstandungen: {
      type: 'array',
      items: {
        type: 'object',
        properties: { wo: { type: 'string', enum: WO }, was: { type: 'string' }, schwere: { type: 'string', enum: ['zurueckgewiesen', 'mit-vorbehalt'] } },
        required: ['wo', 'was', 'schwere'],
      },
    },
    rechenweg_traegt: { type: 'array', items: { type: 'string', enum: ['p1', 'p2', 'p3', 'p3_null'] } },
  },
  required: ['beanstandungen', 'rechenweg_traegt'],
}

function kartentext(r, a) {
  return `ROLLE ${r.id}: ${r.rolle} (Bank ${r.bank})
MANDAT: ${r.mandat}
BEZUGSGRUPPE: ${(ZERL[r.id] || {}).bezugsgruppe || '?'} = ${(ZERL[r.id] || {}).vzae || 0} VZAE

POSITION: ${a.position}
FALSIFIKATOR: ${a.falsifikator}

${a.befunde.map((b, i) => `BEFUND_${i + 1}: ${b.aussage}\n  Quelle: ${b.quelle} | Fundstelle: ${b.fundstelle}`).join('\n')}

P1 Rechenweg: ${a.p1_rechenweg}
P1 Wert: ${a.p1} %
P2 Rechenweg: ${a.p2_rechenweg}
P2 Wert: ${a.p2} % von P1, Hemmnis: ${a.p2_hemmnis}
P3 Rechenweg: ${a.p3_rechenweg}
P3 Wert: ${a.p3} % = ${a.p3_absolut_vzae} VZAE
P3_NULL Rechenweg: ${a.p3_null_rechenweg}
P3_NULL Wert: ${a.p3_null} %
P4: KI ${a.p4_ki} / Demografie ${a.p4_demografie} / Strukturreform ${a.p4_strukturreform}
P5: Erbringer ${a.p5_leistungserbringer} / Preis-Beitrag ${a.p5_preis_beitrag} / Abfluss ${a.p5_abfluss_ausland} / neue Leistung ${a.p5_neue_leistung}
A1: ${a.a1_beschaffung} - ${a.a1_norm}
A2: Erbringerbudget ${a.a2_erbringerbudget} / Verwaltungskosten ${a.a2_verwaltungskosten} / Erloestatbestand ${a.a2_erloestatbestand} / Foerdermittel ${a.a2_foerdermittel} / kein Topf ${a.a2_kein_topf}
A3: ${a.a3_engpass}, zweitens ${a.a3_zweitnennung}`
}

const pruef = await pipeline(vorgelegt, (v) => agent(
`Du bist Pruefinstanz. Du pruefst EINEN Kartensatz - genau, nicht wohlwollend. Du hast kein eigenes Urteil zur Sache.

Pruefe vier Dinge und melde JEDE Beanstandung einzeln mit ihrem Ort. Melde nichts, was in Ordnung ist. Ist alles in Ordnung, gib eine leere Liste zurueck.

1. EXISTENZ: Gibt es die angegebene Quelle? Rufe sie ab.
2. DECKUNG: Traegt die Quelle die Aussage, die mit ihr belegt wird? Eine existierende Quelle, die etwas anderes sagt, ist eine Beanstandung.
3. MANDATSTREUE: Spricht die Rolle nur ueber ihr eigenes Feld? Aussagen ueber fremde Felder sind zu beanstanden. ABER: P1 bis P5 und A1 bis A3 sind Pflichtfragen, die JEDE Rolle beantworten muss - sie sind niemals ein Mandatsbruch, auch wenn sie ueber das engste Fachgebiet hinausreichen.
4. RECHENWEGHALTBARKEIT: Reproduziert jeder Rechenweg den genannten Wert aus der genannten Bezugsgroesse? Rechne nach. Ein Prozentwert, der nicht zur absoluten VZAE-Zahl passt, ist eine Beanstandung. Pruefe die Gegenprobe |P3 - P3_NULL| / (|P3 - P3_NULL| + |P3_NULL|) gegen den P4-KI-Wert, Toleranz 15 Punkte. Pruefe, ob P4, P5 und A2 jeweils auf 100 summieren.

Urteile kartenweise. Ein Fehler in einem Befund macht die Pflichtgroessen nicht ungueltig.

${kartentext(v.r, v.a)}`,
  { label: `Pruefung ${v.r.id}`, phase: 'Validierung', schema: S_VAL, model: 'sonnet' }
).then(p => ({ id: v.r.id, ...p })))

const pruefungen = pruef.filter(Boolean)
const gefunden = gesetzt.filter(g => {
  const p = pruefungen.find(x => x.id === g.rolle)
  return p && p.beanstandungen.some(b => b.wo === g.wo)
})
log(`Pruefschaerfe: ${gefunden.length} von ${gesetzt.length} gesetzten Fehlern gefunden (${Math.round(gefunden.length / Math.max(gesetzt.length, 1) * 100)} %)`)

/* ------------------------------------- Streitindex in beiden Varianten */

function quant(xs, p) {
  const s = [...xs].sort((a, b) => a - b), i = (s.length - 1) * p, lo = Math.floor(i), hi = Math.ceil(i)
  return lo === hi ? s[lo] : s[lo] + (s[hi] - s[lo]) * (i - lo)
}
const iqr = xs => quant(xs, .75) - quant(xs, .25)
const FLOOR = { p1: 5, p2: 5, p3: 3, d: 0.10 }
const durchgriff = a => { const z = a.p1 * a.p2 / 100; return z ? Math.abs(a.p3 - a.p3_null) / z : 0 }

function index(gegenBank) {
  const W = haupt.map(x => ({ id: x.r.id, bank: x.r.bank, a: x.antwort, d: durchgriff(x.antwort) }))
  const alle = k => W.map(x => k === 'd' ? x.d : x.a[k])
  const M4 = ['p4_ki', 'p4_demografie', 'p4_strukturreform'].map(k => quant(alle(k), .5))
  const M5 = ['p5_leistungserbringer', 'p5_preis_beitrag', 'p5_abfluss_ausland', 'p5_neue_leistung'].map(k => quant(alle(k), .5))
  return W.map(x => {
    let s = 0
    for (const k of ['p1', 'p2', 'p3', 'd']) {
      const menge = gegenBank ? W.filter(y => y.bank === x.bank) : W
      const v = menge.map(y => k === 'd' ? y.d : y.a[k])
      const wert = k === 'd' ? x.d : x.a[k]
      s += Math.abs(wert - quant(v, .5)) / Math.max(iqr(v), FLOOR[k])
    }
    const v4 = [x.a.p4_ki, x.a.p4_demografie, x.a.p4_strukturreform]
    const v5 = [x.a.p5_leistungserbringer, x.a.p5_preis_beitrag, x.a.p5_abfluss_ausland, x.a.p5_neue_leistung]
    s += (0.5 * v4.reduce((n, v, i) => n + Math.abs(v - M4[i]), 0)) / 8
    s += (0.5 * v5.reduce((n, v, i) => n + Math.abs(v - M5[i]), 0)) / 8
    return { id: x.id, bank: x.bank, streitindex: Math.round(s * 1000) / 1000 }
  }).sort((a, b) => b.streitindex - a.streitindex)
}

const idxBank = index(true), idxPanel = index(false)
function auswahl(idx) {
  const proBank = {}
  for (const x of idx) if (!proBank[x.bank]) proBank[x.bank] = x.id
  const quote = Object.values(proBank)
  return quote.concat(idx.filter(x => !quote.includes(x.id)).slice(0, 30 - quote.length).map(x => x.id))
}
const aBank = auswahl(idxBank), aPanel = auswahl(idxPanel)
const ueberschneidung = aBank.filter(i => aPanel.includes(i)).length
log(`Streitauswahl: Bankmedian und Panelmedian stimmen in ${ueberschneidung} von 30 Rollen ueberein - ${30 - ueberschneidung} Unterschiede`)

return {
  faktenblaetter: faktenblaetter.filter(Boolean),
  zerlegung, geruestA, geruestB,
  runde1: haupt.map(x => ({ id: x.r.id, bank: x.r.bank, geruest: x.r.geruest, anker: x.r.anker_reihenfolge, ...x.antwort })),
  kontrollarm: kontroll.map(x => ({ id: x.r.id, ...x.antwort })),
  gesetzte_fehler: gesetzt,
  pruefungen,
  pruefschaerfe: { gesetzt: gesetzt.length, gefunden: gefunden.length, nicht_gefunden: gesetzt.filter(g => !gefunden.includes(g)) },
  streitindex_bank: idxBank, streitindex_panel: idxPanel,
  auswahl_bank: aBank, auswahl_panel: aPanel, auswahl_ueberschneidung: ueberschneidung,
  ausfaelle: luecken,
}

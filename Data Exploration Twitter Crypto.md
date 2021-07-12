**Twitter Sentiment Analyse für Cryptowährung Dogecoin**

**Prüfungsleistung Data Exploration Project**

im Studiengang WWI-19DSB

an der Dualen Hochschule Baden-Württemberg Mannheim


von

**Luca Fenucciu**

**Kilian Ebi**

**Miguel Sarasa-y-Zimmermann**

**Sebastian Hildenbeutel**




Abgabedatum 12.07.2021
# **Projektbeschreibung**
Für die Prüfungsleistung der Vorlesung „Data Exploration Project“ wird von der Gruppe eine Sentimentanalyse in Bezug auf die Tweets bezüglich der Cryptowährung Dogecoin durchgeführt. Hierzu bezieht die Gruppe einen geeigneten Datensatz mit Hilfe der Twitter API. Dieser Datensatz wird von der Gruppe bereinigt und zur Verarbeitung vorbereitet. 

Für die Durchführung einer Sentimentanalyse wird ein Modell zur Vorhersage des Sentiments trainiert. Als Trainingsdaten dienen Trainings-Tweets des nltk Pakets in Python. Das Modell wird von der Gruppe gemäß den Machine Learning Standards trainiert, evaluiert und optimiert.
# **Umsetzung**
## **Datenbeschaffung**
Es gibt einige Voraussetzungen für das Beschaffen der Twitter Daten mit einem eigenen Zuagang zur Twitter API.
1. Erstellen eines Twitter Developer accounts, um überhaupt die notwendigen Berechtigungen zu erlangen über die Twitter API Tweets ziehen zu können.
2. Nachdem der access zur Twitter API von Twitter gewährleistet wurde, muss eine App in dem Twitter Developer interface initialisiert werden. 
3. Beim Initialisieren der APP werden einem direkt die Auth tokens und die API access tokens generiert und angezeigt, diese unbedingt sofort speicher, da sie sonst neu generiert werden müssen. 

Im Folgenden werden Befehle zur Installierung von Kafka Servern und den notwendigen Packages in der Syntax von Ubuntu Linux OS beschrieben, der Prozess ändert sich allerdings nicht mit einem anderen OS. 
- Python3 Installation (für die Ausführung des Scripts)
	'apt install python3'

- pip Installation (zum Installieren von Packages)
	'apt install python3-pip'

- Tweepy Installation (Package speziell um Twitterdatenmanipulation in Python zu vereinfachen)
	'pip install tweepy'

- Kafka Installation (Server Kontaktpunkt kommuniziert mit der Twitter API und requested streamed Data nach welcher im Script gefragt wird)
	'pip install kafka-python'

- Python Twitter installation (Python Interface für die Twitter API)
	'pip install python-twitter'

Damit sind alle Voraussetzungen erfüllt.

Wir benötigen in den nächsten Schritten mehrere command line interfaces, denn wir möchten sowohl unseren Kafka Server, als auch unseren listener im hintergrund parallel zum Script ausführen.

- window 1: 
	zookeeper server: (zur Verwaltung und der Orchestrierung von eingehenden Daten und ausgehenden queries 'Management-tool')
	  ./bin/zookeeper-server-start.sh -daemon config/zookeeper.properties (start des Zookeeper servers)

	kafka server: (Datenstromzugang Verbindung mit unseren gewünschten Tweets, erleichtert durch aufbereitung nachfolgende analyse)
  	  ./bin/kafka-server-start.sh config/server.properties

- window 2: 
	topic creation:
	  ./bin/kafka-topics.sh --create --bootstrap-server 192.168.***.***:9092 --replication-factor 1 --partitions 1 --topic cardano

	output file creation: (Text-Datei, in welcher wir unsere Daten speichern für die Weiterverarbeitung)
	  ./bin/kafka-console-consumer.sh --bootstrap-server 192.168.***.***:9092 --topic doge --from-beginning > cryptodoge.txt

Bearbeiten der Server.properties file um die richtigen listener zu definieren
Geräte IP eingeben an Stelle des Listerners (mit welcher ip wird verbunden) Verbindung zum Bootstrap Server Eingabe der eigenen IP mit Port, welcher im Fall von Kafka meist 9092 ist

- window 3:
	run python: (Scriptausführung hier geben wir an was wir genau wollen und wie wir es beziehen (sprich Server configs und Schlüsselwörter), außerdem verifizieren wir uns gegenüber Twitter am Anfang nach den Package Imports)
    	  python3 Tweets.py .

Tweets werden daraufhin in der hierfür angelegten Datei mit Json syntax gespeichert. 
Link zu unserer VM umgebung: https://drive.google.com/file/d/1zEigml1mJAgY2jle0-eTY0Pw3vBQvy5C/view?usp=sharing

## **Datenverarbeitung**
## **Erstellung des Modells**
## **Auswertung**
<img src="https://github.com/Slurbisaur/CryptoSentiment/blob/main/Data/Plots.PNG" width="100" height="100">
# **Fazit und Ausblick**
Die Durchführung des Projekts hat mehrere Probleme einer Sentimentanalyse im Bezug auf Tweets offenbart. Ein Problem ist, dass ein Machine Learning Algorithmus Sarkasmus, Memes und Humor nur schlecht erkennen kann. Dadurch können manche Tweets durch den Algorithmus nicht richtig zugeordnet werden. Des Weiteren ist es in diesem Modell nicht möglich Bilder zu interpretieren, was bedeutet, dass viele Tweets nicht analysiert werden können.

Die Gruppe sieht in dem Modell Potential. Das Modell kann noch erweitert werden, um beispielsweise Bilder noch zu erkennen und Sarkasmus auch teilweise besser interpretieren zu können. Dies ist aufgrund der begrenzten Durchführungszeit allerdings noch nicht möglich gewesen. Im Bezug auf den wirtschaftlichen Nutzen ist es möglich mit dem Modell das Sentiment in Korrelation zu dem aktuellen Kurs zu setzen. Hierzu ist es möglich eine Webapp zu programmieren in dem automatisch täglichen Tweet gezogen werden und das Sentiment automatisch analysiert wird. Dies wiederum bietet dann die Möglichkeit durch die dadurch gewonnen Erkenntnissen ein Modell zur Vorhersage des Kurses zu trainieren.

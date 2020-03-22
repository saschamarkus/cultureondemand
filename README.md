# cultureondemand

## Backend
Das Backend bietet eine einfache REST-API zum Abfragen von Angeboten (offers) http://127.0.0.1:5000/api/v1/offers oder eines einzelnen Angebots http://127.0.0.1:5000/api/v1/offer/3

### Installation
Einrichten des virtuellen Enviroments

`python3 -m venv venv-backend`

`source venv-backend/bin/activate`

`pip install -r requirements.txt`

`pip install -e .`

### Initiallisieren des Systems
`cultureondemand db upgrade`

`cultureondemand init`

### Starten des Servers
`uwsgi --http 127.0.0.1:5000 --module cultureondemand.wsgi:app`

### Aufräumen der DB
`rm /tmp/cultureondemand.db`
Und dann bei "Initialisieren des Systems" wieder beginnen.

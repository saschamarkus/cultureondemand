from cultureondemand.extensions import db

durations = {
    1: "Kürzer als 5 Minuten",
    2: "15-30 Minuten",
    3: "30-45 Minuten",
    4: "45-60 Minuten",
    5: "Mehr als 60 Minuten",
}

interactivity_levels = {
    1: "Inaktiv ohne direkten Kontakt (kein Video)",
    2: "Inaktiv, aber direkter Kontakt: Video Call",
    3: "Leicht interaktiv (an einigen Stellen ist User:innen-Input gefragt)",
    4: "Interaktiv: User:innen Input ist gefragt.",
    5: "Ko-kreativ: Beide schaffen etwas zusammen",
}

emotions = {
    "ÜBERRASCHT": ["Erschrocken", "Verwirrt", "Erstaunt", "Aufgeregt"],
    "FROH": [
        "Verspielt",
        "Zufrieden",
        "Interessiert",
        "Stolz",
        "Akzeptierend",
        "Karftvoll",
        "Friedlich",
        "Vertrauensvoll",
        "Optimistisch",
    ],
    "TRAURIG": [
        "Einsam",
        "Verletzlich",
        "Verzweifelt",
        "Schuldig",
        "Deprimiert",
        "Verletzt",
    ],
    "ANGEWIDERT": ["Abgestoßen", "Schrecklich", "Enttäuscht", "Missbilligend"],
    "WÜTEND": [
        "Kritisch",
        "Distanziert",
        "Frustriert",
        "Aggressiv",
        "Wütend",
        "Bitter",
        "Gedemütigt",
        "Alleingelassen",
    ],
    "ÄNGSTLICH": [
        "Erschreckt",
        "Abgelehnt",
        "Schwach",
        "Unsicher",
        "Änsgtlich",
        "Erschrocken",
    ],
    "BAD": ["Gelangweilt", "Beschäftigt", "Gestresst", "Müde"],
}


class Offer(db.Model):
    """Basic user model
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    user = db.Column(db.String(80), unique=False, nullable=False)
    media = db.Column(db.String(80), unique=False, nullable=True)
    emotion = db.Column(db.String(80), unique=False, nullable=False)
    experience = db.Column(db.String(255), nullable=False)
    paid_content = db.Column(db.Boolean, default=False)
    interactivity = db.Column(db.Integer, unique=False, nullable=False)
    duration = db.Column(db.Integer,  unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(Offer, self).__init__(**kwargs)

    def __repr__(self):
        return "<Offer %s>" % self.title

import click
from flask.cli import FlaskGroup

from cultureondemand.app import create_app


def create_cultureondemand(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_cultureondemand)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from cultureondemand.extensions import db
    from cultureondemand.models import User
    from cultureondemand.models import Offer

    click.echo("create user")
    user = User(
        username="admin",
        email="admin@cultureondemand.com",
        password="admin",
        active=True,
    )
    db.session.add(user)

    offer = Offer(
        id=1,
        title="Bügeln mit Sascha",
        user="admin",
        experience="Haushaltsgerät",
        interactivity=2,
        duration=2,
        emotion="BAD:Gelangweilt",
        media="twitch"
    )
    db.session.add(offer)
    offer = Offer(
        id=2,
        title="Wie war Dein Tag?",
        user="admin",
        experience="Talk",
        duration=3,
        interactivity=4,
        emotion="HAPPY:Vertrauensvoll",
        media="zoom,hangout"
    )
    db.session.add(offer)
    offer = Offer(
        id=3,
        title="Schrei alles raus",
        user="admin",
        experience="Personal teaching/coaching",
        duration=3,
        interactivity=4,
        emotion="WÜTEND",
        media="zoom,hangout,youtube"
    )
    db.session.add(offer)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()

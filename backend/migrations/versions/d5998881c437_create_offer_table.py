"""create offer table

Revision ID: d5998881c437
Revises: 
Create Date: 2020-03-22 00:27:25.419357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5998881c437'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('user', sa.String(length=80), nullable=False),
    sa.Column('media', sa.String(length=80), nullable=True),
    sa.Column('emotion', sa.String(length=80), nullable=False),
    sa.Column('experience', sa.String(length=255), nullable=False),
    sa.Column('paid_content', sa.Boolean(), nullable=True),
    sa.Column('interactivity', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('token_blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('token_type', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token_blacklist')
    op.drop_table('user')
    op.drop_table('offer')
    # ### end Alembic commands ###

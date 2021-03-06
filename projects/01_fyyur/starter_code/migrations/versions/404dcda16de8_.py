"""empty message

Revision ID: 404dcda16de8
Revises: 118aaa72b554
Create Date: 2021-02-16 19:46:28.603416

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '404dcda16de8'
down_revision = '118aaa72b554'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('Venue_id', sa.Integer(), nullable=False),
    sa.Column('Artist_id', sa.Integer(), nullable=False),
    sa.Column('Start_time', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['Venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('Venue_id', 'Artist_id', 'Start_time')
    )
    op.drop_table('shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('Venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], name='shows_Artist_id_fkey'),
    sa.ForeignKeyConstraint(['Venue_id'], ['Venue.id'], name='shows_Venue_id_fkey'),
    sa.PrimaryKeyConstraint('Venue_id', 'Artist_id', 'Start_time', name='shows_pkey')
    )
    op.drop_table('Shows')
    # ### end Alembic commands ###

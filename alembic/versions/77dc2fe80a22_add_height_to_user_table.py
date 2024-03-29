"""Add height to user table

Revision ID: 77dc2fe80a22
Revises: d701d7d281f9
Create Date: 2023-05-12 14:24:36.767928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77dc2fe80a22'
down_revision = 'd701d7d281f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('height', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'height')
    # ### end Alembic commands ###

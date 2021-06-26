"""Cursos added

Revision ID: 5306684eba94
Revises: 7399e3cc6a76
Create Date: 2021-06-02 15:16:34.805703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5306684eba94'
down_revision = '7399e3cc6a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('id_profesor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_profesor'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curso')
    # ### end Alembic commands ###
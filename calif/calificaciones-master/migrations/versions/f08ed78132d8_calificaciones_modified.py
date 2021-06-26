"""Calificaciones modified

Revision ID: f08ed78132d8
Revises: d20b8f3474e5
Create Date: 2021-06-11 16:05:55.290529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f08ed78132d8'
down_revision = 'd20b8f3474e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calificaciones', sa.Column('id_tarea', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'calificaciones', type_='foreignkey')
    op.create_foreign_key(None, 'calificaciones', 'tarea', ['id_tarea'], ['id'])
    op.drop_column('calificaciones', 'id_curso')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calificaciones', sa.Column('id_curso', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'calificaciones', type_='foreignkey')
    op.create_foreign_key(None, 'calificaciones', 'curso', ['id_curso'], ['id'])
    op.drop_column('calificaciones', 'id_tarea')
    # ### end Alembic commands ###
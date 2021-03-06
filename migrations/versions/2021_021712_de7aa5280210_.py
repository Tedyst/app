"""empty message

Revision ID: de7aa5280210
Revises: 85d0655d42c0
Create Date: 2021-02-17 12:43:51.154170

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de7aa5280210'
down_revision = '85d0655d42c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alias', sa.Column('original_owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'alias', 'users', ['original_owner_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'alias', type_='foreignkey')
    op.drop_column('alias', 'original_owner_id')
    # ### end Alembic commands ###

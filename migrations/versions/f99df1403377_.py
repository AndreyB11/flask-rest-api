"""empty message

Revision ID: f99df1403377
Revises: cf25e4209769
Create Date: 2023-03-02 16:38:01.670997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99df1403377'
down_revision = 'cf25e4209769'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
                              existing_type=sa.REAL(),
                              type_=sa.Float(precision=2),
                              existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
                              existing_type=sa.Float(precision=2),
                              type_=sa.REAL(),
                              existing_nullable=False)

    # ### end Alembic commands ###

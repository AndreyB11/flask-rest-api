"""empty message

Revision ID: e3857ee15687
Revises: f99df1403377
Create Date: 2023-03-04 15:11:36.676304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3857ee15687'
down_revision = 'f99df1403377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('store_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('store_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###

"""initial

Revision ID: f81a52604f78
Revises: 690dc26a8591
Create Date: 2023-03-02 17:36:46.427539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f81a52604f78'
down_revision = '690dc26a8591'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions_action', sa.Column('action_url', sa.VARCHAR(length=255), nullable=True))
    op.drop_column('permissions_action', 'action')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions_action', sa.Column('action', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('permissions_action', 'action_url')
    # ### end Alembic commands ###

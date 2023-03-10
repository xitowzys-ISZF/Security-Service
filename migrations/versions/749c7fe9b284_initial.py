"""initial

Revision ID: 749c7fe9b284
Revises: f81a52604f78
Create Date: 2023-03-02 18:37:20.899985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749c7fe9b284'
down_revision = 'f81a52604f78'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions_action', sa.Column('method', sa.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('permissions_action', 'method')
    # ### end Alembic commands ###

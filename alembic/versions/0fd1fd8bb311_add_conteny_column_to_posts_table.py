"""add conteny column to posts table

Revision ID: 0fd1fd8bb311
Revises: ff6ef8be7ca3
Create Date: 2021-12-28 10:03:16.001604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd1fd8bb311'
down_revision = 'ff6ef8be7ca3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

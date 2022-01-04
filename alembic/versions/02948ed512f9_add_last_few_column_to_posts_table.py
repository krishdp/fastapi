"""add last few column to posts table

Revision ID: 02948ed512f9
Revises: e3149857fc84
Create Date: 2021-12-28 10:47:55.489805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02948ed512f9'
down_revision = 'e3149857fc84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

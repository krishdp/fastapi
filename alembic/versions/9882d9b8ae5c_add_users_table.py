"""add users table

Revision ID: 9882d9b8ae5c
Revises: 0fd1fd8bb311
Create Date: 2021-12-28 10:08:14.792870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9882d9b8ae5c'
down_revision = '0fd1fd8bb311'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass

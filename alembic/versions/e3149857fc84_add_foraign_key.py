"""add foraign key

Revision ID: e3149857fc84
Revises: 9882d9b8ae5c
Create Date: 2021-12-28 10:17:43.908043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3149857fc84'
down_revision = '9882d9b8ae5c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols = ['owner_id'], remote_cols=['id'], ondelete = "CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass

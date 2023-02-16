"""add content column to post table

Revision ID: a7a1ffb43262
Revises: c95550a68e69
Create Date: 2023-02-16 13:57:29.412752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a1ffb43262'
down_revision = 'c95550a68e69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

"""add user table

Revision ID: 84eda07f1759
Revises: a7a1ffb43262
Create Date: 2023-02-16 14:04:12.692859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84eda07f1759'
down_revision = 'a7a1ffb43262'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

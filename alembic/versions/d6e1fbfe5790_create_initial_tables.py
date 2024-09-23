"""Create initial tables

Revision ID: d6e1fbfe5790
Revises:
Create Date: 2024-09-23 14:52:54.568342

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy import Boolean, DateTime, Enum, String

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d6e1fbfe5790"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "api_key",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("application_name", String(length=255), nullable=False),
        sa.Column("plan", Enum("FREE", "BASIC", "PREMIUM", name="planenum"), nullable=False),
        sa.Column("api_key", String(length=255), nullable=False),
        sa.Column("created_at", DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("api_key"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", String(length=255), nullable=False),
        sa.Column("password", String(length=255), nullable=False),
        sa.Column("api_key_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["api_key_id"], ["api_key.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "user_email",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("encoded_email", String(), nullable=False),
        sa.Column("token", String(), nullable=False),
        sa.Column("created_at", DateTime(), nullable=True),
        sa.Column("is_verified", Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("user_email")
    op.drop_table("users")
    op.drop_table("api_key")

    op.execute("DROP TYPE IF EXISTS planenum")

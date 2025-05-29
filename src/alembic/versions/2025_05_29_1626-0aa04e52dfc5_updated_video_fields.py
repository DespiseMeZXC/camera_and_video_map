"""updated video fields

Revision ID: 0aa04e52dfc5
Revises: 0ce9374b0944
Create Date: 2025-05-29 16:26:42.508536

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0aa04e52dfc5"
down_revision: str | None = "0ce9374b0944"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "video",
        sa.Column("name", sa.String(), nullable=False, comment="Название видео"),
    )
    op.add_column(
        "video",
        sa.Column(
            "data_updated",
            sa.DateTime(),
            nullable=False,
            comment="Дата обновления",
        ),
    )
    op.drop_column("video", "data_created")
    op.drop_column("video", "mame")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "video",
        sa.Column(
            "mame",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment="Название видео",
        ),
    )
    op.add_column(
        "video",
        sa.Column(
            "data_created",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
            comment="Дата создания",
        ),
    )
    op.drop_column("video", "data_updated")
    op.drop_column("video", "name")

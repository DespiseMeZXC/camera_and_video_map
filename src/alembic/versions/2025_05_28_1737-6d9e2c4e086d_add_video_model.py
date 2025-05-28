"""add video model

Revision ID: 6d9e2c4e086d
Revises: d34141ff3565
Create Date: 2025-05-28 17:37:42.554574

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6d9e2c4e086d"
down_revision: str | None = "d34141ff3565"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "video",
        sa.Column("id", sa.UUID(), nullable=False, comment="Идентификатор"),
        sa.Column("mame", sa.String(), nullable=False, comment="Название видео"),
        sa.Column("duration", sa.Integer(), nullable=False, comment="Длительность"),
        sa.Column(
            "video_resolution",
            sa.String(),
            nullable=False,
            comment="Разрешение видео",
        ),
        sa.Column(
            "fps",
            sa.Integer(),
            nullable=False,
            comment="Количество кадров в секунду",
        ),
        sa.Column("time_of_day", sa.String(), nullable=False, comment="Время суток"),
        sa.Column(
            "tracing",
            sa.Boolean(),
            nullable=False,
            comment="Готовность рассчета",
        ),
        sa.Column("author", sa.String(), nullable=False, comment="Автор"),
        sa.Column("counter", sa.Integer(), nullable=False, comment="Кол-во расчётов"),
        sa.Column(
            "date_created",
            sa.DateTime(),
            nullable=False,
            comment="Дата создания",
        ),
        sa.Column(
            "camera_id",
            sa.UUID(),
            nullable=False,
            comment="Идентификатор камеры",
        ),
        sa.ForeignKeyConstraint(
            ["camera_id"],
            ["d_camera.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("video")

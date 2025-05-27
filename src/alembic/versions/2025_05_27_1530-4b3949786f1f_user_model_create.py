"""user model create

Revision ID: 4b3949786f1f
Revises: 67962fd63d63
Create Date: 2025-05-27 15:30:47.962063

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4b3949786f1f"
down_revision: str | None = "67962fd63d63"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "d_user",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            comment="Идентификатор пользователя",
        ),
        sa.Column("full_name", sa.String(), nullable=True, comment="ФИО"),
        sa.Column("email", sa.String(), nullable=True, comment="Email"),
        sa.Column("password", sa.String(), nullable=True, comment="Пароль"),
        sa.Column("is_active", sa.Boolean(), nullable=True, comment="Активен"),
        sa.Column(
            "date_created",
            sa.DateTime(),
            nullable=True,
            comment="Дата и время добавления записи в таблицу (техн.)",
        ),
        sa.Column(
            "date_updated",
            sa.DateTime(),
            nullable=True,
            comment="Дата и время обновления записи в таблицу (техн.)",
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("d_user")

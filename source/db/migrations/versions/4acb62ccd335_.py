"""empty message

Revision ID: 4acb62ccd335
Revises: 
Create Date: 2021-07-02 15:07:37.486263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4acb62ccd335"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "members",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "account_id", sa.Integer(), sa.Identity(always=False), nullable=False
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "payment_methods",
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("payment_method_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("account_id", "payment_method_id"),
    )


def downgrade():
    op.drop_table("payment_methods")
    op.drop_table("members")

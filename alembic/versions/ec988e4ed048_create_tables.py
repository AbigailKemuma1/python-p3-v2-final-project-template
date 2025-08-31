"""create tables

Revision ID: ec988e4ed048
Revises: 
Create Date: 2025-08-31 03:18:51.890062
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ec988e4ed048'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('age', sa.Integer, nullable=True),
        sa.Column('height', sa.Float, nullable=True),
        sa.Column('weight', sa.Float, nullable=True),
        sa.Column('fitness_goal', sa.String, nullable=True),
        sa.Column('is_admin', sa.Boolean, nullable=True),
    )

    # Create meals table
    op.create_table(
        'meals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('calories', sa.Float, nullable=True),
        sa.Column('protein', sa.Float, nullable=True),
        sa.Column('carbs', sa.Float, nullable=True),
        sa.Column('fats', sa.Float, nullable=True),
    )

    # Create admins table
    op.create_table(
        'admins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
    )

    # Create goals table
    op.create_table(
        'goals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('goal_type', sa.String, nullable=False),
        sa.Column('target', sa.String, nullable=True),
        sa.Column('deadline', sa.String, nullable=True),
        sa.Column('status', sa.String, nullable=True),
        sa.Column('progress_date', sa.DateTime, nullable=True),
        sa.Column('progress_weight', sa.Float, nullable=True),
        sa.Column('progress_notes', sa.String, nullable=True),
    )

    # Create workouts table
    op.create_table(
        'workouts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('workout_type', sa.String, nullable=False),
        sa.Column('duration', sa.Float, nullable=True),
        sa.Column('calories_burned', sa.Float, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('workouts')
    op.drop_table('goals')
    op.drop_table('admins')
    op.drop_table('meals')
    op.drop_table('users')

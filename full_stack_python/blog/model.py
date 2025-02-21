import reflex as rx
from sqlmodel import Field
import sqlalchemy as sa
from datetime import datetime, timezone


class BlogPostModel(rx.Model, table=True):
    """ You'd need to add these lines to __init__.py for reflex makemigrations to work
        
        from .model import BlogPostModel

        __all__ = [
            "BlogPostModel",
        ]

        The import blog in the main app file, that is full_stack_python.py.
    """
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={
            "onupdate": sa.func.now(),
            "server_default": sa.func.now()
        },
        nullable=False,
    )
    # pulish_date
    # publish_time
    
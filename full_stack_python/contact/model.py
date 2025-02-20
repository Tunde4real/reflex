from typing import Optional

from sqlmodel import Field
from datetime import datetime, timezone
import sqlalchemy as sa

import reflex as rx


''' After creating your db model as in 
        class ContactEntryModel(rx.model):
            first_name: str
            last_name: str
            email: str
            message: str
    you will then run the following commands:
        reflex db init
        reflex db makemigrations
        reflex migrate
    
    databse table is still not created yet. add true to class definition line like
        class ContactEntryModel(rx.Model, table=True):
    then run:
        reflex db makemigrations
        reflex migrate
    to save changes.


'''


class ContactEntryModel(rx.Model, table=True):
    """Whenever you change anything here, run:
    'reflex db makemigrations' and 'reflex migrate' to update the database table.
    """
    user_id: Optional[int] = None
    first_name: str
    last_name: Optional[str] = None  # Nullable field using Optional
    email: Optional[str] = Field(nullable=True)  # Nullable field using Field
    message: str
    # message: str = Field(default="No message provided")  # Default value using Field
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
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


class ContactEntryModel(rx.Model, table=True):      #rx.Model not rx.model
    ''' Whenever you change anything here, you should run "reflex db makemigrations" and "reflex migrate" to update the database table.
    '''
    user_id: int | None = None
    first_name: str
    last_name: str | None = None        # first way to declare nullable field
    email: str  = Field(nullable=True)  # second way to declare nullable field
    message: str
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sa.func.now(),
        },
        nullable=False
    )

from typing import List
from sqlmodel import select

import reflex as rx
import asyncio
from .model import ContactEntryModel


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    # timeleft: int = 5
    entries: List['ContactEntryModel'] = []
    

    # @rx.var
    # def timeleft_label(self) -> str:
    #     if self.timeleft < 1:
    #         return "No time left"
    #     return f"{self.timeleft} seconds left"

    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get('first_name') or ""
        return f"Thanks {first_name} for your message"

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        data = {}
        for k, v in form_data.items():
            if v == '' or v is None:
                continue
            data[k] = v

        with rx.session() as session:
            db_entry = ContactEntryModel(**data)
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield   # ensure the data is saved and session is closed

        # handles the clearing away of thank you message after submittion
        yield
        await asyncio.sleep(2)
        self.did_submit=False
        yield
    
    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries=entries

    # async def start_timer(self):
    #     while self.timeleft > 0:
    #         await asyncio.sleep(1)
    #         self.timeleft -= 1
    #         yield
 

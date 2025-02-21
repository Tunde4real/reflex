import reflex as rx 
from ..ui.base import base_page
from .state import ContactState
from . import form, model


def contact_entry_list_item(contact: model.ContactEntryModel):
    return rx.table.row(
            rx.table.cell(contact.first_name, align="center"),
            rx.table.cell(contact.last_name, align="center"),
            rx.table.cell(contact.email, align="center"),
            rx.table.cell(contact.message, align="center"),
            rx.table.cell(contact.created_at, align="center"),
        )                       # be careful of not putting comma here
    return rx.box(
        rx.hstack(
            rx.text(contact.first_name),
            rx.text(contact.last_name),
            rx.text(contact.email),
            rx.text(contact.message),
            rx.text(contact.created_at),
            spacing="5",
            padding='1em',
            align="center",
            width="100%",
        )
    )


def contact_entries_list_page() -> rx.Component:
    """ 
    """
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("First name", align="center"),
                        rx.table.column_header_cell("Last name", align="center"),
                        rx.table.column_header_cell("Email", align="center"),
                        rx.table.column_header_cell("Message", align="center"),
                        rx.table.column_header_cell("CreatedAt", align="center"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(ContactState.entries, contact_entry_list_item),
                ),
            ),
            spacing="5",
            padding='5em',
            align="center",
            min_height="85vh",
        )
    )

# @rx.page(
#         # on_load=ContactState.start_timer, 
#         route=routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    """ 
    """
    # my_form = form.contact_form()
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            # rx.text(ContactState.timeleft_label),
            rx.cond(ContactState.did_submit, ContactState.thank_you, ''),  # type of last two arguments must be same, or last argument can be blank
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width='50vw'        # means 50% of the width of the view port
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.contact_form(),
                    width='75vw'        # means 75% of the width of the view port
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.contact_form(),
                    width='95vw'        # means 75% of the width of the view port
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align = "center",
            min_height="85vh",
        )
    return base_page(my_child)


import reflex as rx 
from ..ui.base import base_page
from ..navigation import routes


@rx.page(route=routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    """ Represents the front end. Anything returned is gonna appear
    """
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.text(
                "Send us a message",
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align = "center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)

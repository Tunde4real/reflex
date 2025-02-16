
import reflex as rx 
from ..ui.base import base_page

def about_page() -> rx.Component:
    """ Represents the front end. Anything returned is gonna appear
    """
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something cool about us",
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align = "center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)

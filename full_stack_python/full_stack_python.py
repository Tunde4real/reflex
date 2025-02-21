"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page
# from .pages.about import about_page
from . import pages, navigation, contact


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_title_input_change(self, val):
        self.label = val
    
    def did_click(self):
        print("Hey I just clicked on something")
        return rx.redirect(navigation.routes.ABOUT_US_ROUTE)    # redirect to about page


def index() -> rx.Component:
    """ Represents the front end. Anything returned is gonna appear
    """
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),

            # rx.button("About Us", on_click=rx.redirect('/about')),
            # rx.button("About Us", on_click=State.did_click),            # still not the best way
            rx.link(
                rx.button("About Us"), 
                href=navigation.routes.ABOUT_US_ROUTE
            ),

            # rx.input(default_value=State.label,
            #          on_click = State.did_click,
            #          on_change = State.handle_title_input_change),       
            # rx.link(
            #     rx.button("Check out our docs!"),
            #     href="https://reflex.dev/docs/getting-started/introduction/",
            #     is_external=True,
            # ),

            spacing="5",
            justify="center",
            align="center",
            text_align = "center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)  #To use like pages.about_page is why we have the code in init.py of pages folder
app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(
    contact.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries,
)




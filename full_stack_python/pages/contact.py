
import reflex as rx 
from ..ui.base import base_page
from ..navigation import routes


class ContactState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data



@rx.page(route=routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    """ Represents the front end. Anything returned is gonna appear
    """
    my_form = rx.form(
                rx.vstack(
                        rx.hstack(
                            rx.input(
                                name="first_name",      # better to put name first
                                placeholder="First Name",
                                required=True,
                                type='text',     #default so not puting type means it's text type
                                width='100%',
                            ),
                            rx.input(
                                name="last_name",
                                placeholder="Last Name",
                                type='text',
                                width='100%',
                            ),
                            width='100%',
                        ),
                        rx.input(
                            name="Email",
                            type="email",
                            placeholder="your email",
                            width='100%',
                        ),
                        rx.text_area(
                            name="Message",
                            placeholder="Your Message",
                            required=True,
                            width='100%',
                        ),
                        rx.button("Submit", type="submit"),
                    ),
                    on_submit=ContactState.handle_submit,
                    reset_on_submit=True,   # clears out the inputed text on submit
                )
    
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'        # means 50% of the width of the view port
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
                    width='75vw'        # means 50% of the width of the view port
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align = "center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)

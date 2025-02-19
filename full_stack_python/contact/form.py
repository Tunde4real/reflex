import reflex as rx 
from .state import ContactState


def contact_form() -> rx.Component:
    """ 
    """
    return  rx.form(
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
                    height='100%',
                )

# import reflex as rx 
# from ..ui.base import base_page
# from ..navigation import routes
# from ..contact import ContactState
# from ..contact import form

# @rx.page(
#         # on_load=ContactState.start_timer, 
#         route=routes.CONTACT_US_ROUTE)
# def contact_page() -> rx.Component:
#     """ 
#     """
#     # my_form = form.contact_form()
#     my_child = rx.vstack(
#             rx.heading("Contact Us", size="9"),
#             # rx.text(ContactState.timeleft_label),
#             rx.cond(ContactState.did_submit, ContactState.thank_you, ''),  # type of last two arguments must be same, or last argument can be blank
#             rx.desktop_only(
#                 rx.box(
#                     form.contact_form(),
#                     width='50vw'        # means 50% of the width of the view port
#                 )
#             ),
#             rx.tablet_only(
#                 rx.box(
#                     form.contact_form(),
#                     width='75vw'        # means 75% of the width of the view port
#                 )
#             ),
#             rx.mobile_only(
#                 rx.box(
#                     form.contact_form(),
#                     width='95vw'        # means 75% of the width of the view port
#                 )
#             ),
#             spacing="5",
#             justify="center",
#             align="center",
#             text_align = "center",
#             min_height="85vh",
#             id="my-child",
#         )
#     return base_page(my_child)

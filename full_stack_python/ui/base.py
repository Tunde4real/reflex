import reflex as rx
from .nav import navbar

def base_page(child: rx.Component, hide_navbar=False, *args, **Kwargs) -> rx.Component:
    """ Just a base image for all pages
    """
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")
        
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="top-right"),    
        )
    
    return rx.fragment(     # fragment renders nothing (doesn't render a div), loosens things up a bit
        navbar(),
        rx.box(
            child,
            padding = "1em",
            width="100%",
            id="my-content-area-el"
        ),
        # rx.logo(),
        rx.color_mode.button(position="bottom-left")
    )
    
    
# rx.container kind of works like a div with some predetermined attributes which you can then edit the 
# attributes or add new ones
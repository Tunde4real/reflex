import reflex as rx 
from ..ui.base import base_page
from .state import BlogPostState
from . import model
from .. import navigation



def blog_post_detail_link(child: rx.Component, post: model.BlogPostModel):
    '''
    '''
    if post is None:
        return rx.fragment(child)
    
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    return rx.link(
        child, 
        href=post_detail_url
    )


def blog_post_list_item(post: model.BlogPostModel):
    return rx.table.row(
            rx.table.cell(
                blog_post_detail_link(post.title, post),
                align="center"
            ),
            rx.table.cell(post.content, align="center"),
            rx.table.cell(post.created_at, align="center"),
            rx.table.cell(post.updated_at, align="center"),
        )                       # be careful of not putting comma here


def blog_post_list_page() -> rx.Component:
    """ 
    """
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="5"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Title", align="center"),
                        rx.table.column_header_cell("Content", align="center"),
                        rx.table.column_header_cell("CreatedAt", align="center"),
                        rx.table.column_header_cell("UpdatedAt", align="center"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(BlogPostState.posts, blog_post_list_item),
                ),
            ),
            spacing="5",
            padding='5em',
            align="center",
            min_height="85vh",
        )
    )

from typing import List, Optional
from sqlmodel import select


import reflex as rx
from .model import BlogPostModel

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            )
            self.posts = result.all()

    # def get_post(self, post_id):
    #     pass

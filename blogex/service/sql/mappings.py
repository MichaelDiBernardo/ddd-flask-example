from sqlalchemy import ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import mapper, relationship
from models import *

def init(db):
    user_mapping = db.Table('user',
        db.Column('username', String(50), primary_key=True),
        db.Column('email', String(100)),
        db.Column('password', String(100)),
    )

    post_mapping = db.Table('post',
        db.Column('id', Integer, primary_key=True),
        db.Column('title', String(200)),
        db.Column('text', Text()),
        db.Column('post_date', DateTime(), nullable=False),
        db.Column('author', String(50), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
    )

    db.mapper(BlogexUser, user_mapping, properties={
        'posts' : relationship(Post, backref='user', order_by=post_mapping.c.post_date.desc())
    })

    db.mapper(Post, post_mapping)

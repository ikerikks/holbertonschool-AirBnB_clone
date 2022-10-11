#!/usr/bin/python3
"""
Define review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define class review"""
    place_id = ""
    user_id = ""
    text = ""

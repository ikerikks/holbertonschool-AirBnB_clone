#!/usr/bin/python3
"""
Define user id
"""
import email
from models.base_model import BaseModel


class User(BaseModel):
    """define a class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

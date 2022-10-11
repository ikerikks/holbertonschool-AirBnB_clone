#!/usr/bin/python3
"""
Define amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define amenity that user can choose from to offer at its place"""
    name = ""

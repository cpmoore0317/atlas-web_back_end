#!/usr/bin/env python3
""" A Python function that inserts a new document in a collection based on kwargs """

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: The fields and values for the new document.

    Returns:
        The _id of the new document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

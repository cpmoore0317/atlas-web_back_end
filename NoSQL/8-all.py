#!/usr/bin/env python3
""" A Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents in the collection. An empty list if no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())

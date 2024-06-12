#!/usr/bin/env python3
""" A Python function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of documents (schools) that have the specified topic.
    """
    return list(mongo_collection.find({ "topics": topic }))

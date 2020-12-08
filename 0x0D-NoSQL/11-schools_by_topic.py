#!/usr/bin/env python3
"""function that returns the list of school having
   a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """query documents in collection"""
    return mongo_collection.find(
        {"topics": topic}
    )

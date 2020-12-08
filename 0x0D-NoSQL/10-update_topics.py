#!/usr/bin/env python3
"""function that changes all topics of a school document based on name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """update documetnt in collection"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

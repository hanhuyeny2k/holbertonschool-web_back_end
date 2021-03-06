#!/usr/bin/env python3
"""function that return all students sorted by avg score"""
import pymongo


def top_students(mongo_collection):
    """return top stop base on their average score"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])

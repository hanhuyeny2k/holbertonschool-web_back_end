#!/usr/bin/env python3
"""function that insert new document"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """return the new _id"""
    return mongo_collection.insert_one(kwargs).inserted_id

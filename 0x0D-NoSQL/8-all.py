#!/usr/bin/env python3
""" function that list all documents"""
import pymongo


def list_all(mongo_collection):
    """return an empty list if no document in the collection"""
    return [doc for doc in mongo_collection.find()]

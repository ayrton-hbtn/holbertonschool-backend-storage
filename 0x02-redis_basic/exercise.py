#!/usr/bin/env python3
"""redis basic"""

import redis
import uuid
from typing import Union


class Cache:
    """class to create a new redis instance and store data into it"""
    def __init__(self):
        """instantiates new redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores new data with unique id into instance"""
        id = str(uuid.uuid4)
        self._redis.set(id, data)
        return id

#!/usr/bin/env python3
"""redis basic"""

import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None):
        """
        take a key string argument and an optional
        Callable argument named fn that will be used
        to convert the data back to the desired format.

        Conserve original get behavior if key doesn't exists
        """
        val = self._redis.get(key)
        if fn is not None:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """parametrize Cache.get to str"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parametrize Cache.get to int"""
        try:
            val = int(self._redis.get(key))
        except ValueError:
            val = 0
        return val

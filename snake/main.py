import time
import collections
import functools
import random
import pygame
import numpy as np
from abc import ABCMeta, abstractmethod
from enum import Enum
from pyparsing import col
from utils import spawn
from config import config


class Block(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass


class Snake:
    def __init__(self, x, y, graph, init_length, is_centered=True, shortcuts=True):
        self.x = x
        self.y = y
        self.graph = graph
        head = self.get_snake_location(is_centered)
        self.queue = collections.deque([head])

        # Once he snake is max_length just chase tail
        self.chase_tail = False

        for _ in range(init_length - 1):
            self.queue.appendleft(self.graph[self.queue[0]])

        self.food = self.spawn_food(x, y)

        self.shortcuts = shortcuts
        self.dist = self.calc_dist(self.food) if shortcuts else collections.defaultdict(int)

    def get_snake_location(self, is_centered: bool):
        return (self.x // 2, self.y // 2) if is_centered else self.spawn_snake(self.x, self.y)

    def spawn_snake(self, x, y):
        return spawn(x, y)

    def spawn_food(self, x, y):
        snake_head = set(self.queue)
        return spawn(x, y, choices=[(i, j) for i in range(x) for j in range(y) if (i, j) not in snake_head])

    @functools.lru_cache(None)
    def calc_dist(self, food):
        """Returns a map of (i, j) -> steps to reach food if following the ham cycle"""
        if self.chase_tail:
            return collections.defaultdict(lambda: self.x * self.y)

        pos = self.graph[food]
        dist = collections.defaultdict(lambda: self.x * self.y)
        dist[food] = 0
        n = self.x * self.y
        steps = 1
        while steps <= n:
            dist[pos] = n - steps
            pos = self.graph[pos]
            steps += 1
        return dist


class Game:
    def __init__(self, **kwargs):
        pygame.init()

        for key in kwargs:
            self.__dict__[key] = kwargs[key]

        self.playground = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.COL_WIDTH = self.WIDTH // self.X
        self.ROW_HEIGHT = self.HEIGHT // self.Y

        self.ham = 


if __name__ == '__main__':
    game = Game(**config)
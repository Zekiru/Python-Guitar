#!/usr/bin/env python3

import random
from math import ceil
from ringbuffer import RingBuffer

SAMP_RATE = 44100
DECAY = 0.996

class GuitarString:
    def __init__(self, frequency: float):
        # Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        self.tick_count = 0
        self.capacity = ceil(SAMP_RATE/frequency)
        self.buffer = RingBuffer(self.capacity)
        for _ in range(self.capacity): self.buffer.enqueue(0)

    @classmethod
    def make_from_array(cls, init: list[int]):
        # Create a guitar string whose size and initial values are given by the array `init`
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        # Set the buffer to white noise
        for _ in range(self.buffer.size()): self.buffer.dequeue()
        for _ in range(self.capacity): self.buffer.enqueue(random.uniform(-0.5, 0.5))

    def tick(self):
        # Advance the simulation one time step by applying the Karplus--Strong update
        sample_1 = self.buffer.dequeue()
        sample_2 = self.buffer.peek()

        self.buffer.enqueue(DECAY * (sample_1 + sample_2) / 2)
        self.tick_count += 1

    def sample(self) -> float:
        # Return the current sample
        return self.buffer.peek()

    def time(self) -> int:
        # Return the number of ticks so far
        return self.tick_count

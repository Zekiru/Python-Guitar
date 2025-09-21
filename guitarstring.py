#!/usr/bin/env python3

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        # TO-DO: implement this
        self.capacity = # TO-DO: compute the max capacity of the ring buffer based on the frequency
        self.buffer =   # TO-DO: construct the ring buffer object

    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this

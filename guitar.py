#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

KEYS = "q2we4r5ty7u8i9op-[=]"
DURATION = 3e5

def clamp_sample(x: float) -> float:
    # clamp into valid float range when playing the sample
    max = 1.0
    min = -max
    if x > max: return max
    elif x < min: return min
    return x

def sample(keymap) -> float:
    # compute the superposition of samples
    return clamp_sample(sum(k.sample() for k in keymap.values()))

def advance(keymap):
    # advance the simulation of each guitar string by one step
    for k in KEYS:
        magnitude = abs(keymap[k].sample())
        if DURATION <= keymap[k].time():
            keymap[k].zero_buffer()
            continue
        if 0 < magnitude: keymap[k].tick()

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    # create dict to relate the characters to the GuitarString Objects
    keymap = {}
    for i, k in enumerate(KEYS):
        frequency = 440 * (1.059463 ** (i - 12))
        keymap[k] = GuitarString(frequency)

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            k = stdkeys.next_key_typed()
            if k != '' and k in KEYS: keymap[k].pluck()

        # play the sample on standard audio
        play_sample(sample(keymap))

        # advance the simulation
        advance(keymap)

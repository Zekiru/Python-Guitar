#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

KEYS = "q2we4r5ty7u8i9op-[=]"
THRESHOLD = 1e-4
TIME = 30000

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keymap = {}
    for i, key in enumerate(KEYS):
        frequency = 440 * (1.059463 ** (i - 12))
        keymap[key] = GuitarString(frequency)

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
            key = stdkeys.next_key_typed()
            if key in keymap:
                keymap[key].pluck()

        # compute the superposition of samples
        sample = sum(key.sample() for key in keymap.values() if key.time() <= TIME and abs(key.sample()) >= THRESHOLD)

        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        for key in keymap.values(): key.tick()

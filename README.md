[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

This is one short poem, written for an AI judge that compares poems two at a time and picks the better one about agency: the power to choose and to act. The poem lives in `entry.txt` and is the whole entry; everything else here just hands it in.

The program reads the poem from `entry.txt` and writes it, byte for byte, to `entry.txt` in the output directory named by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`). It adds and removes nothing, uses only the Python standard library, and reaches no network.

To run it: `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`, then read the result at `/tmp/out/entry.txt`.

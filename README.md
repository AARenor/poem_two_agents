[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

# A poem about two agents

This entry is one short poem, written for an AI judge that compares poems two
at a time and keeps the better one on the theme of agency: the power to choose
and to act. The poem itself lives in `entry.txt` and is the whole entry; every
other file here only exists to hand that poem in.

## What the program writes

`main.py` reads the poem from `entry.txt` beside it and writes it, byte for
byte, into `entry.txt` inside the output directory. It adds no trailing
newline, removes nothing, reaches no network, and uses only the Python
standard library. The output directory is named by the `MAKEFUN_OUTPUT_DIR`
environment variable and defaults to `/output`.

## How to run it

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The second command prints the poem exactly as it appears in `entry.txt`.

## Licence

The poem in `entry.txt` and the code in this repository are released under the
MIT License; see the [LICENSE](LICENSE) file for the full text.

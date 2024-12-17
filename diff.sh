#!/bin/bash
#/ Usage: ./diff.sh [spike|mindstorms]

set -e
set -o nounset

program=mindstorms
ref=refs/heads/programs
if [ $# -gt 0 ] && [ "$1" = spike ]; then
  program=spike
  ref=refs/heads/spike-programs
fi

set -x
exec mind-meld $program diff $ref

#!/bin/bash
#/ Usage: ./diff.sh

set -e
set -o nounset

set -x
exec mind-meld mindstorms diff refs/heads/programs

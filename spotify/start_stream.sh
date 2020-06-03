#!/usr/bin/env bash
if [[ $(ps aux | grep tizonia | awk '{print $0}' | wc -l) = 1 ]]; then
  echo update
  export DISPLAY=:0.0
  coproc tizonia --spotify-playlist-id 1jQlDi7VsAAxWZMkItThlm
else
  echo no
fi
#!/usr/bin/env bash
coproc bluetoothctl
echo -e 'info\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
echo $output
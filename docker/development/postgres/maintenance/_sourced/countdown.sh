#!/usr/bin/env bash

# Coundown Script to Dsiplay Countdown Timer
# it takes number of seconds as first arg, updates in real time till number of seconds has elapsed
# it calc target time in seconds by adding current time obtained using date+%s to the specified number of seconds
# it runs while target time >= current time, to calc time remaining by substracting current time from target time
# it converts to readable hour min sec (HMS) using date command; timer displays on same line as dynamic countdown
# -ne disables newline and enables use of backslash \r as carriage return; sleep puts 0.1s delay betw refresh

countdown(){
  declare desc="Countdown Timer"

  local seconds="${1}"

  local targtm=$(($(date +%s) + "${seconds}"))

  while [ "$targtm" -ge `date +%s` ]; do
  
    echo -ne "$(date -u --date @$(($targtm - `date +%s`)) +%H:%M:%S)\r";

    sleep 0.1
  done

}
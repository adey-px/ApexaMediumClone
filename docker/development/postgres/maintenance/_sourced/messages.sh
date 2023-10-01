#!/usr/bin/env bash

# Define series of bash shell functions to output 
# messages with formatting & styles
# https://linuxhandbook.com/change-echo-output-color/

# Print or create empty new line 
message_newline(){
  echo
}

# Print debug message, ${@} repr all args passed
# should be included in output after DEBUG prefix
message_debug(){
  echo -e "DEBUG: ${@}"
}

# Print welcome message, \e[1m and \e[0m repr 
# ansi escape codes, means show all as bold text
message_welcome(){
  echo -e "\e[1m${@}\e[0m"
}

# Print warning message, change text color to yellow,
# reset it, show output in yellow after Warning prefix
message_warning(){
  echo -e "\e[33mWARNING\e[0m: ${@}" 
}

# Print error message, change text color to red,
# reset it, show output in red after Error prefix
message_error(){
  echo -e "\e[31mERROR\e[0m: ${@}"
}

# Print info message, change text color to gray,
# reset it, show output in gray after Info prefix
message_info(){
  echo -e "\e[37mINFO\e[0m: ${@}"
}

# Print suggestion message, change text color to red,
# reset it, show output in red after Suggestion prefix
message_suggestion(){
  echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

# Print success message, change text color to green,
# reset it, show output in green after Success prefix
message_success(){
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}

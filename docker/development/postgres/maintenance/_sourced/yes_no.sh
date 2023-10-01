#!/usr/bin/env bash

# Yes-No Script to Ask for User to Confirm an Action
# steps: declare description of the function, for documentation purpose
# create local var assigned to first arg passed to the function
# create local var assigned to read user input with a prompt
# check if user response is regex Y or y, then exit with success status

yes_no(){
  declare desc="Prompt for Confirmation. \$\"\{1\}\": confirmation message"

  local arg1="${1}"

  local response= read -r -p "${arg1} (y/[n])? " response

  if [[ "${response}" =~ ^[Yy]$ ]]

  then
    exit 0
  else
    exit 1
  fi
}
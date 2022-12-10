#!/usr/bin/env bash

main() {
  arg=("$@")
  echo $arg
  if [ -z ${array[0]} ]; then
    echo "One for you, one for me."
  else
    printf "One for ${array[0]}, one for me."
  fi
}

main $@

#!/bin/bash

Help ()
{
 # display
  echo "description of the script functions here."
  echo
  echo "Syntax : scriptTemplate [--all|--target|V]"
  echo "options:"
  echo "all displays IP addresses."
  echo "h print this HELP."
  echo "target list of tcp ports"
  echo "V print software version and exit."
  echo
}
#main#
######
#get the option
while getopts ":hat:" option; do
 case $option in
     h) # display HELP
         Help
         exit;;
     a) # ip 
      ifconfig -a
      exit;;
      t) #tcp
      sudo netstat -tnlp
      exit;;
    \?) #Invalid option
   echo "error: invalid option"
    exit;;
 esac
done
echo "hello"


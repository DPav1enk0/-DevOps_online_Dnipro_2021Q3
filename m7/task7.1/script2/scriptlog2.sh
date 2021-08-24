#!/bin/bash

whoami

echo " ips with more requests"
cat apache_logs | awk '{print $1}' | sort | uniq -c | sort -n | tail -n 3

echo " top url pages "
awk -F\" '{print $2}' apache_logs | awk '{print $2}' | sort | uniq -c | sort -n | tail -n 3

echo " top domains "
cat apache_logs | awk '{print $11}'| sort | uniq -c | sort -n | tail -n 3

echo " most request from pages"
cat apache_logs | awk '{print $7}' | sort | uniq -c | sort -g | tail -n 3

echo "each ip requests"
cat apache_logs | awk '{print $1}' | sort | uniq -c | sort -n 
 
echo "404 url"
grep " 404 " apache_logs | cut -d ' ' -f 7 | sort | uniq -c | sort -n | tail  -n 10

echo "404 answer"
cat apache_logs | awk '($9 ~ /404/)' | awk '{ print $7 }' | sort | uniq -c | sort -n | tail -n 10

echo "high load"
cat apache_logs | awk '{print $4}' | sort | uniq | sort -n | tail -n 3

echo "bot agents"
awk -F\" '{print $6}' apache_logs | grep 'bot' | sort | uniq -c | sort -f | tail -n 3

echo "empty agents"
awk -F\" '($6 ~ /^-?$/)' apache_logs | awk '{print $1}' | sort  | uniq 

echo "end" 


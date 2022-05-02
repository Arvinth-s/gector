#!/bin/sh

if [ "$1" == "-h" ]; then
  echo "Usage: `basename $0` \"text message\""
  exit 0
fi

if [ -z "$1" ]
  then
    echo "Add message text as second arguments"
    exit 0
fi

if [ "$#" -ne 1 ]; then
    echo "You can pass only one argument. For string with spaces put it on quotes"
    exit 0
fi

message="$1"
channel_id=`jq -r '.channel_id' credentials/knittsBot.json`
bot_id=`jq -r '.bot_id' credentials/knittsBot.json`

url="https://api.telegram.org/bot${bot_id}/sendMessage?chat_id=${channel_id}&text=${message}" 

curl $url
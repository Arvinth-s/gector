TOKEN=`jq -r '.TOKEN' credentials/api.json`
instance_id=`jq -r '.instance_id' credentials/instances.json`

curl -H "X-Auth-Token: $TOKEN" \
  -X POST "https://api.genesiscloud.com/compute/v1/instances/$instance_id/actions" \
  -H "Content-Type: application/json" \
  --data-binary @- << EOF
{
  "action": "start"
}
EOF

instance=$(curl -H "X-Auth-Token: $TOKEN" \
  "https://api.genesiscloud.com/compute/v1/instances/$instance_id")
x=`echo "$instance" | jq -r '.instance'| jq -r '.status'`
while([[ $x != "active" ]])
do
    sleep 5
    instance=$(curl -H "X-Auth-Token: $TOKEN" \
        "https://api.genesiscloud.com/compute/v1/instances/$instance_id")
    x=`echo "$instance" | jq -r '.instance'| jq -r '.status'`
done

x=`echo "$instance" | jq -r '.instance'| jq -r '.public_ip'`
rm ~/.ssh/config
output=~/.ssh/config
echo "Host spider-gpu" >> ~/.ssh/config
echo "HostName ${x}" >> ~/.ssh/config
echo "User ubuntu" >> ~/.ssh/config

echo "instance started"
./telegram-send.sh "instance-started"
echo -e "\a"
sleep 4
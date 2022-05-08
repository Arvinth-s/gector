TOKEN=`jq -r '.TOKEN' credentials/api.json`
instance_id=`jq -r '.instance_id' credentials/instances.json`


instance=$(curl -H "X-Auth-Token: $TOKEN" \
  "https://api.genesiscloud.com/compute/v1/instances/$instance_id")

# output=instance-ip.txt
# echo "$instance" | jq -r '.instance' | jq -r '.public_ip' >> instance-ip.txt

x=`echo "$instance" | jq -r '.instance'| jq -r '.public_ip'`

rm ~/.ssh/config

output=~/.ssh/config
echo "Host spider-gpu" >> ~/.ssh/config
echo "HostName ${x}" >> ~/.ssh/config
echo "User ubuntu" >> ~/.ssh/config

sleep 2
TOKEN=`jq -r '.TOKEN' credentials/api.json`
instance_id=`jq -r '.instance_id' credentials/instances.json`

curl -H "X-Auth-Token: $TOKEN" \
  -X POST "https://api.genesiscloud.com/compute/v1/instances/$instance_id/actions" \
  -H "Content-Type: application/json" \
  --data-binary @- << EOF
{
  "action": "stop"
}
EOF
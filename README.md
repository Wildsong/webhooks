# webhooks

Listen to whatever comes in and append it to requests.json.

I have to run this in a Docker because it has to be reverse proxied, ArcGIS will not accept a self-signed certificate.

## Environment


### Deploy

```bash
docker-compose up -d
```


Don't use docker swarm for this because it's behind the proxy.


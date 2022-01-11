# webhooks

Listen to whatever comes in and dump it to the console screen.
I need to listen on HTTPS but adding the cryptography
package which forces openssl 3.0 be downgraded to 1.1 -- 
bad for production but okay for testing.

I have to run this in a Docker because it has to be reverse proxied, ArcGIS will not accept a self-signed certificate.

## Environment


### Deploy

```bash
docker-compose up -d
```



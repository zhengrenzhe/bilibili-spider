# bilibili-spider

```bash
cp proxy.tmpl.yaml proxy.yaml # edit proxy config
docker-compose up -d   # start all infrastructure services

cd frontend/dashboard
yarn && yarn build

wget https://caddyserver.com/download/linux/amd64?license=personal&telemetry=off

supervisord -c supervisord.conf
```
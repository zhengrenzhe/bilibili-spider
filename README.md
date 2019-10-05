# bilibili-spider

```bash
cp proxy.tmpl.yaml proxy.yaml # edit proxy config
docker-compose up -d   # start all infrastructure services

cd frontend/dashboard
yarn && yarn build

supervisord -c supervisord.conf
```
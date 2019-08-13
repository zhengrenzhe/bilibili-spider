# bilibili-spider

```bash
cp proxy.tmpl.yaml proxy.yaml # edit proxy config
docker-compose up -d   # start all infrastructure services
python daily_worker.py # fetch daily urls process
python pages_worker.py # fetch video page data process
```
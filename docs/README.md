# docs

## testing and local dev

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt # for a complete installation
# python setup.py install => for release only build installs

./scripts/generate-grpc-codes.sh
python python_grpc_boilerplate/server.py
python python_grpc_boilerplate/client.py
```

## with docker, locally

```sh
./scripts/docker-build.sh
```

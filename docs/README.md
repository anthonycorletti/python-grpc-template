# docs

## code architecture

```sh
# project structure, arch, design decisions go here
```

## testing + local dev

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt # for a complete installation
# python setup.py install => for release only build installs

./scripts/generate_grpc_codes
python v1/server.py
python v1/client.py
```

## with docker, locally

```sh
docker build -t pygrpcboiler-server --file docker/v1/server/Dockerfile .
docker run -p 50051:50051 -it pygrpcboiler-server

docker build -t pygrpcboiler-client --file docker/v1/client/Dockerfile .
docker run --network host -it pygrpcboiler-client

# see scripts/build_run_docker
```

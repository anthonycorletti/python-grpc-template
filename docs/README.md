# docs

## testing and local dev

```sh
python -m venv env
source env/bin/activate
./scripts/install.sh
./scripts/generate-grpc-codes.sh
python python_grpc_boilerplate/server.py
python python_grpc_boilerplate/client.py
```

## locally build and run with docker

```sh
./scripts/docker-build.sh
docker network create pygrpc
# run the server in the new network and name it wrt the name the
# client will expect to connect to
docker run -it --network pygrpc -p 50051:50051 --name pygrpcserver pygrpcboiler-server
# in another shell
docker run -it --network pygrpc pygrpcboiler-client
```

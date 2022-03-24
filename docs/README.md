# docs

Read the [contributing guide](../CONTRIBUTING.md) to get started.

To test this locally, build each container, create the docker network, and run the server and client in separate sessions.

```sh
./scripts/docker-build-client.sh
./scripts/docker-build-server.sh
./scripts/docker-create-network.sh
./scripts/docker-run-server.sh
./scripts/docker-run-client.sh
```

To point the grpc client directly to the server, run your server like so

```sh
docker run -it --rm -e GRPC_SERVER_HOST='0.0.0.0' -p 50051:50051 --name pygrpcserver pygrpcserver
```

And then connect with your client from the host machine like so;

```sh
$ GRPC_SERVER_SVC_NAME=0.0.0.0 python python_grpc_template/client.py
```

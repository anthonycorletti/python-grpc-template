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

# GitDataSanitizer
A service that consumes `git-uploaded` Kafka events and produces `git-sanitized` events.

# Table of Contents

# Installation 
## Local Installation
The following steps instruct how to deploy this service locally

## Docker Installation
The following instructions will setup the Docker Image and Docker Container so that you can run the service locally.

```sh
# Ensure you are in the root directory of this project
# Creating Docker Image
docker build -t python-3.9:git-sanitizer .
# Create Docker image - uses Host network
docker run --name py-git-sanitizer --network="host" -it python-3.9:git-sanitizer
```

# Usage





# Kafka
Create service consumers
```sh
# Create Topic & Consumer Group
bin/kafka-topics.sh --create --topic repo-sanitized --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic repo-sanitized --from-beginning --group repo-sanitized-cg
```



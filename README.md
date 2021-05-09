# GitDataSanitizer
A service that consumes `git-uploaded` Kafka events and produces `git-sanitized` events.

# Table of Contents
0. Development Environment
1. Installation
    1.1. Locally
    1.2. Docker
2. Dependencies
    2.1 Kafka
    2.2. Python Environment
    2.3. Environment Variables
3. Tests
4. Logs
5. Design Decisions

# 0, Development Environment
This project was writting on a Ubuntu 20.04 LTS.
# 1. Installation 
## 1.1. Local Installation
In order to run this service locally, please follow the steps in Sections 2.1, 2.2., 2.3.

Once you have completed this, please run the following command:

```sh
# Ensure you are in the root directory of this project
python ./src/app.py
```
## 1.2. Docker
In order to run this service in Docker, please follow the steps in Sections 2.1. and 2.3.

Once you have completed this, please run the following commands:

```sh
# Ensure you are in the root directory of this project
# Creating Docker Image
docker build -t python-3.9:git-sanitizer .
# Create Docker image - uses Host network
docker run --name py-git-sanitizer --network="host" -it python-3.9:git-sanitizer
```
This has been tested on Docker `v.20`.

# 2. Dependencies
## 2.1. Kafka 
To create the Kafka Message queue, please run the following

```sh
# Downlaod lates version of Kakfa. (Currently: kafka_2.13-2.8.0)
curl https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz --output kafka_2.13-2.8.0.tgz 
# Extract zipped file
tar -xzf kafka_2.13-2.8.0.tgz
# cd into kakfka
cd kafka_2.13-2.8.0
# Starts necessary Zookeeper on a Terminal - used for resource management in Kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
# Starts Kafka broker service on a second Terminal 
bin/kafka-server-start.sh config/server.properties
# Create Consumer Topic - on a third Terminal
bin/kafka-topics.sh --create --topic repo-uploaded --bootstrap-server localhost:9092
# Create Consumer Group
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic repo-uploaded --from-beginning --group repo-uploaded-cg
# Create Producer Topic
bin/kafka-topics.sh --create --topic repo-sanitized --bootstrap-server localhost:9092

```
This has been tested with Kafka `v.2.8`.

## 2.2. Python Environment
To create the Python Environment, please run the following:

```sh
# Ensure you are in the root directory of this project
virtualenv venv --python=/path/to/python3.9
source venv/bin/activate
pip install -r requirements/prod.txt
```

This has been tested on Python `v.3.9`.


## 2.3. Environment Variables
The following are the necessary environment variables of this project. 

```sh
KAFKA_ENDPOINT=...:9092  # Please keep 9092 as Kafka runs on this port.
KAFKA_REPO_UPLOADED_TOPIC=repo-uploaded
KAFKA_REPO_UPLOADED_CONSUMER_GROUP=git-requested
KAFKA_REPO_SANITIZED=repo-sanitized
LOGGING_LEVEL=INFO
```
Please store these at location `./env` relative to root directory.


# 3 Tests
To run tests locally, please follow instructions in Sections 2. to create local environment.

Once this is complete, run local tests from root directory using 

```sh
python -m unittest discover -s test -p '*_test.py'
```

# 4. Logs
You can find the logs of the service in the `./service.log` file.
# 5. Design Decisions

Please refer to the Project's README.md to get an insight in the design decisions of this project.

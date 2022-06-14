# PV Simulator Tech 


# Description
More information about messaging broker: https://www.rabbitmq.com/

## Getting Started

**Step 1:** Make sure git is installed on your os. I will be using Ubuntu 20.04.1  for the project in VM.

**Step 2:** Clone the project into your local machine using below command.

```git clone https://github.com/willycamps/PV-Simulator.git```

### Prerequisites

**1. Docker**

Make sure you have Docker installed. Please follow the below link for official documentation from Docker to install latest version of docker on your os. For this project I am using Docker CE (18.09).

```https://docs.docker.com/docker-for-mac/install/```

## Installing

**Step 1:** Change to the directory where the project was cloned in previous step.

```
cd 
```

**Step 2:** Make sure Docker is up and running. You can start the docker engine from command line.

```
sudo docker info
```

**Step 3:** Run

Build and run in the background. The standard AMQP protocol port (RabbitMQ)
```
docker-compose up --build -d
```



**Step 4:** Run the Consumer
```
python3 consumer.py
```

**Step 5:** Run the Producer
```
python3 producer.py
```

**Step 6:** Open up the browser
* (http://localhost:15672/) - RabbitMQ
![alt text](/img/01.JPG "RabbitMQ")

## Built With

* [Docker](https://docs.docker.com/compose/install/) -  Docker
* [Broker](https://www.rabbitmq.com/) -  RabbitMQ
* [Python](https://www.python.org/) - Programming language
* [pip](https://pip.pypa.io/en/stable/) - Package and dependency manager

## Authors
* Willy E. Campos


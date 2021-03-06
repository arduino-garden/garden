# garden-aggregator

This is a REST API that will serve data for monitored plants in pots with different sensors

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

What things you need to install the software and how to install them

```none
python3 - (sudo) apt install python3
pip3 - (sudo) apt install python3-pip
pytest - (sudo) apt install python-pytest
virtualenv - (sudo) apt install virtualenv
cassandra - http://www.apache.org/dyn/closer.lua/cassandra/3.11.3/apache-cassandra-3.11.3-bin.tar.gz
```

## Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
virtualenv -p python3 env
```

Copy the following: ```export FLASK_APP="$VIRTUAL_ENV/../src/rest_start.py"``` after the ```export VIRTUAL_ENV``` in env/bin/activate


```
source env/bin/activate - to activatate the virtual environment
pip install fabric3
fab install
fab reset
```

## Starting aggregator

First start cassandra

```
fab start_aggregator
```

## Starting rest server

First start cassandra

```
fab start_rest
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
fab test
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://www.dropwizard.io/1.0.2/docs/) -  The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Bozhidar Gevechanov**
* **Didi Milikina**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

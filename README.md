[![powered by National Rail Enquiries](http://www.xcitybrum.co.uk/Content/images/poweredby.png)](http://www.nationalrail.co.uk/100296.aspx)

[![Build Status](https://drone.io/github.com/HackPartners/darwinrest/status.png)](https://drone.io/github.com/HackPartners/darwinrest/latest)

## Overview

* This is a wrapper for National Rail Enquiries' Darwin API that exposes a REST API. 
* The code is open source and is available on the [Hack Partners Github](https://github.com/HackPartners/darwinrest) 
* The API Docs for the Darwin REST API can be found at [darwin.hacktrain.com](http://darwin.hacktrain.com). 
* For more information about the DARWIN APIs you can visit the [National Rail Enquiries documentation](http://www.nationalrail.co.uk/46391.aspx)


## The TrainHackers (Contributors)

The HackTrain team has open sourced this project, and the active contributors to this project include:
* Alejandro Saucedo
* Mansimran Singh

Big shoutout to Mr. [Robert B. Clarke](https://github.com/robert-b-clarke) for creating [nre-darwin-py](https://github.com/robert-b-clarke/nre-darwin-py) - a great python wrapper for Darwin's SOAP interface.


## Motivation

Our vision is to bring innovation to the railway industry, and the first step to achieve this is making the current masses of data available in the industry, easy to access and process. For this reason the HackTrain team has decided to create this open source project to expose a standardized REST API for the Darwin API. This project will be maintained by the community for the community.


## Code Example

The API Docs can be found at [darwin.hacktrain.com](http://darwin.hacktrain.com). It is very simple to use this API. In order to retreive station crs codes, you only have to send:

``` bash
    curl -i http://darwin.hacktrain.com/api/station/code
```


## Installation

In order to run darwinrest, you need to install the following python dependencies:
* flask
* flask_restful
* nre-darwin-py
* lxml cssselect
* beautifulsoup4

These can be installed by running:

``` bash
    pip install flask flask_restful nre-darwin-py lxml cssselect beautifulsoup4
```

If you're running a fresh ubuntu server, make sure you have the following dependencies:
* sudo apt-get install libxml2-dev libxslt1-dev python-dev
* apt-get install python-lxml

The system is currently connected to Drone.io for continuous integration and continuous deployment. 


## Tests

The system uses Dredd to test all the api endpoints. Nose tests will be added soon.


## Roadmap

Currently the project is in early alpha phase. We are waiting for greater support in order to develop this project further. Our future roadmap includes:
* Create a setup.py that sets up all the environment
* Design and expose a REST interface for 'next' and 'fastest' SOAP endpoints
* Adding tests to all endpoints
* Adding continuous integration with TravisCI, or similar framework
* Exploring other datasets that could enhance Darwin (geolocation, etc)
* Exploring other Darwin endpoints, such as Darwin push and see how it can be enhanced


## License

This project is registered under the Apache 2.0 licence. View the LICENCE file for more details.

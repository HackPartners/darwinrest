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

Our vision is to bring innovation to the railway industry, and the first step to achieve this is by making the current masses of data available in the industry, easy to access and process. For this reason the HackTrain team has decided to create this opens source project to expose a standardized REST API for the Darwin API.


## Code Example

The API Docs can be found at [darwin.hacktrain.com](http://darwin.hacktrain.com). It is very simple to use this API. In order to retreive station boards, for example, you only have to send:

``` bash
    curl -i http://darwin.hacktrain.com/board/EUS?apikey=YOUR_KEY
```


## Installation

In order to run darwinrest, you need to install the following python dependencies:
* flask
* flask_restful
* nre-darwin-py


## Tests

System tests will be added as project is developed further.


## Roadmap

Currently the project is in early alpha phase. We are waiting for greater support in order to develop this project further. Our future roadmap includes:
* Exposing a REST interface for Service Details
* Exposing a REST interface for all SOAP endpoints
* Exposing a WebSockets interface for Darwin PUSH data


## License

This project is registered under the Apache 2.0 licence. View the LICENCE file for more details.
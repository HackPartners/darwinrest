define({  "name": "Darwin REST API",  "version": "0.0.1",  "description": "Darwin REST documentation",  "apidoc": "0.2.0",  "header": {    "title": "Introduction",    "content": "<h1>Darwin REST</h1>\n<p>This is a wrapper for National Rail Enquiries' Darwin API that exposes a REST API.</p>\n<p>The API Docs for the Darwin REST API can be found at <a href=\"http://darwin.hacktrain.com\">darwin.hacktrain.com</a>.</p>\n<p>For more information about the DARWIN APIs you can visit the <a href=\"http://www.nationalrail.co.uk/46391.aspx\">National Rail Enquiries documentation</a></p>\n<h2>The TrainHackers (Contributors)</h2>\n<p>The HackTrain team has open sourced this project, and the active contributors to this project include:</p>\n<ul>\n<li>Alejandro Saucedo</li>\n<li>Mansimran Singh</li>\n</ul>\n<p>Big shoutout to Mr. <a href=\"https://github.com/robert-b-clarke\">Robert B. Clarke</a> for creating <a href=\"https://github.com/robert-b-clarke/nre-darwin-py\">nre-darwin-py</a> - a great python wrapper for Darwin's SOAP interface.</p>\n<h2>Motivation</h2>\n<p>Our vision is to bring innovation to the railway industry, and the first step to achieve this is by making the current masses of data available in the industry, easy to access and process. For this reason the HackTrain team has decided to create this opens source project to expose a standardized REST API for the Darwin API.</p>\n<h2>Code Example</h2>\n<p>The API Docs can be found at <a href=\"http://darwin.hacktrain.com\">darwin.hacktrain.com</a>. It is very simple to use this API. In order to retreive station boards, for example, you only have to send:</p>\n<pre><code class=\"language-bash\">    curl -i http://darwin.hacktrain.com/board/EUS?apikey=YOUR_KEY\n</code></pre>\n<h2>Installation</h2>\n<p>In order to run darwinrest, you need to install the following python dependencies:</p>\n<ul>\n<li>flask</li>\n<li>flask_restful</li>\n<li>nre-darwin-py</li>\n</ul>\n<h2>Tests</h2>\n<p>Describe and show how to run the tests with code examples.</p>\n<h2>Roadmap</h2>\n<p>Currently the project is in early alpha phase. We are waiting for greater support in order to develop this project further. Our future roadmap includes:</p>\n<ul>\n<li>Exposing a REST interface for Service Details</li>\n<li>Exposing a REST interface for all SOAP endpoints</li>\n<li>Exposing a WebSockets interface for Darwin PUSH data</li>\n</ul>\n<h2>License</h2>\n<p>This project is registered under the Apache 2.0 licence. View the LICENCE file for more details.</p>\n"  },  "sampleUrl": false,  "generator": {    "name": "apidoc",    "time": "2015-08-17T06:20:01.294Z",    "url": "http://apidocjs.com",    "version": "0.13.1"  }});
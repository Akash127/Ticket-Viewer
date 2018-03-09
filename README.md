# Zendesk Ticket Viewer
This is a Web Application developed using Flask in Python which can be used to view list of all the tickets and display a particular ticket in detail.

## Installation and Usage Instruction

1. Clone this Repo to your local machine or Download as a zip file.
2. Ensure you have python 3.6.4 and python -pip install
3. In terminal cd to the root folder
4. Install dependencies
```
$ pip install -r requirements.txt
```
4. In terminal cd to the app folder and run the following command
```
$ python Main.py
```
5. Go to localhost in your browser to see the app.
```
http://localhost:5000
```
## To Run the Test
```
$ python test_Connector.py
```
```
$ python test_DateParser.py
```

## Design and Implementation
**The project consists of following 4 Python Modules:**
1. ConnectionConfig : This module consists of Configuration class which define the necessary credentials to connect with the Zendesk API. These credentials can be updated in the class by updating the 'API_SERVER', 'USER' and 'TOKEN' variables to connect with different API address.

2. Connector: This module is responsible for handling the connection and response from the API Server. It consists for 4 classes, 'ApiConnector', 'ApiResponse', 'ApiOperation' and 'ApiRequest'.

3. Tickets: This module handles the operation related to tickets. It contains following classes 'Ticket', TicketHandler', 'TicketParser' and 'DateParser'.

4. Main: This module is responsible for handling the frontend of the web application. It provides basic infrastructure for Flask, create CSS Bundles and Render HTML Templates. 

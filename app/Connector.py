import requests
from ConnectionConfig import Configuration


class ApiConnector:
	'''Class defines API Connector Object to execute Query'''
	
	def execute(self, query):
		"""Execute the Query from Request Object using python
		requests library.

	    Args:
	        query: A string which specifies the query to be executed.

	    Returns:
	        Response Object which consists of StatusCode, Parsed Json 
	        Output and Error.

	    """

		config = Configuration()
		user = config.getUserID()
		token = config.getToken()
		response = requests.get(query, auth=(user, token))
		resObj = ApiResponse(response)
		return resObj



class ApiResponse:
	"""Class define a Response Object."""

	def __init__(self, res):
		"""Initialize various properites of Response Object.

		Args:
	        res: Response Object from Python Request Library containing
	        all the information.

		"""

		if(res.status_code != 200):
			res = res.json()
			self.StatusCode = 'Fail'
			self.error = res['error']
			self.output = None
		else:
			res = res.json()
			self.StatusCode = 'Success'
			self.error = None
			self.output = res



class ApiOperation:
	"""Class defines various Available Operations."""

	def getListTicketsOperation(self):
		"""Returns operation for listing tickets."""

		return "/api/v2/tickets.json"

	def getDisplayTicketOperation(self, id):
		"""Returns operation for displaying particular ticket with ID.
		
		Args:
			id: Integer ID of the ticket to be retrieved.
		"""

		return "/api/v2/tickets/{id}.json".format(id=id)




class ApiRequest:
	"""Class defines Request Instance for Particular Query"""

	def __init__(self, operation):
		"""Generate Complete Query String using Configuration API.
		
		Args:
			operation: String for the Operation to be performed.
		"""

		self.query = Configuration().getAPI_SERVER() + operation


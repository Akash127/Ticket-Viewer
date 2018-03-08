class Configuration:
	"""Configuration Class for Initializing Credentials"""

	API_SERVER = 'https://akashsharma.zendesk.com'
	USER = 'mail.akashsharma@gmail.com/token'
	TOKEN = 'ggUZ4J7SIeamKFmlQcqdmnctNLIXPTMNrwk4VsWF'

	def getUserID(self):
		return self.USER

	def getToken(self):
		return self.TOKEN

	def getAPI_SERVER(self):
		return self.API_SERVER

from Connector import *
import datetime

class TicketHandler:
	"""Class defines Tickethandler Object to list
	all the tickets and display particular ticket"""

	def displayTicket(self, id):
		"""Function to retrieve ticket with particular Id.

	    Args:
	        id: Integer ID of the ticket to be displayed.

	    Returns:
	        If the ticket is found returns a ticket object
	        with the ticket details. 
	        If the Ticket is not found returns ticket object
	        with error
	    """

		op = ApiOperation().getDisplayTicketOperation(id)
		reqObj = ApiRequest(op)
		con = ApiConnector()
		r = con.execute(reqObj.query)
		if(r.StatusCode == 'Success'):
			data = r.output
			ticket = data['ticket']
			p = TicketParser()
			ticket = p.parse(ticket)
		else:
			ticket = Ticket()
			ticket.setError(r.error)

		return ticket


	def listTickets(self):
		"""Function to retrieve all the tickets.

	    Returns:
	        If the tickets are found, it returns them as list 
	        of ticket objects.
	        If the Tickets are not found, it returns a list with 
	        one ticket object that contains the error.
	    """

		op = ApiOperation().getListTicketsOperation()
		reqObj = ApiRequest(op)
		con = ApiConnector()
		r = con.execute(reqObj.query)
		if(r.StatusCode == 'Success'):
			data = r.output
			tickets = data['tickets']
			TicketList = []
			for tkt in tickets:
				p = TicketParser()
				tk = p.parse(tkt)
				TicketList.append(tk)				
		else:
			TicketList = []
			ticket = Ticket()
			ticket.setError(r.error)
			TicketList.append(ticket)

		return TicketList




class TicketParser:
	"""Class defines a TicketParser Object to parse Json
	output into ticket objects"""

	def parse(self, ticket):
		"""Function to create ticket object from response.

	    Args:
	        ticket: Python ticket Dictionary from response Object.

	    Returns:
	        Returns a ticket object.
	    """

		tk = Ticket()
		tk.setID(ticket['id'])
		
		if ticket['status']:
			tk.setStatus(ticket['status'])
		
		if ticket['type']:
			tk.setType(ticket['type'])
		
		tk.setSubject(ticket['subject'])
		tk.setDescription(ticket['description'])

		if ticket['priority']:
			tk.setPritority(ticket['priority'])
		
		tk.setRecipient(ticket['recipient'])
		tk.setRequesterId(ticket['requester_id'])
		
		if ticket['via']['source']['from']:
			tk.setSourceName(ticket['via']['source']['from']['name'])
			tk.setSourceAdress(ticket['via']['source']['from']['address'])

		dObj = DateParser()
		postDateTime = dObj.parse(ticket['created_at'])
		updateDateTime = dObj.parse(ticket['updated_at'])

		tk.setPostTime(postDateTime)
		tk.setLastUpdateTime(updateDateTime)

		return tk



class DateParser:
	"""Class defines DateParser object to
	parse Json date."""

	def parse(self, date):
		"""Function to parse the Json date into readable format.

	    Args:
	        date: Json date

	    Returns:
	        Returns a date string. For example:
	        Json Date: "2018-03-03T00:15:44Z"
	        Return:    "Date: 3/3/2018 Time: 0:15:44"
	    """

		date = date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
		str = "Date: {day}/{mon}/{yr} Time: {hr}:{min}:{sec}" \
		.format(day=date.day, mon=date.month, yr=date.year, hr=date.hour,min=date.minute,sec=date.second)

		return str



class Ticket:
	"""Class Ticket defines the Ticket Object and
	Initialize the ticket properties"""

	def __init__(self):
		self.Id = None
		self.Status = 'Not Specified'
		self.Priority = 'Not Specified'
		self.Type = 'Not Specified'
		self.SourceName = 'Not Specified'
		self.SourceAddress = 'Not Specified'
		self.Error = None

	def setID(self, id):
		self.Id = id
	def setStatus(self, status):
		self.Status = status.title()
	def setType(self, ty):
		self.Type = ty.title()
	def setSubject(self, sub):
		self.Subject = sub.title()
	def setDescription(self, desc):
		self.Description = desc
	def setPritority(self, p):
		self.Priority = p.title()
	def setRecipient(self, rec):
		self.Recipient = rec
	def setRequesterId(self, id):
		self.RequesterId = id
	def setSourceAdress(self, adr):
		self.SourceAddress = adr
	def setSourceName(self, name):
		self.SourceName = name
	def setPostTime(self, pt):
		self.PostTime = pt
	def setLastUpdateTime(self, ut):
		self.LastUpdateTime = ut
	def setError(self, e):
		self.Error = e

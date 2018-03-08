from flask import Flask, render_template
from Tickets import TicketHandler
from flask_assets import Bundle, Environment


app = Flask(__name__)


cssBundle = Bundle('bootstrap.min.css','style.css', output='gen/main.css')
assets = Environment(app)
assets.register('main.css', cssBundle)


@app.route('/')
def index():
	"""Function to display all the tickets on the index page.

	    Returns:
	        Html template for displaying the ticket list or error.
	    """

	th = TicketHandler()
	tickets = th.listTickets()
	if tickets[0].Error:
		tickets_found = False
	else:
		tickets_found = True
	return render_template('list.html', Tkt=tickets, isTkt=tickets_found)



@app.route('/<int:ticket_id>')
def displayTicketwithID(ticket_id):
	"""Function to display ticket details.

	    Args:
	        id: Integer ID of the ticket to be displayed.

	    Returns:
	        Html template for displaying the ticket or error.
	    """

	th = TicketHandler()
	ticket = th.displayTicket(ticket_id)
	if(ticket.Id):
		ticket_found = True
	else:
		ticket_found = False

	return render_template('ticket.html', Tkt=ticket, isTkt=ticket_found)



if __name__ == "__main__":
	app.run(debug=True)
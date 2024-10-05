from odoo import http
from odoo.http import request
import logging
import json
class VoxbayApi(http.Controller):
    # Event 1: Incoming call landed on server
    @http.route(
        '/voxbay/api/incoming_landed',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        print(post.items())

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'Incoming call data received',
            'received_data': post  # Echo the received data back to the client
        }
        
        # Return the response in JSON format
        return json.dumps(response_data)
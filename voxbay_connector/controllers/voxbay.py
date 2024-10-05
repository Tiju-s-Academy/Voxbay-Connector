from odoo import http
from odoo.http import request
import logging
import json
_logger = logging.getLogger("Voxbay Debug: ")
class VoxbayApi(http.Controller):

    '''
        *****Incoming Call API******
    '''
    # Event 1: Incoming call landed on server
    @http.route(
        '/voxbay/api/incoming_landed',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'incoming_landed data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
    
    #Event 2: Call answered by an agent
    @http.route(
        '/voxbay/api/incoming_answered',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'incoming_answered data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
    
    #Event 3: When a call is disconnected
    @http.route(
        '/voxbay/api/incoming_disconnected',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'incoming_disconnected data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
    
    # Event 4: CDR push at the end of the call
    @http.route(
        '/voxbay/api/incoming_cdr_push',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'incoming_cdr_push data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
    
    '''
        *****Outgoing Call API******
    '''

    # Event 1: when an outgoing call initiated
    @http.route(
        '/voxbay/api/outgoing_initiated',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'incoming_cdr_push data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
    
    # Event 2: CDR push at the end of the call
    @http.route(
        '/voxbay/api/outgoing_cdr_push',
        type='json', auth='none', methods=["POST"], csrf=False)
    def authenticate(self, *args, **post):
        _logger.info(post)

        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'outgoing_cdr_push data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
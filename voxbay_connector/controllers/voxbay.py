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
    def incoming_landed(self, *args, **post):
        _logger.info(f'{request.httprequest.json}')

        try:
            called_number = post['calledNumber']
            caller_number = post['callerNumber']
            call_uuid = post['CallUUID']

            request.env['voxbay.call.data.record'].sudo().create({
                'called_number': called_number,
                'caller_number': caller_number,
                'call_uuid': call_uuid,
                'event_status': 'agent_received_call',
            })
        except Exception as e:
            print("Exception Occured")
            print(e)
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
    def incoming_answered(self, *args, **post):
        _logger.info(f'{request.httprequest.json}')

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
    def incoming_disconnected(self, *args, **post):
        _logger.info(f'{request.httprequest.json}')

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
    def incoming_cdr_push(self, *args, **post):
        _logger.info(f'{request.httprequest.json}')

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
    def outgoing_initiated(self, *args, **post):
        _logger.info(f'{request.httprequest.json}')

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
    def outgoing_cdr_push(self, **post):
        _logger.info(f'{request.httprequest.json}')
        # Prepare the response data
        response_data = {
            'status': 'success',
            'message': 'outgoing_cdr_push data received',
            'received_data': post  # Echo the received data back to the client
        }
        # Return the response in JSON format
        return json.dumps(response_data)
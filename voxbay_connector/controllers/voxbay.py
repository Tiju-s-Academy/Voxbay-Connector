from odoo import http
from odoo.http import request
import logging
import json
import traceback
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
        try:
            post_data: dict = request.httprequest.json
            request.env['voxbay.call.data.record'].sudo().create({
                'called_number': post_data['calledNumber'],
                'caller_number': post_data['callerNumber'],
                'call_uuid': post_data['CallUUID'],
                'event_status': 'agent_received_call',
                'call_type': 'incoming',
            })
            return json.dumps({'status': 'success',})

        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)
        return json.dumps({'status': 'failed',})
    
    #Event 2: Call answered by an agent
    @http.route(
        '/voxbay/api/incoming_answered',
        type='json', auth='none', methods=["POST"], csrf=False)
    def incoming_answered(self, *args, **post):
        try:
            post_data: dict = request.httprequest.json
            call_record = request.env['voxbay.call.data.record'].sudo().search([('call_uuid','=',post_data['CallUUID'])])
            if call_record:
                call_record.update({
                    'agent_number': post_data['AgentNumber'],
                    'caller_number': post_data['callerNumber'],
                    'event_status': 'agent_answered_call',
                })
                return json.dumps({'status': 'success',})
            else:
                _logger.error(f"Record with CallUUID {post_data['CallUUID']} Doesn't Exist")
        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)

        return json.dumps({'status': 'failed',})
    
    #Event 3: When a call is disconnected
    @http.route(
        '/voxbay/api/incoming_disconnected',
        type='json', auth='none', methods=["POST"], csrf=False)
    def incoming_disconnected(self, *args, **post):
        try:
            post_data: dict = request.httprequest.json
            call_record = request.env['voxbay.call.data.record'].sudo().search([('call_uuid','=',post_data['CallUUID'])])        
            if call_record:
                call_record.update({
                    'agent_number': post_data['AgentNumber'],
                    'event_status': 'call_ended',
                })     
                return json.dumps({'status': 'success',})
            else:
                _logger.error(f"Record with CallUUID {post_data['CallUUID']} Doesn't Exist")   
        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)

        return json.dumps({'status': 'failed',})

    
    # Event 4: CDR push at the end of the call
    @http.route(
        '/voxbay/api/incoming_cdr_push',
        type='json', auth='none', methods=["POST"], csrf=False)
    def incoming_cdr_push(self, *args, **post):
        try:
            post_data: dict = request.httprequest.json
            call_record = request.env['voxbay.call.data.record'].sudo().search([('call_uuid','=',post_data['CallUUID'])])
            if call_record:
                call_record.update({
                    'caller_number': post_data['callerNumber'],              # Customer number
                    'total_call_duration': post_data['totalCallDuration'],   # Total call duration
                    'call_date': post_data['callDate'],                      # Date and time of the call
                    'call_status': post_data['callStatus'],                  # Status of the call
                    'recording_url': post_data['recording_URL'],             # Recording URL
                    'agent_number': post_data['AgentNumber'],                # Agent number or name
                    'call_uuid': post_data['CallUUID'],                      # Unique ID for the call
                    'call_start_time': f"{post_data['callDate'].split(' ')[0]} {post_data['callStartTime']}",           # Call start time
                    'call_end_time': f"{post_data['callDate'].split(' ')[0]} {post_data['callEndTime']}",               # Call end time
                    'conversation_duration': post_data['conversationDuration'],  # Conversation duration
                    'dtmf': post_data['dtmf'],                              # DTMF input sequence
                    'transferred_number': post_data['transferredNumber'],    # Transferred number
                    'event_status': 'call_ended',  
                })

                return json.dumps({'status': 'success',})
            else:
                _logger.error(f"Record with CallUUID {post_data['CallUUID']} Doesn't Exist")

        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)

        return json.dumps({'status': 'failed',})
    
    '''
        *****Outgoing Call API******
    '''

    # Event 1: when an outgoing call initiated
    @http.route(
        '/voxbay/api/outgoing_initiated',
        type='json', auth='none', methods=["POST"], csrf=False)
    def outgoing_initiated(self, *args, **post):
        try:
            post_data: dict = request.httprequest.json
            request.env['voxbay.call.data.record'].sudo().create({
                'caller_number': post_data['callerNumber'],
                'called_number': post_data['calledNumber'],
                # 'caller_id': post_data['callerId'],
                'call_uuid': post_data['CallUUlD'],
                'event_status': 'agent_initiated_call',
                'call_type': 'outgoing',

            })
            return json.dumps({'status': 'success',})

        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)

        return json.dumps({'status': 'failed',})
    
    # Event 2: CDR push at the end of the call
    @http.route(
        '/voxbay/api/outgoing_cdr_push',
        type='json', auth='none', methods=["POST"], csrf=False)
    def outgoing_cdr_push(self, **post):
        try:
            post_data: dict = request.httprequest.json
            call_record = request.env['voxbay.call.data.record'].sudo().search([('call_uuid','=',post_data['CallUUID'])])
            if call_record:
                call_record.update({
                'caller_number': post_data['callerNumber'],
                'called_number': post_data['calledNumber'],
                'agent_number': post_data['AgentNumber'],
                # 'caller_id': post_data['callerid'],
                'call_uuid': post_data['CallUUID'],
                'call_start_time': post_data['callStartTime'],
                'call_end_time': post_data['callEndTime'],
                'total_call_duration': post_data['totalCallDuration'],
                'conversation_duration': post_data['conversationDuration'],
                'dtmf': post_data['dtmf'],
                'call_status': post_data['callStatus'],
                'call_date': post_data['callDate'],
                'recording_url': post_data['recording_URL'],
                'event_status': 'call_ended',

                })   
                return json.dumps({'status': 'success',})
            else:
                _logger.error(f"Record with CallUUID {post_data['CallUUID']} Doesn't Exist")
        except Exception as e:
            _logger.error("Exception Occurred")
            _logger.error(traceback.format_exc())
            _logger.error(post_data)

        return json.dumps({'status': 'failed',})

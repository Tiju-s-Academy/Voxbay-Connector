from odoo import http, SUPERUSER_ID
from odoo.http import request
import logging
import json
import traceback
_logger = logging.getLogger("Telinfy Debug: ")


class TelinfyApi(http.Controller):

    # Event 1: Incoming call landed on server
    @http.route('/telinfy/whatsapp/webhook', type='json', auth='none', methods=["POST"], csrf=False)
    def incoming_landed(self, *args, **post):
        post_data: dict = request.httprequest.json
        _logger.error(f'Webhook Data: {post_data}')
        if post_data.get('messages'):
            messages = post_data.get('messages')
            for message in messages:
                if message.get('type','')=='text':
                    superuser = request.env['res.users'].sudo().browse(SUPERUSER_ID)
                    from_number = message['from']
                    lead_name = post_data.get('contacts')[0]['profile']['name']
                    lead = request.env['crm.lead'].sudo().search([('phone','like',from_number), ('phone','!=',False)], limit=1)
                    if lead:
                        _logger.info(f'Lead already exists for this whatsapp contact {lead_name}, {from_number}.')
                    else:
                        lead = request.env['crm.lead'].with_user(superuser).create({
                        'name': f'[Whatsapp] {lead_name}',
                        'partner_id': request.env['res.partner'].sudo().create({'name': lead_name, 'company_type': 'person', 'phone': from_number}).id,
                        'phone': from_number,
                        'user_id': superuser.id,
                        'description': f"<p>{message['text']['body']}</p>",
                        'type': 'lead',  
                        })
                        _logger.info(f'Lead {lead_name}, {from_number} created successfully!')
        return json.dumps({'status': 'success',})

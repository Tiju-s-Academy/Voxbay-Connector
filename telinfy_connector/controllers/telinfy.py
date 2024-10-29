from odoo import http
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
        headers = dict(request.httprequest.headers)
        # _logger.error(f'Request: {request.httprequest.headers.items()}')
        _logger.error(f'Webhook Data: {post_data}')
        _logger.error(f'Headers: {headers}')
        return json.dumps({'status': 'success',})

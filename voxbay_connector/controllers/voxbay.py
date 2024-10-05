from odoo import http
from odoo.http import request
import logging

class VoxbayApi(http.Controller):
    @http.route(['/voxbay/api/incoming_landed'], type='http', auth="public", website=True)
    def courses_page(self,**kw):
        print(kw)
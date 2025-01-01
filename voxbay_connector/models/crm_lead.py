from odoo import models, fields, api
import requests

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def action_click_to_call(self):
        self.ensure_one()
        employee = self.env.user.employee_id
        if not employee:
            raise UserError("No employee record found for the current user.")
        
        url = "https://pbx.voxbaysolutions.com/api/clicktocall.php"
        params = {
            'uid': employee.voxbay_uid,
            'pin': employee.voxbay_pin,
            'source': employee.voxbay_extension,
            'destination': self.phone,
            'ext': employee.voxbay_extension,
            'callerid': employee.voxbay_callerid,
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise UserError("Failed to initiate call.")
        return True

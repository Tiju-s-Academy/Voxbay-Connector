from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    agent_number = fields.Char(string="Voxbay Agent Number")

    @api.onchange('agent_number')
    def onchange_agent_number(self):
        if self.agent_number:
            domain = [('agent_number','=',self.agent_number)]
            if isinstance(self.id, int):
                domain.append(('id','!=', self.id))
            employee_with_same_agent_no = self.env['hr.employee'].sudo().search(domain, limit=1)
            if employee_with_same_agent_no:
                raise ValidationError(f"This Agent Number is already assigned to {employee_with_same_agent_no[0].name}! You need to unassign this Agent Number from {employee_with_same_agent_no[0].name}, before setting it to another Employee.")
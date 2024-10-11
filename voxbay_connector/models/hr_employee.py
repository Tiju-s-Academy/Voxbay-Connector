from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    agent_number = fields.Char(string="Voxbay Agent Number")
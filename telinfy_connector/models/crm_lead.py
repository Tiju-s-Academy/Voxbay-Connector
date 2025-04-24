from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    has_unread_whatsapp = fields.Boolean(string='Unread WhatsApp', default=False)

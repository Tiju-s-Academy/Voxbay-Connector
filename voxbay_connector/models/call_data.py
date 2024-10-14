from odoo import models,fields,api

class VoxbayCallData(models.Model):
    _name = "voxbay.call.data.record"
    name = fields.Char(string="Name", compute="_compute_name", store=True)
    @api.depends('call_date', 'call_uuid', 'called_number', 'caller_number')
    def _compute_name(self):
        for record in self:
            record.name = ''
            if record.call_date:
                record.name += f'{record.call_date} - '
            if record.call_uuid:
                record.name += f'{record.call_uuid}'

    call_uuid = fields.Char(string="Call UUID")
    call_type = fields.Selection(string="Call Type", selection=[('incoming', 'Incoming Call'), ('outgoing', 'Outgoing Call')])
    event_status = fields.Selection(string="Event Status", selection=[('agent_received_call', 'Agent Received Call'), ('agent_answered_call', 'Agent Accepted Call'), ('agent_initiated_call', 'Agent Initiated Call'), ('call_ended', 'Call Ended')])
    total_call_duration = fields.Integer(string="Duration",)
    call_date = fields.Datetime(string="Call Date")
    call_status = fields.Selection(string="Call Status", selection=[('Connected', 'Connected'), ('Not Connected', 'Not Connected'), ('Cancel', 'Cancel'), ('NOANSWER', 'No Answer'), ('BUSY', 'BUSY'), ('CONGESTION', 'Congestion'), ('CHANUNAVAIL', 'Channel Unavailable'), ('FAILED', 'Failed')])

    called_number = fields.Char(string="Called Number") # Customer Number (Outgoing Calls), Operator Number (Incoming Calls)
    caller_number = fields.Char(string="Caller Number") # Customer Number (Incoming Calls), Operator Number (Outgoing Calls)
    agent_number = fields.Char(string="Number of Agent") #AgentNumber

    recording_url = fields.Char(string="Recording")
    
    call_start_time = fields.Datetime(string="Start Time")
    call_end_time = fields.Datetime(string="End Time")
    dtmf = fields.Char(string="DTMF Sequence")
    transferred_number = fields.Char("Transferred Number")

    extension_number = fields.Char(string="Extension Number") #Not present in data received by voxbay api
    destination_number = fields.Char(string="Destination Number") #Not present in data received by voxbay api
    caller_id = fields.Char(string="Caller ID") #Not present in data received by voxbay api
    conversation_duration = fields.Integer("Conversation Duration")

    operator_employee_id = fields.Many2one('hr.employee', string="Operator Employee", compute="_compute_operator_employee_id", store=True, readonly=False)

    lead_id = fields.Many2one('crm.lead', string="Lead")
    @api.depends('agent_number')
    def _compute_operator_employee_id(self):
        for record in self:
            if record.agent_number:
                operator_employee = self.env['hr.employee'].sudo().search([('agent_number','=',record.agent_number)], limit=1)
                if operator_employee:
                    record.operator_employee_id = operator_employee[0].id
                    continue
            record.operator_employee_id = False

    @api.model_create_multi
    def create(self, vals):
        res = super().create(vals)
        lead = []
        for record in res:
            if record.call_type == 'incoming':
                lead = self.env['crm.lead'].sudo().search([('phone','like',record.caller_number)], limit=1)
                contact_number = record.caller_number
            elif record.call_type == 'outgoing':
                lead = self.env['crm.lead'].sudo().search([('phone','like',record.called_number)], limit=1)
                contact_number = record.called_number
            if lead:
                record.lead_id = lead[0].id
            else:
                record.lead_id = self.env['crm.lead'].create({
                    'name': contact_number,
                    'phone': contact_number,
                }).id
        return res
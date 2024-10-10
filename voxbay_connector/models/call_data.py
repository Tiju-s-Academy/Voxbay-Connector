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
    total_call_duration = fields.Char(string="Duration", readonly=True)
    call_date = fields.Datetime(string="Call Date")
    call_status = fields.Selection(string="Call Status", selection=[('Connected', 'Connected'), ('Not Connected', 'Not Connected'), ('Cancel', 'Cancel'), ('NOANSWER', 'No Answer'), ('BUSY', 'BUSY'), ('CONGESTION', 'Congestion'), ('CHANUNAVAIL', 'Channel Unavailable'), ('FAILED', 'Failed')])

    # Incoming
    called_number = fields.Char(string="Called Number") # Customer Number (Outgoing Calls), Operator Number (Incoming Calls)
    caller_number = fields.Char(string="Caller Number") # Customer Number (Incoming Calls), Operator Number (Outgoing Calls)
    agent_number = fields.Char(string="Number of Agent") #AgentNumber

    recording_url = fields.Char(string="Recording")
    
    call_start_time = fields.Datetime(string="Start Time")
    call_end_time = fields.Datetime(string="End Time")
    dtmf = fields.Char(string="DTMF Sequence")
    transferred_number = fields.Char("Transferred Number")

    # Outgoing
    extension_number = fields.Char(string="Extension Number") #Not present in data received by voxbay api
    destination_number = fields.Char(string="Destination Number") #Not present in data received by voxbay api
    caller_id = fields.Char(string="Caller ID") #Not present in data received by voxbay api
    conversation_duration = fields.Char("Conversation Duration")


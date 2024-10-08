from odoo import models,fields,api

class VoxbayCallData(models.Model):
    _name = "voxbay.call.data.record"
    call_uuid = fields.Char(string="Call UUID")
    call_type = fields.Selection(string="Call Type", selection=[('incoming', 'Incoming Call'), ('outgoing', 'Outgoing Call')])
    event_status = fields.Selection(string="Event Status", selection=[('agent_received_call', 'Agent Received Call'), ('agent_answered_call', 'Agent Accepted Call'), ('agent_initiated_call', 'Agent Initiated Call'), ('call_ended', 'Call Ended')])
    total_call_duration = fields.Char(string="Call Duration", readonly=True)
    call_date = fields.Datetime(string="Call Date")
    call_status = fields.Selection(string="Call Status", selection=[('ANSWERED', 'ANSWERED'), ('BUSY', 'BUSY'), ('NOANSWER', 'NOANSWER'), ('CONGESTION', 'CONGESTION'), ('CHANUNAVAIL', 'CHANUNAVAIL'), ('CANCEL', 'CANCEL')])

    # Incoming
    called_number = fields.Char(string="Customer Called Number")
    caller_number = fields.Char(string="Customer Number")
    agent_number = fields.Char(string="Number of Agent")

    recording_url = fields.Char(string="Recording URL")
    
    call_start_time = fields.Datetime(string="Call Start Time")
    call_end_time = fields.Datetime(string="Call End Time")
    dtmf = fields.Char(string="DTMF Sequence")
    transferred_number = fields.Char("Transferred Number")

    # Outgoing
    extension_number = fields.Char(string="Extension Number")
    destination_number = fields.Char(string="Destination Number")
    caller_id = fields.Char(string="Caller ID")
    conversation_duration = fields.Char("Call Conversation Duration")


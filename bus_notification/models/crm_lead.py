from odoo import models, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def broadcast_notification(self):
        channel = 'broadcast'
        notification_type = 'simple_notification'
        message = {'title': 'Demo notification', 'message': 'Hello World', 'sticky': True}
        self.env['bus.bus']._sendone(channel, notification_type, message)
        return True



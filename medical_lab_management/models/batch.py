from odoo import models, fields, _
from odoo.exceptions import UserError


class Batch(models.Model):
    _name = 'lab.createbatch'
    _description = "Create Batch For Tests."
    _rec_name = 'batch_name'

    batch_name = fields.Char(string="Name", required=True, help="batch name")
    collected_sample = fields.Many2many('lab.request',domain=(['|', ('state', '=', 'sample_collection'), ('state', '=', 'completed')]))
    state = fields.Selection([('draft','Draft'), ('confirm','Confirm'), ('dispatch','Dispatch'), ('received','Received')], required=True, default='draft')



    def confirm_batch(self):
        if self.collected_sample:
            return self.write({'state': 'confirm'})
        else:
            raise UserError(_('Please Select samples.'))


    def dispatch_batch(self):
        return self.write({'state': 'dispatch'})
    
    def receive_batch(self):
        return self.write({'state': 'received'})


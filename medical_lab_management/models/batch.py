from odoo import models, fields, _
from odoo.exceptions import UserError


class Batch(models.Model):
    _name = 'lab.createbatch'
    _description = "Create Batch For Tests."
    _rec_name = 'batch_name'
    _order = 'write_date DESC'

    batch_name = fields.Char(string="Name", required=True, help="batch name")
    collected_sample = fields.Many2many('lab.request')
    state = fields.Selection([('draft','Draft'), ('confirm','Confirm'), ('dispatch','Dispatch'), ('received','Received')], required=True, default='draft')

    def confirm_batch(self):
        confirm_batch = self.env['lab.request'].search([])
        act_domain1 = [
            ("name", "=",self.collected_sample.name),
        ]
        records1 = confirm_batch.search(act_domain1)
        records1.assign_batch = 'confirm'
        return self.write({'state': 'confirm'})

    def dispatch_batch(self):
        return self.write({'state': 'dispatch'})
    
    def receive_batch(self):
        return self.write({'state': 'received'})


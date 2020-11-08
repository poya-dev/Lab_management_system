from odoo import models, fields


class Batch(models.Model):
    _name = 'lab.createbatch'
    _description = "lab.createbatch"

    batch_name = fields.Char(string="Name", required=True, help="batch name")
    collected_sample = fields.Many2many('lab.request')
    state = fields.Selection([('draft','Draft'), ('confirm','Confirm'), ('dispatch','Dispatch'), ('received','Received')], required=True, default='draft')



    def confirm_batch(self):
        return self.write({'state': 'confirm'})

    def dispatch_batch(self):
        return self.write({'state': 'dispatch'})
    
    def receive_batch(self):
        return self.write({'state': 'received'})


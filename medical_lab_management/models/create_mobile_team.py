from odoo import models, fields, api, _


class CreateMobileTeam(models.Model):
    _name = 'lab.createmobileteam'
    _description = "lab.createmobileteam"

    name = fields.Char(string="Name")
    member = fields.Many2many('res.users', string="Members")
    duty_state = fields.Selection([('waiting','Waiting'), ('on_duty','On_Duty')], default='waiting')


    # def confirm_batch(self):
    #     return self.write({'state': 'confirm'})

    # def dispatch_batch(self):
    #     return self.write({'state': 'dispatch'})
    
    # def receive_batch(self):
    #     return self.write({'state': 'received'})

    # def returned(self):
    #     return self.write({'state': 'returned'})




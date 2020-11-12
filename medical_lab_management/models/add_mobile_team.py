from odoo import models, fields


class MobileTeam(models.Model):
    _name = 'lab.mobileteam'
    _description = "lab.mobileteam"

    team_name = fields.Char(string="Name", required=True, help="team name")
    patients_requested = fields.Many2many('lab.request', domain=([('mobile_team', '=', 'y')]))
    state = fields.Selection([('draft','Draft'), ('confirm','Confirm'), ('dispatch','Dispatch'), ('received','Received'), ('returned', 'Returned')], required=True, default='draft')


    def confirm_batch(self):
        return self.write({'state': 'confirm'})

    def dispatch_batch(self):
        return self.write({'state': 'dispatch'})
    
    def receive_batch(self):
        return self.write({'state': 'received'})

    def returned(self):
        return self.write({'state': 'returned'})




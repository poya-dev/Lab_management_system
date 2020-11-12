from odoo import models, fields, api, _


class AssignTeam(models.Model):
    _name = 'lab.assignteam'
    _description = "lab.assignteam"

    team = fields.Many2one('lab.createmobileteam')
    patient = fields.Many2many('lab.patient', domain=[('mobile_team_request','=','y')])
    state = fields.Selection([('draft','Draft'), ('assign','Assign'), ('return','returned')], default='draft')


    def assign_team(self):
        return self.write({'state': 'assign'})

    def return_team(self):
        return self.write({'state': 'return'})
    
    # def receive_batch(self):
    #     return self.write({'state': 'received'})

    # def returned(self):
    #     return self.write({'state': 'returned'})




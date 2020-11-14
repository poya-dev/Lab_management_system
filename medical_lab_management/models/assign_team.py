from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AssignTeam(models.Model):
    _name = 'lab.assignteam'
    _description = "lab.assignteam"
    _rec_name = 'team'

    team = fields.Many2one('lab.createmobileteam', domain=[('duty_state', '=', 'waiting')])


    patient = fields.Many2many('lab.patient', domain=[('mobile_team_request','=','y'), ])


    state = fields.Selection([('draft','Draft'), ('assign','Assign'), ('return','returned')], default='draft')



    def assign_team(self):
        team_name = self.team.name
        test_obj = self.env["lab.createmobileteam"].search([])
        act_domain = [
            ("name", "=", team_name),
        ]
        records = test_obj.search(act_domain)
        if records.duty_state =='on_duty':
            raise UserError(_('This team is on duty, please select another one.'))
        else:
            records.duty_state = 'on_duty'
            return self.write({'state': 'assign'})

    def return_team(self):
        t_name = self.team.name
        test_obj = self.env["lab.createmobileteam"].search([])
        act_domain = [
            ("name", "=", t_name),
        ]
        records = test_obj.search(act_domain)
        records.duty_state = 'waiting'
        return self.write({'state': 'return'})

            
    # def receive_batch(self):
    #     return self.write({'state': 'received'})

    # def returned(self):
    #     return self.write({'state': 'returned'})




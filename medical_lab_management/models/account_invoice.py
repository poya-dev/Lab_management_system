# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Anusha P P @ cybrosys and Niyas Raphy @ cybrosys(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api,_
from odoo.exceptions import UserError


class LabRequestInvoices(models.Model):
    _inherit = 'account.move'

    is_lab_invoice = fields.Boolean(string="Is Lab Invoice")
    lab_request = fields.Many2one('lab.appointment', string="Lab Appointment", help="Source Document")
    lab_status = fields.Selection([('lab_request', 'Lab Requested')])
    appointment_lines = fields.One2many('lab.appointment.lines', 'test_line_appointment', string="Test Request")


    def action_invoice_paid(self):
        res = super(LabRequestInvoices, self).action_invoice_paid()
        lab_app_obj = self.env['lab.appointment'].search([('id', '=', self.lab_request.id)])
        for obj in lab_app_obj:
            obj.write({'state': 'to_invoice'})
        return res

    
    def action_request(self):
        tname = self.lab_request.id

        test_obj = self.env["lab.appointment"].search([])
        act_domain = [
            ("id", "=", tname),
        ]
        records = test_obj.search(act_domain)

        valueee = records.appointment_lines
        
        for v in valueee:


                data1 = self.env['lab.appointment'].search([('name', '=', self.lab_request.name)])
                name1 = data1.name
                mobile_team1 = data1.mobile_team
                llid = data1.id
                
                patient_id1 = data1.patient_id.id
                appointment_date1 = data1.appointment_date
            
                data = self.env['lab.test'].search([('lab_test', '=', v.lab_test.lab_test)])
                self.env['lab.request'].create({'lab_request_id': name1,
                                                'mobile_team': mobile_team1,
                                                'app_id': llid,
                                                'lab_requestor': patient_id1,
                                                'lab_requesting_date': appointment_date1,
                                                'test_request': data.id,
                                                'request_line': [(6, 0, [x.id for x in data.test_lines])],
                                                })

                print([(6, 0, [x.id for x in data.test_lines])])
                data1.state = 'request_lab'
                self.lab_status = 'lab_request'

    
    def sticker_barcode_generator(self):
        pass
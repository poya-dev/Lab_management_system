from odoo import models, fields, api
from datetime import date


class Summary(models.Model):
    _name = 'lab.summary'
    _description = "lab.summary"

    no_of_visitor = fields.Integer(string="No of visitor", compute='count_visitor')
    no_of_appointment = fields.Integer(string='No of Appointment', compute='count_total_appoitment')
    no_of_todays_appointment = fields.Integer(string='To-Day Appointment',compute='count_today_appoitment')
    total_amount_of_payment = fields.Float(string='Total Payment', compute='count_total_payment')
    total_amount_paid = fields.Float(string='Total Amount Paid', compute='count_total_amount_paid')
    total_due_amount = fields.Float(string='Total Due Amount',compute='count_total_due_amount')
    total_discount = fields.Float(string='Total Discounts',compute='count_total_discount')
    no_of_test = fields.Integer(string='Total No of Test',compute='count_test')
    no_of_completed_test = fields.Integer(string='completed Test',compute='count_completed_test')
    no_of_inprogress_test = fields.Integer(string='inprogress Test',compute='count_inprogress_test')
    unique_ident = fields.Integer(string="record id")

    @api.depends('no_of_visitor')
    def count_visitor(self):
        test_obj = self.env["lab.patient"].search([])
        no_of_count = len(test_obj)
        
        print('--------------------------------------------------')
        print(no_of_count)
        
        self.no_of_visitor = no_of_count

    @api.depends('no_of_appointment')
    def count_total_appoitment(self):
        test_obj = self.env["lab.appointment"].search([])
        no_of_count = len(test_obj)
        self.no_of_appointment = no_of_count

    @api.depends('no_of_todays_appointment')
    def count_today_appoitment(self):
        today = date.today
        test_obj = self.env["lab.appointment"].search([])
        no_of_count = len(test_obj)
        self.no_of_todays_appointment = no_of_count

    @api.depends('total_amount_of_payment')
    def count_total_payment(self):
        total = 0
        test_obj = self.env["account.move"].search([])
        for record in test_obj:
            total = total + record.amount_total
        self.total_amount_of_payment = total

    
    @api.depends('total_amount_paid')
    def count_total_amount_paid(self):
        total = 0
        test_obj = self.env["account.move"].search([('payment_state', '=', 'paid')])
        for record in test_obj:
            total = total + record.amount_total
        self.total_amount_paid = total

    
    @api.depends('total_due_amount')
    def count_total_due_amount(self):
        total = 0
        test_obj = self.env["account.move"].search([('payment_state', '=', 'not_paid')])
        for record in test_obj:
            total = total + record.amount_total
        self.total_due_amount = total


    @api.depends('total_discount')
    def count_total_discount(self):
        self.total_discount = 0.0



    @api.depends('no_of_test')
    def count_test(self):
        test_obj = self.env["lab.request"].search([])
        no_of_count = len(test_obj)
        self.no_of_test = no_of_count

    @api.depends('no_of_completed_test')
    def count_completed_test(self):
        test_obj = self.env["lab.request"].search([('state', '=', 'completed')])
        no_of_count = len(test_obj)
        self.no_of_completed_test = no_of_count
    
    @api.depends('no_of_inprogress_test')
    def count_inprogress_test(self):
        test_obj = self.env["lab.request"].search([('state', '=', 'test_in_progress')])
        no_of_count = len(test_obj)
        self.no_of_inprogress_test = no_of_count


    




        

        
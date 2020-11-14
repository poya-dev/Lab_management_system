from odoo import http
from odoo.http import request
import base64

class labpatientForm(http.Controller):
    # mention class name
    @http.route(['/book-appointment/form'], type='http', auth="user", website=True)
    # mention a url for redirection.
    # define the type of controller which in this case is ‘http’.
    # mention the authentication to be either public or user.
    def index(self, **post):
        return request.render("medical_lab_management.tmp_patient_form", {})

    @http.route(['/patient/form/submit'], type='http', auth="user", website=True)
    # next controller with url for submitting data from the form#
    def save_test_appointment(self, **post):
        partner_id = request.env['res.partner'].sudo().create({
            'name': post.get('patient')
        })

        patient = request.env['lab.patient'].sudo().create({
            'patient': partner_id.id,
            'title': post.get('title'),
            'gender': post.get('gender'),
            'dob': post.get('dob'),
            'blood_group': post.get('blood_group'),
            'visa_info': post.get('visa_info'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'mobile_team_request': post.get('mobile_team'),
        })

        vals = {
            'patient': patient,
        }
        
        return request.render("medical_lab_management.tmp_patient_form_success", vals)

    @http.route(['/view-lab-result'], type='http',  auth="user", website=True)
    def lab_result(self, **kw):
        
        lab_patient = http.request.env['lab.patient'].sudo()
        patient_ids = lab_patient.search([('create_uid', '=', request.uid)]).patient.ids
        lab_request = http.request.env['lab.request'].sudo()
        lab_results = []
        
        for pid in patient_ids:
            pdf = lab_request.search([('lab_requestor.patient', '=', pid)])
            lab_results.append(pdf)        
        
        return http.request.render('medical_lab_management.index', {
            'lab_result': lab_results,

        })





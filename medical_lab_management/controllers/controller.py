from odoo import http
from odoo.http import request


class labpatientForm(http.Controller):
    # mention class name
    @http.route(['/patient/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):

        return request.render("medical_lab_management.tmp_patient_form", {})

    @http.route(['/patient/form/submit'], type='http', auth="user", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):

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
            'email': post.get('email')
        })

        vals = {
            'patient': patient,
        }
        return request.render("medical_lab_management.tmp_patient_form_success", vals)


class ViewPatient(http.Controller):
    @http.route(['/record/view'], type='http',  auth="user", website=True)
    def index(self, **kw):
        patient = http.request.env['lab.patient'].sudo()
        print("****************************************Hello ***********************************")
        return http.request.render('medical_lab_management.index', {
            'patient': patient.search([('create_uid', '=', request.uid)])

        })

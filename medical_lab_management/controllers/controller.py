from odoo import http
from odoo.http import request
import base64
# from odoo import pdfhttpheaders
# from odoo import pdf


# class PartnerForm(http.Controller):
#     @http.route(['/customer/form'], type='http', auth="public", website=True)
#      def partner_form(self, **post):
#          return request.render("medical_lab_management.tmp_customer_form", {})

#     @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
#      def customer_form_submit(self, **post):
#         customer = request.env['medical_lab_management.customer'].create({
#             'name': post.get('name'),
#             'last_name': post.get('last_name'),
#             'email': post.get('email'),
#             'password': post.get('password')
#         })
#         vals = {
#             'customer': customer,
#         }
#          return request.render("medical_lab_management.tmp_customer_form_success", vals)


class labpatientForm(http.Controller):
    # mention class name
    @http.route(['/patient/form'], type='http', auth="user", website=True)
    # mention a url for redirection.
    # define the type of controller which in this case is ‘http’.
    # mention the authentication to be either public or user.
    def partner_form(self, **post):
        # create method
        # this will load the form webpage
        return request.render("medical_lab_management.tmp_patient_form", {})

    @http.route(['/patient/form/submit'], type='http', auth="user", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):

        partner_id = request.env['res.partner'].sudo().create({
            'name': post.get('patient')
        })

        patient = request.env['lab.patient'].sudo().create({
            'patient': partner_id.id,
            # 'patient_image': post.get('patient_image'),
            # 'patient_id': post.get('patient_id'),
            # 'name': lambda self: _('New'),
            'title': post.get('title'),
            # 'emergency_contact': post.get('emergency_contact'),
            'gender': post.get('gender'),
            'dob': post.get('dob'),
            # 'age': post.get('age'),
            'blood_group': post.get('blood_group'),
            'visa_info': post.get('visa_info'),
            # 'id_proof_number': post.get('id_proof_number'),
            # 'note': post.get('note'),
            # 'date': post.get('date'),
            'phone': post.get('phone'),
            'email': post.get('email')
        })

        vals = {
            'patient': patient,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("medical_lab_management.tmp_patient_form_success", vals)
        #finally send a request to render the thank you page#

        # @http.route(['/shop/print'], type='http', auth="public", website=True)


class ViewPatient(http.Controller):
    @http.route(['/record/view'], type='http',  auth="user", website=True)
    def index(self, **kw):

        lab_patient = http.request.env['lab.patient'].sudo()
        print("****************************************Hello ***********************************")


        patient_id = lab_patient.search([('create_uid', '=', request.uid)]).patient.id
        lab_request = http.request.env['lab.request'].sudo()
        pdf = lab_request.search([('lab_requestor.patient', '=', patient_id)])


        return http.request.render('medical_lab_management.index', {
            'lab_result': pdf,
        })


class Print(http.Controller):
    @http.route('/print/print', csrf=False, type='http', auth="user", website=True)
    def index(self, **kw):
        patient = http.request.env['lab.patient'].sudo()
        print("****************************************Hello ***********************************")
        return http.request.render('medical_lab_management.report_patient_labtest', {
            'patient': patient.search([])


        })

    # def print_id(self, **kw):
    #     record_id = http.request.env['lab.patient'].sudo()
    #     record_id = kw['patient_id']

    #     print(record_id)
    #     print("***************************************PRINT METHOD ***********************************")

    #     print(kw)
    #     if record_id:
    #         pdf = request.env['lab.patient'].sudo().get_pdf(
    #             [record_id], 'medical_lab_management.report_patient_labtest', data=None)
    #         pdfhttpheaders = [('Content-Type', 'application/pdf'),
    #                           ('Content-Length', len(pdf))]
    #         return request.make_response(pdf, headers=pdfhttpheaders)
    #     else:
    #         return request.redirect('/')

# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         Teachers = http.request.env['academy.teachers']
#         return http.request.render('academy.index', {
#             'teachers': Teachers.search([])
#         })

# class ViewPatient(http.Controller):
#     @http.route('/record/view/', type='http', auth='public', website=True)
#     def index(self, **kw):
#         return "Hello, world  how are you!!!!!!!"

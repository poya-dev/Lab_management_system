# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
from odoo.addons.ehcs_qr_code_base.models.qr_code_base import generate_qr_code


class QRCodePatient(models.Model):
    _inherit = 'lab.patient'

    qr_image = fields.Binary("Patient QR Code", compute='_generate_qr_code')
    def _generate_qr_code(self):
        self.qr_image = generate_qr_code(self.name)

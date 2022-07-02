# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteDepartement(models.Model):
    _name = 'universite.departement'

    name = fields.Char()
    code = fields.Char()
    professor_ids = fields.One2many(comodel_name="universite.professor",inverse_name="departement_id")
    subject_ids = fields.One2many(comodel_name="universite.subject",inverse_name="departement_id")
    student_ids = fields.One2many(comodel_name="universite.student",inverse_name="departement_id")
    classroom_ids = fields.One2many(comodel_name="universite.classroom",inverse_name="departement_id")
   

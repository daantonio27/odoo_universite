# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteSubject(models.Model):
    _name = 'universite.subject'

    name = fields.Char()
    code = fields.Char()
    professor_ids = fields.One2many(comodel_name="universite.professor",inverse_name="subject_id")
    departement_id = fields.Many2one("universite.departement")
    classroom_ids = fields.Many2many(comodel_name="universite.classroom",
                                     relation="class_subject_rel",
                                     column1="name",
                                     column2="classroom_name",
                                     )
    
   

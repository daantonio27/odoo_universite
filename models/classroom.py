# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteClassroom(models.Model):
    _name = 'universite.classroom'

    classroom_name = fields.Char(string="name")
    code = fields.Char("")
    student_ids = fields.One2many(comodel_name="universite.student",inverse_name="classroom_id")
    departement_id = fields.Many2one("universite.departement",inverse_name="classroom_ids")
    professor_ids = fields.Many2many(comodel_name="universite.professor",
                                     relation="class_prof_rel",
                                     column1="classroom_name",
                                     column2="f_name",
                                     )
    subject_ids = fields.Many2many(comodel_name="universite.subject",
                                     relation="class_subject_rel",
                                     column1="classroom_name",
                                     column2="name",
                                     )

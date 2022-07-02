# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteProfessor(models.Model):
    _name = 'universite.professor'

    f_name = fields.Char("Nom")
    l_name = fields.Char("Prénom")
    sexe   = fields.Selection([("homme","Homme"),("femme","Femme")])
    cni = fields.Char("carte ")
    value2 = fields.Float(compute="_value_pc", store=True)
    address = fields.Text()
    birthday = fields.Date()
    #start_date = fields.Datetime("start date")
    email = fields.Char()
    phone = fields.Char()
    subject_id = fields.Many2one("universite.subject")
    departement_id = fields.Many2one("universite.departement")
    classroom_ids = fields.Many2many(comodel_name="universite.classroom",
                                     relation="prof_class_rel",
                                     column1="f_name",
                                     column2="classroom_name",
                                     )

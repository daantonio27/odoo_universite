# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteStudent(models.Model):
    _name = 'universite.student'

    f_name = fields.Char("Nom")
    l_name = fields.Char("Prénom")
    sexe   = fields.Selection([("homme","Homme"),("femme","femme")])
    cni = fields.Char("carte ")
    address = fields.Text()
    birthday = fields.Date()
    #registration_date = fields.Datetime()
    email = fields.Char()
    phone = fields.Char()
    departement_id = fields.Many2one("universite.departement")
    classroom_id = fields.Many2one("universite.classroom")

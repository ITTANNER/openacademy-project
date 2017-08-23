from openerp import fields, models


'''
This module create model of Course 2
'''


class Course(models.Model):

    '''
    This class create model of Course
    '''
    #  Model odoo name
    _name = 'openacademy.course'
    #  Field reserved to identified name rec
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session',
                                  'course_id', string="Sessions")

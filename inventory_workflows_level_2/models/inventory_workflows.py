from odoo import api, fields, models

_STATES = [
    ('draft', 'Draft'),
    ('to_approve', 'To Approve'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
  
    ('done', 'Done')
]


class Picking1(models.Model):
    _inherit = "stock.picking"        
         
    
    
    state = fields.Selection([
        ('draft', 'Draft'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('acc','Accountant'),
        ('sic','Store In-charge'),
        ('assigned', 'Available'), 
         
        ('approved1', '1st Approval'),
        ('approval','Final Approval'),
        ('done', 'Done')], string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, track_visibility='onchange',)
     
     
  
    @api.multi
    def button_seniorac(self):
        self.write({'state':'approval'})
    
    @api.multi    
    def button_apprinvent(self):
        return self.do_new_transfer()
         
         
   

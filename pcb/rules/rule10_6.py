# -*- coding: utf-8 -*-

from rules.rule import *

class Rule(KLCRule):
    """
    Create the methods check and fix to use with the kicad_mod files.
    """
    def __init__(self, module):
        super(Rule, self).__init__(module, 'Rule 10.6', 'Attributes is set to the appropriate value, see tooltip for more information.')

    def check(self):
        """
        Proceeds the checking of the rule.
        The following variables will be accessible after checking:
            * pth_count
            * smd_count
        """
        module = self.module
        self.pth_count = len(module.filterPads('thru_hole'))
        self.smd_count = len(module.filterPads('smd'))

        if (self.pth_count > self.smd_count and module.attribute != 'pth'):
            self.verbose_message=self.verbose_message+"There are mode THT-pads ({0}) than SMD-pads ({1}), but the attribute is not set to 'pth', but '{2}'. ".format(self.pth_count,self.smd_count, module.attribute)
            return True
        
        if (self.smd_count > self.pth_count and module.attribute != 'smd'):
            self.verbose_message=self.verbose_message+"There are mode SMD-pads ({1}) than THT-pads ({0}), but the attribute is not set to 'smd', but '{2}'. ".format(self.pth_count,self.smd_count, module.attribute)
            return True

        return False

    def fix(self):
        """
        Proceeds the fixing of the rule, if possible.
        """
        module = self.module
        if self.check():
            if self.pth_count > self.smd_count:
                module.attribute = 'pth'
            elif self.smd_count > self.pth_count:
                module.attribute = 'smd'

# -*- coding: utf-8 -*-

from rules.rule import *

class Rule(KLCRule):
    """
    Create the methods check and fix to use with the kicad_mod files.
    """
    def __init__(self, module):
        super(Rule, self).__init__(module, 'Rule 10.3', 'Keywords are separated by spaces.')

    def check(self):
        """
        Proceeds the checking of the rule.
        """
        module = self.module
        if module.tags and module.tags.count(',') > 0:
            self.verbose_message=self.verbose_message+"Tags ('{0}') contains commas!\n".format(module.tags)
            return True
        return False

    def fix(self):
        """
        Proceeds the fixing of the rule, if possible.
        """
        module = self.module
        if self.check():
            module.tags = ' '.join(module.tags.replace(' ', '').split(','))

# -*- coding: utf-8 -*-

from rules.rule import *

class Rule(KLCRule):
    """
    Create the methods check and fix to use with the kicad_mod files.
    """
    def __init__(self, module):
        super(Rule, self).__init__(module, 'Rule 6.9', 'Value and reference have a height of 1mm, width of 1mm and thickness of 0.12mm.')
        self.height = 1
        self.width = 1
        self.thickness = 0.12

    def check(self):
        """
        Proceeds the checking of the rule.
        """
        module = self.module
        if (module.reference['font']['height'] != self.height or module.value['font']['height'] != self.height or
            module.reference['font']['width'] != self.width or module.value['font']['width'] != self.width or
            module.reference['font']['thickness'] != self.thickness or module.value['font']['thickness'] != self.thickness):
           return True

        return False

    def fix(self):
        """
        Proceeds the fixing of the rule, if possible.
        """
        module = self.module
        if self.check():
            module.reference['font']['height'] = self.height
            module.reference['font']['width'] = self.width
            module.reference['font']['thickness'] = self.thickness

            module.value['font']['height'] = self.height
            module.value['font']['width'] = self.width
            module.value['font']['thickness'] = self.thickness


#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==#
##== @/core/validation ==######################################################
##== Input Validation ==#######################################################

#==============================================================================#

class Verifier:
    def __init__(self):
        pass

    def type(self, value, type):
        """
        Validate input type.

        Args:
        -   value (any): Input value to be validated.
        -   type (type): Expected input type.
        """
        if not isinstance(value, type):
            raise Exception(f"Expected {type} but got {type(value)}")
        else:
            return value
        
    def empty(self, value):
        """
        Validate input emptiness.

        Args:
        -   value (any): Input value to be validated.
        """
        if not value:
            raise Exception(f"Expected non-empty value but got {value}")
        else:
            return value
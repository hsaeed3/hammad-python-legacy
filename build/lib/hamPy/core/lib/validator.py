
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/core/lib/validator ==####################################################
##== Validates inputs, using Pydantic models ==#################################

#==============================================================================#

from pydantic import BaseModel, validator, ValidationError
from typing import Any

class Validator(BaseModel):
    input: Any
    val: str

    @validator('input', pre=True, always=True)
    def validate_input(cls, v, values):
        val = values.get('val')

        if val == 'string':
            if isinstance(v, str):
                return v
            else:
                raise ValueError('input must be a string')

        # Integer validation
        elif val == 'integer':
            if isinstance(v, int):
                return v
            else:
                raise ValueError('input must be an integer')

        # Boolean validation
        elif val == 'bool':
            if isinstance(v, bool):
                return v
            else:
                raise ValueError('input must be a boolean')

        else:
            raise ValueError('Unknown validator type')
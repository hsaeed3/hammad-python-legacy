from pydantic import BaseModel, create_model

class ExtendableBaseModelMeta(type(BaseModel)):
    """Metaclass to enable direct extension of a Pydantic BaseModel."""

    def __new__(cls, name, bases, namespace, **kwargs):
        all_fields = {}
        for base in bases:
            if issubclass(base, BaseModel):
                all_fields.update(base.__fields__)
        namespace.update(all_fields)

        return super().__new__(cls, name, bases, namespace, **kwargs)

class Model(BaseModel, metaclass=ExtendableBaseModelMeta):
    """Base class for extensible Pydantic models."""
    __config__ = None
from pydantic import BaseModel, EmailStr


class LeadSchema(BaseModel):
    ''' Схема для клиента/лида ''' 
    
    email: EmailStr
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class Spost(BaseModel):
    
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class SNewpost(BaseModel):
    
    title: str
    content: str
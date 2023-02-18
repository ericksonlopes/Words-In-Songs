from pydantic import BaseModel


class SetenceFound(BaseModel):
    music: str
    phase: str
    link: str

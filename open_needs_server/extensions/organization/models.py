from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from open_needs_server.database import Base


class OrganizationModel(Base):
    __tablename__ = "organizations"

    def __repr__(self) -> str:
        return self.title

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)

    projects = relationship("ProjectModel", back_populates="organization", lazy='selectin')


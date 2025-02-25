from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import DelcarativeBase, Mapped, mapped_column, relationship

class Base(DelcarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Company(Base):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    postal_code: Mapped[str] 
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    analytics_module: Mapped[bool] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    website: Mapped[str] = mapped_column(nullable=True)    

    def __repr__(self):
        return f"<Company {self.name}>"
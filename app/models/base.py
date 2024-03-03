import uuid
from datetime import datetime

from sqlalchemy import sql
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        if cls.__name__[-1] == "y":
            return f"{cls.__name__.lower()[:-1]}ies"
        return f"{cls.__name__.lower()}s"

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=sql.func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=sql.func.now(),
        onupdate=sql.func.now(),
    )

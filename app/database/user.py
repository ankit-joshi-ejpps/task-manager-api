from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship

from app.database.user_role import UserRole


class User(DeclarativeBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    user_name = Column(String(50), unique = True, nullable = False)
    email = Column(String(100), unique = True, nullable = False)
    full_name = Column(String(100), nullable = False)
    hashed_password = Column(String(255), nullable = False)
    role = Column(Enum(UserRole), default = UserRole.USER, nullable = False)
    is_active = Column(Boolean, default = True)
    is_verified = Column(Boolean, default = False)

    assigned_tasks = relationship("Task", foreign_keys = "Task.assignee_id", back_populates = "assignee")
    created_tasks = relationship("Task", foreign_keys = "Task.created_by_id", back_populates = "creator")

    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    last_login = Column(DateTime(timezone = True), nullable = True)

    def __repr__(self):
        return f"<User(user_name = {self.user_name}, email = {self.email}, full_name = {self.full_name}, role = {self.role})>"

from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship

from app.database.task_priority import TaskPriority
from app.database.task_status import TaskStatus

class Task(DeclarativeBase):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True)
    title = Column(String(200), nullable = False)
    description = Column(Text, nullable = True)
    status = Column(Enum(TaskStatus), default = TaskStatus.TODO, nullable = False)
    priority = Column(Enum(TaskPriority), default = TaskPriority.MEDIUM, nullable = False)
    is_deleted = Column(Boolean, default = False)

    assignee_id = Column(Integer, ForeignKey("users.id"), nullable = True)
    assignee = relationship("User", foreign_keys = [assignee_id], back_populates = "assigned_tasks")
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    creator = relationship("User", foreign_keys = [created_by_id], back_populates = "created_tasks")

    due_date = Column(DateTime(timezone = True), nullable = True)
    completed_at = Column(DateTime(timezone = True), nullable = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

    def __repr__(self):
        return f"<Task(title = {self.title}, status = {self.status}, priority = {self.priority})>"

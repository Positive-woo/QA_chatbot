import datetime
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    DateTime,
    String,
    Text,
)
from typing import List, Optional
from base import Base


class Chat(Base):
    __tablename__ = "chat"

    chat_id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.now)
    host_ip = Column(Text)


class ChatMessage(Base):
    __tablename__ = "chat_message"

    chat_message_id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.now)
    chat_id = Column(Integer, ForeignKey("chat.chiat_id"), nullable=False)
    message_group_id = Column(String(50))
    role_type = Column(String(50), nullable=False)
    message = Column(Text, nullable=False)
    memory = Column(Text)
    use_token = Column(Integer, nullable=False)
    chat = relationship(
        "Chat",
    )

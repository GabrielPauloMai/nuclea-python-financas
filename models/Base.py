from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float, Date, DateTime, Boolean
from datetime import datetime, date
class Base(DeclarativeBase):
    type_annotations_map = {
        int: Integer,
        datetime: DateTime,
        date: Date,
        bool: Boolean,
        float: Float(precision=10,scale=2),
        str: String()
    }
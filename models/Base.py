from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float, Date, DateTime, Boolean
from datetime import datetime, date


class Base(DeclarativeBase):
    type_annotations_map = {
        int: Integer,
        datetime: DateTime,
        date: Date['%d/%m/%Y'],
        bool: Boolean,
        float: Float(10, 2),
        str: String()
    }

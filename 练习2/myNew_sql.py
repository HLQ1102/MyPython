
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker   # 添加会话模块

engine = create_engine(
    'mysql+pymysql://root:123456@192.168.1.50/xia1807?charset=utf8',
    encoding='utf8',
    echo=True
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    stu_num = Column(Integer, primary_key=True)
    stu_name = Column(String(10), unique=True, nullable=False)
    denger = Column(String(6))

    def __str__(self):
        return '学生:%s' % self.stu_name

class Stubasic(Base):
    __tablename__ = 'stubasic'
    num = Column(Integer, primary_key=True)
    stu_id = Column(Integer, ForeignKey('student.stu_num'))
    stu_yuwen = Column(Integer)
    stu_shuxue = Column(Integer)

    def __str__(self):
        return '成绩:%d' % (self.stu_yuwen + self.stu_shuxue)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

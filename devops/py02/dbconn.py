# create database tedu1807 default charset utf8;

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker   # 添加会话模块

engine = create_engine(  # 创建mysql的引擎
    # mysql+pymysql://用户名：密码@数据库地址/数据库/?charset=指定编码方式(允许中文输入)
    'mysql+pymysql://root:123456@127.0.0.1/tedu1807?charset=utf8',
    encoding='utf8',  # 编码
    echo=True  # 在终端打印日志，生产环境要设置为False，默认值为false
)
Session = sessionmaker(bind=engine)   # 将会话绑定到引擎
Base = declarative_base()


class Departments(Base):
    __tablename__ = 'departments'
    dep_id   =  Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return "部门: %s" % self.dep_name


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    gender = Column(String(6))
    phone = Column(String(11))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '员工:%s' % self.emp_name


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    data    = Column(Date)
    emp_id  = Column(Integer, ForeignKey('employees.emp_id'))
    basic   = Column(Integer)
    awards  = Column(Integer)

    def __str__(self):
        return '工资:%s' % self.basic + self.awards

    def __call__(self, *args, **kwargs):
        print('工资:%s' % self.basic + self.awards)


if __name__ == '__main__':
    Base.metadata.create_all(engine)


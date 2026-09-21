# class MyContext:
#     def __enter__(self):
#         print("enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         print("exit")
#         print("异常类型",exc_type)
#         print("异常内容",exc_val)
#
# with MyContext():
#     print("processing...")
#     print(1/0)
from sqlalchemy import true
#
#
# class MyContext:
#     def __enter__(self):
#         print("enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         print("exit")
#         return True
#
# with MyContext():
#     print("processing...")
#     print(1/0)
#
# print("next processing...")

from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("enter")
#
#     yield
#
#     print("exit")
#
# with my_context():
#     print("processing...")


@contextmanager
def open_resource():
    print("打开资源")
    resource = "数据库连接"
    yield resource

    print("关闭资源")

with open_resource() as r:
    print("正在使用：",r)

import time
@contextmanager
def timer():
    start = time.perf_counter()

    try:
        yield
    finally:
        print(time.perf_counter() - start)

with timer():
    print("processing")
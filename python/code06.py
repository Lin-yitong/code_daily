# def normal_func():
#     print("normal 开始")
#     return 10
#
# async def async_normal_func():
#     print("async 开始")
#     return 20
#
# a = normal_func()
# b = async_normal_func()
# print("a = ", a)
# print("b = ", b)

# import asyncio
#
# async def async_func():
#     print("async 开始")
#     return 20
#
# result = asyncio.run(async_func())
# print("result = ",result)

import asyncio
from unittest import result


# async def get_data():
#     print("get_data 开始")
#     await asyncio.sleep(2)
#     print("get_data 结束")
#     return 100
#
#
# async def main():
#     print("main 开始")
#
#     result = await get_data()
#
#     print("result = ",result)
#     print("main 结束")
#
# asyncio.run(main())


async def get_user():
    print("开始获取用户")
    await asyncio.sleep(2)
    print("用户获取完成")
    return "Tom"

async def get_orders():
    print("开始获取订单")
    await asyncio.sleep(3)
    print("订单获取完成")
    return  ["order1", "order2", "order3"]

async def main():
    user = await get_user()
    orders = await get_orders()

    print(user)
    print(orders)

asyncio.run(main())
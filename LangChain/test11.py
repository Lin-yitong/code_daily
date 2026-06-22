# import time
#
# # 同步IO
# def boil_water():
#     print("开始烧水...")
#     time.sleep(5)
#     print("烧水完成...")
#
# def send_msg():
#     print("开始发消息...")
#     time.sleep(2)
#     print("发消息完成...")
#
# def main():
#     # 1. 烧水
#     boil_water()
#     # 2. 发消息
#     send_msg()
#
# main()

# 异步IO

import asyncio

# 协程
async def boil_water_async():
    print("开始烧水...")
    await asyncio.sleep(5)
    print("烧水完成...")

# 协程
async def send_msg_async():
    print("开始发消息...")
    await asyncio.sleep(2)
    print("发消息完成...")

# 协程: 调度
# 事件循环
async def main():
    task1 = asyncio.create_task(boil_water_async())
    task2 = asyncio.create_task(send_msg_async())
    await task1
    await task2

# run 会创建一个时间循环
asyncio.run(main())
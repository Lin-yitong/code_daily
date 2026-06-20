from langchain_core.tools import tool

@tool
def add(a:int, b:int) -> int:
    '''

    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两个整数得到和
    '''
    return a + b


print(add.invoke({"a": 3, "b": 5}))
class Tool:
"""
一些小工具，用于进行数据处理
"""
    def Deduplication(obj_list):
    """
    对列表中的元素去重 （python3 有效）
    """
        return list(set(obj_list))

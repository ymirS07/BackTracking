def BackTracking(params):
  if 【condition】:
    res = 【update】
    return
  for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）):
       【处理节点】
        BackTracking(路径，选择列表)
       【回溯，撤销处理结果】
  

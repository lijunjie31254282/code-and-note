nametotal = ["张三", "李四", "王五", "赵六"]

# 方法1：使用map和lambda
nameadd = list(map(lambda name: "QG_" + name, nametotal))
print("加上统一前缀后的名字:", nameadd)
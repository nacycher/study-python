# 九九乘法表（右上三角形）
for i in range(1, 10):
    for j in range(1, i + 1):
        # 使用end='\t'使输出在同一行，并用制表符分隔
        print(f"{j}×{i}={i*j}", end='\t')
    # 每一行结束后换行
    print()
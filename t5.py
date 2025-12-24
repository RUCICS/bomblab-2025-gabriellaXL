array = [10, 2, 14, 7, 8, 12, 15, 11, 0, 4, 1, 13, 3, 9, 6, 5]

# 计算
for start in range(15):
    current = start
    steps = 0
    total = 0
    visited = set()
    
    while current != 15 and steps < 20 and current not in visited:
        visited.add(current)
        next_val = array[current]
        steps += 1
        total += next_val
        current = next_val
    
    if current == 15 and steps == 14:
        print(f"找到: 起始{start}, {steps}步, 总和{total}")
        # 重新计算显示路径
        current = start
        total2 = 0
        for i in range(14):
            val = array[current]
            total2 += val
            print(f"  步骤{i+1}: array[{current}]={val}, 总和={total2}")
            current = val
        
        # 找到负数
        for x in range(-1, -100, -1):
            if x & 0xF == start:
                print(f"  答案: {x} {total2}")
                break
        break
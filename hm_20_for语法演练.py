for num in [1, 2, 3]:

    print(num)
    if num == 2:
        break
else:
    # 集合内部中的元素遍历完成,且循环体内部没有使用break,else就会执行
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会被执行
    print("会执行吗?")

print("循环结束")
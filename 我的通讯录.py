import function

choice = 1
while(choice):
    menu()
    print("请输入你的选择:",end=' ')
    choice=int(input())
    if choice==0:
        print("使用结束")
        break
    elif choice == 1:
        #添加联系人
        Add()
        continue
    elif choice == 2:
        #展示通讯录
        Show()
        continue
    elif choice == 3:
        #查询联系人
        Search()
        continue
    elif choice == 4:
        #删除联系人
        Dele()
        continue
    elif choice == 5:
        #根据名字首字母进行排序
        Sort()
        continue





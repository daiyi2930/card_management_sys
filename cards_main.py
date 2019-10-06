#TODO（周曦） 完成名片管理系统
import cards_tools

while True:
    cards_tools.show_menu()
    #only when user input break,the xunhuan will be end,other circums the circle will continue
    action_str = input("plz choose the operation you want to use: ")
    print("the operation you choose is : [%s] "%action_str)

    if action_str in ['1','2','3']:
        if action_str =='1':
            cards_tools.new_card()
        elif action_str =='2':
            cards_tools.show_all()
        elif action_str =='3':
            cards_tools.search_card()
    elif action_str =='0':
        print('welcome back.byebye.')
        break
    else:
        print('wrong number,plz choose again')
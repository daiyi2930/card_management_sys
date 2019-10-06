#record all the cards
card_list=[]

def show_menu():
    """show menu"""
    print("*"*50)
    print('welcome to use my system.1.0')
    print('')
    print('1:create new card')
    print('2.show all')
    print('3.search card')
    print('')
    print('0:sign out')
    print("*"*50)

#TODO three tools to instead 3 passes
def new_card():
    """create a new card"""
    print('x'*50)
    name_str=input('name plz:')
    phone_str=input('phone num plz:')
    qq_str=input('qq num plz:')
    email_str=input('mail plz:')
    card_dict={'name':name_str,'phone':phone_str,'qq':qq_str,'email':email_str}
    card_list.append(card_dict)
    print('the card of %s has been created.'%name_str)
    print(card_dict)
    #1.need info from user
    #2.use the input info to create a dictionary
    #3.add the dic to card_list
    #4.tell the user the function has done.

def show_all():
    print('x'*50)
    print("show all cards.")
    if len(card_list)==0:
        print('no card exist here,please use function1.')
    else:
        print("name\t\tphone\t\tqq\t\temail")
        for card_dic in card_list:
            print('%s\t\t%s\t\t%s\t\t%s\t\t'%(card_dic['name'],card_dic['phone'],card_dic['qq'],card_dic['email']))

def search_card():
    print('x'*50)
    print("find a card.")
    name_search=input('plz input the name you want to find: ')
    for card_dic in card_list:
        count=0
        if card_dic['name']==name_search:
            print('we find your card:')
            print(card_dic)
            deal_card(card_dic)
            count+=1 
            break
        else:
            pass
    if count == 0:
        print('sorry,we dont find the card named %s.plz try another name.'%name_search)

def deal_card(find_dic):
    action_str=input('choose:1.change 2.del 0.return to previous step.')
    if action_str=='1':
        find_dic['name']=input_card_info(find_dic['name'],'change name:')
        find_dic['qq']=input_card_info(find_dic['qq'],'change qq:')
        find_dic['phone']=input_card_info(find_dic['phone'],'change phone:')
        find_dic['email']=input_card_info(find_dic['email'],'change email:')
        print('successfully changed the card.')
    elif action_str=='2':
        print('delete card.')
        card_list.remove(find_dic)

def input_card_info(dict_value,tip_message):
    """

    :param dict_value: 如果用户未输入任何参数，返回名片中原参数
    :param tip_message: 提示用户输入需要修改的参数
    :return: return原名片参数或修改参数
    """
    result_str=input(tip_message)
    if len(result_str)>0:
        return result_str
    else:
        return dict_value

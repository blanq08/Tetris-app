from tkinter import *

drink_dict = {(1, "Cocacola"): 2000,
              (2, "Sprite"): 2000,
              (3, "Cafe Americano"): 3000,
              (4, "Water"): 1000,
              (5, "Orange Juice"): 2500}

balance = 0

def show_avail_options():
    global balance
    balance= int(User_option.get())
    balance_label['text']=f'Current balance: {balance}'
    menu['text'] = 'here are available options\n\n'
    money['text']='Choose your drink form above option'
    for key in drink_dict:
#menu['text'] += str(key[0])+ '. ' + key[1] + ' : ' + str(drink_dict[key]) +'\n'
        menu['text'] += f'{str(key[0])}. {key[1]}: {str(drink_dict[key])} \n'
    #buy_btn = Button(window, text='Buy', command = purchase)
    buy_btn['command']=purchase
def purchase():
    global balance
    choice=int(User_option.get())
    drink_dict = {1: 2000,
                  2: 2000,
                  3: 3000,
                  4: 1000,
                  5: 2500}

    for i in range(1,10000000):
        if i != choice:
            continue
        else:
            if i > 5:
                get['text'] = 'Not a choice'
            else:
                    if balance >= int(drink_dict[i]):
                        balance= balance-int(drink_dict[i])
                        print("hi")
                        balance_label['text'] = f'Current balance: {balance}'
                        if i == 1:
                            get['text'] =f'Got one Cocacola'
                        elif i == 2:
                            get['text'] =f'Got one Sprite'
                        elif i == 3:
                            get['text'] =f'Got one Cafe Americano'
                        elif i == 4:
                            get['text'] =f'Got one Water'
                        elif i == 5:
                            get['text'] =f'Got one Orange Juice'
                    else:
                        get['text'] = 'not enough balance'



window = Tk()
menu= Label(window, text='Click below button to insert money and display menu\n')
menu.pack()
money= Label(window, text='Insert Money')
money.pack()
User_option= Entry(window)
User_option.pack()
balance_label= Label(window,text="")
balance_label.pack()
buy_btn= Button(window, text='Buy', command=show_avail_options)
buy_btn.pack()
get = Label(window,text="")
get.pack()


window.mainloop()


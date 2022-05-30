from tkinter import*
import tkinter.messagebox

root = Tk()
root.title('GAME')
root.geometry('400x500+100+100')
root.resizable(width='False',height='False')

label = Label(root, text="TIC TAC TOE",font = "times 22 bold")
label.pack(side = TOP)

frame = Frame(root,bg = 'green')
frame.pack(fill = 'both',expand = True)

m = "times 10 bold"

def game():

    frame1 = Frame(frame,bg = 'green')
    frame1.pack(side=TOP)

    frame2 = Frame(frame,bg = 'green')
    frame2.pack()

    frame4 = Frame(frame,bg = 'green')
    frame4.pack()

    frame3 = Frame(frame,bg = 'green')
    frame3.pack()
    list1 = []


    def show():

        button1 = Button(frame3, text='', height=5, width=10, command=sel1, font=m )
        button2 = Button(frame3, text='', height=5, width=10, command=sel2, font=m)
        button3 = Button(frame3, text='', height=5, width=10, command=sel3, font=m)
        button4 = Button(frame3, text='', height=5, width=10, command=sel4, font=m)
        button5 = Button(frame3, text='', height=5, width=10, command=sel5, font=m)
        button6 = Button(frame3, text='', height=5, width=10, command=sel6, font=m)
        button7 = Button(frame3, text='', height=5, width=10, command=sel7, font=m)
        button8 = Button(frame3, text='', height=5, width=10, command=sel8, font=m)
        button9 = Button(frame3, text='', height=5, width=10, command=sel9, font=m)
        button1.grid(row=0,pady=10)
        button2.grid(row=0, column=1, padx=20)
        button3.grid(row=0, column=2)
        button4.grid(row=1)
        button5.grid(row=1, column=1, pady = 10)
        button6.grid(row=1, column=2)
        button7.grid(row=2)
        button8.grid(row=2, column=1,pady=10)
        button9.grid(row=2, column=2)
        list1.append(button1)
        list1.append(button2)
        list1.append(button3)
        list1.append(button4)
        list1.append(button5)
        list1.append(button6)
        list1.append(button7)
        list1.append(button8)
        list1.append(button9)


    list2 = []
    def setX():
        list2.append('O')
        frame2.destroy()
        label3 = Label(frame4, text='PLAYER 1 : X \nPLAYER 2 : O', font="times 12 bold ",bg = 'green')
        label3.grid()
        show()

    def setO():
        list2.append('X')
        frame2.destroy()
        label3 = Label(frame4, text='PLAYER 1 : O \nPLAYER 2 : X', font="times 12 bold ",bg = 'green')
        label3.grid()
        show()

    def check():
        if (list2[len(list2)-1] == 'X'):
            list2.append('O')
            return 'O'
        else:
            list2.append('X')
            return 'X'

    def check3():
        return (list1[0]['text'] == list1[4]['text'] == list1[8]['text'] and list1[0]['text'] == list1[4]['text'] == list1[8]['text'] != '') or (list1[2]['text'] == list1[4]['text'] == list1[6]['text']  and list1[2]['text'] == list1[4]['text'] == list1[6]['text']!='')

    def check1():
        c= 0
        for i in range(0, 3):
            if (list1[i]['text'] == list1[i + 3]['text'] == list1[i + 6]['text'] and list1[i]['text'] == list1[i + 3]['text'] == list1[i + 6]['text'] != ''):
                c+=1
                break
        if(c==0):
            return False
        else:
            return True

    def check2():
        c=0
        for j in [0, 3, 6]:
            if (list1[j]['text'] == list1[j + 1]['text'] == list1[j + 2]['text']) and (list1[j]['text'] == list1[j + 1]['text'] == list1[j + 2]['text'] != '' ):
                c+=1
                break
        if(c==0):
            return False
        else:
            return True


    def sel1():
        list1[0]['text'] = check()
        list1[0].configure(state='disabled')
        result()

    def sel2():
        list1[1]['text']= check()
        list1[1].configure(state='disabled')
        result()

    def sel3():
        list1[2]['text']= check()
        list1[2].configure(state='disabled')
        result()

    def sel4():
        list1[3]['text']= check()
        list1[3].configure(state='disabled')
        result()

    def sel5():
        list1[4]['text']= check()
        list1[4].configure(state='disabled')
        result()

    def sel6():
        list1[5]['text']= check()
        list1[5].configure(state='disabled')
        result()

    def sel7():
        list1[6]['text']= check()
        list1[6].configure(state='disabled')
        result()

    def sel8():
        list1[7]['text']= check()
        list1[7].configure(state='disabled')
        result()

    def sel9():
        list1[8]['text']= check()
        list1[8].configure(state='disabled')
        result()

    def Start():

        button_start['text'] = 'Started'
        button_start['fg'] = 'green'
        button_start.configure(state='disabled')

        label2 = Label(frame2, text='player1 choose your input X or O', font="times 12 bold ", bg='green')
        label2.grid(padx=20)

        button_x = Button(frame2, text='X', font="times 12 bold ", height=1, width=5, command=setX)
        button_x.grid(pady=5)
        button_o = Button(frame2, text='O', font="times 12 bold ", height=1, width=5, command=setO)
        button_o.grid(pady=5)


    def pause():
        # button_x.configure(state = 'disabled')
        if(button_start['text']=='Started'):
            if(button_pause['text']=='Continue' ):
                for i in range(0, 9):
                    if(list1[i]['text'] == ''):
                        list1[i]['state'] = 'normal'
                button_pause['text'] = 'Pause'
            else:
                button_pause['text'] = 'Continue'
                for i in range(0,9):
                    list1[i]['state'] = 'disable'
        else:
            tkinter.messagebox.showinfo('Warning',"can't pause without startig a game!")


    button_start = Button(frame1,text  = 'Start',font = "times 12 bold ",fg = 'blue',height  = 2,width = 10,command = Start)
    button_start.configure(state = 'normal')
    button_start.grid(pady=5,row=0)

    button_quit = Button(frame1, text='Quit', font="times 12 bold ", fg='red', height=2, width=10, command=root.destroy) #root.destroy() directl closes the current winow
    button_quit.grid(pady=5,row=0,column=1,padx=15)

    button_pause = Button(frame1, text='Pause', font="times 12 bold ", fg='orange', height=2, width=10,command= pause)
    button_pause.grid(pady=5, row=0, column=2)


    def clearall():
        list2.clear()
        frame3.destroy()
        frame1.destroy()
        frame4.destroy()
        game()

    def result():
        if (check1() or check2() or check3()):
            if(list2[0] != list2[len(list2)-1] ):
                tkinter.messagebox.showinfo('Congrats!',"Player 1 You WON !")
            else:
                tkinter.messagebox.showinfo('Congrats!', "Player 2 You WON !")
            clearall()
        else:
            c=0
            for i in range(0,9):
                if(list1[i]['text']!=''):
                    c+=1
            if(c==9):
                tkinter.messagebox.showinfo('Oops!', "No one won!")
                clearall()
game()

root.mainloop()

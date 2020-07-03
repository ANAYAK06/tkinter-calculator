from tkinter import *

screen = Tk()
screen.title("Calculator")
screen.geometry("311x432")
screen.resizable(0, 0)
screen.iconbitmap("cal.ico")

display = Label(screen,
                background = "#000000",
                fg = "#ffffff",
                font = ("Verdana", 20),
                text = "Display",
                anchor = SE,
                padx = 10,
                pady = 10,
                relief = SUNKEN,
                border = 8,
                width = 16,

                )
display.grid(row = 0, columnspan = 10, )

btn7 = Button(screen, text = 7, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff", )
btn7.grid(row = 1, column = 0, )

btn8 = Button(screen, text = 8, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn8.grid(row = 1, column = 1, )

btn9 = Button(screen, text = 9, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn9.grid(row = 1, column = 3, )

btn_multi = Button(screen, text = '*', font = ("Verdana", 20), padx = 16, pady = 16,
                   relief = GROOVE,
                   border = 4,
                   background = "#000000",
                   fg = "#ffffff",
                   )
btn_multi.grid(row = 1, column = 4, )

btn4 = Button(screen, text = 4, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff", )
btn4.grid(row = 2, column = 0, )

btn5 = Button(screen, text = 5, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn5.grid(row = 2, column = 1, )

btn6 = Button(screen, text = 6, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn6.grid(row = 2, column = 3, )

btn_division = Button(screen,
                      text = chr(247),
                      font = ("Verdana", 19),
                      padx = 16,
                      pady = 16,
                      relief = GROOVE,
                      border = 4,
                      background = "#000000",
                      fg = "#ffffff",
                      )
btn_division.grid(row = 2, column = 4, )

btn1 = Button(screen, text = 1, font = ("Verdana", 18), padx = 19, pady = 18,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff", )
btn1.grid(row = 3, column = 0, )

btn2 = Button(screen, text = 2, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn2.grid(row = 3, column = 1, )

btn3 = Button(screen, text = 3, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              )
btn3.grid(row = 3, column = 3, )

btn_subtract = Button(screen, text = '-', font = ("Verdana", 20), padx = 19, pady = 16,
                      relief = GROOVE,
                      border = 4,
                      background = "#000000",
                      fg = "#ffffff",
                      )
btn_subtract.grid(row = 3, column = 4, )

btn0 = Button(screen, text = 0, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff", )
btn0.grid(row = 4, column = 0, )

btn_cancel = Button(screen, text = 'C', font = ("Verdana", 20), padx = 15, pady = 16,
                    relief = GROOVE,
                    border = 4,
                    background = "#000000",
                    fg = "#ffffff",
                    )
btn_cancel.grid(row = 4, column = 1, )

btn_equal = Button(screen, text = '=', font = ("Verdana", 20), padx = 14, pady = 16,
                   relief = GROOVE,
                   border = 4,
                   background = "#000000",
                   fg = "#ffffff",
                   )
btn_equal.grid(row = 4, column = 3, )

btn_add = Button(screen,
                 text = '+',
                 font = ("Verdana", 20),
                 padx = 14,
                 pady = 16,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 )
btn_add.grid(row = 4, column = 4, )

screen.mainloop()

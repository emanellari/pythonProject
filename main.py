import tkinter as tk
from tkinter import *
from tkinter import Frame, Menu, Button
from tkinter import LEFT, TOP
from tkinter import filedialog, Tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
import customtkinter
import pandas as pd
from dateutil.parser import parse
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from calculations import Mode, Table, Det_he, MostRare, Columns, is_integer, len_max, date_is_quant, auto_options

plt.style.use("ggplot")
from pynput.mouse import Controller
from ttkwidgets.autocomplete import AutocompleteCombobox

mouse = Controller()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "Dark-blue"

# Main Window
root = Tk()
root.title("BEST DATA ENTRY")
root.geometry(f"{1500}x{700}+{0}+{0}")

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)


##################################################################################################################
def save_file_as():
    variables = []
    data = []
    for line in tree.get_children():
        vec = []
        for value in tree.item(line)['values']:
            vec.append(value)
        data.append(vec)
    for column in tree['columns']:
        variables.append(column)
    print(data)
    df = pd.DataFrame(data=data, columns=variables)
    try:
        with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
            df.to_excel(file.name, index=False)
    except:
        print("The user cancelled save")
    return data



def Mode_Result(left2, col, need, Det_he):
    variables = []
    for column in tree['columns']:
        variables.append(column)
    temp = Frame(scrollable_frame4, width=800, height=Det_he(Mode(col)), background="white",
                 highlightbackground="black", highlightthickness=2)
    temp.pack(pady=4)
    Label(temp, text=f'The mode of {variables[need - 1]} is :', bg="white", font="Arial, 15", fg="red").pack()
    for x in Mode(col):
        Label(temp, text=x, bg="white", font="Arial, 15", fg="black").pack()
    # R1.grid(row=0,column=0)





def ds(topl, pieable, count, element, table, to_remember_color):
    i = 0
    for x in table:
        if x == element:
            coni = i
        i = i + 1
    to_remember_color[coni] = askcolor(title="Tkinter Color Chooser")[1]
    # topl.destroy()
    print(f'element={element}')
    for widget in pieable.winfo_children():
        widget.destroy()
    patches, fig = prepare_pie(count, table)
    for i in range(len(to_remember_color)):
        if to_remember_color[i] != "":
            patches[i].set_color(to_remember_color[i])
    chart1 = FigureCanvasTkAgg(fig, pieable)
    chart1.draw()
    chart1.get_tk_widget().pack()
    return to_remember_color


def Full_screen(pieable, count, table, to_remember_color, title_editable):
    fig = Figure(figsize=(4, 3), facecolor="white")  # create a figure object
    patches, texts, autotexts = plt.pie(count, radius=1, labels=table, autopct='%0.1f%%', shadow=True)
    plt.title(title_editable.get())
    for i in range(len(to_remember_color)):
        if to_remember_color[i] != "":
            patches[i].set_color(to_remember_color[i])
    manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()


def prepare_pie(count, table):
    fig = Figure(figsize=(4, 3), facecolor="white")  # create a figure object
    ax = fig.add_subplot(111)  # add an Axes to the figure
    patches, texts, autotexts = ax.pie(count, radius=1, labels=table, autopct='%0.1f%%', shadow=True)
    # ax.legend(patches,table, loc="upper right")
    return patches, fig

def prepare_hist(data):
    fig = Figure(figsize=(4, 3), facecolor="white")  # create a figure object
    ax = fig.add_subplot(111)  # add an Axes to the figure
    hist_obj = ax.hist(data, bins=5, edgecolor='black')

    # Merr disa informacione nga objekti i histogramës
    counts, bin_edges = hist_obj[0], hist_obj[1]
    return bin_edges,fig



def prepare_ring(count, table):
    fig = Figure(figsize=(4, 3), facecolor="white")  # create a figure object
    ax = fig.add_subplot(111)  # add an Axes to the figure
    patches, texts, autotexts = plt.pie(count, radius=1, labels=table, autopct='%0.1f%%', shadow=True,
                                        wedgeprops=dict(width=0.6))
    plt.show()
    return patches, fig


def ring_transform(pieable, count, table, change_color):
    for widgets in pieable.winfo_children():
        widgets.destroy()
    patches, fig = prepare_ring(count, table)
    chart1 = FigureCanvasTkAgg(fig, pieable)
    chart1.draw()
    w = chart1.get_tk_widget()
    w.pack()

def basic_chart_envir(left2, col, need):
        variables = []
        for column in tree['columns']:
            variables.append(column)
        temp = Frame(scrollable_frame4, width=200, height=150, background="white", highlightbackground="black",
                     highlightthickness=2)
        temp.pack(pady=4)
        l = Label(temp, text=f'The pie of {variables[need - 1]}:', bg="white", font="Arial, 15", fg="red")
        l.pack()
        title_editable = Entry(temp, font="arial 14", width=100)

        def temp_text(e):
            title_editable.delete(0, "end")
            title_editable.unbind("<FocusIn>")

        title_editable.pack(padx=20)
        title_editable.insert(0, "Add a title")
        title_editable.bind("<FocusIn>", temp_text)
        # add=Button(temp,text="Add",width=10)
        # add.pack(padx=20)
        pieable = Frame(temp, width=200, height=150, background="white", highlightbackground="black",
                        highlightthickness=2)
        pieable.pack(pady=4)
        return temp,l,title_editable,pieable
def Pie_Result(left2, col, need):
    temp,l,title_editable,pieable=basic_chart_envir(left2,col,need)
    table, count = Table(col)
    patches, fig = prepare_pie(count, table)
    chart1 = FigureCanvasTkAgg(fig, pieable)
    chart1.draw()
    w = chart1.get_tk_widget()
    w.pack()
    table, count = Table(col)

    def label_col(table, to_remember_color):
        topl = Toplevel(pieable)
        topl.title("The color of witch item do you want to choose?")
        topl.geometry("250x70+100+200")
        Label(topl, text="Choose the item").pack()
        color_ops = AutocompleteCombobox(topl, completevalues=table)
        color_ops.insert(0, table[0])
        color_ops.focus()
        color_ops.pack()

        ok = Button(topl, text='ok', command=lambda: ds(topl, pieable, count, color_ops.get(), table, to_remeber_color))
        ok.pack()

    to_remeber_color = []
    for x in table:
        to_remeber_color.append("")
    change_color = Button(temp, text="Change Color", height=2, width=10, bg="WHITE",
                          command=lambda: label_col(table, to_remeber_color))
    change_color.pack(side=LEFT, padx=(30, 10), pady=(0, 10))
    # def show_change_mode_menu():
    #      x, y = change_mode.winfo_rootx(), change_mode.winfo_rooty()
    #      Change_mode_menu.post(x, y)
    # change_mode=Button(temp,text="Change Mode",height=2,width=10,bg="WHITE",command=show_change_mode_menu)
    # change_mode.pack(side=LEFT,padx=(10,10),pady=(0,10))
    # Change_mode_menu=Menu(temp)
    # Change_mode_menu.add_command(label="Ring",command=lambda :ring_transform(pieable,count,table,change_color))

    # download=Button(temp,text="↓",width=4,height=1,bg="white",font="Arial 15",command=fig.savefig('PIE.png'))
    # download.pack(side=LEFT,padx=(10,10),pady=(0,10))
    full_screen = Button(temp, text="⛶", width=4, bg="white", font="Arial 15",
                         command=lambda: Full_screen(pieable, count, table, to_remeber_color, title_editable))
    full_screen.pack(side=LEFT, padx=(10, 10), pady=(0, 10))



def Hist_Result(left2, col, need):
    variables = []
    for column in tree['columns']:
        variables.append(column)
    table, count = Table(col)
    temp = Frame(scrollable_frame4, width=200, height=150, background="white", highlightbackground="black",
                 highlightthickness=2)
    temp.pack(pady=4)
    l = Label(temp, text=f'The pie of {variables[need - 1]}:', bg="white", font="Arial, 15", fg="red")
    l.pack()
    title_editable = Entry(temp, font="arial 14", width=100)

    def temp_text(e):
        title_editable.delete(0, "end")
        title_editable.unbind("<FocusIn>")

    title_editable.pack(padx=20)
    title_editable.insert(0, "Add a title")
    title_editable.bind("<FocusIn>", temp_text)
    # add=Button(temp,text="Add",width=10)
    # add.pack(padx=20)
    pieable = Frame(temp, width=200, height=150, background="white", highlightbackground="black", highlightthickness=2)
    pieable.pack(pady=4)
    data=col
    patches, fig = prepare_hist(data)
    chart1 = FigureCanvasTkAgg(fig, pieable)
    chart1.draw()
    w = chart1.get_tk_widget()
    w.pack()
    table, count = Table(col)
    def label_col(table, to_remember_color):
        topl = Toplevel(pieable)
        topl.title("The color of witch item do you want to choose?")
        topl.geometry("250x70+100+200")
        Label(topl, text="Choose the item").pack()
        color_ops = AutocompleteCombobox(topl, completevalues=table)
        color_ops.insert(0, table[0])
        color_ops.focus()
        color_ops.pack()

        ok = Button(topl, text='ok', command=lambda: ds(topl, pieable, count, color_ops.get(), table, to_remeber_color))
        ok.pack()

    to_remeber_color = []
    for x in table:
        to_remeber_color.append("")
    change_color = Button(temp, text="Change Color", height=2, width=10, bg="WHITE",
                          command=lambda: label_col(table, to_remeber_color))
    change_color.pack(side=LEFT, padx=(30, 10), pady=(0, 10))
    full_screen = Button(temp, text="⛶", width=4, bg="white", font="Arial 15",
                         command=lambda: Full_screen(pieable, count, table, to_remeber_color, title_editable))
    full_screen.pack(side=LEFT, padx=(10, 10), pady=(0, 10))



def Table_Result(left2, col, need):
    variables = []
    for column in tree['columns']:
        variables.append(column)
    temp = Frame(scrollable_frame4, width=800, height=Det_he(Mode(col)), background="white",
                 highlightbackground="black", highlightthickness=2)

    Label(temp, text='TABLE', bg="white", font="Arial, 15", fg="BLUE").grid(row=0, column=0)
    # temp1=Frame(scrollable_frame4,width=800, height=Det_he(Mode(col)),background="black",border=3)
    # temp1.pack(side=LEFT,fill=Y)
    # temp2=Frame(scrollable_frame4,width=800, height=Det_he(Mode(col)),background="black",border=3)
    # temp2.pack(side=LEFT)

    Label(temp, text=f'{variables[need - 1]}', bg="white", font="Arial, 15", fg="RED", width=22, borderwidth=0.5,
          relief="solid").grid(row=1, column=0)
    Label(temp, text="Density", bg="white", font="Arial, 15", fg="RED", width=6, borderwidth=0.5, relief="solid").grid(
        row=1, column=1)
    table, count = Table(col)
    i = 2
    j = 2
    for x in table:
        Label(temp, text=x, bg="white", font="Arial, 15", fg="black", width=22, borderwidth=0.5, relief="solid").grid(
            row=i, column=0)
        i = i + 1
    for x in count:
        Label(temp, text=x, bg="white", font="Arial, 15", fg="black", width=6, borderwidth=0.5, relief="solid").grid(
            row=j, column=1)
        j = j + 1
    temp.pack(pady=4)

def MostRare_Result(left2, col, need):
    variables = []
    for column in tree['columns']:
        variables.append(column)
    temp = Frame(scrollable_frame4, width=800, height=Det_he(MostRare(col)), background="white",
                 highlightbackground="black", highlightthickness=2)
    temp.pack(pady=4)
    Label(temp, text=f'The most rare of {variables[need - 1]} is :', bg="white", font="Arial, 15", fg="red").pack()
    for x in MostRare(col):
        Label(temp, text=x, bg="white", font="Arial, 15", fg="black").pack()
    # R1.grid(row=0,column=0)


def get_obs_values(entries, data):
    this_obs = []
    index = 0
    for e in entries:
        try:
            if len(e.get()) > maxx[index]:
                maxx[index] = len(e.get())
                tree.column(index, minwidth=maxx[index] * 10)
        except:
            tree.column(index, minwidth=40)
        if is_integer(e.get()):
            this_obs.append(float(e.get()))
        else:
            this_obs.append(e.get())
        index = index + 1
    if len(tree.get_children()) % 2 == 0:
        tree.insert('', tk.END, values=this_obs, tags=['t2'])
    else:
        tree.insert('', tk.END, values=this_obs, tags=['t1'])
    data.append(this_obs)
    for items in tree.get_children():
        tree.see(items)
    return data


def Plus(info, comm, com_text_box, data):
    if coment == []:
        for d in range(len(data)):
            coment.append([])
    entries = [child for child in scrollable_frame3.winfo_children() if
               isinstance(child, customtkinter.CTkEntry) or isinstance(child, AutocompleteCombobox)]
    checked = [child for child in scrollable_frame3.winfo_children() if isinstance(child, customtkinter.CTkCheckBox)]
    get_obs_values(entries, data)
    index = 0
    for e in entries:
        if not checked[index].get():
            e.delete(0, END)
        index = index + 1
    info.configure(text=f'Observation {len(data) + 1}')
    comm.configure(text=f'Any comment for Observation {len(data) + 1}?')
    temp = com_text_box.get("1.0", END)
    temp.replace('\n', '')
    coment.append(temp)
    com_text_box.delete('1.0', END)
    entries[0].focus_set()
    return data




def AddNewColumn():
    def new_entry_appear(oppss, title):
        keep = customtkinter.CTkCheckBox(master=scrollable_frame3, text='keep', font=('arial', 10))
        keep.grid(row=len(tree['columns']), column=2, sticky='nsew', padx=(20, 0))
        label = customtkinter.CTkLabel(master=scrollable_frame3, text=title[0], font=('arial', 14))
        label.grid(row=len(tree['columns']), column=0, sticky='nsew', padx=(20, 0))
        if oppss == ['']:
            en = customtkinter.CTkEntry(master=scrollable_frame3)
        else:
            en = AutocompleteCombobox(scrollable_frame3, completevalues=oppss)
        go_to_next_entry()
        en.grid(row=len(tree['columns']), column=1, sticky='nsew')

    def add_columns(columns, **kwargs):

        current_columns = list(tree['columns'])
        print('columns')
        print(current_columns)
        current_columns = {key: tree.heading(key) for key in current_columns}
        print(current_columns)
        # Update with new columns
        tree['columns'] = list(current_columns.keys()) + list(columns)
        print(list(current_columns.keys()))
        print(list(columns))
        for key in columns:
            tree.heading(key, text=key, **kwargs)
            tree.column(key, anchor=CENTER)
        # Set saved column values for the already existing columns
        for key in current_columns:
            # State is not valid to set with heading
            state = current_columns[key].pop('state')
            tree.heading(key, **current_columns[key])
            tree.column(key, anchor=CENTER)

    global this_column
    this_column = []
    length = len(tree.get_children(0))
    print(length)
    i = [0]
    n = [1]

    def Complete_it(this_column, length, n):
        if length == 0:
            Finish_it()
        else:
            n[0] = n[0] + 1
            try:
                titlab.configure(text=f"{title[0]} of {items[n[0] - 1]}'s is:")
            except:
                print('')
            if i[0] != length - 1:
                this_column.append(en2.get())
                en2.delete(0, END)
                i[0] = i[0] + 1
                if i[0] == length - 1:
                    confbut.configure(text='Finish')
            elif i[0] == length - 1:
                this_column.append(en2.get())
                Finish_it()
        return this_column

    def TitleConfirm():
        global title
        global oppss
        title = ent1.get()
        ent1.delete(0, END)
        temp = ''.join(enop.get())
        oppss = ''.join(temp).split(',')
        print(oppss)
        title = [title]

        confbut.configure(command=lambda: Complete_it(this_column, length, n))
        optionlab.destroy()
        optionlab2.destroy()
        enop.destroy()
        ent1.destroy()
        global en2
        if oppss == ['']:
            en2 = customtkinter.CTkEntry(master=toadd, height=15, width=25)
        else:
            en2 = AutocompleteCombobox(toadd, completevalues=oppss, height=15, width=25)
        global items
        items = []
        for item in tree.get_children():
            items.append(tree.item(item)['values'][0])

        titlab.configure(text=f"{title[0]} of {items[0]}'s is:")
        en2.configure(width=200, height=40)
        en2.pack(side=TOP)
        if len(tree.get_children()) == 0:
            Finish_it()
        return title, oppss, items

    record = []

    def Finish_it():
        add_columns(title)
        variables.append(title)
        print(variables)
        columnspace.destroy()
        i = 0
        print(this_column)
        for selected_item in tree.get_children():
            item = tree.item(selected_item)
            record.append(item['values'])
            record[i].append(this_column[i])
            i = i + 1
        i = 0
        for xitem in tree.get_children():
            tree.item(xitem, values=record[i])
            i = i + 1
            print(this_column)
        new_entry_appear(oppss, title)

    def Cancel_it():
        columnspace.destroy()

    columnspace = Toplevel(root)
    columnspace.title('Add a new column.')
    columnspace.resizable(0, 0)
    columnspace.geometry('300x200+900+30')
    toadd = Frame(columnspace, width=300, height=150, bg='#d7a7f2', bd=2)
    toadd.place(x=0, y=0)
    toadd.pack_propagate(False)
    toconf = Frame(columnspace, width=300, height=50, bg='white', bd=2)
    toconf.place(x=0, y=150)
    toconf.pack_propagate(False)
    titlab = customtkinter.CTkLabel(master=toadd, fg_color='transparent', text="Write the title of the new column.",
                                    text_color='red', font=('arial', 15), bg_color='#d7a7f2')
    titlab.pack()
    ent1 = customtkinter.CTkEntry(master=toadd)
    ent1.pack()
    optionlab = customtkinter.CTkLabel(master=toadd, fg_color='transparent',
                                       text="Add options separated by comma (',').",
                                       text_color='black', font=('arial', 15), bg_color='#d7a7f2')
    optionlab.pack()
    optionlab2 = customtkinter.CTkLabel(master=toadd, fg_color='transparent', text="(not necessary).",
                                        text_color='black', font=('arial', 15), bg_color='#d7a7f2')
    optionlab2.pack()
    enop = customtkinter.CTkEntry(master=toadd, width=300)
    enop.pack()
    confbut = customtkinter.CTkButton(master=toconf, text='Next', command=TitleConfirm)
    confbut.pack(side=LEFT, padx=10)
    cancbut = customtkinter.CTkButton(master=toconf, text='Cancel')
    cancbut.pack(side=LEFT, padx=10)


def Update(text, item_index, vector):
    temp = ''.join(text.get('2.0', END))
    realend = temp.find("Comment:")
    coment[item_index] = temp[realend + 8:len(temp)]
    temp = temp[:realend]
    vector[0] = ''.join(temp).split(',')
    i = 0
    for x in vector[0]:
        vector[0][i] = vector[0][i].replace("\n", "")
        i = i + 1
    tl.destroy()
    xitem = tree.selection()[0]
    tree.item(xitem, values=vector[0])
    return vector


def Cancel(item_index):
    tl.destroy()


def item_selected(*args):
    def delete_items():
        # Get selected item to Delete
        tl.destroy()
        selected_item = tree.selection()[0]
        tree.delete(selected_item)

    selected_iid = tree.focus()
    item_index = tree.index(selected_iid)
    record = ""
    try:
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            print(record)
    except:
        print("Doesn't exist any selection.")
    if record != "":
        global tl
        tl = Toplevel(table)
        tl.title('Edit the row values separated by ","')
        tl.resizable(0, 0)
        tl.geometry('400x200+600+300')
        ftb = Frame(tl, width=400, height=160, bg='#d7a7f2', bd=2)
        ftb.place(x=0, y=0)
        endtb = Frame(tl, width=400, height=30, bd=2)
        endtb.pack_propagate(False)
        endtb.place(x=0, y=160)
        text = customtkinter.CTkTextbox(ftb, font=('arial', 18, 'bold'), width=370, height=140,
                                        fg_color='transparent')
        text.pack(padx=10)
        temp = '#'.join(map(str, record))
        print(temp)
        vector = [[]]
        vector[0] = ''.join(temp).split('#')
        print('v0')
        print(vector[0])
        update_button = customtkinter.CTkButton(endtb, width=100, text='Update',
                                                command=lambda: Update(text, item_index, vector))
        update_button.pack(side=LEFT, padx=20)
        ok_button = customtkinter.CTkButton(endtb, width=100, text='Cancel', command=lambda: Cancel(item_index))
        ok_button.pack(side=LEFT, padx=20)
        delete_button = customtkinter.CTkButton(endtb, width=100, text='Delete', command=delete_items)
        delete_button.pack(side=LEFT, padx=20)
        final = ''
        i = 0
        text.insert(END, f'Observation:{item_index + 1}')
        text.insert(END, '\n')
        for x in vector[0]:
            if i != len(vector[0]) - 1:
                if len(final + x + ',') < 34:
                    final = final + x + ','
                else:
                    text.insert(END, final)
                    text.insert(END, '\n')
                    final = x + ","
            else:
                if len(final + x) < 34:
                    final = final + x
                    text.insert(END, final)
                else:
                    text.insert(END, final + '\n' + x)
            i = i + 1
        if coment != []:
            if coment[item_index] != []:
                text.insert(END, '\n')
                text.insert(END, f'Comment:{coment[item_index]}')
            else:
                text.insert(END, '\nComment:')
        else:
            text.insert(END, '\nComment:')


def appear_tabview(variables, data):
    col = Columns(data)
    tree.configure(columns=variables, height=18, show='headings')
    print(data)
    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.place(x=3, y=0, width=880)
    for i in range(len(variables)):
        maxx.append(len(variables[i]))
        if data != []:
            tree.column(i, anchor='center', minwidth=len_max(col[i], variables[i]) * 9)
        else:
            tree.column(i, anchor='center', width=len(variables[i]) * 9)
        tree.heading(variables[i], text=variables[i], anchor=CENTER)

    i = 0
    for items in tree.get_children():
        tree.delete(items)
    for d in data:

        if i % 2 == 0:
            tree.insert('', tk.END, values=d, tags=['t2'])
        else:
            tree.insert('', tk.END, values=d, tags=['t1'])
        i = i + 1
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
    ttk.Style().configure("Treeview", background="#988dd9", fieldbackground="#f0afaa", foreground="black", rowheight=30)
    tree.tag_configure('t2', background='white')
    horscrlbar = ttk.Scrollbar(table, orient='horizontal', command=tree.xview)
    horscrlbar.place(x=1, y=580, width=900)
    verscrlbar = ttk.Scrollbar(table, orient='vertical', command=tree.yview)
    verscrlbar.place(x=883, y=0, height=583)
    tree.configure(xscrollcommand=horscrlbar.set, yscrollcommand=verscrlbar.set, style="mystyle.Treeview")

    def prevent_resize(event):
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"

    tree.bind('<Button-1>', prevent_resize)
    tree.bind('<Motion>', prevent_resize)


def move_cursor(event, entry_list, this_index):
    next_index = (this_index + 1) % (len(entry_list))
    entry_list[next_index].focus_set()


def go_to_next_entry():
    entries = [child for child in scrollable_frame3.winfo_children() if
               isinstance(child, customtkinter.CTkEntry) or isinstance(child, AutocompleteCombobox)]
    for idxx, entry in enumerate(entries):
        entry.bind("<Return>", lambda en, idx=idxx: move_cursor(en, entries, idx))


def appear_entries(all_options, variables, data):
    info = customtkinter.CTkLabel(master=scrollable_frame3, fg_color='transparent', text=f'Observation {len(data) + 1}',
                                  text_color='red', font=('arial', 15))
    info.grid(row=0, column=1, sticky='nsew', padx=(0, 20))
    comm = customtkinter.CTkLabel(master=left2.tab("Enter Data"), fg_color='transparent',
                                  text=f'Any comment for Observation {len(data) + 1}?', text_color='red',
                                  font=('arial', 20))
    comm.grid(row=2, column=0, sticky='nsew', pady=5)
    com_text_box = customtkinter.CTkTextbox(master=left2.tab("Enter Data"), fg_color='transparent', text_color='black',
                                            font=('arial', 13), height=40, border_width=2, border_color='red')
    com_text_box.grid(row=3, column=0, sticky='nsew', pady=10, padx=40)
    data = data

    i = 0
    for x in variables:
        lab = customtkinter.CTkLabel(master=scrollable_frame3, text=x, fg_color='transparent', font=('arial', 13))
        lab.grid(row=i + 1, column=0, sticky='nsew', padx=(0, 20))
        keep = customtkinter.CTkCheckBox(master=scrollable_frame3, text='keep', font=('arial', 10))
        keep.grid(row=i + 1, column=2, sticky='nsew', padx=(20, 0))
        if all_options[i] == ['']:
            en = customtkinter.CTkEntry(master=scrollable_frame3)
        else:
            en = AutocompleteCombobox(scrollable_frame3, completevalues=all_options[i])
        go_to_next_entry()
        # en.bind('<Control-Key-p>', lambda: Plus(info, comm, com_text_box))
        # en.bind('<Control-Key-P>', lambda: Plus(info, comm, com_text_box))
        en.grid(row=i + 1, column=1, sticky='nsew')
        i = i + 1
    variables = variables
    tree = appear_tabview(variables, data)
    plus = customtkinter.CTkButton(left2.tab("Enter Data"), text='+',
                                   command=lambda: Plus(info, comm, com_text_box, data), width=30)
    plus.configure(width=20, bg_color='green', fg_color='green')
    plus.grid(row=1, column=0, sticky='nsew', padx=100, pady=10)


def Create_frame1():
    # second frame level
    left = Frame(frame4.place(x=0, y=0), width=200, bg='#988dd9')
    center = Frame(frame4.place(x=0, y=0), bg='#d7a7f2', width=1100, height=800)
    center.pack_propagate(False)
    center.grid_propagate(False)

    # create tabview
    tabview1 = customtkinter.CTkTabview(left)
    tabview1.grid(row=1, column=0, rowspan=7, padx=(3, 3), pady=(3, 380), sticky="nsew")
    tabview1.add("Variables List")
    tabview1.add("Show Variables and Options")
    tabview1.tab("Show Variables and Options").grid_columnconfigure(0, weight=1)

    # Create the variable entering and its tools
    l = customtkinter.CTkLabel(master=center, width=200, height=30, text='ENTER A VARIABLE', font=('arial', 20),
                               text_color="#8521bf")
    e = Entry(center, width=13, font='arial 20 bold')
    submit = customtkinter.CTkButton(master=center, width=200, height=30, text='Submit')
    clear = customtkinter.CTkButton(master=center, width=200, height=30, text='Clear')
    Continue = customtkinter.CTkButton(master=center, width=200, height=30, text='Continue')
    threepoint = Button(center, text="☰", bg='#cda8e3')

    # Dark Mode
    switch = customtkinter.CTkSwitch(master=left, text="Dark Mode")
    switch.grid(row=0, column=0, padx=90, pady=(10, 10))

    # For information
    inf = customtkinter.CTkLabel(master=left, text_color=("red", "gray75"), text='There are 0 variables!',
                                 bg_color='transparent', font=('arial', 20))
    inf.place(x=50, y=400)

    inf1 = customtkinter.CTkLabel(master=left, text_color=("red", "gray75"), text='The last variable:',
                                  bg_color='transparent', font=('arial', 20))
    inf1.place(x=10, y=440)

    # Undo Redo button
    undo_button1 = customtkinter.CTkButton(master=left, border_width=0, text_color=("gray10", "#DCE4EE"),
                                           font=('arial', 40), text='↰', width=40, bg_color='transparent')
    undo_button1.place(x=100, y=520)

    redo_button1 = customtkinter.CTkButton(master=left, border_width=0, text_color=("gray10", "#DCE4EE"),
                                           font=('arial', 40), text='↱', width=40, bg_color='transparent')
    redo_button1.place(x=150, y=520)

    undo_label = customtkinter.CTkLabel(master=left, text_color=("purple", "gray75"), text='Undo',
                                        bg_color='transparent', font=('arial', 15))
    undo_label.place(x=100, y=580)

    redo_label = customtkinter.CTkLabel(master=left, text_color=("purple", "gray75"), text='Redo',
                                        bg_color='transparent', font=('arial', 15))
    redo_label.place(x=150, y=580)
    scrollable_frame1 = customtkinter.CTkScrollableFrame(tabview1.tab("Variables List"),
                                                         label_text="The List of Variables", width=240)
    scrollable_frame1.grid(row=0, column=0, padx=(10, 3), sticky="nsew")
    scrollable_frame1.grid_columnconfigure(0, weight=1)
    scrollable_frame1_switches = []
    # scrollable_frame1.pack()
    scrollable_frame2 = customtkinter.CTkScrollableFrame(tabview1.tab("Show Variables and Options"),
                                                         label_text="The list of variables and options", width=240)
    scrollable_frame2.grid(row=0, column=0, padx=(10, 3), pady=(5, 0), sticky="nsew")
    scrollable_frame2.grid_columnconfigure(0, weight=1)
    scrollable_frame2_switches = []
    # scrollable_frame2.pack()
    op_label = customtkinter.CTkLabel(master=center, width=600, font=('Arial', 20))
    op_entry = customtkinter.CTkEntry(master=center, width=600, height=30, font=('Arial', 20))
    save_button = customtkinter.CTkButton(master=center, width=100, height=25, font=('Arial', 20), text='SAVE')
    abort_button = customtkinter.CTkButton(master=center, width=100, height=25, font=('Arial', 20), text='ABORT')

    return left, center, tabview1, l, e, submit, clear, Continue, threepoint, switch, inf, inf1, undo_button1, redo_button1, undo_label, redo_label, scrollable_frame1, scrollable_frame2, op_label, op_entry, save_button, abort_button


def sed():
    frame4.place(x=0, y=0)
    left, center, tabview1, l, e, submit, clear, Continue, threepoint, switch, inf, inf1, undo_button1, redo_button1, undo_label, redo_label, scrollable_frame1, scrollable_frame2, op_label, op_entry, save_button, abort_button = Create_frame1()
    e.focus_set()

    for widgets in scrollable_frame1.winfo_children():
        widgets.destroy()
    for widgets in scrollable_frame2.winfo_children():
        widgets.destroy()
    for widgets in scrollable_frame3.winfo_children():
        widgets.destroy()

    def menupopup():
        (x, y) = mouse.position
        try:
            pop_up.tk_popup(x, y, 0)
        finally:
            pop_up.grab_release()

    def Undo():
        if variables != [] and options[0] == ['']:
            copy_variables.append(variables[n[0] - 1])
            copy_all_options.append(all_options[n[0] - 1])
            variables.remove(variables[n[0] - 1])
            all_options.remove(all_options[n[0] - 1])
            unshow_vars()
            unshow_ops()
            m[0] = m[0] + 1
            n[0] = n[0] - 1
            litt_inf()
        else:
            options[0] = ['']

    def Redo():
        print(all_options)
        print(copy_all_options)
        print(m)
        print(n)
        if copy_variables != [] and m[0] != 0 and copy_all_options != []:
            n[0] = n[0] + 1
            variables.append(copy_variables[m[0] - 1])
            all_options.append(copy_all_options[m[0] - 1])
            copy_all_options.remove(copy_all_options[m[0] - 1])
            copy_variables.remove(copy_variables[m[0] - 1])
            litt_inf()
            show_variables()
            show_variables_options()
            m[0] = m[0] - 1

    def Clear(*args):
        for widgets in scrollable_frame1.winfo_children():
            widgets.destroy()
            unshow_vars()
            unshow_ops()
            n[0] = n[0] - 1
        sh_vars = []

        for widgets in scrollable_frame2.winfo_children():
            widgets.destroy()
        sh_ops = []

        variables.clear()
        all_options.clear()
        options[0] = ['']
        copy_variables.clear()
        copy_all_options.clear()
        m[0] = 0
        litt_inf()
        e.delete(0, END)

    def litt_inf():
        inf.configure(text=f"There are {n[0]} variables!")
        if n[0] != 0:
            inf1.configure(text=f"The last variable:{variables[n[0] - 1]}")
        else:
            inf1.configure(text="The last variable:")

    def show_variables():
        l = Label(scrollable_frame1, text=f'  {variables[n[0] - 1]}', fg='black', bg='#d0d4cc', relief="groove",
                  width=150, font='arial 12 bold', bd=0)
        l.pack()
        sh_vars.append(l)

    def fit_new_line():
        print(all_options[n[0] - 1])
        txt = '►  Options:'
        i = 0
        txt_list = []
        t = 1
        for option in all_options[n[0] - 1]:
            if len(txt + ' ' + option) <= 31:
                txt = txt + ' ' + option
            else:
                t = t + 1
                txt_list.append(txt)
                txt = option
        txt_list.append(txt)
        return txt_list, t

    def show_variables_options():
        l = Label(scrollable_frame2, text=variables[n[0] - 1], fg='black', bd=0, bg='#d0d4cc', relief="groove",
                  width=150, font='arial 12 bold')
        l.pack()
        text_ops = ''

        if all_options[n[0] - 1] == ['']:
            l1 = Label(scrollable_frame2, text='►  no options', font='arial 13 italic', bg='#d0d4cc', width=150)
            l1.pack()
        else:
            l1 = Text(scrollable_frame2, fg='black', bd=0, bg='#d0d4cc', relief="groove", width=150,
                      font='arial 12 italic')
            txt_list, h = fit_new_line()
            for items in txt_list:
                l1.insert(END, items)
                l1.insert(END, '\n')
            fit_new_line()
            l1.config(height=h)
            l1.config(state=DISABLED)
            l1.pack()
        sh_ops.append(l1)
        shl_ops.append(l)

    def unshow_vars():
        copy_sh_vars = sh_vars
        sh_vars[n[0] - 1].destroy()
        sh_vars.remove(sh_vars[n[0] - 1])

    def unshow_ops():
        copy_sh_ops = sh_ops
        sh_ops[n[0] - 1].destroy()
        shl_ops[n[0] - 1].destroy()
        sh_ops.remove(sh_ops[n[0] - 1])
        shl_ops.remove(shl_ops[n[0] - 1])

    def Submit(*args):
        copy_variables.clear()
        copy_all_options.clear()
        m[0] = 0
        n[0] = n[0] + 1
        variables.append(e.get())
        litt_inf()
        e.delete(0, END)
        all_options.append(options[0])
        show_variables()
        show_variables_options()
        options[0] = ['']
        desappear_opp_envir()

    def Save_options(*args):
        e.focus_set()
        options[0] = ''.join(op_entry.get()).split(',')
        desappear_opp_envir()

    def abort_options(*args):
        e.focus_set()
        options[0] = ['']
        desappear_opp_envir()

    def Options(*args):
        op_entry.bind('<Return>', Save_options)
        op_entry.bind('<Control-Key-a>', abort_options)
        op_entry.place(x=100, y=600)
        op_entry.focus_set()
        op_label.place(x=100, y=570)
        save_button.place(x=750, y=570)
        abort_button.place(x=750, y=620)
        op_entry.delete(0, END)
        op_label.configure(text=f'Add options for {e.get()}. (Input options list separated by comma )')
        op_entry.insert(0, 'ex:Male,Female,Other')

    def desappear_opp_envir():
        op_label.place_forget()
        op_entry.place_forget()
        save_button.place_forget()
        abort_button.place_forget()

    def make_replacement(rep_entry=None):
        rpl \
            = ''.join(rep_entry.get()).split(',')
        data[int(rpl[0]) - 1][int(rpl[1]) - 1] = rpl[2]
        for items in tree.get_children():
            tree.delete(items)
        for i in range(n[0]):
            tree.heading(variables[i], text=variables[i])
        for d in data:
            tree.insert('', tk.END, values=d)

    def CONTINUE():
        left.grid_forget()
        center.place_forget()
        frame2.place(x=0, y=0)
        appear_entries(all_options, variables, data)
        appear_tabview(variables, data)

    # Menu menupop
    pop_up = Menu(root, tearoff=0, bg='#e0b4fa')
    pop_up.add_command(label="Add Options")
    pop_up.add_command(label="Date Format")
    pop_up.add_separator()
    pop_up.add_command(label="Time Format")
    pop_up.add_command(label="Delete Variable")

    # Variables needed
    variables = []
    copy_variables = []
    copy_all_options = []
    sh_vars = []
    op_confirm = []
    sh_ops = []
    shl_ops = []
    copy_sh_vars = []
    copy_sh_ops = []
    n = [0]
    m = [0]
    all_options = []
    options = [['']]
    data = []
    coment = []

    # appear var entry environment
    left.grid(row=0, column=0, rowspan=4, sticky="nsew")
    left.grid_rowconfigure(4, weight=1)
    center.place(x=310, y=1)
    e.bind('<Return>', Submit)
    e.bind('<Control-Key-k>', Clear)
    e.bind('<Control-Key-K>', Clear)
    e.bind('<Control-Key-o>', Options)
    e.bind('<Control-Key-O>', Options)
    e.place(x=400, y=280)
    l.place(x=400, y=240)
    submit.place(x=400, y=330)
    clear.place(x=400, y=380)
    Continue.place(x=400, y=430)
    threepoint.place(x=375, y=280, width=20, height=37)

    # configure commands
    submit.configure(command=Submit)
    save_button.bind('<Return>', Save_options)
    pop_up.entryconfig('Add Options', command=Options)
    threepoint.configure(command=menupopup)
    undo_button1.configure(command=Undo)
    redo_button1.configure(command=Redo)
    clear.configure(command=Clear)
    save_button.configure(command=Save_options)
    abort_button.configure(command=abort_options)
    Continue.configure(command=CONTINUE)
    save_fl.configure(command=save_file_as)





def show_context_menu(event):
    data = []
    for line in tree.get_children():
        vec = []
        for value in tree.item(line)['values']:
            value = str(value)
            try:
                if value == 'nan':
                    value = ''
            except:
                print("")
            vec.append(value)
        print(vec)
        data.append(vec)
    columns = Columns(data)
    print(columns)
    x = event.x_root
    y = event.y_root
    region = tree.identify("region", event.x, event.y)
    if region == "heading":
        xcol = tree.identify_column(x - 430)
        xcol = str(xcol)
        print(xcol)
        need = xcol.replace(xcol[0], "")
        need = int(need)
        print("need")
        print(need)
        print(columns[need - 1])
        if date_is_quant(columns[need - 1]):
            quantitive_menu.post(x, y)
            print(columns[need - 1])
            quantitive_menu.entryconfig('Histogram', command=lambda: Hist_Result(left2, columns[need - 1], need))
        else:
            qualitative_menu.post(x, y)
            print(columns[need - 1])

            qualitative_menu.entryconfig('Table', command=lambda: Table_Result(left2, columns[need - 1], need))
            qualitative_menu.entryconfig('Mode', command=lambda: Mode_Result(left2, columns[need - 1], need))
            qualitative_menu.entryconfig('Most Rare', command=lambda: MostRare_Result(left2, columns[need - 1], need))
            qualitative_menu.entryconfig('Pie', command=lambda: Pie_Result(left2, columns[need - 1], need))
            # qualitative_menu.entryconfig('Bar', command=lambda:Bar_result(left2,columns[need-1],need))


###########################################################################################################################
coment = []
variables = []
maxx = []

# Menu context_menu
# Create the context menu

quantitive_menu = tk.Menu(root, tearoff=0)
quantitive_menu.add_command(label="Sum")
quantitive_menu.add_command(label="Median")
quantitive_menu.add_command(label="Mean")
quantitive_menu.add_command(label="Q1")
quantitive_menu.add_command(label="Q3")
quantitive_menu.add_command(label="Variance")
quantitive_menu.add_command(label="Mean")
quantitive_menu.add_command(label='Histogram')
quantitive_menu.add_command(label='Boxplot')
quantitive_menu.add_command(label='Histogram Smooth')

qualitative_menu = tk.Menu(root, tearoff=0)
qualitative_menu.add_command(label="Table")
qualitative_menu.add_command(label="Mode")
qualitative_menu.add_command(label="Most Rare")
qualitative_menu.add_command(label="Pie")
qualitative_menu.add_command(label="Plot")
qualitative_menu.add_separator()
qualitative_menu.add_command(label="Histogram")
qualitative_menu.add_command(label="Q3")
qualitative_menu.add_command(label="Bar")
qualitative_menu.add_command(label="Line Graph")









def CONT(all_options, variables, data, Tops):
    Tops.destroy()
    frame2.place(x=0, y=0)
    appear_entries(all_options, variables, data)
    appear_tabview(variables, data)
    save_fl.configure(command=save_file_as)
    i = 0
    for d in data:
        j = 0
        for element in d:
            if is_integer(element):
                try:
                    data[i][j] = float(data[i][j])
                except:
                    print("")
            j = j + 1
        i = i + 1


def confirm_options(scrollable_frame3, variables, data, Tops):
    op_text_boxes = [child for child in scrollable_frame3.winfo_children() if isinstance(child, Text)]
    all_ops = []
    for box in op_text_boxes:
        option = ''.join(box.get("1.0", END)).split(',')
        option[0] = option[0].replace('►Options:', '')
        option[len(option) - 1] = option[len(option) - 1].replace('\n', '')
        all_ops.append(option)
    variables = variables
    data = data
    CONT(all_ops, variables, data, Tops)


def appear_vars_and_ops_2(scrollable_frame3, all_ops, variables):
    i = 0
    for x in variables:
        txt = '►Options:'
        txt_list = []
        l = Label(scrollable_frame3, text=x, font='arial 13 bold', bg='#d0d4cc')
        l.pack()
        if all_ops[i] != ['']:
            k = 0
            for op in all_ops[i]:
                if k != len(all_ops[i]) - 1:
                    txt = txt + str(op) + ','
                else:
                    txt = txt + str(op)
                k = k + 1
            op_text_box = Text(scrollable_frame3, font='arial 13', height=1)
            op_text_box.insert(END, f'{txt}')
        else:
            op_text_box = Text(scrollable_frame3, font='arial 13', height=1)
            op_text_box.insert(END, '►Options:')
        op_text_box.pack()
        i = i + 1


def appear_top_level_options(filename, all_ops, variables, data):
    data = data
    Tops = Toplevel(root)
    Tops.title(f'The options of the   {filename}   are generated automaticly')
    Tops.geometry('600x300+400+200')
    Tops.configure(background='#d7a7f2')
    Tops.resizable(0, 0)
    scrollable_frame3 = customtkinter.CTkScrollableFrame(Tops,
                                                         label_text="You can confirm or edit auto-generated options",
                                                         width=570, height=200)
    scrollable_frame3.pack()
    all_ops = all_ops
    variables = variables
    appear_vars_and_ops_2(scrollable_frame3, all_ops, variables)
    conf = customtkinter.CTkButton(Tops, text='Confirm',
                                   command=lambda: confirm_options(scrollable_frame3, variables, data, Tops))
    conf.pack(pady=10)


def open_file():
    try:
        filename = filedialog.askopenfilename(title="Select file",
                                              filetypes=(("Excel files", "*.xlsx"), ("Excel files", ".xls")))
        df = pd.read_excel(filename)
        data = df.values.tolist()
        x = len(data)
        global coment
        coment = []
        for i in range(x):
            coment.append("")
        all_ops = auto_options(data)
        variables = []
        for col_name in df.columns:
            variables.append(col_name)
        appear_top_level_options(filename, all_ops, variables, data)
        tree.delete(*tree.get_children())
        for widgets in scrollable_frame3.winfo_children():
            widgets.destroy()
    except:
        print('Open file canceled')
    return coment


####################################################################################################
# first frame
frame1 = Frame(root, width=1517, height=800, bg='#d7a7f2')
frame1.place(x=0, y=0)
frame1.pack_propagate(False)

frame4 = Frame(root, width=1517, height=800, bg='#d7a7f2')
frame4.pack_propagate(False)

# 3-rd frame level
frame2 = Frame(root, width=1517, height=800, bg='#d7a7f2')
frame2.pack_propagate(False)
frame2.grid_propagate(False)

save_fl = customtkinter.CTkButton(frame2, text='Save as xlsx file')
save_fl.place(x=420, y=630)
addcolumn = customtkinter.CTkButton(frame2, text='+', command=AddNewColumn, width=30)
addcolumn.place(x=1325, y=15)

# Create table frame

table = Frame(frame2, width=900, height=610, bg='#d7a7f2', bd=2)
table.pack_propagate(False)
table.grid_propagate(False)
table.place(x=420, y=10)

# create treeview
tree = ttk.Treeview(table)

# Vendosim menune
menubar = Menu(root)
File = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=File)
File.add_command(label="+ New", command=sed)
File.add_command(label="Open", command=open_file)
File.add_command(label="Save")
File.add_command(label="Save as...")
File.add_command(label="Exit")

Edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=Edit)
Edit.add_command(label="Select All")
Edit.add_command(label="Cut")
Edit.add_command(label="Copy")
Edit.add_command(label="Paste")
Edit.add_command(label="Replace")

Window = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Window', menu=Window)
Window.add_command(label="Dark Mode")
Window.add_command(label="Zoom in")
Window.add_command(label="Zoom out")

# Dark Mode
# switch = customtkinter.CTkSwitch(master=left, text="Dark Mode")
# switch.grid(row=0, column=0, padx=90, pady=(10, 10))

# create data entry environement
# left2 = Frame(frame2, width=400, height=770, bg='#988dd9')
left2 = customtkinter.CTkTabview(frame2, height=770, width=400, bg_color="#988dd9")
# left2.grid_propagate(False)
# left2.grid(row=0, column=0)
# left2.grid(row=0, column=0,padx=1, pady=(10,10))
left2.pack(side=LEFT)
left2.add("Enter Data")
left2.tab("Enter Data").configure(fg_color="#988dd9")
left2.add("Results")
left2.tab("Results").configure(fg_color="#988dd9")
# create scrollable frame

scrollable_frame3 = customtkinter.CTkScrollableFrame(left2.tab("Enter Data"), width=370, height=450,
                                                     fg_color='WHITE')
scrollable_frame3.grid(row=0, column=0, padx=(5, 5), sticky="nsew")
scrollable_frame3.grid_columnconfigure(0, weight=1)
scrollable_frame3_switches = []
# scrollable_frame3.pack()

scrollable_frame4 = customtkinter.CTkScrollableFrame(left2.tab("Results"), width=370, height=600,
                                                     fg_color='GREY')
# scrollable_frame4.grid(row=0, column=0, padx=(5, 5), sticky="nsew")
# scrollable_frame4.grid_columnconfigure(0, weight=1)
# scrollable_frame4_switches = []
scrollable_frame4.pack()

# Frame1 buttons
main_button1 = customtkinter.CTkButton(master=frame1, fg_color="#9874db", border_width=2,
                                       text_color=("gray10", "#DCE4EE"), font=('arial', 20),
                                       text='Start entering data.', command=sed)
main_button1.place(x=600, y=300)

main_button2 = customtkinter.CTkButton(master=frame1, fg_color="#9874db", border_width=2,
                                       text_color=("gray10", "#DCE4EE"), font=('arial', 20), text='Open a xlsx file',
                                       width=180, command=open_file)
main_button2.place(x=600, y=350)

# Save button
tree.bind("<Button-3>", show_context_menu)

root.config(menu=menubar)
root.mainloop()

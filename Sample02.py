#!/usr/bin/env python

import wx
import os
import csv
import matplotlib.pyplot as plt

import wx.lib.mixins.listctrl as listmix


# ---------------------------------------------------------------------------
wildcard = "Python source (*.py)|*.py|" \
           "Compiled Python (*.pyc)|*.pyc|" \
           "SPAM files (*.spam)|*.spam|" \
           "Egg file (*.egg)|*.egg|" \
           "All files (*.*)|*.*"


listctrldata = {
    1 : ("Hey!", "You can edit", "me!"),
    2 : ("Try changing the contents", "by", "clicking"),
    3 : ("in", "a", "cell"),
    4 : ("See how the length columns", "change", "?"),
    5 : ("You can use", "TAB,", "cursor down,"),
    6 : ("and cursor up", "to", "navigate"),
}

# ---------------------------------------------------------------------------
name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
num_list = [52.4, 57.8, 59.1, 54.6]


def showchart():
    rects = plt.bar(range(len(num_list)), num_list, color='rgby')
    # X軸標題
    index = [0, 1, 2, 3]
    index = [float(c)+0.4 for c in index]
    plt.ylim(ymax=80, ymin=0)
    plt.xticks(index, name_list)
    plt.ylabel("arrucay(%)")    # X軸標籤
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height) + '%', ha='center', va='bottom')
    plt.show()


class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin, listmix.TextEditMixin):

    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.Populate()
        listmix.TextEditMixin.__init__(self)

    def Populate(self):
        # for normal, simple columns, you can add them like this:
        self.InsertColumn(0, "Column 1")
        self.InsertColumn(1, "Column 2")
        self.InsertColumn(2, "Column 3")
        self.InsertColumn(3, "Len 1", wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(4, "Len 2", wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(5, "Len 3", wx.LIST_FORMAT_RIGHT)

        items = listctrldata.items()
        for key, data in items:
            index = self.InsertItem(self.GetItemCount(), data[0])
            self.SetItem(index, 1, data[1])
            self.SetItem(index, 2, data[2])
            self.SetItemData(index, key)

        self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(2, 100)

        self.currentItem = 0

    def SetStringItem(self, index, col, data):
        if col in range(3):
            wx.ListCtrl.SetItem(self, index, col, data)
            wx.ListCtrl.SetItem(self, index, 3+col, str(len(data)))
        else:
            try:
                datalen = int(data)
            except:
                return

            wx.ListCtrl.SetItem(self, index, col, data)

            data = self.GetItem(index, col-3).GetText()
            wx.ListCtrl.SetItem(self, index, col-3, data[0:datalen])


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)
        list = TestListCtrl(pnl, 10,
                             style=wx.LC_REPORT
                                   | wx.BORDER_NONE
                                   #| wx.LC_SORT_ASCENDING            # Content of list as instructions is
                                   | wx.LC_HRULES | wx.LC_VRULES      # nonsense with auto-sort enabled
                             )
        self.lsv = list
        b1 = wx.Button(pnl, 11, "Open")
        b2 = wx.Button(pnl, 12, "Chart")
        b3 = wx.Button(pnl, 13, "Save")

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(list, 10, wx.EXPAND)
        sizer.Add(b1, 11, wx.EXPAND)
        sizer.Add(b2, 12, wx.EXPAND)
        sizer.Add(b3, 13, wx.EXPAND)
        pnl.SetSizer(sizer)

        # event
        self.Bind(wx.EVT_BUTTON, self.OnOpen, b1)
        self.Bind(wx.EVT_BUTTON, self.OnChart,  b2)
        self.Bind(wx.EVT_BUTTON, self.OnSave, b3)

    def OnOpen(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            path = paths[0]
            with open(path, 'r', encoding="utf-8-sig") as f:    # https://blog.csdn.net/idwtwt/article/details/100328331
                rows = csv.reader(f)
                global listctrldata
                global num_list
                listctrldata.clear()
                for idx, val in enumerate(rows):
                    tex = tuple([i for i in val])
                    listctrldata[idx] = tex

                    if idx == 0:
                        num_list.clear()
                        for n in val:
                            num_list.append(float(n))

                f.close()
            self.lsv.ClearAll()
            self.lsv.Populate()

        dlg.Destroy()

    def OnChart(self, event):
        showchart()

    def OnSave(self, event):
        count = self.lsv.GetItemCount()
        cols = self.lsv.GetColumnCount()
        text = [[0 for i in range(cols)] for j in range(count)]     # 初始化陣列

        for row in range(count):
            for col in range(cols):
                item = self.lsv.GetItem(itemIdx=row, col=col)
                text[row][col] = item.GetText()
        print(text)
        dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=' ')
                writer.writerows(text)
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Sample 02')
    frm.Show()
    app.MainLoop()
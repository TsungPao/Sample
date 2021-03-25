import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title, size=(400,500))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()  #the status bar in the bottom

        menuBar = wx.MenuBar()
        testMenu = wx.Menu()
        menuOnce = testMenu.Append(wx.ID_ANY, "Once", "print something")
        menuTwice = testMenu.Append(wx.ID_ANY, "Twice", "print something and another thing")
        menuBar.Append(testMenu, "Test")

        self.Bind(wx.EVT_MENU, self.First, menuOnce)

        self.Bind(wx.EVT_MENU, self.First, menuTwice)
        self.Bind(wx.EVT_MENU, self.Second, menuTwice)

        self.SetMenuBar(menuBar)


        self.Show(True)

    def First(self, event):
        print("something")
        event.Skip()
    def Second(self, event):
        print("another thing")
        event.Skip()


app = wx.App(False)  #what does False mean?
frame = MyFrame(None, 'Small editor')
app.MainLoop()

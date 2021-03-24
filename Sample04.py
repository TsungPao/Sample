# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

MFrame2 = None
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.SetStatusWidths([200, -1])						# 更改比例 self.SetStatusWidths([200, 300])
		self.SetStatusText("A Custom StatusBar...", 0)		# 一定要放在上述這行m_statusBar1之後任意區域都可以
		self.SetStatusText("A Custom StatusBar2...", 1)
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", "StatusTextMessages", wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menu2.AppendSeparator()

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menubar1.Append( self.m_menu2, u"MyMenu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnBtnClick )
		self.Bind( wx.EVT_MENU, self.MenuClick, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_UPDATE_UI, self.MenuUpdateUI, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuClick2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_UPDATE_UI, self.MenuUpdateUI2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuClick3, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_UPDATE_UI, self.MenuUpdateUI3, id = self.m_menuItem3.GetId() )
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)		# 關閉視窗觸發

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnBtnClick( self, event ):
		msg = self.m_textCtrl1.GetValue()
		self.m_staticText1.SetLabel(msg)
		event.Skip()

	def MenuClick( self, event ):
		global MFrame2
		print('點擊MenuItem')
		MFrame2 = MyFrame2(None)		# 將MyFrame2(None)放入 MFrame2
		MFrame2.Show()
		event.Skip()

	def MenuUpdateUI( self, event ):
		print('觸發MenuUI')
		event.Skip()

	def MenuClick2( self, event ):
		print('點擊MenuItem2')
		event.Skip()

	def MenuUpdateUI2( self, event ):
		print('觸發MenuUI2')
		event.Skip()

	def MenuClick3( self, event ):
		print('點擊MenuItem3')
		event.Skip()

	def MenuUpdateUI3( self, event ):
		print('觸發MenuUI3')
		event.Skip()

	def OnCloseWindow(self, event):
		if MFrame2 != None:
			MFrame2.Destroy()
			print("OnCloseWindow2")
		else:
			pass
		print("OnCloseWindow1")
		self.Destroy()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"MyButton5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"MyButton6", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"MyButton7", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"MyButton8", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button8, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnBtnClick2 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnBtnClick3 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnBtnClick4 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnBtnClick5 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnBtnClick6 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnBtnClick7 )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnBtnClick8 )
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def OnBtnClick2( self, event ):
		print('btn2')
		print(self)
		event.Skip()

	def OnBtnClick3( self, event ):
		event.Skip()

	def OnBtnClick4( self, event ):
		event.Skip()

	def OnBtnClick5( self, event ):
		event.Skip()

	def OnBtnClick6( self, event ):
		event.Skip()

	def OnBtnClick7( self, event ):
		event.Skip()

	def OnBtnClick8( self, event ):
		event.Skip()

	def OnCloseWindow(self, event):
		global MFrame2
		MFrame2 = None
		print("OnCloseWindow2")
		self.Destroy()


if __name__ == '__main__':
	# When this module is run (not imported) then create the app, the
	# frame, show it, and start the event loop.
	app = wx.App()
	frm = MyFrame1(None)
	frm.Show()
	app.MainLoop()

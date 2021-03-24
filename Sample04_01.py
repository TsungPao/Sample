# -*- coding: utf-8 -*-

import wx
import Sample04

MFrame2 = None


class GUIFrame1(Sample04.MyFrame1):
    def __init__(self, parent):
        Sample04.MyFrame1.__init__(self, parent)

    def OnBtnClick( self, event ):
        msg = self.m_textCtrl1.GetValue()
        self.m_staticText1.SetLabel(msg)
        event.Skip()

    def MenuClick( self, event ):
        global MFrame2
        print('點擊MenuItem')
        MFrame2 = GUIFrame2(None)		# GUIFrame2(None)放入 MFrame2
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

class GUIFrame2(Sample04.MyFrame2):
    def __init__(self, parent):
        Sample04.MyFrame2.__init__(self, parent)

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
    app = wx.App()
    frm = GUIFrame1(None)
    frm.Show()
    app.MainLoop()

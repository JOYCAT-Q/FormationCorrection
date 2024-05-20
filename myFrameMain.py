# -*- coding: utf-8 -*-

# ==============================
# @author: Joycat
# @time: 2024/04/05
# ==============================

###########################################################################
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx.adv
from formationsFixedMain import FormationFixed 
###########################################################################
## Class MyFrameMain
###########################################################################

class MyFrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"仿真2D Fedit2阵型修正软件", pos = wx.DefaultPosition, size = wx.Size( 1200,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 900,600 ), wx.Size( 1600,1500 ) )
		self.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False, "楷体" ) )
		self.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizerMainWindow = wx.BoxSizer( wx.HORIZONTAL )

		gSizerImg = wx.GridSizer( 5, 3, 0, 0 )

		self.m_animCtrlUniversity = wx.adv.AnimationCtrl( self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 400,100 ), wx.adv.AC_DEFAULT_STYLE )

		self.m_animCtrlUniversity.SetInactiveBitmap( wx.Bitmap( u"./logo/university.png", wx.BITMAP_TYPE_ANY ) )
		gSizerImg.Add( self.m_animCtrlUniversity, 0, wx.ALIGN_LEFT, 5 )

		self.m_animCtrlTeamLogo = wx.adv.AnimationCtrl( self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 300,150 ), wx.adv.AC_DEFAULT_STYLE )

		self.m_animCtrlTeamLogo.SetInactiveBitmap( wx.Bitmap( u"./logo/team.jpg", wx.BITMAP_TYPE_ANY ) )
		gSizerImg.Add( self.m_animCtrlTeamLogo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_animCtrlCollege = wx.adv.AnimationCtrl( self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 400,100 ), wx.adv.AC_DEFAULT_STYLE )

		self.m_animCtrlCollege.SetInactiveBitmap( wx.Bitmap( u"./logo/college.png", wx.BITMAP_TYPE_ANY ) )
		self.m_animCtrlCollege.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizerImg.Add( self.m_animCtrlCollege, 0, wx.ALIGN_RIGHT, 5 )

		bSizerGetDir = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticTextGetDir = wx.StaticText( self, wx.ID_ANY, u"请选择阵型文件夹: ", wx.DefaultPosition, wx.Size( 500,-1 ), wx.ALIGN_RIGHT )
		self.m_staticTextGetDir.Wrap( -1 )

		self.m_staticTextGetDir.SetFont( wx.Font( 22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "楷体" ) )

		bSizerGetDir.Add( self.m_staticTextGetDir, 0, wx.ALL, 5 )

		self.m_dirPickerPath = wx.DirPickerCtrl( self, wx.ID_ANY, u"./", u"Select a folder", wx.DefaultPosition, wx.Size( 400,30 ), wx.DIRP_DEFAULT_STYLE )
		self.m_dirPickerPath.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		bSizerGetDir.Add( self.m_dirPickerPath, 1, wx.ALL, 5 )


		gSizerImg.Add( bSizerGetDir, 0, wx.ALIGN_BOTTOM, 0 )

		bSizerBlank0 = wx.BoxSizer( wx.HORIZONTAL )

		bSizerBlank0.SetMinSize( wx.Size( -1,1 ) )

		gSizerImg.Add( bSizerBlank0, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 1 )

		bSizerBlank1 = wx.BoxSizer( wx.VERTICAL )


		gSizerImg.Add( bSizerBlank1, 1, wx.EXPAND, 5 )

		bSizerBlank2 = wx.BoxSizer( wx.VERTICAL )


		gSizerImg.Add( bSizerBlank2, 1, wx.EXPAND, 5 )

		bSizerRunAuto = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonRunAuto = wx.Button( self, wx.ID_ANY, u"点击执行修正", wx.DefaultPosition, wx.Size( 250,75 ), 0 )
		self.m_buttonRunAuto.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		bSizerRunAuto.Add( self.m_buttonRunAuto, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )


		gSizerImg.Add( bSizerRunAuto, 1, wx.EXPAND, 5 )

		bSizerTitleConent = wx.BoxSizer( wx.HORIZONTAL )


		gSizerImg.Add( bSizerTitleConent, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 1 )

		self.m_staticTextOutput0 = wx.StaticText( self, wx.ID_ANY, u"处理结果输出台:", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_LEFT )
		self.m_staticTextOutput0.Wrap( -1 )

		self.m_staticTextOutput0.SetFont( wx.Font( 15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		gSizerImg.Add( self.m_staticTextOutput0, 0, wx.ALL, 0 )

		self.m_staticTextOutput1 = wx.StaticText( self, wx.ID_ANY, u"无需处理的文件:", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticTextOutput1.Wrap( -1 )

		self.m_staticTextOutput1.SetFont( wx.Font( 15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		gSizerImg.Add( self.m_staticTextOutput1, 0, wx.ALL, 0 )

		self.m_staticTextErrors = wx.StaticText( self, wx.ID_ANY, u"执行中出现的错误信息:", wx.DefaultPosition, wx.Size( 250,-1 ), wx.ALIGN_RIGHT )
		self.m_staticTextErrors.Wrap( -1 )

		self.m_staticTextErrors.SetFont( wx.Font( 15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		gSizerImg.Add( self.m_staticTextErrors, 0, wx.ALL, 5 )

		self.m_textCtrlOutputProcessed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 390,250 ) ,style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LEFT)
		self.m_textCtrlOutputProcessed.SetFont( wx.Font( 8, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_textCtrlOutputProcessed.SetMaxSize( wx.Size( -1,500 ) )

		gSizerImg.Add( self.m_textCtrlOutputProcessed, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 0 )

		self.m_textCtrlOutputUnProcessed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 390,250 ) ,style=wx.TE_MULTILINE | wx.TE_READONLY )
		self.m_textCtrlOutputUnProcessed.SetFont( wx.Font( 8, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_textCtrlOutputUnProcessed.SetMaxSize( wx.Size( -1,500 ) )

		gSizerImg.Add( self.m_textCtrlOutputUnProcessed, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

		self.m_textCtrlErrors = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 390,250 ) ,style=wx.TE_MULTILINE | wx.TE_READONLY )
		self.m_textCtrlErrors.SetFont( wx.Font( 8, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_textCtrlErrors.SetMaxSize( wx.Size( -1,500 ) )

		gSizerImg.Add( self.m_textCtrlErrors, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizerMainWindow.Add( gSizerImg, 0, wx.FIXED_MINSIZE|wx.SHAPED, 0 )


		self.SetSizer( bSizerMainWindow )
		self.Layout()
		self.m_statusBarTail = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonRunAuto.Bind( wx.EVT_BUTTON, self.RunAuto )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def RunAuto( self, event ):
		conf = FormationFixed(self.m_dirPickerPath.GetPath())
		conf.auto_process()
		processed_files_str = '\n\n'.join(conf.get_processed_files()) 
		self.m_textCtrlOutputProcessed.SetValue( processed_files_str )
		skipped_files_str = '\n\n'.join(conf.get_skipped_files())
		self.m_textCtrlOutputUnProcessed.SetValue( skipped_files_str )
		Errors_str = '\n'.join(conf.get_errors())
		self.m_textCtrlErrors.SetValue( Errors_str )

# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrameMain(None)
#     frame.Show(True)
#     # start the applications
#     app.MainLoop()

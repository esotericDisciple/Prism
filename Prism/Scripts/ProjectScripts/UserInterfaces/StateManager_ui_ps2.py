# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StateManager.ui',
# licensing of 'StateManager.ui' applies.
#
# Created: Mon Sep 30 23:46:09 2019
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mw_StateManager(object):
    def setupUi(self, mw_StateManager):
        mw_StateManager.setObjectName("mw_StateManager")
        mw_StateManager.resize(722, 1024)
        mw_StateManager.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(mw_StateManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 1001))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(336, 0))
        self.widget.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setContentsMargins(1, 10, 0, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 371))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(5, 14, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_CreateImports = QtWidgets.QWidget(self.groupBox)
        self.w_CreateImports.setObjectName("w_CreateImports")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.w_CreateImports)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_createImport = QtWidgets.QPushButton(self.w_CreateImports)
        self.b_createImport.setMinimumSize(QtCore.QSize(55, 25))
        self.b_createImport.setMaximumSize(QtCore.QSize(55, 25))
        self.b_createImport.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createImport.setObjectName("b_createImport")
        self.horizontalLayout_3.addWidget(self.b_createImport)
        self.b_shotCam = QtWidgets.QPushButton(self.w_CreateImports)
        self.b_shotCam.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_shotCam.setObjectName("b_shotCam")
        self.horizontalLayout_3.addWidget(self.b_shotCam)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.w_CreateImports)
        self.f_import = QtWidgets.QFrame(self.groupBox)
        self.f_import.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_import.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_import.setObjectName("f_import")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.f_import)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tw_import = QtWidgets.QTreeWidget(self.f_import)
        self.tw_import.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tw_import.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_import.setAcceptDrops(True)
        self.tw_import.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_import.setDragEnabled(True)
        self.tw_import.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tw_import.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tw_import.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw_import.setIndentation(20)
        self.tw_import.setObjectName("tw_import")
        self.tw_import.headerItem().setText(0, "1")
        self.tw_import.header().setVisible(False)
        self.verticalLayout_7.addWidget(self.tw_import)
        self.verticalLayout_3.addWidget(self.f_import)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(5, 14, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.w_CreateExports = QtWidgets.QWidget(self.groupBox_2)
        self.w_CreateExports.setObjectName("w_CreateExports")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.w_CreateExports)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b_createExport = QtWidgets.QPushButton(self.w_CreateExports)
        self.b_createExport.setMinimumSize(QtCore.QSize(50, 25))
        self.b_createExport.setMaximumSize(QtCore.QSize(50, 25))
        self.b_createExport.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createExport.setObjectName("b_createExport")
        self.horizontalLayout_4.addWidget(self.b_createExport)
        self.b_createRender = QtWidgets.QPushButton(self.w_CreateExports)
        self.b_createRender.setMinimumSize(QtCore.QSize(50, 25))
        self.b_createRender.setMaximumSize(QtCore.QSize(50, 25))
        self.b_createRender.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createRender.setObjectName("b_createRender")
        self.horizontalLayout_4.addWidget(self.b_createRender)
        self.b_createPlayblast = QtWidgets.QPushButton(self.w_CreateExports)
        self.b_createPlayblast.setMinimumSize(QtCore.QSize(60, 25))
        self.b_createPlayblast.setMaximumSize(QtCore.QSize(60, 25))
        self.b_createPlayblast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createPlayblast.setObjectName("b_createPlayblast")
        self.horizontalLayout_4.addWidget(self.b_createPlayblast)
        self.b_createDependency = QtWidgets.QPushButton(self.w_CreateExports)
        self.b_createDependency.setMinimumSize(QtCore.QSize(35, 25))
        self.b_createDependency.setMaximumSize(QtCore.QSize(35, 25))
        self.b_createDependency.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createDependency.setObjectName("b_createDependency")
        self.horizontalLayout_4.addWidget(self.b_createDependency)
        self.b_stateFromNode = QtWidgets.QPushButton(self.w_CreateExports)
        self.b_stateFromNode.setMinimumSize(QtCore.QSize(110, 0))
        self.b_stateFromNode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_stateFromNode.setAutoDefault(False)
        self.b_stateFromNode.setObjectName("b_stateFromNode")
        self.horizontalLayout_4.addWidget(self.b_stateFromNode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.w_CreateExports)
        self.f_export = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_export.sizePolicy().hasHeightForWidth())
        self.f_export.setSizePolicy(sizePolicy)
        self.f_export.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_export.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_export.setLineWidth(1)
        self.f_export.setMidLineWidth(0)
        self.f_export.setObjectName("f_export")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.f_export)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tw_export = QtWidgets.QTreeWidget(self.f_export)
        self.tw_export.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tw_export.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_export.setAcceptDrops(True)
        self.tw_export.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_export.setDragEnabled(True)
        self.tw_export.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tw_export.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tw_export.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw_export.setIndentation(20)
        self.tw_export.setObjectName("tw_export")
        self.tw_export.headerItem().setText(0, "1")
        self.tw_export.header().setVisible(False)
        self.verticalLayout.addWidget(self.tw_export)
        self.verticalLayout_4.addWidget(self.f_export)
        self.gb_publish = QtWidgets.QGroupBox(self.groupBox_2)
        self.gb_publish.setObjectName("gb_publish")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_publish)
        self.verticalLayout_6.setContentsMargins(-1, 14, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.gb_publish)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setContentsMargins(-1, 14, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sp_rangeStart = QtWidgets.QSpinBox(self.groupBox_3)
        self.sp_rangeStart.setEnabled(True)
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.horizontalLayout_7.addWidget(self.sp_rangeStart)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.sp_rangeEnd = QtWidgets.QSpinBox(self.groupBox_3)
        self.sp_rangeEnd.setEnabled(True)
        self.sp_rangeEnd.setSuffix("")
        self.sp_rangeEnd.setMinimum(0)
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.horizontalLayout_7.addWidget(self.sp_rangeEnd)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.b_getRange = QtWidgets.QPushButton(self.groupBox_3)
        self.b_getRange.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b_getRange.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_getRange.setAutoDefault(False)
        self.b_getRange.setObjectName("b_getRange")
        self.horizontalLayout_7.addWidget(self.b_getRange)
        self.b_setRange = QtWidgets.QPushButton(self.groupBox_3)
        self.b_setRange.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b_setRange.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_setRange.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_setRange.setAutoDefault(False)
        self.b_setRange.setObjectName("b_setRange")
        self.horizontalLayout_7.addWidget(self.b_setRange)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.widget_2 = QtWidgets.QWidget(self.gb_publish)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l_comment = QtWidgets.QLabel(self.widget_2)
        self.l_comment.setObjectName("l_comment")
        self.horizontalLayout_5.addWidget(self.l_comment)
        self.e_comment = QtWidgets.QLineEdit(self.widget_2)
        self.e_comment.setObjectName("e_comment")
        self.horizontalLayout_5.addWidget(self.e_comment)
        self.b_description = QtWidgets.QPushButton(self.widget_2)
        self.b_description.setMinimumSize(QtCore.QSize(20, 25))
        self.b_description.setMaximumSize(QtCore.QSize(20, 25))
        self.b_description.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_description.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_description.setObjectName("b_description")
        self.horizontalLayout_5.addWidget(self.b_description)
        self.b_preview = QtWidgets.QPushButton(self.widget_2)
        self.b_preview.setMinimumSize(QtCore.QSize(20, 25))
        self.b_preview.setMaximumSize(QtCore.QSize(20, 25))
        self.b_preview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_preview.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_preview.setObjectName("b_preview")
        self.horizontalLayout_5.addWidget(self.b_preview)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.b_publish = QtWidgets.QPushButton(self.gb_publish)
        self.b_publish.setEnabled(False)
        self.b_publish.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_publish.setAutoDefault(False)
        self.b_publish.setObjectName("b_publish")
        self.verticalLayout_6.addWidget(self.b_publish)
        self.verticalLayout_4.addWidget(self.gb_publish)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(358, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(358, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.w_stateUi = QtWidgets.QWidget(self.widget_3)
        self.w_stateUi.setObjectName("w_stateUi")
        self.lo_stateUi = QtWidgets.QVBoxLayout(self.w_stateUi)
        self.lo_stateUi.setContentsMargins(9, 9, 9, 9)
        self.lo_stateUi.setObjectName("lo_stateUi")
        self.verticalLayout_8.addWidget(self.w_stateUi)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(378, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        mw_StateManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mw_StateManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuRecentProjects = QtWidgets.QMenu(self.menuAbout)
        self.menuRecentProjects.setObjectName("menuRecentProjects")
        mw_StateManager.setMenuBar(self.menubar)
        self.actionProjectBrowser = QtWidgets.QAction(mw_StateManager)
        self.actionProjectBrowser.setObjectName("actionProjectBrowser")
        self.actionPrismSettings = QtWidgets.QAction(mw_StateManager)
        self.actionPrismSettings.setObjectName("actionPrismSettings")
        self.actionZu = QtWidgets.QAction(mw_StateManager)
        self.actionZu.setObjectName("actionZu")
        self.actionCopyStates = QtWidgets.QAction(mw_StateManager)
        self.actionCopyStates.setObjectName("actionCopyStates")
        self.actionPasteStates = QtWidgets.QAction(mw_StateManager)
        self.actionPasteStates.setObjectName("actionPasteStates")
        self.actionRemoveStates = QtWidgets.QAction(mw_StateManager)
        self.actionRemoveStates.setObjectName("actionRemoveStates")
        self.menuAbout.addAction(self.actionCopyStates)
        self.menuAbout.addAction(self.actionPasteStates)
        self.menuAbout.addAction(self.actionRemoveStates)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionProjectBrowser)
        self.menuAbout.addAction(self.actionPrismSettings)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuRecentProjects.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mw_StateManager)
        QtCore.QMetaObject.connectSlotsByName(mw_StateManager)

    def retranslateUi(self, mw_StateManager):
        mw_StateManager.setWindowTitle(QtWidgets.QApplication.translate("mw_StateManager", "State Manager", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Import", None, -1))
        self.b_createImport.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create an ImportFile state", None, -1))
        self.b_createImport.setText(QtWidgets.QApplication.translate("mw_StateManager", "Import", None, -1))
        self.b_shotCam.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Import the latest Shot Camera", None, -1))
        self.b_shotCam.setText(QtWidgets.QApplication.translate("mw_StateManager", "Import Cam", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Export", None, -1))
        self.b_createExport.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create an Export state", None, -1))
        self.b_createExport.setText(QtWidgets.QApplication.translate("mw_StateManager", "Export", None, -1))
        self.b_createRender.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create an ImangeRender state", None, -1))
        self.b_createRender.setText(QtWidgets.QApplication.translate("mw_StateManager", "Render", None, -1))
        self.b_createPlayblast.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create a Playblast state", None, -1))
        self.b_createPlayblast.setText(QtWidgets.QApplication.translate("mw_StateManager", "Playblast", None, -1))
        self.b_createDependency.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create an Dependency state", None, -1))
        self.b_createDependency.setText(QtWidgets.QApplication.translate("mw_StateManager", "Dep", None, -1))
        self.b_stateFromNode.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Create states from nodes in the scene", None, -1))
        self.b_stateFromNode.setText(QtWidgets.QApplication.translate("mw_StateManager", "States from Nodes", None, -1))
        self.gb_publish.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Publish", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Global Framerange:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("mw_StateManager", "to:", None, -1))
        self.b_getRange.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Get the global framerange for the current shot", None, -1))
        self.b_getRange.setText(QtWidgets.QApplication.translate("mw_StateManager", "Get", None, -1))
        self.b_setRange.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Set the framerange defined on the left to the timeline", None, -1))
        self.b_setRange.setText(QtWidgets.QApplication.translate("mw_StateManager", "Set", None, -1))
        self.l_comment.setText(QtWidgets.QApplication.translate("mw_StateManager", "Comment:", None, -1))
        self.b_description.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Add a description to the published file", None, -1))
        self.b_description.setText(QtWidgets.QApplication.translate("mw_StateManager", "D", None, -1))
        self.b_preview.setToolTip(QtWidgets.QApplication.translate("mw_StateManager", "Add a preview to the published file", None, -1))
        self.b_preview.setText(QtWidgets.QApplication.translate("mw_StateManager", "P", None, -1))
        self.b_publish.setText(QtWidgets.QApplication.translate("mw_StateManager", "Publish", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Options", None, -1))
        self.menuRecentProjects.setTitle(QtWidgets.QApplication.translate("mw_StateManager", "Recent projects", None, -1))
        self.actionProjectBrowser.setText(QtWidgets.QApplication.translate("mw_StateManager", "Project Browser...", None, -1))
        self.actionPrismSettings.setText(QtWidgets.QApplication.translate("mw_StateManager", "Prism Settings...", None, -1))
        self.actionZu.setText(QtWidgets.QApplication.translate("mw_StateManager", "zu", None, -1))
        self.actionCopyStates.setText(QtWidgets.QApplication.translate("mw_StateManager", "Copy all states", None, -1))
        self.actionPasteStates.setText(QtWidgets.QApplication.translate("mw_StateManager", "Paste all states", None, -1))
        self.actionRemoveStates.setText(QtWidgets.QApplication.translate("mw_StateManager", "Remove all states", None, -1))


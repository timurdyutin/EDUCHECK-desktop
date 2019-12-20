# -*- coding: utf-8 -*-

import datetime
import locale
import sys
import time
from random import choice
from threading import Thread

import os
import lxml
import requests
from bs4 import BeautifulSoup as bs4
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCalendarWidget, QFileDialog,
                             QInputDialog, QMainWindow, QSizePolicy,
                             QTableWidgetItem, QTextEdit, QWidget)

from newUI import AuthWindow, MainWindow
count = 0

loginElementName = "main_login"
passwordElementName = "main_password"
successElementText = "Личный кабинет"
URL = "https://edu.tatar.ru/logon"

locale.setlocale(locale.LC_ALL, "ru")
style = """QMainWindow {
	background-color:#ececec;
}
QTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QPlainTextEdit {
	border-width: 1px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QToolButton {
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QToolButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(142,142,142);
}
QPushButton{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton::default{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(255,255,255);
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: rgb(0,0,0);
	padding: 2px;
	background-color: rgb(142,142,142);
}
QPushButton:disabled{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));
	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));
	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));
	border-width: 1px;
	border-radius: 5px;
	color: #808086;
	padding: 2px;
	background-color: rgb(142,142,142);
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-style: solid;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QLabel {
	color: #000000;
}
QLCDNumber {
	color: rgb(0, 113, 255, 255);
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(230, 230, 230);
	border-style: solid;
	background-color:rgb(207,207,207);
}
QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
	border-radius: 10px;
}
QMenuBar {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));
}
QMenuBar::item {
	color: #000000;
  	spacing: 3px;
  	padding: 1px 4px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));
}

QMenuBar::item:selected {
  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #FFFFFF;
}
QMenu::item:selected {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	border-bottom-color: transparent;
	border-left-width: 2px;
	color: #000000;
	padding-left:15px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
}
QMenu::item {
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: transparent;
	border-bottom-width: 1px;
	color: #000000;
	padding-left:17px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:7px;
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:#000000;
}
QTabWidget::pane {
		border-color: rgb(223,223,223);
		background-color:rgb(226,226,226);
		border-style: solid;
		border-width: 2px;
    	border-radius: 6px;
}
QTabBar::tab:first {
	border-style: solid;
	border-left-width:1px;
	border-right-width:0px;
	border-top-width:1px;
	border-bottom-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	border-top-left-radius: 4px;
	border-bottom-left-radius: 4px;
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab:last {
	border-style: solid;
	border-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	border-top-right-radius: 4px;
	border-bottom-right-radius: 4px;
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab {
	border-style: solid;
	border-top-width:1px;
	border-bottom-width:1px;
	border-left-width:1px;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #000000;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
	border-right-color: transparent;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {
  	border-style: solid;
  	border-left-width:1px;
  	border-bottom-width:1px;
  	border-top-width:1px;
	border-right-color: transparent;
	border-top-color: rgb(209,209,209);
	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));
	border-bottom-color: rgb(229,229,229);
	color: #FFFFFF;
	padding: 3px;
	margin-left:0px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QCheckBox {
	color: #000000;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: transparent;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
}
QRadioButton {
	color: 000000;
	padding: 1px;
}
QRadioButton::indicator:checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #a9b7c6;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QRadioButton::indicator:!checked {
	height: 10px;
	width: 10px;
	border-style:solid;
	border-radius:5px;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #a9b7c6;
	background-color: transparent;
}
QStatusBar {
	color:#027f7f;
}
QSpinBox {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDoubleSpinBox {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QTimeEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDateTimeEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QDateEdit {
	border-style: solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}

QToolBox {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab {
	color: #a9b7c6;
	background-color:#000000;
}
QToolBox::tab:selected {
	color: #FFFFFF;
	background-color:#000000;
}
QScrollArea {
	color: #FFFFFF;
	background-color:#000000;
}
QSlider::groove:horizontal {
	height: 5px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::groove:vertical {
	width: 5px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	width: 12px;
	margin: -5px 0;
	border-radius: 7px;
}
QSlider::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	height: 12px;
	margin: 0 -5px;
	border-radius: 7px;
}
QSlider::add-page:horizontal {
    background: rgb(181,181,181);
}
QSlider::add-page:vertical {
    background: rgb(181,181,181);
}
QSlider::sub-page:horizontal {
    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QSlider::sub-page:vertical {
    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));
}
QScrollBar:horizontal {
	max-height: 20px;
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
}
QScrollBar:vertical {
	max-width: 20px;
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
}
QScrollBar::handle:horizontal {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::handle:horizontal:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(147, 200, 200);
	border-radius: 7px;
	min-width: 25px;
}
QScrollBar::handle:vertical {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(207,207,207);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::handle:vertical:hover {
	background: rgb(253,253,253);
	border-style: solid;
	border-width: 1px;
	border-color: rgb(147, 200, 200);
	border-radius: 7px;
	min-height: 25px;
}
QScrollBar::add-line:horizontal {
   border: 2px transparent grey;
   border-top-right-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-right-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: right;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
   border: 2px transparent grey;
   border-bottom-left-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed {
   border: 2px transparent grey;
   border-bottom-left-radius: 7px;
   border-bottom-right-radius: 7px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: bottom;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-bottom-left-radius: 7px;
   background: rgba(34, 142, 255, 255);
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-bottom-left-radius: 7px;
   background: rgb(181,181,181);
   width: 20px;
   subcontrol-position: left;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-top-right-radius: 7px;
   background: rgba(34, 142, 255, 255);
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:pressed {
   border: 2px transparent grey;
   border-top-left-radius: 7px;
   border-top-right-radius: 7px;
   background: rgb(181,181,181);
   height: 20px;
   subcontrol-position: top;
   subcontrol-origin: margin;
}
QScrollBar::left-arrow:horizontal {
   border: 1px transparent grey;
   border-top-left-radius: 3px;
   border-bottom-left-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::right-arrow:horizontal {
   border: 1px transparent grey;
   border-top-right-radius: 3px;
   border-bottom-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::up-arrow:vertical {
   border: 1px transparent grey;
   border-top-left-radius: 3px;
   border-top-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::down-arrow:vertical {
   border: 1px transparent grey;
   border-bottom-left-radius: 3px;
   border-bottom-right-radius: 3px;
   width: 6px;
   height: 6px;
   background: white;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
   background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
   background: none;
}"""

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


class Auth(QWidget, AuthWindow):
    def __init__(self):
        super(Auth, self).__init__()
        self.setStyleSheet(style)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.collectUserAuthData)
        self.session = requests.Session()
        self.session.get(URL)
        self.calendar = None
        self.setStyleSheet(style)

    def collectUserAuthData(self):
        login = self.textEdit.toPlainText().strip()
        password = self.textEdit_2.toPlainText().strip()
        if self.checkUserAuthData(login, password) is True:
            status, session, name = self.authInSite(login, password)
            if status is True:
                self.label_4.setText("Авторизация выполнена успешно")
                self.widget = Main(session, login, password, name)
                wid.hide()
                self.widget.show()
            else:
                self.label_4.setText("Вы ввели неверный логин или пароль")

    def checkUserAuthData(self, login, password):
        if login == "" or password == "":
            self.label_4.setText("Поле 'Логин' и 'Пароль' не могут быть пустыми")
            return False
        try:
            login = int(login)
            return True
        except:
            self.label_4.setText("Логин может содержать только цифры от 0 до 9")
            return False

    def authInSite(self, login, password):
        name = None
        cookie = {'_ga': 'GA1.2.1804685607.1574325953',
                  '_gid': 'GA1.2.1116002961.1574325953'}
        data = {loginElementName: login, passwordElementName: password}
        headers = {'Referer': URL}
        RH = self.session.post(URL, data=data, cookies=cookie, headers=headers).text
        soup = bs4(RH, "lxml")
        if soup.h2.text.strip() == successElementText:
            name = soup.find("b").text
            return (True, self.session, name)
        else:
            return (False, self.session, name)


class Main(QWidget, MainWindow):
    def __init__(self, session, login, password, name):
        super(Main, self).__init__()
        self.setStyleSheet(style)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.parseDay)
        self.pushButton_4.clicked.connect(self.quit)
        self.pushButton_3.clicked.connect(self.parseTable)
        self.pushButton_2.clicked.connect(self.parseWeek)
        self.pushButton_5.clicked.connect(self.getCalendarWidget)
        self.session = session
        self.login = login
        self.password = password
        self.reportCard = []
        self.username = name
        self.label.setText(f"Привет, {' '.join(self.username.split()[0:2])}")
        self.parseDay()

    def parseWeek(self):
        reportCard = []
        self.calendar.hide()
        q = int(str(time.time()).split(".")[0])
        today = datetime.datetime.today().isoweekday()
        startDay = q - (86400 * (today - 1))
        endDay = q - (86400 * (7 - today - 3))
        while startDay <= endDay:
            startDay = str(startDay)
            con = ThreadWithReturnValue(target=self.parseDay, args=(startDay, ))
            con.start()
            content = con.join()
            reportCard.append(content)
            startDay = int(str(startDay).split(".")[0])
            startDay += 86400
            print(reportCard)
        self.returnWeekContent(reportCard)

    def returnWeekContent(self, reportCard):
        self.calendar.hide()

        self.clearPreviousContent()

        self.tableWidget.show()

        self.tableWidget.setColumnCount(5)
        item = QTableWidgetItem()
        item.setText("Время")
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QTableWidgetItem()
        item.setText("Предмет")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QTableWidgetItem()
        item.setText("Что задали")
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QTableWidgetItem()
        item.setText("Комментарий")
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QTableWidgetItem()
        item.setText("Оценка")
        self.tableWidget.setHorizontalHeaderItem(4, item)

        
    def getCalendarWidget(self):
        self.tableWidget.hide()
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(QtCore.QRect(10, 90, 621, 251))
        self.calendar.show()
        self.calendar.clicked[QDate].connect(self.selectMonthDay)

    def selectMonthDay(self, date):
        selectedDate = " ".join([str(i) for i in list(date.getDate())])
        selectedDate = int(time.mktime(time.strptime(selectedDate, '%Y %m %d')))
        self.parseDay(selectedDate)
        self.calendar.hide()

    def parseTable(self):
        self.calendar.hide()
        reportCard = {}
        self.checkSessionIsValid()
        URL = "https://edu.tatar.ru/user/diary/term"
        RH = self.session.get(URL).text
        soup = bs4(RH, "lxml")
        soup = soup.find("table").findAll("td")
        resultTags = [tag.text for tag in soup if (len(tag.attrs) == 0 or tag.text == "ИТОГО") and tag.string is not None and tag.text != '\n' and tag.text != "просмотр"][1:-3]

        for index, item in enumerate(resultTags, 1):
            if item.isdigit():
                item = int(item)
                reportCard[subjectName].append(item)
            else:
                try:
                    item = float(item)
                    reportCard[subjectName].append(item)
                except:
                    reportCard[item] = []
                    subjectName = item
        self.returnTableContent(reportCard)

    def returnTableContent(self, reportCard):
        self.calendar.hide()
        self.clearPreviousContent()
        self.tableWidget.setColumnCount(3)
        item = QTableWidgetItem()
        item.setText("Предмет")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setText("Оценки")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setText("Средний балл")
        self.tableWidget.setHorizontalHeaderItem(2, item)

        for row, link in enumerate(reportCard.keys()):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(link))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(", ".join([str(i) for i in reportCard[link][0:-1]])))
            cost = reportCard[link][-1] if len(reportCard[link]) != 0 else "—"
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(cost)))
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def parseDay(self, date=None):
        self.calendar.hide()
        if date is None or date == 0:
            date = int(str(time.time()).split(".")[0])
        else:
            date = int(str(date).split(".")[0])
        reportCard = {}
        resultTags = []
        self.checkSessionIsValid()
        URL = f"https://edu.tatar.ru/user/diary/day?for={date}"
        RH = self.session.get(URL).text
        soup = bs4(RH, "lxml")
        p = []
        soup = soup.find("tbody").findAll("td")
        for tag in soup:
            if "title" in tag.attrs:
                resultTags.append(tag.get("title"))
            else:
                resultTags.append(tag.text.replace("\n", ""))
        resultTags = list(reversed(resultTags))
        reportCard[time.strftime("%a, %d %b %Y", time.localtime(int(URL.split("=")[1])))] = []
        for tag in resultTags:
            if len(tag.split("—")) == 2 and tag.count(":") == 2:
                p.append(tag)
                if len(p) % 2 == 0:
                    p = self.prepareDayContent(list(reversed(p)))
                else:
                    p = list(reversed(p))
                reportCard[time.strftime("%a, %d %b %Y", time.localtime(date))].append(p)
                p = []
            else:
                if tag.isdigit() is True and len(tag) >= 2:
                    tag = ", ".join(list(tag))
                if len(tag) != 0:
                    tag = tag.strip()
                p.append(tag)
                
        self.prepareDayContent(reportCard)                
        self.returnDayContent(reportCard)
        return reportCard

    def prepareDayContent(self, reportCard):
        for i in range(len(reportCard) - 1):
            if i >= 4 and reportCard[i + 1].isdigit() is False:
                reportCard[i] = ", ".join([reportCard[i], reportCard[i + 1]])
                reportCard.remove(reportCard[i + 1])
        return reportCard
        

    def returnDayContent(self, reportCard):
        self.calendar.hide()

        self.clearPreviousContent()

        self.tableWidget.show()

        self.tableWidget.setRowCount(1)
        item = QTableWidgetItem()
        item.setText(list(reportCard.keys())[0])
        self.tableWidget.setVerticalHeaderItem(0, item)

        self.tableWidget.setColumnCount(5)
        item = QTableWidgetItem()
        item.setText("Время")
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QTableWidgetItem()
        item.setText("Предмет")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QTableWidgetItem()
        item.setText("Что задали")
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QTableWidgetItem()
        item.setText("Комментарий")
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QTableWidgetItem()
        item.setText("Оценка")
        self.tableWidget.setHorizontalHeaderItem(4, item)

        day = list(reportCard.values())[0]
        print(day)
        for row, link in enumerate(list(reversed(day)), 1):
            link = list(link)
            print(link)
            self.tableWidget.insertRow(row)
            for column in range(len(link)):
                self.tableWidget.setItem(row, column, QTableWidgetItem(link[column]))
                self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(str(row)))
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

    def clearPreviousContent(self):
        self.tableWidget.clearContents()
        self.calendar.hide()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

    def checkSessionIsValid(self):
        response = self.session.get("https://edu.tatar.ru/user/diary/term", allow_redirects=False)
        if response.status_code != 200:
            wid.authInSite(self.login, self.password)

    def quit(self):
        self.hide()
        wid.show()
        wid.textEdit.setText("")
        wid.textEdit_2.setText("")
        wid.label_4.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = Auth()
    wid.show()
    sys.exit(app.exec_())
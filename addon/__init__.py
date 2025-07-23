# -*- coding: utf-8 -*-
from aqt import mw
from aqt.qt import *
from anki.hooks import addHook

def show_dialog():
    dialog = QDialog(mw)
    dialog.setWindowTitle("Transparency")
    dialog.resize(200, 80)
    dialog.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowStaysOnTopHint)
    
    layout = QVBoxLayout(dialog)
    
    title = QLabel("Transparency Level")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet("font-size: 14px; font-weight: bold; margin: 10px;")
    layout.addWidget(title)
    
    opacity_label = QLabel("100%")
    opacity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(opacity_label)
    
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setRange(50, 100)
    slider.setValue(100)
    
    def update_opacity(v):
        opacity_label.setText(f"{v}%")
        mw.setWindowOpacity(v / 100.0)
    
    slider.valueChanged.connect(update_opacity)
    layout.addWidget(slider)
    
    dialog.show()

def setup_menu():
    action = QAction("🎛️ Transparency", mw)
    action.triggered.connect(show_dialog)
    mw.form.menuTools.addAction(action)

addHook("profileLoaded", setup_menu)
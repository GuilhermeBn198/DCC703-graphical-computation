
import {QMainWindow, QWidget, FlexLayout, QLabel  } from '@nodegui/nodegui';

const win_max = {
	h: 600,
	w: 1900
};

export class MainWindow {
	win:			QMainWindow = new QMainWindow();
	view: 			QWidget = new QWidget();
	label2: 		QLabel = new QLabel();

	//////////////////////////////// declaração dos widgets

	constructor(win_name: string, w_: number = 1280, h_: number = 720, w_max: number = win_max.w, h_max: number = win_max.h) {
		this.win.setWindowTitle(win_name);
		//this.win.setMaximunSize(win_max.w, win_max.h);
		this.win.resize(w_, h_);

	}
	
	generatelayout(){
			
	}
}
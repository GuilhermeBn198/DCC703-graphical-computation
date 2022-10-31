const { 
	QLabel, 
	QMainWindow, 
	QWidget, 
	FlexLayout 
} = require("@nodegui/nodegui");

const tam_wind = {
	wid: 1280,
	hei: 720
}
//window setup
const win = new QMainWindow();
win.setWindowTitle("workhome")
win.resize(tam_wind.wid,tam_wind.hei)

// main window declaration
const rootview = new QWidget();
rootview.setObjectName("rootview");
const layout = new FlexLayout();
layout.setObjectName("layout");
rootview.setLayout(layout);

//widgets declaration
const janela = new QWidget();
janela.setObjectName("janela");

const janela2 = new QWidget();
janela2.setObjectName("janela2");

const janela3 = new QWidget();
janela3.setObjectName("janela3");





//main window children
layout.addWidget(janela);
layout.addWidget(janela2);
layout.addWidget(janela3);





win.setStyleSheet(
	`
	  #rootview {
		background-color: #009688;
		display: flex;
		align-content: stretch;
		align-items: stretch;
		justify-content: space-between;
		flex-direction: row;	
		flex-wrap: wrap;
	  }
	  #janela {
		background-color: #D9D9D9;
		width: 1246px;
		height: 93px;
		flex-grow: 1;
		padding: 10em;
	  }
	  #janela2 {
		background-color: #3f3;
		width: 610px;
		height: 582px;
      }
	  #janela3 {
		background-color: #79f;
		width: 610px;
		height: 582px;
	  }
	`
  );
win.setCentralWidget(rootview);
win.show();
(global as any).win = win;
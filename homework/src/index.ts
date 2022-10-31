const { 
	QLabel, 
	QMainWindow, 
	QWidget, 
	FlexLayout 
} = require("@nodegui/nodegui");

const tam_wind = {
	wid: 720,
	hei: 560
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
	  *{
		  margin: 10px;
		  align-content: space-between;
		  justify-content: space-between;
		  border: 3px solid #a21
     	  border-radius: 3px;

		}
		#rootview {
		background-color: #1E1E1E;
		display: flex;
		flex-direction: row;	
		flex-wrap: wrap;
		margin: 0px;
		border: 0px;
	  }
	  #janela {
		background-color: #D9D9D9;
		width: 688px;
		height: 92px;
		margin: 0px auto;
	  }
	  #janela2 {
		background-color: #D9D9D9;
		width: 326px;
		height: 426px;

      }
	  #janela3 {
		background-color: #D9D9D9;
		width: 326px;
		height: 426px;

	  }
	`
  );
win.setCentralWidget(rootview);
win.show();
(global as any).win = win;
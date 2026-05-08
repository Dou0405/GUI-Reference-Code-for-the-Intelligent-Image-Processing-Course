import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QPushButton, 
                             QStackedWidget, QSpacerItem, QSizePolicy, 
                             QGraphicsDropShadowEffect) 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor 

FONT_FAMILY = '"Microsoft YaHei", "SimHei", sans-serif' 
SIZE_TITLE = "52px"      
SIZE_INFO = "22px"       
SIZE_LAB_BTN = "26px"     
SIZE_BOTTOM_BTN = "16px"  

def apply_shadow(widget):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)        
    shadow.setXOffset(3)          
    shadow.setYOffset(5)            
    shadow.setColor(QColor(0, 0, 0, 80)) 
    widget.setGraphicsEffect(shadow)

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能图像处理 - 实验平台")
        self.resize(900, 700) 
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.init_pages()
        
    def init_pages(self):
        # 1. 创建主界面 (Index 0)
        self.main_page = QWidget()
        self.setup_main_page()
        self.stacked_widget.addWidget(self.main_page)
        
        # 2. 创建四个实验的空白接口页面 (Index 1-4)
        self.lab1_page = self.create_lab_placeholder("实验一 图像变换", 0)
        self.lab2_page = self.create_lab_placeholder("实验二 图像增强复原", 0)
        self.lab3_page = self.create_lab_placeholder("实验三 CIFAR-10物体识别", 0)
        self.lab4_page = self.create_lab_placeholder("实验四 图像分割处理", 0)
        
        self.stacked_widget.addWidget(self.lab1_page)
        self.stacked_widget.addWidget(self.lab2_page)
        self.stacked_widget.addWidget(self.lab3_page)
        self.stacked_widget.addWidget(self.lab4_page)

    def setup_main_page(self):
        main_layout = QVBoxLayout(self.main_page)
        main_layout.setAlignment(Qt.AlignCenter)
        
        # 顶部弹簧
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # --- 标题 ---
        title_label = QLabel("智能图像处理实验")
        title_label.setObjectName("TitleLabel")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # --- 姓名与学号 ---
        info_label = QLabel("姓名：xxxx    学号：xxxx")
        info_label.setObjectName("InfoLabel")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)
        
        main_layout.addSpacing(50)
        
        # --- 2x2 按钮网格 ---
        grid_layout = QGridLayout()
        grid_layout.setSpacing(25) 
        
        btn_lab1 = QPushButton("实验一：图像变换")
        btn_lab2 = QPushButton("实验二：图像增强复原")
        btn_lab3 = QPushButton("实验三：CIFAR-10物体识别")
        btn_lab4 = QPushButton("实验四：图像分割处理")
        
        for btn in [btn_lab1, btn_lab2, btn_lab3, btn_lab4]:
            btn.setProperty("class", "LabButton")
            btn.setCursor(Qt.PointingHandCursor)
            apply_shadow(btn)
            
        grid_layout.addWidget(btn_lab1, 0, 0)
        grid_layout.addWidget(btn_lab2, 0, 1)
        grid_layout.addWidget(btn_lab3, 1, 0)
        grid_layout.addWidget(btn_lab4, 1, 1)
        
        grid_container = QHBoxLayout()
        grid_container.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        grid_container.addLayout(grid_layout)
        grid_container.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        main_layout.addLayout(grid_container)
        
        # 底部弹簧
        main_layout.addSpacerItem(QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # --- 退出按钮 ---
        exit_btn = QPushButton("退出程序")
        exit_btn.setObjectName("ExitButton")
        exit_btn.setCursor(Qt.PointingHandCursor)
        exit_btn.clicked.connect(self.close)
        apply_shadow(exit_btn)
        
        exit_layout = QHBoxLayout()
        exit_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        exit_layout.addWidget(exit_btn)
        exit_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        main_layout.addLayout(exit_layout)
        
        # --- 绑定页面跳转 ---
        btn_lab1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        btn_lab2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        btn_lab3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        btn_lab4.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

    def create_lab_placeholder(self, title_text, main_page_index):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel(f"【{title_text}】 的工作区域")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(f"font-family: {FONT_FAMILY}; font-size: {SIZE_TITLE}; color: #2C3E50; font-weight: bold;")
        
        instruction = QLabel("UI 设计接口")
        instruction.setAlignment(Qt.AlignCenter)
        instruction.setStyleSheet(f"font-family: {FONT_FAMILY}; font-size: 20px; color: #7F8C8D;")
        
        back_btn = QPushButton("返回主界面")
        back_btn.setObjectName("BackButton")
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(main_page_index))
        apply_shadow(back_btn) 
        
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(title)
        layout.addWidget(instruction)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        btn_layout = QHBoxLayout()
        btn_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        btn_layout.addWidget(back_btn)
        btn_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(btn_layout)
        
        return page

def apply_stylesheet(app):
    """
    动态生成 QSS 样式表，将配置区的变量注入其中
    """
    qss = f"""
    QMainWindow, QWidget {{
        background-color: #F4F6F7;
    }}
    
    QLabel#TitleLabel {{
        font-family: {FONT_FAMILY};
        font-size: {SIZE_TITLE};
        font-weight: bold;
        color: #2C3E50;
        letter-spacing: 2px;
    }}
    
    QLabel#InfoLabel {{
        font-family: {FONT_FAMILY};
        font-size: {SIZE_INFO};
        color: #5D6D7E;
        font-weight: normal;
    }}
    
    QPushButton.LabButton {{
        font-family: {FONT_FAMILY};
        font-size: {SIZE_LAB_BTN};
        font-weight: bold;
        background-color: #34495E;
        color: #ECF0F1;
        border: none;
        border-radius: 8px;
        padding: 25px 40px;  
        min-width: 280px;
    }}
    QPushButton.LabButton:hover {{
        background-color: #3D566E;
    }}
    QPushButton.LabButton:pressed {{
        background-color: #1A252F;
        padding-top: 27px; /* 模拟被按下的视觉位移 */
        padding-bottom: 23px;
    }}
    
    QPushButton#ExitButton, QPushButton#BackButton {{
        font-family: {FONT_FAMILY};
        font-size: {SIZE_BOTTOM_BTN};
        background-color: #95A5A6;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 12px 50px;
        min-width: 150px;
    }}
    QPushButton#ExitButton:hover, QPushButton#BackButton:hover {{
        background-color: #AAB7B8; 
    }}
    QPushButton#ExitButton:pressed, QPushButton#BackButton:pressed {{
        background-color: #7F8C8D;
        padding-top: 14px; /* 模拟被按下的视觉位移 */
        padding-bottom: 10px;
    }}
    """
    app.setStyleSheet(qss)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app)
    
    window = ImageProcessingApp()
    window.show()
    
    sys.exit(app.exec_())
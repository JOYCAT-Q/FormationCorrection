# 仿真2d_fedit2阵型修正软件[对fedit2编辑的阵型文件进行修正]
# 仅测试于YuShan的代码
# 其余队伍未测试，若无法运行请自行对源代码进行修改

# 环境依赖：

Python>=3.8

wxPython>=4

# 方式一：

将源码打包下载到本地 

Linux下在终端中输入 
python3 runMain.py 即可

Windows下在命令窗口中输入 

python runMain.py 即可

# 方式二：

下载对应系统发行版

Windows：仿真2D_Fedit2阵型修正软件V1.0_Windows.exe

双击运行即可(请确保logo文件夹与可执行处于同级目录下)

Ubuntu：仿真2D_Fedit2阵型修正软件V1.0_Ubuntu

右键运行即可(请确保logo文件夹与可执行处于同级目录下)

如出现文件无权限，

输入：chmod 777 ./仿真2D_Fedit2阵型修正软件V1.0_Ubuntu 即可

# 对于源码打包命令：

下载打包工具：

pip/pip3 install pyinstaller  -i  https://pypi.tuna.tsinghua.edu.cn/simple

在源码所在文件夹打开终端输入：

pyinstaller --onefile --icon=./favicon.ico --windowed --name="仿真2D_Fedit2阵型修正软件" runMain.py

# 在Windows下补全环境：

1. 安装Python>=3.8
2. 打开cmd命令窗口，输入：

pip install wxPython -i  https://pypi.tuna.tsinghua.edu.cn/simple 即可

# 在Ubuntu下补全环境(有些可能需要进入root用户下进行)：

1. 打开终端输入：
sudo apt-get install python3 python3-dev python3-pip

3. 输入：
pip3 install wxPython -i  https://pypi.tuna.tsinghua.edu.cn/simple

即可或者 
输入：

sudo apt-get install python3-wxgtk4.0

(可能会出现无法定位此软件包的错误)

# formations-dt压缩包为阵型测试文件

# PS:
此外保留无界面的预发布版本(Formations_Fixed_Tools)，对于有一定能力的读者

通过终端直接使用无界面版本更加快速，高效

仿真2D_Fedit2阵型修正软件.fbp 为 wxFormBuilder 所创建大体框架文件，可自行安装 wxFormBuilder 并对其进行修改更新



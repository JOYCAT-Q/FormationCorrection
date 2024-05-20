# -*- coding: utf-8 -*- 
  
# ==============================
# @author: Joycat
# @time: 2024/04/05
# ==============================

###########################################################################
##
## PLEASE DO *NOT* EDIT THIS FILE!
##
###########################################################################
from os import listdir, path
from json import load, JSONDecodeError
###########################################################################
## Class FormationFixed
###########################################################################

class FormationFixed:  
    """  
    处理目标文件夹下所有文件的类
    """  
    def __init__(self, goal_dir):  
        """  
        初始化FormationFixed类实例, 设置目标文件夹路径  
  
        :param goal_dir: 目标文件夹路径
        :type goal_dir: str  
        """  
        self.goal_dir = goal_dir  
        self.processed_files = []  
        self.skipped_files = []
        self.normal_errors = []  
        self.path_errors = [] 
  
    def get_all_conf(self):  
        """  
        获取目标文件夹下所有配置文件列表
  
        :return: 配置文件列表
        :rtype: list[str]  
        """  
        # 这里需要实现获取所有配置文件列表的逻辑  
        # 使用os.listdir和过滤.conf文件  
        all_files = listdir(self.goal_dir)  
        conf_files = [path.join(self.goal_dir, f) for f in all_files if f.endswith('.conf')]
        if len(conf_files) == 0:
            self.normal_errors.append(f'No files endwith .conf in {self.goal_dir}') 
            # raise ValueError(f'No files endwith .conf in {self.goal_dir}')
        return conf_files  
  
    def get_formation_conf(self, conf_file):  
        """  
        读取并返回指定配置文件的内容
  
        :param conf_file: 配置文件路径
        :type conf_file: str  
        :return: 配置文件的数据
        :rtype: dict  
        """  
        try:  
            with open(conf_file, 'r') as file:  
                data = load(file)  
            return data  
        except (JSONDecodeError, OSError) as e:  
            # print(f"文件 {conf_file} \t非 JSON 目标格式") 
            self.path_errors.append(f"文件 {conf_file} \t非 JSON 目标格式\n\n") 
            return None  


    def get_default_headers(self, method):
        """
        返回 Static 方法和 DelaunayTriangulation 方法的默认头部内容
        
        :return: 默认标头
        :rtype:  str 
        """
        if method == "Static":
            default_headers = '''Formation Static\n# ---------------------------------------------------------\n# move positions when playmode is BeforeKickOff or AfterGoal.(In before-kick-off conf)\n# for free kick after opponent goalie catch(In goalie-catch-opp conf)\n# kick after our goalie catch(In goalie-catch-our conf)\n# for opponent goal kick(In goal-kick-opp conf)\n# for our goalie catch(In goal-kick-our conf)\n'''
            return default_headers
        elif method == "delaunayTriangulation":
            default_headers = '''Formation DelaunayTriangulation 2\nBegin Roles\n1 Goalie 0\n2 CenterBack -1\n3 CenterBack 2\n4 SideBack -1\n5 SideBack 4\n6 DefensiveHalf 0\n7 OffensiveHalf -1\n8 OffensiveHalf 7\n9 SideForward -1\n10 SideForward 9\n11 CenterForward 0\nEnd Roles\n'''
            return default_headers
        else:
            self.normal_errors.append(f"Unknown method: {method}")
            # raise ValueError(f"Unknown method: {method}")
            

    def is_json_file(self, conf_file):
        """  
        判断指定文件是否为有效的JSON文件。  
  
        :param conf_file: 待判断的文件路径  
        :type conf_file: str  
        :return: 如果是JSON文件则返回True，否则返回False  
        :rtype: bool  
        """ 

        try:
            with open(conf_file, "r") as f:
                load(f)
            return True
        except JSONDecodeError:
            return False
        except Exception as e:
            return False

    def get_conf_headers(self, suffix, method):
        """  
        获取指定后缀和方法的配置文件头部内容。  
      
        :param suffix: 配置文件后缀  
        :type suffix: str  
        :param method: 方法名称  
        :type method: str  
        :return: 配置文件头部内容  
        :rtype: str  
        """  
        
        lines = ''
        headers = ''
        # 获取目标目录下的所有文件
        all_files = listdir(self.goal_dir)  
        # 过滤出以指定后缀结尾的文件
        conf_suffix_file = [path.join(self.goal_dir, f) for f in all_files if f.endswith(f'.conf_{suffix}')]  
        # 如果找到的文件数量不为1或者没有找到文件，则记录错误并返回默认头部内容
        if len(conf_suffix_file) != 1 or len(conf_suffix_file) == 0:
            # print(f"There may be multiple identical or no such file(s) endwith: {suffix}\n")
            self.normal_errors.append(f"There may be multiple identical or no such file(s) endwith: {suffix}\n\n")
            headers = self.get_default_headers(method)
            return headers
        # 获取第一个匹配文件的完整路径,正常情况下只返回一个目标文件
        conf_suffix_file = conf_suffix_file[0]
        # 如果是JSON文件，则直接返回默认头部内容
        if self.is_json_file(conf_suffix_file):
            headers = self.get_default_headers(method)
            return headers
        # 根据方法名称确定关键字
        if method == "Static":
            keyword = "Goalie"
        elif method == "delaunayTriangulation":
            keyword = "Begin Samples"
        else:
            self.normal_errors.append(f"Unknown method: {method}")
            # raise ValueError(f"Unknown method: {method}")
        try:  
            with open(conf_suffix_file, 'r') as file:  
                lines = file.readlines()
                for line in lines:
                    if keyword in line:
                        return headers
                    headers += line
        except Exception as e:
            self.normal_errors.append(e)
            # print(e)
        # 如果文件为空或未找到关键字，返回默认头部内容
        if lines == '':
            headers = self.get_default_headers(method)
            return headers


    def process_static_method(self, data, conf_file):  
        """  
        处理配置文件中的Static方法。  
  
        :param data: 配置文件的数据。  
        :type data: dict  
        :param conf_file: 配置文件路径。  
        :type conf_file: str  
        """  
        # 实现Static方法的处理逻辑  
        roles = data["role"]
        dataPoints = data["data"]
        headers = self.get_conf_headers(data["version"], "Static")
        finalData = headers
        for role in roles:
            number = str(role["number"])
            name = role["name"]
            # 以下为美化文件内容保存格式部分代码
            # =====================================
            margin1 = 20
            margin2 = 6
            len_name = len(name)
            for dataPoint in dataPoints:
                X = str(dataPoint[number]['x'])
                Y = str(dataPoint[number]['y'])
                len_x = len(X)
                len_y = len(Y)
                margin1Left = margin1 - len_name - len_x
                margin2Left = margin2 - len_y
                margin1Blank = ''
                margin2Blank = ''
                for _ in range(margin1Left):
                    margin1Blank = margin1Blank + ' '
                for _ in range(margin2Left):
                    margin2Blank = margin2Blank + ' '
            # =====================================
                finalData = finalData + f"{number if len(number)==2 else number+' '}  {name}{margin1Blank}{X}{margin2Blank}{Y}\n"
        finalData = finalData + "# ---------------------------------------------------------"
        try:
            with open(f"{conf_file}", "w") as f:
                f.write(finalData)
        except Exception as e:
            # print(f"There has an error when opening the: {conf_file}")
            self.normal_errors.append(f"There has an error when opening the: {conf_file}\n\n")



    def process_delaunay_triangulation_method(self, data, conf_file):  
        """  
        处理配置文件中的DelaunayTriangulation方法。  
  
        :param data: 配置文件的数据。  
        :type data: dict  
        :param conf_file: 配置文件路径。  
        :type conf_file: str  
        """  
        # 实现DelaunayTriangulation方法的处理逻辑  
        roles = data["role"]
        dataPoints = data["data"]
        dataPointsLen = len(dataPoints)
        headers = self.get_conf_headers(data["version"], "delaunayTriangulation")
        finalData = headers + f'Begin Samples 2 {dataPointsLen}\n'
        for dataPoint in dataPoints:
            X = str(dataPoint['ball']['x'])
            Y = str(dataPoint['ball']['y'])
            finalData = finalData + f'----- {dataPoint["index"]} -----\n'
            finalData = finalData + f'Ball {X} {Y}\n'
            for role in roles:
                number = role["number"]
                number = str(number)
                X = str(dataPoint[number]['x'])
                Y = str(dataPoint[number]['y'])
                finalData = finalData + f"{number} {X} {Y}\n"
            
        finalData = finalData + "End Samples\nEnd"
        try:
            with open(f"{conf_file}", "w") as f:
                f.write(finalData)
        except Exception as e:
            # print(f"There has an error when opening the: {conf_file}")
            self.normal_errors.append(f"There has an error when opening the: {conf_file}\n\n")
  
    def auto_process(self):  
        """  
        自动处理目标文件夹下所有配置文件。  
        """ 
        if not self.get_all_conf():
            return False 
        for conf_file in self.get_all_conf():  
            data = self.get_formation_conf(conf_file)  
            if not data:  
                self.skipped_files.append(conf_file)  
                continue  
  
            if data["method"] == "Static":  
                try:  
                    self.process_static_method(data, conf_file)  
                    self.processed_files.append(conf_file)  
                except Exception as e:  
                    # print(f"处理文件 {conf_file} (Static 方法) 时发生错误: {e}")
                    self.normal_errors.append(f"处理文件 {conf_file} (Static 方法) 时发生错误: {e}\n\n")  
                    self.skipped_files.append(conf_file)  
  
            elif data["method"] == "DelaunayTriangulation":  
                try:  
                    self.process_delaunay_triangulation_method(data, conf_file)  
                    self.processed_files.append(conf_file)  
                except Exception as e:  
                    # print(f"处理文件 {conf_file} (DelaunayTriangulation 方法) 时发生错误: {e}")  
                    self.normal_errors.append(f"处理文件 {conf_file} (DelaunayTriangulation 方法) 时发生错误: {e}\n\n")
                    self.skipped_files.append(conf_file)  
  
            else:  
                # print(f"文件 {conf_file} 包含未知的方法: {data['method']}")  
                self.normal_errors.append(f"文件 {conf_file} 包含未知的方法: {data['method']}\n\n")
                self.skipped_files.append(conf_file)  
        return True
    

    def get_processed_files(self):  
        """  
        获取已处理的文件列表。  
  
        :return: 已处理的文件列表。  
        :rtype: list[str]  
        """  
        processed_files = []
        for file in self.processed_files:
            processed_files.append(path.basename(file))

        return processed_files
  
    def get_skipped_files(self):  
        """  
        获取被跳过的文件列表。  
  
        :return: 已通过的文件列表。  
        :rtype: list[str]
        """
        skipped_files = []
        for file in self.skipped_files:
            skipped_files.append(path.basename(file))

        return skipped_files

    def get_errors(self):
        """  
        获取发生的错误日志列表。  
  
        :return: 错误列表。  
        :rtype: list[str]
        """

        errors_files = []
        for file in self.path_errors:
            errors_files.append(path.basename(file))
        for file in self.normal_errors:
            errors_files.append(file)
            
        return errors_files

# if __name__ == '__main__':
#     try:
#         a = FormationFixed('./')
#         a.auto_process()
#     except Exception as e:
#         print(e)
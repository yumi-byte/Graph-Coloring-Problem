import plotly.express as px
import json
from random import *

# 省份名称列表
countries = [
    "安徽省", "北京市", "重庆市", "福建省", "甘肃省", "广东省", "广西壮族自治区", "贵州省",
    "海南省", "河北省", "黑龙江省", "河南省", "香港特别行政区", "湖北省", "湖南省", "内蒙古自治区",
    "江苏省", "江西省", "吉林省", "辽宁省", "澳门特别行政区", "宁夏回族自治区", "青海省", "陕西省",
    "山东省", "上海市", "山西省", "四川省", "台湾省", "天津市", "西藏自治区", "新疆维吾尔自治区",
    "云南省", "浙江省"
]

# 颜色列表
colors = ["blue", "red", "yellow", "green"]


# 类 省份
class Country:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    # 用给定颜色绘制省份
    def paintCountry(self, color):
        self.color = color

    # 删除省份的颜色
    def removeColor(self):
        self.color = None

    # 将相邻省份添加为此省份邻居
    def addNeighbors(self, *neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)


# 类 地图
class Map:
    def __init__(self):
        # 包含省份的列表
        self.countries = []

    # 检查邻居的颜色是否与现绘制的颜色冲突
    def isSafe(self, c1, color):
        for neighbor in c1.neighbors:
            if neighbor.color == color:
                return False

        return True

    # 将省份添加到地图
    def addCountry(self, country):
        self.countries.append(country)

    # 检查 c2 是否为 c1 的邻居
    def isNeighbor(self, c1, c2):
        if c2 in c1.neighbors:
            return True

        return False

    # 返回每个国家的字典及其相应的颜色的字典，为plot_cloropleth函数做准备
    def mapAsDict(self):
        countriesDict = {}
        for country in self.countries:
            countriesDict[country.name] = country.color

        return countriesDict

    # 初始化中国地图
    def initializeMap(self):
        chinaMap = Map()

        anhui = Country("安徽省")
        beijing = Country("北京市")
        chongqing = Country("重庆市")
        fujian = Country("福建省")
        gansu = Country("甘肃省")
        guangdong = Country("广东省")
        guangxi = Country("广西壮族自治区")
        guizhou = Country("贵州省")
        hainan = Country("海南省")
        hebei = Country("河北省")
        heilongjiang = Country("黑龙江省")
        henan = Country("河南省")
        hongkong = Country("香港特别行政区")
        hubei = Country("湖北省")
        hunan = Country("湖南省")
        innermongolia = Country("内蒙古自治区")
        jiangsu = Country("江苏省")
        jiangxi = Country("江西省")
        jilin = Country("吉林省")
        liaoning = Country("辽宁省")
        macau = Country("澳门特别行政区")
        ningxia = Country("宁夏回族自治区")
        qinghai = Country("青海省")
        shaanxi = Country("陕西省")
        shandong = Country("山东省")
        shanghai = Country("上海市")
        shanxi = Country("山西省")
        sichuan = Country("四川省")
        taiwan = Country("台湾省")
        tianjin = Country("天津市")
        tibet = Country("西藏自治区")
        xinjiang = Country("新疆维吾尔自治区")
        yunnan = Country("云南省")
        zhejiang = Country("浙江省")

        # 建立省份之间的邻居关系
        anhui.addNeighbors(jiangsu, zhejiang, jiangxi, hubei, henan, shandong)
        beijing.addNeighbors(tianjin, hebei)
        chongqing.addNeighbors(hubei, guizhou, sichuan, shaanxi)
        fujian.addNeighbors(zhejiang, jiangxi, guangdong)
        gansu.addNeighbors(xinjiang, qinghai, innermongolia, shaanxi, sichuan, ningxia)
        guangdong.addNeighbors(fujian, jiangxi, hunan, guangxi, hongkong, macau)
        guangxi.addNeighbors(guizhou, yunnan, guangdong, hunan)
        guizhou.addNeighbors(yunnan, sichuan, chongqing, hunan, guangxi)
        hainan.addNeighbors(guangdong)  # 海接广东省
        hebei.addNeighbors(beijing, tianjin, shanxi, innermongolia, shandong, henan, liaoning)
        heilongjiang.addNeighbors(jilin, innermongolia)
        henan.addNeighbors(shanxi, shandong, anhui, hubei, shaanxi, hebei)
        hongkong.addNeighbors(guangdong)
        hubei.addNeighbors(anhui, henan, chongqing, shaanxi, hunan, jiangxi)
        hunan.addNeighbors(guizhou, guangxi, guangdong, jiangxi, hubei, chongqing)
        innermongolia.addNeighbors(heilongjiang, jilin, liaoning, hebei, shanxi, shaanxi, ningxia, gansu, xinjiang)
        jiangsu.addNeighbors(shanghai, anhui, shandong, zhejiang)
        jiangxi.addNeighbors(anhui, hubei, hunan, guangdong, fujian, zhejiang)
        jilin.addNeighbors(heilongjiang, liaoning, innermongolia)
        liaoning.addNeighbors(hebei, jilin, innermongolia)
        macau.addNeighbors(guangdong)
        ningxia.addNeighbors(gansu, innermongolia, shaanxi)
        qinghai.addNeighbors(xinjiang, tibet, gansu, sichuan)
        shaanxi.addNeighbors(innermongolia, ningxia, gansu, sichuan, chongqing, hubei, henan, shanxi)
        shandong.addNeighbors(hebei, henan, anhui, jiangsu)
        shanghai.addNeighbors(jiangsu, zhejiang)
        shanxi.addNeighbors(innermongolia, hebei, henan, shaanxi)
        sichuan.addNeighbors(qinghai, tibet, yunnan, guizhou, chongqing, shaanxi, gansu)
        taiwan.addNeighbors()  # 台湾无邻居
        tianjin.addNeighbors(beijing, hebei)
        tibet.addNeighbors(xinjiang, qinghai, sichuan, yunnan)
        xinjiang.addNeighbors(gansu, qinghai, tibet, innermongolia)
        yunnan.addNeighbors(tibet, sichuan, guizhou, guangxi)
        zhejiang.addNeighbors(jiangsu, shanghai, anhui, jiangxi, fujian)

        # 将每个国家添加到地图中及其邻居
        chinaMap.addCountry(anhui)
        chinaMap.addCountry(beijing)
        chinaMap.addCountry(chongqing)
        chinaMap.addCountry(fujian)
        chinaMap.addCountry(gansu)
        chinaMap.addCountry(guangdong)
        chinaMap.addCountry(guangxi)
        chinaMap.addCountry(guizhou)
        chinaMap.addCountry(hainan)
        chinaMap.addCountry(hebei)
        chinaMap.addCountry(heilongjiang)
        chinaMap.addCountry(henan)
        chinaMap.addCountry(hongkong)
        chinaMap.addCountry(hubei)
        chinaMap.addCountry(hunan)
        chinaMap.addCountry(innermongolia)
        chinaMap.addCountry(jiangsu)
        chinaMap.addCountry(jiangxi)
        chinaMap.addCountry(jilin)
        chinaMap.addCountry(liaoning)
        chinaMap.addCountry(macau)
        chinaMap.addCountry(ningxia)
        chinaMap.addCountry(qinghai)
        chinaMap.addCountry(shaanxi)
        chinaMap.addCountry(shandong)
        chinaMap.addCountry(shanghai)
        chinaMap.addCountry(shanxi)
        chinaMap.addCountry(sichuan)
        chinaMap.addCountry(taiwan)
        chinaMap.addCountry(tianjin)
        chinaMap.addCountry(tibet)
        chinaMap.addCountry(xinjiang)
        chinaMap.addCountry(yunnan)
        chinaMap.addCountry(zhejiang)

        return chinaMap

    # 显示是否找到解
    def BacktrackSearch(self):
        if self.__BacktrackSearchUtil__(0):
            print("存在着色方法。")
        else:
            print("不存在着色方法。")

    # 回溯法
    def __BacktrackSearchUtil__(self, countryIndex):
        if countryIndex == len(self.countries):
            return True

        # 随机排列数组以每次获得不同的着色，具有随机性，可能引发多次回溯，后续予以改进
        shuffle(colors)

        for color in colors:
            if self.isSafe(self.countries[countryIndex], color):
                self.countries[countryIndex].paintCountry(color)

                if self.__BacktrackSearchUtil__(countryIndex + 1):
                    return True

                self.countries[countryIndex].removeColor()

        return False


# 绘制交互式地图
def plot_choropleth(colormap):
    # 读取 GeoJSON 文件
    with open('china_provinces.json', 'r', encoding='utf-8') as f:
        china_geojson = json.load(f)

    # 使用 GeoJSON 绘制地图
    fig = px.choropleth(
        geojson=china_geojson,
        locations=[c for c in countries],  # 地图中的信息标注 省份名称
        featureidkey="properties.name",  # GeoJSON中标识省份的键 与countries列表中元素对应
        color=countries,  # 地图中的信息标注
        color_discrete_sequence=[colormap[c] for c in countries],
        scope="asia"
    )
    fig.show()


import time

if __name__ == '__main__':
    # 初始化地图并执行回溯搜索
    start_t = time.clock()
    chinaMap = Map().initializeMap()
    chinaMap.BacktrackSearch()
    end_t = time.clock()
    print(end_t - start_t)

    # 将结果转换为字典
    dictionary = chinaMap.mapAsDict()

    # 将字典打印到终端 测试
    # print(dictionary)

    # 着色并显示地图
    plot_choropleth(colormap=dictionary)
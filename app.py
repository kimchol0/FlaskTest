from flask import Flask, render_template
import datetime

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():
#     return '你好！'


@app.route("/index")
def index():
    return 'Hello'


# 通过访问路径，获取用户的字符串参数
@app.route("/user/<name>/<sex>")
def welcome(name, sex):
    return '你好，%s%s' % (name, sex)


# 通过访问路径，获取用户的整形参数
@app.route("/user/<int:id>")
def welcome2(id):
    return '你好，%d的会员' % id


# 通过访问路径，获取用户的浮点型参数
@app.route("/user/<float:id>")
def welcome3(id):
    return '您好，您的金额为：%f' % id


# 注意，路由路径不能重复，用户通过唯一路径访问特定的函数

# 返回给用户渲染后的网页文件
@app.route("/index2")
def index2():
    return render_template("index.html")


# 向页面传递一个变量
@app.route("/index3")
def index3():
    time = datetime.date.today()  # 普通变量
    name = ['小张', '小王', '小赵']  # 列表类型
    task = {"任务": "打扫卫生", "时间": "3小时"}  # 字典类型
    return render_template("index.html", var=time, list=name, task=task)


if __name__ == '__main__':
    app.run()

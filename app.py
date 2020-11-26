from flask import Flask,render_template

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
@app.route("/")
def index2():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()

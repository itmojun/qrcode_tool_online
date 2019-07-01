import flask
import qrcode

app = flask.Flask(__name__)

@app.route("/")
def home():
    # # 第一步：获取要生成二维码的数据
    # data = flask.request.args.get("data")


    # # 第二步：生成二维码图片
    # img = qrcode.make(data)
    # img.save(r"E:\纺织大学Python实训\day6\代码\qrcode_tool_online\static\qr.png")

    # # 第三步：在页面上显示二维码图片
    # return '<img src="/static/qr.png" />'

    return flask.render_template('qr_tool.html')

@app.route("/qr", methods=["POST"])
def qr():
    # 第一步：获取要生成二维码的数据
    data = flask.request.form.get("data")


    # 第二步：生成二维码图片
    img = qrcode.make(data)
    img.save(r"E:\纺织大学Python实训\day6\代码\qrcode_tool_online\static\qr.png")

    # 第三步：在页面上显示二维码图片
    return '<img src="/static/qr.png" />'    


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

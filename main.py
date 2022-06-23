import argparse

import tornado.httpserver
from tornado.web import Application
import tornado.ioloop


def callback():
    print("start web server process")

if __name__ == '__main__':
    # 创建命令行解析器
    parser=argparse.ArgumentParser()
    #  add_argument() 方法，该方法用于指定程序能够接受哪些命令行选项。
    parser.add_argument(
        '--port',type=int,default=8405,help='The service port of websocket.'
    )

    args=parser.parse_args()
    app=Application(
        handlers=[(r"/keyword",keyword_replace_handler),
                  (r"/keywordHandler",keywordHandler)]
    )

    http_server=tornado.httpserver.HTTPServer(app,callback())
    http_server.listen(int(args.port))
    print(f"start{int(args.port)}")
    tornado.ioloop.IOLoop.current().start()



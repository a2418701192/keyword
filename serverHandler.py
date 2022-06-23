import json
from concurrent.futures import ThreadPoolExecutor

import tornado.web
import tornado.concurrent
import tornado.gen


class keyword_replace_handler(tornado.web.RequestHandler):
    # 线程池
    max_thread_num =50
    executor=ThreadPoolExecutor(max_workers=max_thread_num)

    # ->表明返回数据的类型
    @tornado.concurrent.run_on_executor
    def handler(self,txt:str)->(int,str,str):
        result =self.application.replace.replace_keyWord(txt)
        return result
    # @tornado.gen.engine # 同步处理,不能及时响应
    @tornado.gen.coroutine #支持异步处理
    def post(self):
        ok=False
        try:
            body=json.loads(self.request.body.decode('utf-8'))
            ok=True



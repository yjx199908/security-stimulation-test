import smtplib
import datetime
import traceback
from email.mime.text import MIMEText #邮件正文
from email.mime.multipart import MIMEMultipart #邮件主体
from email.header import Header #邮件头，标题、收件人等
from logs.log_service import LogService
from utils.global_data import auto_wired

class ExceptionReporter:
    def __init__(self) -> None:
        self.host_server = 'smtp.qq.com'
        self.sender = '1399590856@qq.com' 
        self.pwd = 'ompoxywkxnfdifgf' #邮箱密码
        self.receiver = '2079925508@qq.com'
    
    @auto_wired
    def reported(self,module_name,path_name,detail,stack_info,log_service:LogService=None):
        log_service.log(kind="error",content="detail => {}  in {}.{}".format(detail,module_name,path_name))
        with open(file="./exception_report_template.html",mode="r",encoding="utf-8") as fp:
            mail_content = fp.read()
            mail_content = mail_content.format(datetime.datetime.now().ctime(),module_name,path_name,detail,stack_info)
            mail_title = "东安用户模拟测试异常汇报"
            msg = MIMEMultipart()
            msg["Subject"] = Header(mail_title,'utf-8')
            msg["From"] = self.sender
            msg.attach(MIMEText(mail_content,'html','utf-8'))
            smtp = smtplib.SMTP_SSL(self.host_server)
            smtp.login(self.sender,self.pwd)
            smtp.sendmail(self.sender,self.receiver,msg.as_string())

def exception_agent(module_name,path_name):
    def agenter(fn):
        def new_function(*args,**kwords):
            try:
                return fn(*args,**kwords)
            except Exception as exception:
                exception_reporter = ExceptionReporter()
                exception_reporter.reported(module_name=module_name,path_name=path_name,detail=repr(exception),stack_info=traceback.format_exc())
        return new_function
    return agenter

            
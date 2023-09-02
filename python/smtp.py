 
import smtplib
from email.mime.text import MIMEText # 邮件正⽂文 from email.header import Header # 邮件头
# 登录邮件服务器器
smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465) # 发件⼈人邮箱中的SMTP服务 器器，端⼝口是25
smtp_obj.login("nami@luffycity.com", "pwd") # 括号中对应的是发件⼈人邮箱账 号、邮箱密码
#smtp_obj.set_debuglevel(1) # 显示调试信息
# 设置邮件头信息
msg = MIMEText("Hello, text", "plain", "utf-8") msg["From"] = Header("来⾃自娜美的问候","utf-8") # 发送者
msg["To"] = Header("有缘⼈人","utf-8") # 接收者
msg["Subject"] = Header("娜美的信","utf-8") # 主题
# 发送
smtp_obj.sendmail("nami@luffycity.com", ["xx@xxxx.com", "xxxxx@qq.com"], msg.as_string())
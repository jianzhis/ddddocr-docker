# 使用官方 Python 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将当前目录的文件复制到容器的 /app 目录
COPY . /app

# 使用清华大学源安装 requirements.txt 中列出的所有必需包
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 对外开放 5000 端口
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=ocr.py
ENV FLASK_RUN_HOST=0.0.0.0

# 运行 Flask 应用
CMD ["flask", "run"]

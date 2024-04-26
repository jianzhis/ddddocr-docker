# ddddocr Docker版本

## 介绍

本项目是ddddocr的Docker版本，旨在通过Docker容器化技术简化部署和使用流程。原项目是一个验证码识别工具，本版本在保持原功能的基础上，增加了Docker支持和Web接口，以满足更灵活的部署需求。

## 新增功能

### Docker 支持

通过Docker，用户可以快速部署和启动本项目，无需手动配置环境。

### Web 接口

新增Web接口，用户可以通过HTTP请求直接调用验证码识别服务。

## 快速开始

### 使用Docker部署

1. 构建Docker镜像：
   ```bash
   git clone https://github.com/jianzhis/ddddocr-docker.git
   cd ddddocr-docker
   docker build -t ddddocr .
   ```

2. 运行容器：
   ```bash
   docker run -p 8080:5000 ddddocr
   ```

### 调用Web接口

向`http://localhost:8080/recognize`发送POST请求，附带图片数据，即可进行验证码识别。

## 贡献

欢迎通过GitHub的Pull Request或Issues方式提交代码修正、功能建议等贡献。

## 许可证

[MIT](LICENSE) © [Sekey]

## 致谢

特此感谢原项目的作者，本项目在原有基础上进行了增强以更好地服务于社区。
```
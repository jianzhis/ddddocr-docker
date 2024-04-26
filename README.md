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
   docker run -p 10049:5000 ddddocr
   ```

### 调用Web接口

您可以使用以下`curl`命令从命令行发送POST请求，附带一个验证码图片：

```bash
curl --location --request POST 'http://localhost:10049/ocr_url' \
--header 'Content-Type: application/json' \
--data-raw '{
    "image_url": "https://img.xwyue.com/i/2024/04/26/662b805c43cd7.png"
}'
```

确保将 `http://localhost:10049/ocr_url` 替换为您的服务器地址及端口，并且将 `"image_url"` 的值替换为您的图片的URL。

## 贡献

欢迎通过GitHub的Pull Request或Issues方式提交代码修正、功能建议等贡献。

## 许可证

[MIT](LICENSE) © [Sekey]

## 致谢

特此感谢原项目[ddddocr](https://github.com/sml2h3/ddddocr)，本项目在原有基础上进行了增强以更好地服务于社区。
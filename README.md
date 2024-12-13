# Live2D Chatbot Demo

A live2D Chatbot Demo build with python and js.

![](screenshot.png)

## 使用说明

### 1. 安装依赖
见：requirements.txt

### 2. 配置ChatGPT

见：chatbot_demo.py
``` py

API_KEY = "USE YOUR OWN OPENAI API KEY"
BASE_URL = "USE YOUR OWN BASE URL"
MODEL_NAME = "CHOOSE YOUR MODEL"

```


### 3. 启动前后端服务
```
python live2d_display_server.py
```

### 4. 启动ChatBot
```
python chatbot_demo.py
```

### 5. 打开浏览器
打开浏览器输入http://127.0.0.1:4800/ ，查看虚拟形象。

## 代码目录
- scripts文件夹：声音分析
- src：前端js代码
- index.html：前端html

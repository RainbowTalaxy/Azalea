# 备忘录

[init by docker guide](https://docs.docker.com/language/python/build-images/)

虚拟环境：

```sh
# 创建虚拟环境
python3 -m venv .venv
# 激活虚拟环境
source .venv/bin/activate
# 退出虚拟环境
deactivate
```

跑项目：

```sh
# 安装依赖
pip install -r requirements.txt
# 运行项目
python app.py
```

安装数据：

```
python -m nltk.downloader punkt

python -m spacy download en_core_web_lg
```

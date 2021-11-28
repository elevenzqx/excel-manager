# 表格管理器

## 介绍

用于数表格的管理

```
pip freeze > requirements.txt
```

```
# 安装

pip install pipreqs

# 在当前目录生成

pipreqs . --encoding=utf8 --force
```

注意 --encoding=utf8 为使用utf8编码，不然可能会报UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 406: illegal multibyte sequence 的错误。

--force 强制执行，当 生成目录下的requirements.txt存在时覆盖。

```
pip install -r requirements.txt
```

# MuseRAG


## 1.部署环境
```bash
conda create -n muser python=3.11 -y

conda activate muser

pip install -r requirements.txt

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

#下载模型
python download_model.py
```

## 2.添加数据
在 数据库.txt  文件里面填入数据，当前只可填入纯文本


## 3.启动项目

```bash
conda activate muser

python run_rag.py
```

## 4.测试
```bash
python test.py
```

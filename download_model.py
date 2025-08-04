import subprocess

# 正确的命令：去掉多余的 README.md
subprocess.Popen(
    'modelscope download --model BAAI/bge-m3 --local_dir ./RAG-model',
    shell=True
)
import os

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'   # 这个镜像网站可能也可以换掉

from huggingface_hub import snapshot_download
model_name="Qwen/Qwen2.5-0.5B-Instruct"
snapshot_download(repo_id=model_name,
                  local_dir_use_symlinks=False,
                  local_dir="/root/model/"+model_name)

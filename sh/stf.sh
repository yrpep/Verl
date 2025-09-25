set -x

nproc_per_node=1
CONFIG_PATH="/root/verl/scripts/sft.yaml"

torchrun --standalone --nnodes=1 --nproc_per_node=$nproc_per_node --master_port=123456 \
     -m verl.trainer.fsdp_sft_trainer \
    --config_path=$CONFIG_PATH

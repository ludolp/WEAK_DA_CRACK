#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/scripts/common_crack_to_crack.sh


# pseudoweak-cw-pa -> ~ 48.02 mIoU
#
snapshot_dir="snapshot/"$source"-"$target"-convnext-1226"
result_dir="result/"$source"-"$target"-convnext-1226"
python train.py \
    --model $model \
    --dataset-source $source \
    --dataset-target $target \
    --data-path-source $source_path \
    --data-path-target $target_path \
    --input-size-source $source_size \
    --input-size-target $target_size \
    --num-classes $num_classes \
    --source-split $source_split \
    --target-split $target_split \
    --test-split $test_split \
    --batch-size $batch_size \
    --num-steps $num_steps \
    --num-steps-stop $num_steps_stop \
    --lambda-seg $lambda_seg \
    --lambda-adv-target1 $lambda_adv1 \
    --lambda-adv-target2 $lambda_adv2 \
    --lambda-weak-cwadv2 $lambda_weak_cwadv2 \
    --lambda-weak-target2 $lambda_weak2 \
    --learning-rate $lr \
    --learning-rate-D $lr_d \
    --restore-from $pretrain \
    --pweak-th $pweak_th \
    --snapshot-dir $snapshot_dir \
    --result-dir $result_dir \
    --save-pred-every $save_step \
    --print-loss-every $print_step \
    --use-weak \
    --use-pseudo \
    --use-weak-cw \
    --use-pixeladapt \
    --val

#!/bin/bash
for i in {0..9}
do
   CUDA_VISIBLE_DEVICES=$1 python crossval_training.py $i
done


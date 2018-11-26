#! /bin/bash

process=/home/wangjian/projects/VarNDRR/data/data_preprocess/script/data_preprocess.py
split=/home/wangjian/projects/VarNDRR/data/data_preprocess/script/data_split.py

data=/home/wangjian/projects/VarNDRR/data/data_preprocess/data

if [ ! -d "work" ];then
mkdir work
else
rm -rf work
fi
cd work

# split dataset
python $split train $data/train.raw.txt
python $split test $data/test.raw.txt
python $split dev $data/dev.raw.txt

# preprocess
python $process 2 train train.arg1 train.arg2 train.lbl
python $process 2 dev dev.arg1 dev.arg2 dev.lbl arg1.vcb.pkl arg2.vcb.pkl
python $process 2 test test.arg1 test.arg2 test.lbl arg1.vcb.pkl arg2.vcb.pkl

rm *.arg1 *.arg2 *.lbl

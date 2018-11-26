#! /bin/bash

process=script/data_preprocess.py
split=script/data_split.py

data=data/

mkdir work
cd work

# split dataset
python $split train $data/train
python $split test $data/test
python $split dev $data/dev

# preprocess
python $process 4 train train.arg1 train.arg2 train.lbl
python $process 4 dev dev.arg1 dev.arg2 dev.lbl arg1.vcb.pkl arg2.vcb.pkl
python $process 4 test test.arg1 test.arg2 test.lbl arg1.vcb.pkl arg2.vcb.pkl

rm *.arg1 *.arg2 *.lbl

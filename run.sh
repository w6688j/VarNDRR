#! /bin/bash

THEANO_FLAGS='floatX=float32,device=cuda,nvcc.fastmath=True' python VarNDrr.py config.py

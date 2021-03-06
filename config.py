dict(
    z=20,  # the dimension of latent variable
    batch_size=16,  # mini-batch size
    label_size=2,  # the number of discourse relation label, we model it as one-vs-all
    L=1,  # the sample number
    learning_rate=0.001,  # lerning rate for Adam
    max_iter=1000,  # maximum iteration number, here we set to 100, we use 1000 in our paper
    clip_c=1.,  # gradient clip
    is_load=False,  # whether load model parameters, during testing, this should be corrected
    seed=1473769786,  # the seed for random, same seed for same results.

    train_arg1='./data/finally/train.arg1.dta.pkl',
    train_arg2='./data/finally/train.arg2.dta.pkl',
    train_lbl='./data/finally/train.lbl.dta.pkl',
    dev_arg1='./data/finally/dev.arg1.dta.pkl',
    dev_arg2='./data/finally/dev.arg2.dta.pkl',
    dev_lbl='./data/finally/dev.lbl.dta.pkl',
    test_arg1='./data/finally/test.arg1.dta.pkl',
    test_arg2='./data/finally/test.arg2.dta.pkl',
    test_lbl='./data/finally/test.lbl.dta.pkl',

    mode='train',  # train or test, if test, make the is_load True
)

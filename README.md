# itk-physionet-17
Supplementary content for our Special Issue Article submitted to Physiological Measurement

## Quick-demo
Clone the repo and make it the working directory
```
git clone https://github.com/botcs/itk-physionet-17
cd itk-physionet-17
```

Install the python dependencies
```
pip install -r requirements.txt
```

Download and extract the training data from Physionet's server
```
cd data
./download_raw.sh
cd ..
```

Create reference files for the K-fold cross-validation
```
python data/cross_val_reference_generator.py --K 10
```

Run the training script on the i^th fold
```
python crossval_training.py 1 --dryrun
```

Training for 100 epochs takes ~30 min. average result is F1=0.75 on the validation set.

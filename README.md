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
```

Create reference files for the K-fold cross-validation
```
python data/cross_val_reference_generator.py --K 10
cd ..
```

Run the training script on the 1st fold (indexing starts at 0)
```
python crossval_training.py 0 --dryrun
```

Training on RTX 2080 for 100 epochs takes ~30 min. average result is F1=0.75 on the validation set.

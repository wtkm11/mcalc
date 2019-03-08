# mcalc

A program for computing LACE scores

## Install
```
$ git clone https://github.com/wtkm11/mcalc
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e .
```

## Run
`$ mcalc lace MEASURE_NAME` where `MEASURE_NAME` is the name of a
measure like `AMI` or `COPD`

*NOTE: MEASURE_NAME is case-sensitive.*


## Run tests
```
$ pip install pytest pytest-cov
$ pytest
```

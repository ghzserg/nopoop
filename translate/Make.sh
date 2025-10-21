#!/bin/bash

for i in *.csv; do
    python3 translate.py $i
done

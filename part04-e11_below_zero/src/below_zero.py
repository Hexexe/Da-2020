#!/usr/bin/env python3
import pandas as pd

def below_zero():
    a = pd.read_csv("src/kumpula-weather-2017.csv")
    return len(a[a["Air temperature (degC)"] < 0])

def main():
    print(f"Number of days below zero: {below_zero()}")
    
if __name__ == "__main__":
    main()
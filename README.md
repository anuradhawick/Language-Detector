# Language Classifier
### Training process
#### Pre-requistites 
Install the library to read unicode

`$ pip3 install chardet`
#### Inputs
`$ python3 build_stat.py <LANGUAGE DATA> <TARGET DATA>`
* `<LANGUAGE DATA>` for training the model
* `<TARGET DATA>` for storing trained model

#### Process
* Repeat the above process for both the languages SINHALA and TAMIL.
* Then repeat the process for the TEST SAMPLE whose language needs to be detected.

### Running the detector
`$ python3 detector.py <TARGET STATS> <SINHALA STATS> <TAMIL STATS>`
* `<TARGET STATS>` file name of the stored data of TEST SAMPLE
* `<SINHALA STATS>` file name of the stored data of SINHALA model
* `<TAMIL STATS>` file name of the stored data of TAMIL model

### Output
```Language detected: SINHALA```

```MAE: 1.0206944116 < 1.70093005005```

MAE:  Mean Absolute Error
### Stat analysis process
#### Pre-requistites 
Install the matplotlib to read unicode

`$ pip3 install matplotlib`
#### Inputs
`$ cd stat_analysis`
`$ python3 plotter.py`

#### Process
* Provide plots for variation of the combinations for each language
* Identify the critical combinations to be tested that demontrate significant difference in distribution
* Define tolerance values in the detector.py file
# Evaluation
These are the steps needed to reproduce our evaluation plots.
## Requirements
The requirements from the README in the root directory must also be met to run our evaluation
- plotly
    - To install, run:
        ```
        sudo pip2 install plotly
        ```
- defects4j (https://github.com/rjust/defects4j)

## Reproduce Results
To reproduce the results for Lang and Math, move to the commit-min repo and run:
```
./scripts/evaluate Lang 65
./scripts/evaluate Math 106
```

This will run on all in Lang, then all bugs in math and output the results as html files. Note this takes several hours.


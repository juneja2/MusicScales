* How to run this project?

1. Install python3 if it's not already installed.
2. In order to check if python3 is installed, run ```which python3``` if you are on Linux or MacOS.
3. Navigate to the root of this project.
4. Install dependencies with ```pipenv install``` or ```pipenv install --dev```.
5. Now run ```python3 main.py```.
6. If it doesn't work make sure python3 was added to your path.
7. The scale waveform should be outputted to ```A4_scale.wav``` file in the ```root folder```.
8. To listen to the the generated scale on MacOS, go to terminal and cd to the root of the project.
   Run ```afplay A4_scale.py```.

* How to customize the project?

1. To create a new scale open up the main.py.
2. Change line 7 to whatever scale you want to hear. 
   You can change the root note or the quality of the scale(Major or Minor).
   Make sure to ```use # or natural notes``` in order to generate scales.
   Right now there is no support for flat notes. See ```scale.py``` for more information.
   For example, ```Scale('A#', Scale.MINOR)```



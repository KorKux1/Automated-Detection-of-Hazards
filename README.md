# AQUDA

<div align="center">
  <img src="resources/logo.png" height="250px">
</div>

We propose a data integration and prediction system (AQUDA), that has state-of-the-art machine learning algorithms for novelty detection and a web app that includes dashboards that allow any researcher to make real time decisions, moreover the system is designed that any user regardless of his or her academic background can receive some information about the actual situation of the geographic zone with the purpose to bring awareness of climate change. We consider it a very important problem to solve, because we want to make people conscious that pollution is getting worse due to vehicles and industries that throw out harmful gases to the atmosphere, and if we don't act now, there will be an irreversible damage.

<p align="center">

<a href="https://github.com/KorKux1/Automated-Detection-of-Hazards/pulls">
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/></a>

<a href="https://github.com/KorKux1/Automated-Detection-of-Hazards/blob/develop/LICENSE">
<img alt="GitHub license" src="https://img.shields.io/github/license/KorKux1/Automated-Detection-of-Hazards?label=license"/></a>

<a href="https://github.com/KorKux1/Sleepy-Monitor/graphs/contributors">
<img src="https://img.shields.io/badge/contributors-3-red" alt="GitHub contributors"/></a>

<a href="https://github.com/KorKux1/Automated-Detection-of-Hazards/issues">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/KorKux1/Automated-Detection-of-Hazards"></a>

<a href="https://github.com/KorKux1/Automated-Detection-of-Hazards/network">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/KorKux1/Automated-Detection-of-Hazards"></a>

<a href="https://github.com/KorKux1/Automated-Detection-of-Hazards/stargazers">
<img alt="GitHub stars" src="https://img.shields.io/github/stars/KorKux1/Automated-Detection-of-Hazards"></a>

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KorKux1/Automated-Detection-of-Hazards">

<div align="center">
    <a href="https://github.com/urcuqui">
        <img alt="GitHub followers" src="https://img.shields.io/github/followers/urcuqui?label=urcuqui&style=social">
    </a>
    <a href="https://github.com/KorKux1">
        <img alt="GitHub followers" src="https://img.shields.io/github/followers/KorKux1?label=KorKux&style=social">
    </a>
    <a href="https://github.com/jsvillatech">
        <img alt="GitHub followers" src="https://img.shields.io/github/followers/jsvillatech?label=jsvillatech&style=social">
    </a>
</div>

</p>

## Space Apps Challenge - AQUDA Solution

AQUA was born from the hackathon space apps 2020. You can find more information [HERE](https://2020.spaceappschallenge.org/challenges/inform/automated-detection-hazards/teams/mlonfire/project).

## Requirements

- Languages:
  
<img alt="python" src="https://img.shields.io/badge/python-3.8-green"> 

- Libraries: scikit-learn, numpy, matplotlib, dash, torchvision, PIL, Django, bootstrap, pytorch, pandas, seaborn.

## Dashboard

We build a dashboard for the visualization of data on air quality.

<p align="center">

<img alt="AQUDA Index" src="resources/index.png">

Visualization of statistics for the metrics of PM, RH, UGRD, VGRD, HPBL, TMP, GOES per year.

<img alt="AQUDA Index" src="resources/data.png">

Visualization of the behavior of the measures with respect to the others

<img alt="AQUDA Measurament Relationship" src="resources/measurement relationship.gif">

Visualization of the averages of the different measurements per month.

<img alt="AQUDA Measurament Relationship" src="resources/measurement dates.gif">

We raise awareness for all people. It consists of knowing how many cigarettes smoked per day the air you breathe is equivalent.

<img alt="AQUDA awareness" src="resources/smoking.png">

</p>

## [System for the detection of harmful particles in the air](https://github.com/KorKux1/Automated-Detection-of-Hazards/blob/develop/Notebooks/AQUDA-Novelty%20detection.ipynb)

We created a system based on the detection of anomalies to be able to identify data of harmful particles and make predictions of future records.

<p align="center">

<img alt="AQUDA Novelty 1" src="resources/novelty1.png">

<img alt="AQUDA Novelty 2" src="resources/novelty2.png">
</p>

## [System for the detection of dust particles given satellite images](https://github.com/KorKux1/Automated-Detection-of-Hazards/blob/develop/Notebooks/Nasa_Analytics.ipynb)

We developed a deep neural network based on ResNet-50 to perform dust detection in the air by satellite images.

<img alt="AQUDA Dust" src="resources/dust detection.png">

## Installation

**Clone the repository**

    $ git clone https://github.com/KorKux1/Automated-Detection-of-Hazards.git

**Create virtual enviroment:**

    $ python -m venv env

Active your enviroment

**Install dependencies**

    $ pip install -r requirements.txt

**Run the project**

    $ python manage.py runserver

## Contributors

- Christian Urcuqui.
- Cristhian Eduardo Castillo.
- Jhoan Delgado.

## License

AGPL-3.0

---
⌨️ with the ❤️

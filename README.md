# ovos-m2v-pipeline Model Comparison

This repository contains training code and evaluation results for several sentence classification models trained on intent-labeled utterances. Models are either **language-specific** (trained only on utterances in a particular language) or **multilingual** (trained on all languages jointly).

## Overview

The goal of this experiment is to compare the performance of different sentence embedding models for intent classification. Each model is trained and evaluated on a subset of a dataset filtered by language or used in full for multilingual models. 

## Dataset

* The training dataset consists of labeled user utterances (intents) stored in a single CSV file. Consists mostly of the data exported from our [GitLocalize]() platform
* A new version of this dataset is generated every 24h with the latest translations and new skills at https://github.com/OpenVoiceOS/skill-metrics
* Only labels with at least two samples are retained for training.
* Stratified train-test splits (80/20) ensure balanced class distributions.

## Training Procedure

For each model:

* Train using a maximum of 25 epochs on the filtered dataset
* Evaluate on the held-out test set using:
    * Accuracy
    * Weighted F1 Score
    * Cohen’s Kappa
    * Matthews Correlation Coefficient (MCC)
* Save:
    * Trained pipeline
    * Classification report
    * Confusion matrix
    * Per-class F1 bar chart
    * Top 20 misclassified intents chart
    * Markdown file with metrics summary

## Results Summary

* **Multilingual models** were trained with the full dataset across all languages.
* **Language-specific models** were trained on sentences corresponding to that language only.

| Language     | Base Model                                           | Accuracy | F1 Score |
| :----------- | :--------------------------------------------------- | -------: | -------: |
| galician     | Jarbas/m2v-256-bertinho-gl-small-cased               | 0.981051 | 0.979181 |
| galician     | Jarbas/m2v-256-bertinho-gl-base-cased                | 0.986219 | 0.984496 |
| english      | minishlab/potion-base-2M                             | 0.959474 | 0.954859 |
| english      | minishlab/potion-base-4M                             | 0.958421 | 0.953956 |
| english      | minishlab/potion-base-8M                             | 0.964211 | 0.959403 |
| english      | minishlab/potion-base-32M                            | 0.973684 | 0.969956 |
| english      | minishlab/potion-retrieval-32M                       | 0.965789 | 0.961320 |
| multilingual | Jarbas/m2v-256-LaBSE                                 | 0.989988 | 0.989524 |
| multilingual | Jarbas/m2v-256-paraphrase-multilingual-MiniLM-L12-v2 | 0.981112 | 0.980015 |
| multilingual | Jarbas/m2v-256-paraphrase-multilingual-mpnet-base-v2 | 0.982745 | 0.981604 |
| multilingual | Jarbas/m2v-256-distiluse-base-multilingual-cased-v2  | 0.985798 | 0.985126 |

## Outputs

For each model, the following files are generated:

* `metrics_*.md`: Detailed classification metrics.
* `*_f1_per_class.png`: Bar chart of per-intent F1 scores.
* `*_top20_misclassified_intents.png`: Top 20 lowest-F1 intents.
* `model_comparison_en.md`: Markdown summary table comparing all English models.

## Requirements

*Required packages include*:

* `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tqdm`, `requests`, `model2vec[train]` 

## Future Work

* Expand evaluation to additional languages and base models.
* Introduce more robust intent augmentation techniques.

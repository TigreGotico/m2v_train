# Quickstart — gather, distill, train, benchmark

`m2v_train` distills transformer encoders into [model2vec](https://github.com/MinishLab/model2vec)
static embeddings and trains them as **intent classifiers** for OpenVoiceOS. It is
a set of standalone scripts run from the repo root, not a Python package.

## 1. Install

```bash
pip install -r requirements.txt   # model2vec[train]
pip install pandas matplotlib seaborn scikit-learn tqdm requests
```

A GPU helps the distillation step; classifier training runs on CPU.

## 2. The one idea — OVOS `domain:intent` labels

Every utterance is labelled `domain:intent`, where `domain` is an OVOS skill id and
`intent` is the intent handler. The label is the exact bus target that triggers the
intent, so a classifier trained here drops straight into the `ovos-m2v-pipeline`
with no remapping:

```python
label = "ovos-skill-date-time.openvoiceos:what.time.is.it.intent"
skill, intent = label.split(":", 1)
print(skill)    # ovos-skill-date-time.openvoiceos
print(intent)   # what.time.is.it.intent
```

`gather_dataset.py` normalizes messy source data into this shape — lowercasing,
stripping quotes, and merging near-duplicate intents (e.g. `what.date.is.it.intent`
→ `current_date.intent`) so the label space stays clean.

## 3. The pipeline

Four stages, run in order from the repo root:

```bash
python gather_dataset.py        # merge sources -> merged_intents_dataset.csv (+ label files)
python distill.py               # (optional) encoders -> 256-dim M2V models
python train_pt.py              # train + evaluate Portuguese models
```

`gather_dataset.py` writes the corpus and three label files
(`labels.txt`, `adapt_labels.txt`, `padatious_labels.txt`) plus
`skill_metrics.json`. The `train_<lang>.py` scripts read the corpus, filter by
language, keep labels with more than one sample, do a stratified 80/20 split, fit
each base model, and emit a metrics markdown, two charts, and a comparison table.

## 4. First real call — train a classifier

The core training object is `StaticModelForClassification`. With a tiny inline
corpus you can fit and predict end to end:

```python
from model2vec.train import StaticModelForClassification

X = ["que horas são", "que dia é hoje", "toca uma música"]
y = [
    "ovos-skill-date-time.openvoiceos:what.time.is.it.intent",
    "ovos-skill-date-time.openvoiceos:current_date.intent",
    "ocp:play",
]
clf = StaticModelForClassification.from_pretrained(model_name="minishlab/potion-base-8M")
clf.fit(X, y, max_epochs=3)
print(clf.predict(["que horas são agora"]))
```

`from_pretrained` and `fit` download the base model on first use, so the snippet
above needs network access the first time. The runnable examples avoid that by
demonstrating the normalization and evaluation logic on inline data, and
guard-and-skip the model download.

## 5. Distill your own encoder

To add a new base model, distill it to the house width of 256 dims:

```python
from model2vec.distill import distill

m2v = distill(model_name="neuralmind/bert-base-portuguese-cased", pca_dims=256)
m2v.save_pretrained("bert-base-portuguese-cased-distill256")
```

## Where next

- [api.md](api.md) — model2vec calls, the normalization helpers, metric shapes
- [advanced.md](advanced.md) — run order, Adapt/Padatious split, gotchas, OVOS integration
</content>

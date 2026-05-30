# API — calls, helpers, and shapes

This repo has no importable package. Its surface is (1) the model2vec calls the
trainers drive, (2) the normalization helpers in `gather_dataset.py`, and (3) the
scikit-learn metric shapes each trainer emits.

## model2vec — training a classifier

```python
from model2vec.train import StaticModelForClassification
```

### `StaticModelForClassification.from_pretrained(*, model_name="minishlab/potion-base-32m", out_dim=2, **kwargs)`

Loads a static (distilled) model and wraps it with a classification head. The
trainers pass the published id, e.g. `model_name="Jarbas/m2v-256-LaBSE"`.
Returns a `StaticModelForClassification`.

### `clf.fit(X, y, learning_rate=0.001, batch_size=None, min_epochs=None, max_epochs=-1, early_stopping_patience=5, test_size=0.1, device="auto", ...)`

Trains the head. `X` is a `list[str]` of utterances, `y` a parallel list of
`domain:intent` label strings. The trainers use `max_epochs=25`. Returns the same
classifier (fitted, chainable).

### `clf.predict(X, show_progress_bar=False, batch_size=1024, threshold=0.5) -> np.ndarray`

Predicts labels for a `list[str]`. Returns a NumPy array of label strings aligned
with `X`.

### `clf.to_pipeline() -> StaticModelPipeline`

Converts the fitted classifier into an inference pipeline.
`pipeline.save_pretrained(path)` writes a directory loadable later with
`StaticModelPipeline.from_pretrained(path)` (in `model2vec.inference`).

## model2vec — distillation

```python
from model2vec.distill import distill
```

### `distill(model_name, vocabulary=None, device=None, pca_dims=256, sif_coefficient=0.0001, ...) -> StaticModel`

Distills a transformer encoder into a static model. This repo always uses
`pca_dims=256`. `model.save_pretrained(path)` writes the M2V model directory.

## Normalization helpers (`gather_dataset.py`)

Pure string functions that map noisy source data onto the OVOS label convention.
They take a value and return a cleaned string. Because importing the module runs
its full pipeline, reuse these by copying the definitions rather than importing.

### `normalize(text) -> str`

Utterance cleaner: lowercases, drops commas, takes the last `/`-segment, collapses
double spaces, strips surrounding whitespace and quote characters.

```python
normalize('  "Que Horas São?, "')   # 'que horas são?'
```

### `normalize_domain(text) -> str`

Skill-id cleaner: strips quotes, rewrites `.OpenVoiceOS.openvoiceos` →
`.openvoiceos`, fixes the inverted `skill-ovos-` → `ovos-skill-`, lowercases.

```python
normalize_domain("skill-ovos-Weather.OpenVoiceOS.openvoiceos")
# 'ovos-skill-weather.openvoiceos'
```

### `normalize_intent(text) -> str`

Intent cleaner: applies the `INTENT_REPLACEMENTS` merge map (e.g.
`what.date.is.it.intent` → `current_date.intent`) and collapses a doubled
`.intent.intent` suffix.

### `normalize_label(text) -> str`

Final label cleaner: strips quotes and applies the `LABEL_FIXES` map for known bad
full labels. A label is built as `domain + ":" + intent` then passed through this.

## Label files written by `gather_dataset.py`

| File | Contents |
| --- | --- |
| `merged_intents_dataset.csv` | columns `lang, label, sentence` — the training corpus |
| `labels.txt` | every unique `domain:intent` label, sorted |
| `adapt_labels.txt` | labels with no `.intent` suffix containing `ovos-skill-` |
| `padatious_labels.txt` | labels ending in `.intent` containing `ovos-skill-` |
| `skill_metrics.json` | `{n_skills, n_intents, n_adapt_intents, n_padatious_intents}` |

## Evaluation metrics (per trainer)

Each `train_<lang>.py` computes, per base model, with scikit-learn:

```python
from sklearn.metrics import (
    accuracy_score, f1_score, cohen_kappa_score,
    matthews_corrcoef, classification_report, confusion_matrix,
)

accuracy = accuracy_score(y_test, y_pred)              # float
f1       = f1_score(y_test, y_pred, average="weighted")# float
kappa    = cohen_kappa_score(y_test, y_pred)           # float
mcc      = matthews_corrcoef(y_test, y_pred)           # float
report   = classification_report(y_test, y_pred)               # str
report_d = classification_report(y_test, y_pred, output_dict=True)  # dict
cm       = confusion_matrix(y_test, y_pred)            # np.ndarray (n_labels, n_labels)
```

The per-class F1 comes from `report_d[label]["f1-score"]`; `1 - f1` drives the
"top 20 misclassified intents" chart.

### Output files per model

| Pattern | Contents |
| --- | --- |
| `metrics_<lang>_<model>.md` | accuracy, F1, kappa, MCC, classification report |
| `<lang>_<model>_f1_per_class.png` | per-intent F1 bar chart |
| `<lang>_<model>_top20_misclassified_intents.png` | lowest-F1 intents |
| `model_comparison_<lang>.md` | markdown table: language, model, accuracy, F1 |

## Where next

- [quickstart.md](quickstart.md) — the four-stage pipeline end to end
- [advanced.md](advanced.md) — run order, Adapt/Padatious split, gotchas, OVOS integration
</content>

# Advanced — recipes, gotchas, integration

## Run order

`gather_dataset.py` must run before any `train_<lang>.py`: the trainers read
`merged_intents_dataset.csv`, which the gather step writes (and which is
gitignored). `distill.py` is independent and optional — the trainers default to
already-distilled `Jarbas/m2v-256-*` and `minishlab/potion-*` models on the Hub.

```bash
python gather_dataset.py        # -> merged_intents_dataset.csv (+ label files)
python train_pt.py              # -> metrics_pt_*.md, pt_*.png, model_comparison_pt.md
```

## Recipe — distill a new encoder at the house width

Every published model in this repo is 256-dim. Match that when adding an encoder:

```python
from model2vec.distill import distill

src = "PORTULAN/serafim-100m-portuguese-pt-sentence-encoder"
m2v = distill(model_name=src, pca_dims=256)
m2v.save_pretrained(src + "-distill256")
```

Add the resulting `Jarbas/m2v-256-<name>` id to the `base_models` list in the
matching `train_<lang>.py`.

## Recipe — keep only trainable labels

Stratified splitting needs at least two samples per class. The trainers drop
singletons before splitting and print what they dropped:

```python
import pandas as pd

counts = pd.Series(y).value_counts()
keep = counts[counts > 1].index
mask = pd.Series(y).isin(keep).values
X, y = X[mask], y[mask]
```

[examples/05_label_buckets.py](../examples/05_label_buckets.py) shows the same
filtering plus the Adapt/Padatious split that `gather_dataset.py` applies.

## The OVOS label split — Adapt vs Padatious

`gather_dataset.py` partitions labels by suffix so each OVOS intent engine gets
only the labels it can train on:

- **`adapt_labels.txt`** — labels whose intent has **no** `.intent` suffix
  (keyword/Adapt-style), e.g. `common_query:common_query`.
- **`padatious_labels.txt`** — labels ending in `.intent` (example-based
  Padatious-style), e.g. `ovos-skill-date-time.openvoiceos:what.time.is.it.intent`.

Both buckets are restricted to ids containing `ovos-skill-`. This is a label
**convention**, not a per-engine model — the trained M2V classifier predicts the
full `domain:intent` string regardless of which bucket a label falls in.

## Per-language vs multilingual

The single-language trainers filter the corpus first:

```python
df = df[df["lang"].isin(valid_langs)]   # e.g. ["pt"]
```

`train_multilingual.py` omits that filter and fits on the whole corpus, so its
`base_models` are cross-lingual encoders (`LaBSE`,
`distiluse-base-multilingual`, …).

## Gotchas

- **Scores are optimistic.** The 80/20 split is drawn from the same corpus the
  models train on; there is no separate human-validated test set yet. Treat
  reported accuracy/F1 as a relative ranking between models, not absolute quality.
- **English skips local distillation.** `train_en.py` points straight at
  `minishlab/potion-*`, which are pre-distilled — running `distill.py` for English
  is unnecessary.
- **Saturated languages.** Catalan and Galician sit near 0.99 F1, partly because
  their source data is template-heavy; small deltas there are noise.
- **`gather_dataset.py` is side-effectful at import.** Importing it runs the full
  network + file-writing pipeline. To reuse only the normalization logic, copy the
  helper functions rather than `import gather_dataset` (the examples do this).
- **GPU for distillation.** `distill()` is the heavy step; classifier `fit()` runs
  on CPU but is faster with `device="cuda"`.

## Integration — using a trained model in OVOS

Because labels are already `domain:intent` bus targets, the saved pipeline plugs
into the `ovos-m2v-pipeline` with no remapping. Load and predict:

```python
from model2vec.inference import StaticModelPipeline

pipe = StaticModelPipeline.from_pretrained(
    "model_pt_m2v-256-serafim-100m-portuguese-pt-sentence-encoder-ir"
)
label = pipe.predict(["que horas são"])[0]
skill, intent = label.split(":", 1)
print(skill, intent)
```

## Automation

The corpus is regenerated from `OpenVoiceOS/lang-support-tracker` (treated as the
authoritative, latest data) plus HuggingFace augmentation sets. Re-running
`gather_dataset.py` picks up new default skills automatically, which makes the
gather → train → benchmark loop a candidate for scheduled CI.

## Where next

- [quickstart.md](quickstart.md) — install + the label idea + first call
- [api.md](api.md) — model2vec calls, normalization helpers, metric shapes
</content>

"""Drop singleton labels and make a stratified 80/20 split, like the trainers.

Stratified splitting requires at least two samples per class; the trainers report
and drop singletons first.

Run::

    python examples/04_filter_and_split.py
"""
import pandas as pd
from sklearn.model_selection import train_test_split

DT = "ovos-skill-date-time.openvoiceos"
WX = "ovos-skill-weather.openvoiceos"


def main() -> None:
    rows = [
        (f"{DT}:what.time.is.it.intent", "que horas são"),
        (f"{DT}:what.time.is.it.intent", "diz-me as horas"),
        (f"{DT}:what.time.is.it.intent", "que horas tens"),
        (f"{DT}:what.time.is.it.intent", "sabes que horas são"),
        (f"{DT}:what.time.is.it.intent", "diz-me a hora certa"),
        (f"{DT}:current_date.intent", "que dia é hoje"),
        (f"{DT}:current_date.intent", "em que dia estamos"),
        (f"{DT}:current_date.intent", "qual é a data de hoje"),
        (f"{DT}:current_date.intent", "diz-me a data"),
        (f"{DT}:current_date.intent", "que data temos"),
        (f"{WX}:is_rain.intent", "vai chover"),
        (f"{WX}:is_rain.intent", "preciso de guarda-chuva"),
        (f"{WX}:is_rain.intent", "vai chover hoje"),
        (f"{WX}:is_rain.intent", "está a chover lá fora"),
        (f"{WX}:is_rain.intent", "vai cair chuva"),
        (f"{WX}:wind_speed.intent", "está muito vento"),  # singleton -> dropped
    ]
    df = pd.DataFrame(rows, columns=["label", "sentence"])

    counts = df["label"].value_counts()
    keep = counts[counts > 1].index
    dropped = counts[counts <= 1].index.tolist()
    df_ok = df[df["label"].isin(keep)]

    print(f"labels before : {df['label'].nunique()}")
    print(f"dropped (1 ex): {dropped}")

    X = df_ok["sentence"].values
    y = df_ok["label"].values
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=0
    )
    print(f"train samples : {len(X_tr)}")
    print(f"test  samples : {len(X_te)}")
    print(f"test labels   : {sorted(set(y_te))}")


if __name__ == "__main__":
    main()

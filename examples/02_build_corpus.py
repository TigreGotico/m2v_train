"""Build a ``lang, label, sentence`` corpus and dedupe it, like gather_dataset.py.

Uses an inline Portuguese intent set instead of the live HuggingFace / lang-support
-tracker sources, so it runs offline.

Run::

    python examples/02_build_corpus.py
"""
import pandas as pd

DATE_TIME = "ovos-skill-date-time.openvoiceos"
WEATHER = "ovos-skill-weather.openvoiceos"


def main() -> None:
    rows = [
        ("pt", DATE_TIME, "what.time.is.it.intent", "que horas são"),
        ("pt", DATE_TIME, "what.time.is.it.intent", "que horas são"),   # dup
        ("pt", DATE_TIME, "what.time.is.it.intent", "diz-me as horas"),
        ("pt", DATE_TIME, "current_date.intent", "que dia é hoje"),
        ("pt", WEATHER, "current_weather.intent", "como está o tempo"),
        ("pt", WEATHER, "is_rain.intent", "vai chover hoje"),
    ]
    df = pd.DataFrame(rows, columns=["lang", "domain", "intent", "sentence"])
    df["label"] = df["domain"] + ":" + df["intent"]
    df = df[["lang", "label", "sentence"]].drop_duplicates(ignore_index=True)

    print(df.to_string(index=False))
    print()
    print(f"rows           : {len(df)}")
    print(f"unique labels  : {df['label'].nunique()}")
    print(f"unique domains : {df['label'].apply(lambda x: x.split(':')[0]).nunique()}")


if __name__ == "__main__":
    main()

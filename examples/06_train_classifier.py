"""Train a model2vec intent classifier on a tiny inline Portuguese corpus.

Training downloads a base model from HuggingFace, so it is gated behind an opt-in
flag to keep the example offline by default::

    M2V_TRAIN_ONLINE=1 python examples/06_train_classifier.py

Without the flag (or without network access) it prints the corpus and the calls it
would make.

Run::

    python examples/06_train_classifier.py
"""
import os

DT = "ovos-skill-date-time.openvoiceos"
WX = "ovos-skill-weather.openvoiceos"

X = [
    "que horas são", "diz-me as horas", "que horas tens",
    "sabes que horas são", "diz-me a hora certa",
    "que dia é hoje", "em que dia estamos", "qual é a data de hoje",
    "diz-me a data", "que data temos",
    "vai chover hoje", "preciso de guarda-chuva", "está a chover",
    "vai cair chuva", "vai chover esta tarde",
]
y = (
    [f"{DT}:what.time.is.it.intent"] * 5
    + [f"{DT}:current_date.intent"] * 5
    + [f"{WX}:is_rain.intent"] * 5
)


def main() -> None:
    print(f"corpus: {len(X)} utterances over {len(set(y))} labels")
    print("base model: minishlab/potion-base-8M (256-dim house width)")
    print("calls: StaticModelForClassification.from_pretrained(...).fit(X, y, max_epochs=...)")

    if os.environ.get("M2V_TRAIN_ONLINE") != "1":
        print("\nSKIP: set M2V_TRAIN_ONLINE=1 to download the base model and fit.")
        return

    try:
        from model2vec.train import StaticModelForClassification
        clf = StaticModelForClassification.from_pretrained(
            model_name="minishlab/potion-base-8M"
        )
        clf.fit(X, y, max_epochs=3)
    except Exception as e:
        print(f"SKIP: training unavailable ({type(e).__name__}: {e})")
        return

    for utt in ["que horas são agora", "será que chove amanhã"]:
        print(f"{utt!r} -> {clf.predict([utt])[0]}")


if __name__ == "__main__":
    main()

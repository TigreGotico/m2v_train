"""Normalize messy source fields into the OVOS ``domain:intent`` convention.

Mirrors the helpers in ``gather_dataset.py``. They are copied here because
importing that module runs its full network + file-writing pipeline.

Run::

    python examples/01_normalize_labels.py
"""

INTENT_REPLACEMENTS = {
    "what.date.is.it.intent": "current_date.intent",
    "handle_show_time": "what.time.is.it.intent",
    "who.intent": "common_query",
}
LABEL_FIXES = {
    "ovos-skill-ddg.openvoiceos:search_wolfie.intent":
        "ovos-skill-wolfie.openvoiceos:search_wolfie.intent",
}


def normalize(text):
    return (
        str(text).lower().replace(",", "").split("/")[-1]
        .replace("  ", " ").strip().strip('"').strip("'").strip("`")
    )


def normalize_domain(text):
    n = str(text).strip().strip('"').strip("'").strip("`")
    n = n.replace(".OpenVoiceOS.openvoiceos", ".openvoiceos")
    return n.replace("skill-ovos-", "ovos-skill-").lower()


def normalize_intent(text):
    n = str(text).strip().strip('"').strip("'").strip("`")
    for k, v in INTENT_REPLACEMENTS.items():
        n = n.replace(k, v)
    return n.replace(".intent.intent", ".intent")


def normalize_label(text):
    n = str(text).strip().strip('"').strip("'").strip("`")
    for k, v in LABEL_FIXES.items():
        n = n.replace(k, v)
    return n


def main() -> None:
    # Real-world noisy rows: stray quotes, casing, inverted skill prefix.
    rows = [
        ('skill-ovos-Date-Time.OpenVoiceOS.openvoiceos', '  "handle_show_time"  ', '  Que Horas São?  '),
        ('ovos-skill-weather.openvoiceos', 'what.date.is.it.intent', '"Que dia é hoje"'),
        ('ovos-skill-ddg.openvoiceos', 'search_wolfie.intent', 'Pesquisa no wolfram'),
    ]
    for domain, intent, sentence in rows:
        d = normalize_domain(domain)
        i = normalize_intent(intent)
        label = normalize_label(f"{d}:{i}")
        print(f"sentence : {normalize(sentence)!r}")
        print(f"label    : {label}")
        print("-" * 60)


if __name__ == "__main__":
    main()

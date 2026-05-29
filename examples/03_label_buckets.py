"""Split labels into the Adapt and Padatious buckets that gather_dataset.py writes.

A label ending in ``.intent`` (and containing ``ovos-skill-``) is Padatious-style
(example-based); one without the suffix is Adapt-style (keyword-based).

Run::

    python examples/03_label_buckets.py
"""


def main() -> None:
    labels = sorted({
        "ovos-skill-date-time.openvoiceos:what.time.is.it.intent",
        "ovos-skill-date-time.openvoiceos:current_date.intent",
        "ovos-skill-weather.openvoiceos:is_rain.intent",
        "ovos-skill-volume.openvoiceos:volume.mute.toggle.intent",
        "common_query:common_query",
        "ocp:play",
    })

    adapt = [l for l in labels if not l.endswith(".intent") and "ovos-skill-" in l]
    padatious = [l for l in labels if l.endswith(".intent") and "ovos-skill-" in l]

    print(f"all labels        : {len(labels)}")
    print(f"adapt_labels.txt  : {len(adapt)}")
    for l in adapt:
        print(f"  {l}")
    print(f"padatious_labels  : {len(padatious)}")
    for l in padatious:
        print(f"  {l}")

    other = [l for l in labels if "ovos-skill-" not in l]
    print(f"non-skill labels  : {len(other)} (e.g. {', '.join(other)})")


if __name__ == "__main__":
    main()

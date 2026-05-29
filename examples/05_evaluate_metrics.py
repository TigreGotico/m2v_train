"""Compute the same metric set the trainers emit, from inline predictions.

Shows accuracy, weighted F1, Cohen's Kappa, MCC, and the per-class F1 that drives
the "top misclassified intents" chart.

Run::

    python examples/05_evaluate_metrics.py
"""
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    cohen_kappa_score,
    matthews_corrcoef,
    classification_report,
    confusion_matrix,
)

TIME = "ovos-skill-date-time.openvoiceos:what.time.is.it.intent"
DATE = "ovos-skill-date-time.openvoiceos:current_date.intent"
RAIN = "ovos-skill-weather.openvoiceos:is_rain.intent"


def main() -> None:
    y_test = [TIME, TIME, DATE, DATE, RAIN, RAIN, RAIN, TIME]
    y_pred = [TIME, TIME, DATE, RAIN, RAIN, RAIN, DATE, TIME]  # two mistakes

    print(f"accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"f1       : {f1_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"kappa    : {cohen_kappa_score(y_test, y_pred):.4f}")
    print(f"mcc      : {matthews_corrcoef(y_test, y_pred):.4f}")

    report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
    print("\nper-class F1 (worst first):")
    per_class = {
        lbl: vals["f1-score"]
        for lbl, vals in report.items()
        if lbl in {TIME, DATE, RAIN}
    }
    for lbl, f1 in sorted(per_class.items(), key=lambda kv: kv[1]):
        print(f"  {f1:.3f}  {lbl.split(':')[-1]}")

    print("\nconfusion matrix shape:", confusion_matrix(y_test, y_pred).shape)


if __name__ == "__main__":
    main()

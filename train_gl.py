import logging
import os

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from model2vec.train import StaticModelForClassification
from sklearn.metrics import classification_report, accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import cohen_kappa_score, matthews_corrcoef
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def download_dataset(url, path):
    """Download the dataset if it does not already exist."""
    if not os.path.exists(path):
        logger.info(f"Downloading dataset from {url}")
        with open(path, "wb") as f:
            f.write(requests.get(url).content)


base_models = [
    "Jarbas/m2v-256-bertinho-gl-small-cased",
    "Jarbas/m2v-256-bertinho-gl-base-cased"
]

# Metrics storage for later comparison
metrics_summary = []
valid_langs = ["gl"]
csv_path = "merged_intents_dataset.csv"

# Load the dataset and remove duplicates based on the "utterance" column
df = pd.read_csv(csv_path)
df = df[df["lang"].isin(valid_langs)]

# galician model, use all loaded datasets for training
# Combine all datasets into a single training set
all_y = df["label"].values

label_counts = pd.Series(all_y).value_counts()
valid_labels = label_counts[label_counts > 1].index
df_filtered = df[df["label"].isin(valid_labels)]

all_X = df_filtered["sentence"].values
all_y = df_filtered["label"].values

# Identify dropped labels (those with only 1 sample)
dropped_labels = label_counts[label_counts <= 1]

# Filter the original DataFrame to get the example utterances for dropped labels
dropped_examples = df[df["label"].isin(dropped_labels.index)]

# Print the dropped labels along with their corresponding utterances
print("Dropped labels (only 1 sample) with their example utterances:")
for label, utterance in zip(dropped_examples["label"], dropped_examples["sentence"]):
    print(f"Label: {label}, Utterance: {utterance}")

# Split the combined dataset into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(all_X, all_y, test_size=0.2, stratify=all_y)

# Initialize a classifier from one of the galician models
for base_model in base_models:
    classifier = StaticModelForClassification.from_pretrained(model_name=base_model)

    # Train the galician classifier on the combined data
    logger.info(f"Training galician model {base_model}...")
    classifier.fit(X_train, y_train, max_epochs=25)

    # Predict using the trained galician classifier
    logger.info(f"Predicting using the galician model {base_model}...")
    y_pred = classifier.predict(X_test)

    # Evaluate the galician model using various metrics
    logger.info(f"Evaluating galician model {base_model}...")
    report = classification_report(y_test, y_pred)
    report_dict = classification_report(y_test, y_pred,
                                        output_dict=True)
    accuracy = accuracy_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)
    kappa = cohen_kappa_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    conf_matrix = confusion_matrix(y_test, y_pred)

    logger.info(f"galician Classification report:")
    logger.info(f"Accuracy: {accuracy}")
    logger.info(f"F1 Score: {f1}")
    logger.info(f"Matthews Corrcoef: {mcc:.4f}")
    logger.info(f"Cohen Kappa: {kappa:.4f}")
    logger.info("Confusion Matrix:")
    logger.info(f"\n{conf_matrix}")

    # Save the trained galician model
    galician_model_path = f"model_gl_{base_model.split('/')[-1]}"
    pipeline = classifier.to_pipeline()

    if os.path.isfile(galician_model_path):
        os.remove(galician_model_path)
    pipeline.save_pretrained(galician_model_path)
    logger.info(f"galician Model saved as {galician_model_path}")

    # Save the evaluation metrics for the galician model
    summary = {
        "language": "galician",
        "model": base_model,
        "accuracy": accuracy,
        "mcc": mcc,
        "kappa": kappa,
        "f1_score": f1,
        "report": report
    }
    metrics_summary.append(summary)

    # Save the metrics summary to a markdown file
    with open(f"metrics_gl_{base_model.split('/')[-1]}.md", "w") as f:
        f.write("# Model Evaluation Metrics Summary\n")
        f.write(f"## {summary['language']} - Model: {summary['model']}\n")
        f.write(f"### Accuracy: {summary['accuracy']}\n")
        f.write(f"### F1 Score: {summary['f1_score']}\n")
        f.write(f"### Cohen Kappa Score: {summary['kappa']}\n")
        f.write(f"### Matthews Corrcoef Score: {summary['mcc']}\n")
        f.write(f"### Classification Report:\n```\n{summary['report']}\n```\n")
        f.write("\n")

    # === Per-class F1 Bar Chart ===
    logger.info("plotting Per-class F1 Bar Chart")
    f1_per_class = {label: report_dict[label]["f1-score"] for label in valid_labels if label in report}
    f1_df = pd.DataFrame(f1_per_class.items(), columns=["Intent", "F1 Score"])
    f1_df = f1_df.sort_values("F1 Score", ascending=False)
    f1_df["Misclassification"] = 1 - f1_df["F1 Score"]

    plt.figure(figsize=(12, 8))
    sns.barplot(data=f1_df, x="F1 Score", y="Intent", palette="coolwarm")
    plt.title(f"Per-Class F1 Scores: {base_model.split('/')[-1]}")
    plt.tight_layout()
    plt.savefig(f"gl_{base_model.split('/')[-1]}_f1_per_class.png")
    plt.close()

    # === Top 20 Most Misclassified Intents ===
    # Calculate misclassification (1 - F1) and keep top 20 worst (lowest F1 scores)
    misclassified_df = f1_df.sort_values("Misclassification", ascending=False).head(20)

    # Plot the misclassified intents based on F1 scores
    plt.figure(figsize=(12, 8))
    sns.barplot(data=misclassified_df, x="Misclassification", y="Intent", palette="Reds_d")
    plt.title(f"Top 20 Most Misclassified Intents (Low F1): {base_model.split('/')[-1]}")
    plt.tight_layout()
    plt.savefig(f"gl_{base_model.split('/')[-1]}_top20_misclassified_intents.png")
    plt.close()

# Save metrics to a DataFrame for better visualization and comparison
comparison_df = pd.DataFrame(columns=["Language", "Model", "Accuracy", "F1 Score"])

# Loop through the metrics summary to fill the comparison DataFrame
for summary in tqdm(metrics_summary, desc="Building Model Comparison", unit="model"):
    comparison_df = pd.concat([
        comparison_df,
        pd.DataFrame([{
            "Language": summary['language'],
            "Model": summary['model'],
            "Accuracy": summary['accuracy'],
            "F1 Score": summary['f1_score']
        }])
    ], ignore_index=True)

# Save the comparison DataFrame to a markdown table
with open("model_comparison_gl.md", "w") as f:
    f.write("# Model Comparison\n")
    f.write(comparison_df.to_markdown(index=False))

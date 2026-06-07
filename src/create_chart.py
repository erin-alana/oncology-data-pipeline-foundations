import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "outputs/stage_summary.csv"
OUTPUT_PATH = "outputs/stage_distribution.png"

def main():
    df = pd.read_csv(INPUT_PATH)
    df["stage"] = df["stage"].fillna("Missing").astype(str)

    plt.figure(figsize=(8, 5))
    plt.bar(df["stage"], df["patient_count"])

    plt.title("Patient Distribution by Stage")
    plt.xlabel("Stage")
    plt.ylabel("Patient Count")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)

    print(f"Chart saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
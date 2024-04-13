import argparse
import csv
import matplotlib.pyplot as plt

def generate_histogram(input_file, output_file):
    # Load gap information from the CSV file
    gap_lengths = []
    with open(input_file, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            gap_lengths.append(int(row['Gap Length']))

    # Plot histogram
    plt.hist(gap_lengths, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Gap Length')
    plt.ylabel('Number of Gaps')
    plt.title('Distribution of Gap Lengths')
    plt.grid(True)

    # Save histogram plot as PNG file
    plt.savefig(output_file)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate histogram image from CSV file of gap lengths.")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file path")
    parser.add_argument("-o", "--output", required=True, help="Output PNG file path")
    args = parser.parse_args()

    generate_histogram(args.input, args.output)

import argparse
import csv
import os
import pysam

def generate_gap_csv(input_file, output_file):
    # Open the BAM file
    bam_file = pysam.AlignmentFile(input_file, "rb")

    # Get the reference genome length from the BAM header
    reference_length = sum(bam_file.lengths)

    # Initialize a list to store gap information
    gap_info = []

    # Initialize a variable to track the current position in the reference genome
    current_position = 0

    # Iterate over each read in the BAM file
    for read in bam_file:
        # Check if the read starts after the current position
        if read.reference_start > current_position:
            # If there is a gap, record it
            gap_start = current_position
            gap_end = read.reference_start - 1
            gap_length = gap_end - gap_start + 1
            gap_info.append((read.reference_name, gap_start, gap_end, gap_length))  # Include gap length
        # Update the current position
        current_position = read.reference_end + 1

    # If there is a gap at the end of the reference genome, record it
    if current_position < reference_length:
        gap_start = current_position
        gap_end = reference_length - 1
        gap_length = gap_end - gap_start + 1
        gap_info.append((bam_file.references[-1], gap_start, gap_end, gap_length))  # Include gap length

    # Close the BAM file
    bam_file.close()

    # Write gap information to CSV file
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Reference', 'Gap Start', 'Gap End', 'Gap Length'])  # Include header for gap length
        writer.writerows(gap_info)

    print("Gap information exported to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CSV file of gaps from BAM file.")
    parser.add_argument("-i", "--input", required=True, help="Input BAM file path")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file path")
    args = parser.parse_args()

    generate_gap_csv(args.input, args.output)

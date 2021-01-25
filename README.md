# split_bam_by_chromosome
Split aligned reads in Bam file by chromosome/contig/scaffold ids

## Usage:

Let's say you have combined two reference sequences and aligned the raw reads to the combined reference. Now you would like to separated the reads aligning to the first reference only with 10 chromosomes.

First, create a list of 10 chromosomes from the first reference.
```
grep ">" firstref.fasta | sed 's/>//' | awk '{print $1}' > chromosomes.txt
```

The command below will separate reads aligning to the chromosomes in the list, generating a sorted bam file.
```
samtools view -h sample.bam | python split_bam_by_chromosome.py chromosomes.txt | samtools view -b > mappedToFirstSorted.bam
```

# Whole genome sequencing medical diagnostic report

## Introduction

Step 1: Query HPO IDs by sample clinical phenotype ([CHPO](https://www.chinahpo.net/chpo/#/search)), and make
**samplename.hpo.txt**.

Step 2: Run pipline for snv and indel call for genetic disease analysis. (**WGS_variation_call_hg38_v2.py**)

Step 3: Based on the pipline results, manual analysis based on the gene-phenotype relationship is performed to manually
filter out candidate genes and fill in the Excel file used to automatically generate the report. (**template.xlsx**)

Step 4: Run the automatic report generation script and manually add IGV screenshots to the generated report for
validating the results. (**auto_report.py**)

## Installation

### Docker

The Installation of Docker can be seen in https://docs.docker.com/

Run the image in bash:

    docker exec -it WGS_v2 /bin/bash

## Usage

### 1. In Step 2:

    usage: WGS_variation_call_hg38_v2.py [-h] --fastq1 FASTQ1 --fastq2 FASTQ2
                                     --sample_name SAMPLE_NAME
                                     [--threads THREADS] --bed BED
                                     [--hpo_file HPO_FILE] --output_dir
                                     OUTPUT_DIR

    description: pipline for snv and indel call
    eg: python WGS_variation_call_hg38.py --fastq1 /xxx/sample_1.fastq.gz --fastq2 /xxx/sample_2.fastq.gz --output_dir /xxx/out 

    optional arguments:
      -h, --help            show this help message and exit
      --fastq1 FASTQ1       the raw fastq1 file
      --fastq2 FASTQ2       the raw fastq2 file
      --sample_name SAMPLE_NAME
                            the sample name
      --threads THREADS     number of threads
      --bed BED             the genome bed file
      --hpo_file HPO_FILE   the sample hpo list file
      --output_dir OUTPUT_DIR
                            the output file directory

Command:

    python /script/WGS_variation_call_hg38_v2.py --fastq1 /sample/samplename.R1.fastq --fastq2 /sample/samplename.R2.fastq --sample_name samplename --output_dir /test/samplename --threads 8 --bed /data/access.hg38.bed --hpo_file /hpo/samplename.hpo.txt
    sh /test/samplename/script/samplename.SNV.run.sh

### 1. In Step 4:

    usage: auto_report.py [-h] --input_docx_temp INPUT_DOCX_TEMP
                          --input_excel_temp INPUT_EXCEL_TEMP --output OUTPUT
    
    Automation Report.
    
    optional arguments:
      -h, --help            show this help message and exit
      --input_docx_temp INPUT_DOCX_TEMP
                            Input report template file) (*.docx)
      --input_excel_temp INPUT_EXCEL_TEMP
                            Input filled excel template file) (*.xlsx)
      --output OUTPUT       Output filled report file (*.docx)

Command:

    python /script/auto_report.py --input_docx_temp /template/template.docx --input_excel_temp /template/samplename.template.xlsx --output /template/samplename.template.docx

## Input

### 1. samplename.hpo.txt (In Step 2)

For example:

    HP:0000252
    HP:0000054
    HP:0001263
    HP:0001161
    HP:0001178
    ...

### 2. samplename.template.xlsx (In Step 4)

For example:

    index	values
    性别  男
    年龄	早产33w+6
    样本编号	DI000070101
    临床信息	超低体重（1.05kg），尿道下裂，发育迟缓（体力、智力、语言行为异常），散光，母亲孕期：重度子痫前期，高血压，剖宫产。
    样本名称	先证者
    总测序reads数目	676923010
    reads比对率	0.9962
    平均测序深度	32.39
    基因组覆盖度	0.9995
    10x以上覆盖度	0.995
    突变基因	FGFR3
    突变类型	nonsynonymous SNV
    突变位置	chr4:1803744-1803744
    转录本编号	NM_000142
    外显子编号	exon8
    ...

## Output

### 1. samplename.bam.stat.csv (In Step 2)

For example:

    Sample	Total_reads	Mapped_pct	Properly_paired_pct	Mean	Std	Median	Quartile_25	Quartile_75	Coverage	Coverage_10x	Coverage_30x
    samplename	636271378	97.71%	96.27%	34.93	12.28	45	39	52	99.96%	99.71%	94.34%
    ...

### 2. samplename.gene.rank.final.xlsx (In Step 2)

For example:

    Chr	Start	End	Ref	Alt	Func.refGene	Gene.refGene	ExonicFunc.refGene	AAChange.refGene	cytoBand	avsnp150	ACMG_automated	SIFT_pred	Polyphen2_HDIV_pred	MutationTaster_pred	MetaSVM_pred	CADD_phred	gnomAD_ALL	ExAC_ALL	CLNALLELEID	CLNSIG	Otherinfo	GQ	gnomAD_ALL_trans	ExAC_ALL_trans
    chr1	97573943	97573944	CA	-	exonic	DPYD	stopgain	DPYD:NM_000110:exon11:c.1155_1156del:p.C385*	1p21.3	rs769925158	.	.	.	.	.	.	2.443e-05	2.483e-05	.	.	DI000070101=Het,Sdpth=18,Ndepth=25,GQ=99	99	0.00002443	0.00002483
    chr6	32584273	32584273	A	T	exonic	HLA-DRB1	nonsynonymous SNV	HLA-DRB1:NM_002124:exon2:c.T206A:p.F69Y	6p21.32	rs17882455	Uncertain significance	T	D	D	T	23.0	0.0029	0.0077	.	.	DI000070101=Het,Sdpth=5,Ndepth=35,GQ=99	99	0.0029	0.0077
    chr6	32589684	32589684	A	G	exonic	HLA-DRB1	nonsynonymous SNV	HLA-DRB1:NM_002124:exon1:c.T59C:p.M20T	6p21.32	rs35053532	Uncertain significance	D	B	N	T	15.46	0.0003	0.0009	.	.	DI000070101=Het,Sdpth=15,Ndepth=75,GQ=99	99	0.0003	0.0009
    chr6	32589703	32589703	C	G	exonic	HLA-DRB1	nonsynonymous SNV	HLA-DRB1:NM_002124:exon1:c.G40C:p.A14P	6p21.32	.	Uncertain significance	D	P	N	T	17.11	0	.	.	.	DI000070101=Het,Sdpth=14,Ndepth=81,GQ=99	99	0	0
    chr6	32581622	32581622	C	-	exonic	HLA-DRB1	frameshift deletion	HLA-DRB1:NM_002124:exon3:c.587delG:p.S196Mfs*14	6p21.32	rs757139064	.	.	.	.	.	.	0.0016	0.0066	.	.	DI000070101=Het,Sdpth=13,Ndepth=50,GQ=99	99	0.0016	0.0066
    chr6	32581625	32581625	-	T	exonic	HLA-DRB1	frameshift insertion	HLA-DRB1:NM_002124:exon3:c.583_584insA:p.R195Qfs*28	6p21.32	rs375154056	.	.	.	.	.	.	0.0027	0.0012	.	.	DI000070101=Het,Sdpth=14,Ndepth=52,GQ=99	99	0.0027	0.0012
    chr4	1803744	1803744	A	G	exonic	FGFR3	nonsynonymous SNV	FGFR3:NM_000142:exon8:c.A983G:p.N328S,FGFR3:NM_001354809:exon8:c.A983G:p.N328S,FGFR3:NM_001354810:exon8:c.A983G:p.N328S	4p16.3	.	Likely pathogenic	D	D	D	D	21.2	4.066e-06	.	.	.	DI000070101=Het,Sdpth=27,Ndepth=23,GQ=99	99	0.000004066	0
    chr21	46367035	46367035	C	T	exonic	PCNT	nonsynonymous SNV	PCNT:NM_001315529:exon15:c.C2707T:p.R903W,PCNT:NM_006031:exon15:c.C3061T:p.R1021W	21q22.3	rs138361417	Uncertain significance	D	D	N	T	18.91	7.315e-05	6.622e-05	430469	Uncertain_significance	DI000070101=Het,Sdpth=22,Ndepth=10,GQ=99	99	0.00007315	0.00006622
    ...

### 3. samplename.template.docx (In Step 4)
    Note the manual addition of IGV screenshots！
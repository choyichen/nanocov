"""Parse variable list from dbGaP GTEx data dict XML files.
"""
import pandas as pd

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

FILE1 = "../dbGaP/phs000424.v6.pht002742.v6.GTEx_Subject_Phenotypes.data_dict.xml"
FILE2 = "../dbGaP/phs000424.v6.pht002743.v6.GTEx_Sample_Attributes.data_dict.xml"
OUTPUT1 = "../meta/subj_var_list.tsv"
OUTPUT2 = "../meta/samp_var_list.tsv"

def parse_xml(FILE):
    tree = ET.ElementTree(file=FILE)
    root = tree.getroot()
    return pd.DataFrame([[n.find('name').text, n.find('description').text, n.find('type').text] for n in root.findall('variable')], \
                        columns=["name", "description", "type"])

parse_xml(FILE1).to_csv(OUTPUT1, sep="\t", index=False)
parse_xml(FILE2).to_csv(OUTPUT2, sep="\t", index=False)

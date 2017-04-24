from __future__ import print_function
# coding: utf-8
"""
Evaluation scripts for BLEU, ROUGE, CIDEr-D, and METEOR, adapted from the MSCOCO
Caption Evaluation Code (https://github.com/tylin/coco-caption)

The input and output data formats are simplified compared to the reference
implementation.

Reference and Candidate input formats:
    List of dict {image_id: "$image_name", caption: "$caption"}

    where $image_name and $caption are strings

In case of multiple sentences for the same image, each sentence needs to be spec-
ified in the above format (along with the image_id).

Configuration for the evaluation code can be specified in params.json. Generally,
you would want to specify the path to your data, name of the reference file, name
of the candidate file (as per the above format) and the source to use for IDF,
either using the reference corpus or using some precomputed values from MSCOCO
Validation Set.

NOTE: The number of images in the reference and candidate datasets should be the
same. The code will throw an error otherwise.
"""

# demo script for running coco evaluation scripts
import json
import os
from pycocoevalcap.eval import COCOEvalCap as COCOEval

# load the configuration file
config = json.loads(open('params.json', 'r').read())

pathToData = config['pathToData']
refName = config['refName']
candName = config['candName']
resultFile = config['resultFile']
dfMode = config['idf']

# Print the parameters
print("Running metrics with the following settings")
print("*****************************")
print("Reference File:%s" % (refName))
print("Candidate File:%s" % (candName))
print("Result File:%s" % (resultFile))
print("IDF:%s" % (dfMode))
print("*****************************")

# calculate metric scores
scorer = COCOEval(pathToData, refName, candName, dfMode)
# scores: dict of list with key = metric and value = score given to each
# candidate
scorer.evaluate()
scores = scorer.eval
multiple_scores = scorer.multiple_eval
print(multiple_scores)


# write results to output file
with open(os.path.join('results', resultFile), 'w') as outfile:
    json.dump(scores, outfile)

Microsoft COCO Caption Evaluation
===================

Evaluation codes for MS COCO caption generation.

## Important Note ##
CIDEr by default (with idf parameter set to "corpus" mode) computes IDF values using the reference sentences provided. Thus, CIDEr score for a reference dataset with only 1 image will be zero. When evaluating using one (or few) images, set idf to "coco-val-df" instead, which uses IDF from the MSCOCO Vaildation Dataset for reliable results.

#
## Requirements ##
- java 1.8.0
- python 2.7

For running the ipython notebook file, update your Ipython to [Jupyter](https://jupyter.org/)


## Files ##
./
- evalscripts.py (demo script)

./PyDataFormat
- loadData.py (load the json files for references and candidates)

./data
- Reference and Candidate input JSON files in the following format:
    List of dict {image_id: "$image_name", caption: "$caption"}

    where $image_name and $caption are strings

In case of multiple sentences for the same image, each sentence needs to be specified in the above format (along with the image_id).

./results
- results.json (an example of fake results for running demo)
- Visit MS COCO [format](http://mscoco.org/dataset/#format) page for more details.

./pycocoevalcap: The folder where all evaluation codes are stored.
- evals.py: The file includes COCOEavlCap class that can be used to evaluate results on COCO.
- tokenizer: Python wrapper of Stanford CoreNLP PTBTokenizer
- bleu: Bleu evalutation codes
- meteor: Meteor evaluation codes
- rouge: Rouge-L evaluation codes
- cider: CIDEr-D evaluation codes

## Instructions ##
1. Edit the params.json file to contain path to reference and candidate json files, and the result file where the scores are stored<sup>\*</sup>. 

2. Set the "idf" value in params.json to "corpus" if not evaluating on a single image/instance. Set the "idf" value to "coco-val-df" if evaluating on a single image. In this case IDF values from the MSCOCO dataset are used. If using some other corpus, get the document frequencies into a similar format as "coco-val-df", and put them in the data/ folder as a pickle file. Then set mode to the name of the document frequency file (without the '.p' extension).

3. Sample json reference and candidate files are pascal50S.json and pascal_test.json

4. All metric scores are stored in "scores" variable: scores['CIDEr'] -> CIDEr scores and so on

<sup>*</sup>Even when evaluating with independent candidate/references (for eg. when using "coco-val-df"), put multiple candidate and reference entries into the same json files. This is much faster than having separate candidate and reference files and calling the evaluation code separately on each candidate/reference file.
#
## References ##

- [Microsoft COCO Captions: Data Collection and Evaluation Server](http://arxiv.org/abs/1504.00325)
- PTBTokenizer: We use the [Stanford Tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml) which is included in [Stanford CoreNLP 3.4.1](http://nlp.stanford.edu/software/corenlp.shtml).
- BLEU: [BLEU: a Method for Automatic Evaluation of Machine Translation](http://www.aclweb.org/anthology/P02-1040.pdf)
- Meteor: [Project page](http://www.cs.cmu.edu/~alavie/METEOR/) with related publications. We use the latest version (1.5) of the [Code](https://github.com/mjdenkowski/meteor). Changes have been made to the source code to properly aggreate the statistics for the entire corpus.
- Rouge-L: [ROUGE: A Package for Automatic Evaluation of Summaries](http://anthology.aclweb.org/W/W04/W04-1013.pdf)
- CIDEr: [CIDEr: Consensus-based Image Description Evaluation] (http://arxiv.org/pdf/1411.5726.pdf)

## Developers ##
- Xinlei Chen (CMU)
- Hao Fang (University of Washington)
- Tsung-Yi Lin (Cornell)
- Ramakrishna Vedantam (Virgina Tech)

## Acknowledgement ##
- David Chiang (University of Norte Dame)
- Michael Denkowski (CMU)
- Alexander Rush (Harvard University)

---
annotations_creators: []
language: en
license: cc-by-4.0
size_categories:
- 1K<n<10K
task_categories:
- image-classification
- object-detection
task_ids: []
pretty_name: dacl10k
tags:
- WACV2024
- classification
- construction
- defect-detection
- fiftyone
- image
- image-classification
- image-segmentation
- object-detection
dataset_summary: '



  ![image/png](dataset_preview.jpg)



  This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 8922 samples.


  ## Installation


  If you haven''t already, install FiftyOne:


  ```bash

  pip install -U fiftyone

  ```


  ## Usage


  ```python

  import fiftyone as fo

  import fiftyone.utils.huggingface as fouh


  # Load the dataset

  # Note: other available arguments include ''max_samples'', etc

  dataset = fouh.load_from_hub("Voxel51/dacl10k")


  # Launch the App

  session = fo.launch_app(dataset)

  ```

  '
---

# Dataset Card for dacl10k

dacl10k stands for damage classification 10k images and is a multi-label semantic segmentation dataset for 19 classes (13 damages and 6 objects) present on bridges.

The dacl10k dataset includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges.

🏆 This dataset is used in the challenge associated with the "[1st Workshop on Vision-Based Structural Inspections in Civil Engineering](https://dacl.ai/workshop.html)" at [WACV2024](https://wacv2024.thecvf.com/workshops/).




![image/png](dataset_preview.jpg)


This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 8922 samples.

## Installation

If you haven't already, install FiftyOne:

```bash
pip install -U fiftyone
```

## Usage

```python
import fiftyone as fo
import fiftyone.utils.huggingface as fouh

# Load the dataset
# Note: other available arguments include 'max_samples', etc
dataset = fouh.load_from_hub("Voxel51/dacl10k")

# Launch the App
session = fo.launch_app(dataset)
```


## Dataset Details

### Dataset Description


- **Curated by:** Johannes Flotzinger, Philipp J. Rösch, Thomas Braml
- **Funded by:** The project
was funded by the Bavarian Ministry of Economic Affairs
(MoBaP research project, IUK-1911-0004// IUK639/003)
- **Language(s) (NLP):** en
- **License:** cc-by-4.0

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Repository:** https://github.com/phiyodr/dacl10k-toolkit
- **Paper:** https://arxiv.org/abs/2309.00460
- **Demo:** https://try.fiftyone.ai/datasets/dacl10k/samples
- **Homepage:** https://dacl.ai/workshop.html

## Uses

- identifying reinforced concrete defects
- informing restoration works, traffic load limitations or bridge closures


[More Information Needed]

## Dataset Structure

The dacl10k dataset includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges. dacl10k distinguishes 13 bridge defects as well as 6 bridge components that play a key role in the building assessment. Based on the assessment, actions (e.g., restoration works, traffic load limitations, and bridge closures) are determined. The inspection itself and the resulting actions often impede the traffic and thus private persons and the economy. Furthermore, an ideal timing for restoration helps achieving long-term value added and can save a lot of money. It is important to note that dacl10k includes images from bridge inspections but is not restricted to this building type. Classes of the concrete and general defect group in dacl10k can appear on any building made of concrete. Therefore, it is relevant for most of the other civil engineering structures, too.

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->




## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bibtex
@misc{flotzinger2023dacl10k,
      title={dacl10k: Benchmark for Semantic Bridge Damage Segmentation}, 
      author={Johannes Flotzinger and Philipp J. Rösch and Thomas Braml},
      year={2023},
      eprint={2309.00460},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Dataset Card Authors

[Jacob Marks](https://huggingface.co/jamarks)

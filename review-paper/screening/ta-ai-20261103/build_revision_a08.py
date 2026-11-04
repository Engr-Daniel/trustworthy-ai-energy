#!/usr/bin/env python3
"""Write compact/a08.txt: the 4 November re-screen of the 168 title/metadata-only exclusions of 3 November.

Evidence: run ABSTRACT-CAPTURE-20261103-02 (Semantic Scholar title match, arXiv exact title, DOI landing
page), which captured 54 abstracts. Abstract records are re-decided from the abstract (ABSTRACT below).
Records still title-only keep the exclusion only where the title alone clearly fails a criterion; where
the failure is inferred rather than evident they become Unclear and full text is sought (UNCLEAR below).
Earlier rows stay in packet-20261103.csv; this revision supersedes them in confirmed-decisions.csv.
"""
import csv, pathlib

HERE = pathlib.Path(__file__).resolve().parent
RP = HERE.parents[1]
ABSTRACT = {
    "O5271": ("TA01", "Bayesian U-net surrogate for stress-field prediction from material microstructure with epistemic UQ; computational mechanics, not inspection"),
    "O5375": ("TA01", "Generic open-set recognition method (synthetic unknowns); no inspection context"),
    "O5459": ("TA01", "Dataset distillation for histopathology; medical"),
    "O5599": ("TA01", "Optical tactile sensor for robotic manipulation; not inspection"),
    "O5603": ("TA01", "Carotid plaque anomaly detection in ultrasound; medical"),
    "O5633": ("TA01", "Generic cross-domain generalisation heuristic (RSC); no inspection context"),
    "O5648": ("TA01", "Generic probabilistic domain generalisation (MetaVIB); no inspection context"),
    "O5650": ("TA01", "Generic domain generalisation framework; no inspection context"),
    "O5653": ("TA01", "Generic sequential-learning domain generalisation; no inspection context"),
    "O5655": ("TA01", "Generic domain generalisation with domain-specific masks; no inspection context"),
    "O5701": ("TA01", "Generic unsupervised domain adaptation (Deep CORAL) on standard benchmarks; no inspection context"),
    "O5724": ("TA01", "Noisy-label medical image segmentation; medical"),
    "O5733": ("TA01", "Generic open-set adversarial defence; no inspection context"),
    "O5757": ("TA01", "Generic open-set adversarial defence (OSDN-CAML); no inspection context"),
    "O5761": ("TA01", "Gastric intestinal metaplasia segmentation in endoscopy; medical"),
    "O5768": ("TA01", "Pixel-wise anomaly segmentation for urban driving scenes; driving context"),
    "O5813": ("TA01", "Generic adversarially robust autoencoder for novelty detection; no inspection context"),
    "O5849": ("TA01", "Synthetic-to-real urban scene segmentation; driving context"),
    "O5861": ("TA01", "Few-shot scene-adaptive video anomaly detection; surveillance context"),
    "O5862": ("TA01", "Weakly supervised anomalous event detection (UCF-Crime, ShanghaiTech); surveillance context"),
    "O5874": ("TA01", "Generic domain-adversarial training (DANN); no inspection context"),
    "O5877": ("TA01", "Domain-generalised point-cloud understanding on generic benchmarks; no inspection context"),
    "O5919": ("TA01", "Perspective on simulators and synthetic data for deep learning; generic, no inspection study"),
    "O5920": ("TA01", "Generic multi-task weight masking (Piggyback); no inspection context"),
    "O5923": ("TA01", "Generic bilevel regularisation for generalisation; no inspection context"),
    "O5934": ("TA01", "Generic polyhedral conic classifier for open-set recognition; no inspection context"),
    "O5964": ("TA01", "Generic visual explanation method (Grad-CAM); no inspection context"),
    "O5990": ("TA01", "Cross-disciplinary digital-twin review (modelling and twinning technologies); not AI visual inspection"),
    "O6006": ("TA01", "Generic dataset-bias correction for object recognition; no inspection context"),
    "O6013": ("TA01", "Benchmark of segmentation losses on 3D medical tasks; medical"),
    "O6018": ("TA01", "ImageNet challenge benchmark description; generic vision"),
    "O6129": ("TA01", "Explainable ML for breast-cancer histology profiling; medical"),
    "O6136": ("TA01", "Fetal brain segmentation from noisy annotations; medical"),
    "O6137": ("TA01", "Principal-component analysis of adversarial samples on ImageNet; generic vision"),
    "O6169": ("TA01", "Text-guided synthetic augmentation for polyp segmentation; medical"),
    "O6170": ("TA01", "Generic deep-ensemble anomaly detection on benchmark datasets; no inspection context"),
    "O6211": ("TA01", "Review of vision datasets and methods for unmanned surface vehicles; maritime navigation, not inspection"),
    "O6232": ("TA01", "Generic domain-aware triplet loss for domain generalisation; no inspection context"),
    "O6233": ("TA01", "Generic open-set object detector (Grounding DINO); no inspection context"),
    "O6242": ("TA01", "Open-set video anomaly detection with evidential learning; surveillance context"),
    "O6245": ("TA01", "Generic semi-supervised domain adaptation; no inspection context"),
    "O6253": ("TA01", "Generic source-free domain adaptation with label refinery; no inspection context"),
    "O6270": ("TA02", "Heterogeneous-data domain adaptation for process monitoring and equipment matching; process data, non-visual"),
    "O6286": ("TA01", "Generic adversarial attack for segmentation robustness; no inspection context"),
    "O6303": ("TA01", "Explainable interactive medical image classification; medical"),
    "O6358": ("TA01", "Explanation-guided feature construction on tabular data; no inspection context"),
    "O6390": ("TA01", "Theory of optimal transport and Schroedinger bridges; no inspection context"),
    "O6397": ("TA01", "Dichotomous image segmentation of natural images; generic vision"),
    "O6419": ("TA01", "Failure and anomaly detection for segmentation in driving and medical imaging; not industrial inspection"),
    "O6421": ("TA02", "Few-shot anomaly detection in text; non-visual"),
    "O6425": ("TA01", "Review of additive manufacturing for biomedical applications; no AI inspection study"),
    "O6427": ("TA01", "Unsupervised anomaly segmentation in brain MRI; medical"),
    "O6459": ("TA01", "Mini review of anomaly detection in medical imaging; medical"),
    "O6523": ("TA01", "Cross-domain sequential recommendation with multimodal fusion; e-commerce"),
}
UNCLEAR = {
    "O5293": "(title only) Noise-robust industrial anomaly detection; 'temporal features' may be video or sensor data, so modality is unknown. Full text sought",
    "O5398": "(title only) Ship-structure corrosion detection by image processing; the title does not show whether a learned model or a reliability dimension is involved. Full text sought",
    "O6001": "(title only) Hybrid ellipse detection in industrial images; the title does not show whether the hybrid includes a learned model. Full text sought",
    "O6070": "(title only) Image-based characterisation of concrete cracking; the title does not show whether a learned model is used. Full text sought",
}
NOTE = {
    "O5388": "Crossref container title 'Explainable Large Language Models in Healthcare Applications'; healthcare book chapter",
    "O5480": "Crossref container title 'Explainable Large Language Models in Healthcare Applications'; healthcare book chapter",
}

def main():
    ids = (HERE / "title-only-exclusions-20261103.txt").read_text(encoding="utf-8").split()
    old = {}
    for f in sorted((HERE / "compact").glob("a0[1-7].txt")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                p = line.split(";", 3); old[p[0]] = p
    cap = {r["Paper ID"]: r for r in csv.DictReader(open(RP / "screening/abstract-capture-ABSTRACT-CAPTURE-20261103-02/abstracts.csv", encoding="utf-8"))}
    assert set(ABSTRACT) == {p for p in ids if cap[p]["Abstract"]}, "abstract set mismatch"
    out = ["# a08: 4 November 2026 re-screen of the 168 title/metadata-only exclusions of 3 November, by Claude (AI-assisted, single reviewer). "
           "54 abstracts from ABSTRACT-CAPTURE-20261103-02 are decided from the abstract; 114 remain title-only. A title-only exclusion is kept "
           "only where the title (or Crossref container title) clearly fails a criterion; otherwise U and full text is sought. Supersedes the a07 rows."]
    for p in ids:
        if p in ABSTRACT:
            code, why = ABSTRACT[p]; out.append(f"{p};X;{code};{why}")
        elif p in UNCLEAR:
            out.append(f"{p};U;;{UNCLEAR[p]}")
        else:
            _, d, code, why = old[p]
            assert d == "X"
            why = why.replace("(title only) ", "")
            basis = NOTE.get(p, "title clearly outside criterion")
            out.append(f"{p};X;{code};(title only, rechecked 2026-11-04; no abstract in five sources; {basis}) {why}")
    (HERE / "compact/a08.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(len(out) - 1, "lines;", len(ABSTRACT), "abstract;", len(UNCLEAR), "unclear")

if __name__ == "__main__":
    main()

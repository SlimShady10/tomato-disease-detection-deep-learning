# tomato-disease-detection-deep-learning
Master's Thesis project on tomato crop disease detection and classification using deep learning.

# DETECTION AND CLASSIFICATION OF TOMATO CROP DISEASE USING DEEP LEARNING MODELS WITH VARIED OPTIMIZATION TECHNIQUES

This repository contains the code, data (organized for model training), and documentation for my Master's Thesis project focused on the detection and classification of tomato leaf diseases using deep learning models.

## Abstract

Tomato leaf diseases can severely impact crop yield and quality, resulting in substantial economic losses for farmers. Effective management of these diseases relies on early detection and accurate classification, which are crucial for mitigating their adverse effects. This thesis focuses on classifying tomato leaf diseases using advanced deep learning models, including Convolutional Neural Networks (CNN), ResNet-50, InceptionV3, and EfficientNetB0. The study utilizes the Plant Village database to train and evaluate these models, with a particular emphasis on comparing their performance using two different optimizers, Adam and Nadam. EfficientNetB0 stands out among the models, achieving an impressive accuracy of 99%. Its superior performance in this classification task is noteworthy, especially given its low computational requirements. This highlights EfficientNetB0's efficiency not only in terms of accuracy but also in reducing the computational burden, making it a highly effective tool for practical applications in agriculture. The study also explores the role of transfer learning, a technique that uses pre-trained knowledge from large datasets to enhance model performance. By applying transfer learning, the study achieved significant improvements in both accuracy and training efficiency, demonstrating the practicality of this approach for real-world scenarios. Furthermore, the comparative analysis underscores the varying capabilities of the different models, with EfficientNetB0 consistently outperforming the others in terms of both accuracy and computational efficiency. The research findings suggest that deep learning, particularly when combined with transfer learning, offers a robust solution for the early detection and classification of tomato leaf diseases. These insights are not only valuable for improving crop management practices but also for minimizing the economic impact of plant diseases on the agricultural sector. Ultimately, the study provides practical, data-driven solutions that can significantly aid farmers in managing and mitigating the effects of tomato leaf diseases.

## Thesis Document

The full thesis document can be found here: [thesis.pdf](thesis.pdf)

## Repository Structure

* `README.md`: This file, providing an overview of the project.
* `.gitignore`: Specifies intentionally untracked files that Git should ignore.
* `LICENSE`: Contains the license under which the project is distributed (e.g., MIT License). **(Which license do you want to use?)**
* `thesis.pdf`: The complete Master's Thesis document.
* `code/`: Contains the Python scripts for model definitions, training, and evaluation.
    * `models.py`: Defines the architectures of CNN, ResNet-50, InceptionV3, and EfficientNetB0.
    * `train.py`: Scripts to train the models using Adam and Nadam optimizers.
    * `evaluate.py`: Scripts to evaluate the trained models.
    * `utils.py`: Helper functions for data loading, preprocessing, etc.
* `data/`: Contains the organized Plant Village dataset (or the subset used). **(How is your data organized within this folder?)**
    * `train/`: Training data.
    * `val/`: Validation data.
* `notebooks/`: (Optional) Jupyter notebooks for exploratory data analysis or model experimentation.
* `requirements.txt`: Lists the Python libraries required to run the code.
* `results/`: (Optional) Contains saved model weights, evaluation reports, and other output files.
* `images/`: Contains images such as model architecture diagrams, accuracy/loss plots, and confusion matrices.

## Dependencies

The project relies on the following Python libraries:

tensorflow

keras

scikit-learn

matplotlib

numpy

pandas

Pillow (PIL)


You can install these dependencies using pip:

```bash
pip install -r requirements.txt

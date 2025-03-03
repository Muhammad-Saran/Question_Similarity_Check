# Question Similarity Check

This repository contains an implementation of a Question Similarity Checking system using PyTorch. The model is trained on predefined question pairs and their similarity scores, allowing it to determine how similar two questions are. A graphical user interface (GUI) has been added to enhance user interaction.

## Installation

### Create a Virtual Environment
You can use either `venv` or `conda` to create an isolated environment for this project.

#### Using `venv`
```sh
mkdir similarity_project
cd similarity_project
python3 -m venv venv
```

#### Activate the Virtual Environment

- **Mac / Linux:**
  ```sh
  source venv/bin/activate
  ```
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```

### Install Dependencies
Install PyTorch and required libraries:
```sh
pip install torch torchvision torchaudio
pip install nltk
pip install tkinter
```

If you encounter issues related to NLTK, install `punkt`:
```sh
python -c "import nltk; nltk.download('punkt')"
```

## Usage

### Train the Model
To train the question similarity model, run:
```sh
python train.py
```
This will generate a `data.pth` file, which contains the trained model weights.

### Run the Question Similarity GUI
After training, launch the similarity checking system’s graphical interface:
```sh
python app.py
```

## Customization
You can modify `questions.json` to customize the dataset. This file defines the possible question pairs and their similarity scores.

Example:
```json
{
  "questions": [
    {
      "question1": "How to learn Python?",
      "question2": "What is the best way to learn Python?",
      "similarity": 0.9
    }
  ]
}
```

After modifying `questions.json`, re-run `train.py` to update the model.

## About

This system uses a feedforward neural network with two hidden layers to evaluate the similarity between questions. It is designed for easy customization and can be extended for different use cases. The addition of a GUI provides a more interactive and user-friendly experience.

Feel free to contribute and enhance the project!



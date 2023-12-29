# Fundamental AI Concepts

## How Machine Learning Works

Simply put, machine learning models try to figure out the relationship between data.

As an example, let's say you want to train an AI to look at a car and tell you what make/model it is.

1. You collect images of various cars.
2. You label the images with the correct make/model.
3. The data is processed using an algorithm that finds relationships between the features of cars in the pictures and what is labeled.
4. The results of this processing are encapsulated in a mathematical model.

In Azure, we have the Azure Machine Learning service, which lets us create and manage ML models. Azure Machine Learning Studio has various features to support model creation such as:
- Automated machine learning
    - Easier for non-experts to quickly create a model from data
- Azure Machine Learning Designer
    - GUI enabling no-code development of ML solutions
- Data metric visualization
    - Analyze experiments with visuals
- Notebooks
    - Write and run your own code in managed Jupyter Notebook servers


## Areas of AI

### Computer Vision

Computer vision is the area of AI that deals with processing visual information.

Computer vision encompasses several capabilities:
- Image classification
    - Training a model to classify an image based on contents.
    - Example: Classify pictures of cars based on car color.
- Object detection
    - Locating and classifying an object within an image.
    - Example: In an image of a traffic stop, identify buses and cyclists.
- Semantic segmentation
    - Similar to object detection, this works by classifying individual pixels according to the object to which they belong.
- Image analysis
    - Generating information about the provided image.
    - Example: If you give the model a picture of a crosswalk, it may return "A busy crosswalk in a city."
- Face detection/analysis/recognition
    - Locate and identify faces within an image.
    - Often combines classification and facial geometry analysis.
- Optical character recognition (OCR)
    - Detecting and reading text from images.

Microsoft provides Azure Vision Studio and Azure AI Vision, a development platform for computer vision solutions. Azure AI Vision has many features including:
- Image analysis
- Face detection and recognition
- OCR

### Natural Language Processing (NLP)

NLP is the area of AI for understanding written and spoken language. This includes:
- Analyzing and interpreting text in documents
- Interpreting spoken language and synthesizing responses
- Automatically translating spoken or written phrases
- Interpret commands and determine appropriate actions

Microsoft's Azure AI Language platform allows you to build NLP solutions.
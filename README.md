   ![842441e38f7a8a0896a9d8a0a940f76d_w200](https://github.com/Rohii1515/PYRJrenderer/assets/101645749/04daafe6-9389-46de-ae9e-aabb64ce014e)
# 📦PYRJrenderer python package
PYRJrenderer is a versatile Python package designed for real-world business use cases, offering a seamless solution for rendering Websites, Docs, and Videos within Jupyter Notebooks. It simplifies your workflow by providing an end-to-end solution for easy reference and integration.

## Problem Statement

In today's business landscape, professionals often need to analyze, reference, and present information from various sources, including websites, documents, and videos. Manually extracting and incorporating content into Jupyter Notebooks can be time-consuming and error-prone. This package addresses this challenge by automating the rendering process.

## Proposed Solution

PYRJrenderer offers a comprehensive solution to the problem by:

- **Website Rendering**: It can capture and render web pages directly within Jupyter Notebooks, allowing you to interactively analyze online content without leaving your environment.

- **Document Rendering**: With support for document rendering, you can easily incorporate and visualize content from various document formats, making it ideal for data analysis and reporting.

- **Video Rendering**: PYRJrenderer can embed videos within Jupyter Notebooks, facilitating presentations and analysis that involve multimedia content.

- **Documentation**: The package includes detailed documentation, created using the `mkdocs-material` library, ensuring that users can quickly understand and utilize its features.

- **Cross-Platform Compatibility**: PYRJrenderer is designed to be OS-independent, enabling users on different operating systems to benefit from its functionality.

- **Python Compatibility**: It has undergone extensive testing for compatibility with multiple versions of Python, making it accessible to a wide range of users.

## Tech Stack

PYRJrenderer is built using the following technologies:

- Python: The core programming language for developing the package.
- Jupyter Notebooks: The platform for interactive data analysis and documentation.
- `mkdocs-material`: The library used for creating user-friendly documentation.
- Various Python libraries and modules for web scraping, document processing, and multimedia handling.

## Installation

You can install PYRJrenderer using pip:

```bash
pip install PYRJrenderer
```
## Quickstart

Watch the quickstart video for a step-by-step guide to getting started with PYRJrenderer:

[![Quickstart Video](https://img.youtube.com/vi/JuhkuXp1H18/0.jpg)](https://youtu.be/JuhkuXp1H18)

## Usage
For detailed usage instructions and examples, please refer to the [documentation](https://rohii1515.github.io/PYRJrenderer/)

## API Reference

### Rendering Youtube videos

You can use the `render_YouTube_video` function to embed YouTube videos in your Jupyter Notebook.
**Example:**
   
``` python
    from PYRJrenderer import render_YouTube_video
    URL = "https://www.youtube.com/watch?v=JuhkuXp1H18"
    render_YouTube_video(URL=URL, width = 780, height = 480)
```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| URL    | str |input URL of a youtube video as a string |
| height | int |height of the video to display in jupyter notebook, defaults to 720 |
| width  | int |width of the video to display in jupyter notebook, defaults to 600 | 

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  str   | "success" or InvalidURLException       |


## Rendering reference website

You can use the `render_site` function to embed web sites in your Jupyter Notebook for reference.
**Example:**
```python
    from PYRJrenderer import render_site
    URL = "https://pytorch.org/"
    render_site(URL = URL, width = "90%", height = "500")
```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| URL    | str |input URL of a youtube video as a string |
| height | str |height of the website to display in jupyter notebook, defaults to "600" |
| width  | str |width of the website to display in jupyter notebook, defaults to "100%" | 

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  str   | "success" or InvalidURLException       |

***

project board - https://github.com/users/Rohii1515/projects/2/views/1

### Contributing
If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive messages.
- Push your branch to your fork.
- Create a pull request to merge your changes into the main branch of this repository.
### License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

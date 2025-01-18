# Knowledge Distillation for C/C++ Vulnerability Detection (CDD) on Gemini 2.0 Flash Thinking

This project focuses on **knowledge distillation** techniques applied to the task of **C/C++ vulnerability detection (CDD)**, leveraging the experimental **Gemini 2.0 Flash Thinking** model. The goal is to capture and utilize the reasoning capabilities of this powerful model to enhance the performance of vulnerability detection systems.

## Project Overview

The core idea is to train a smaller, more efficient model (student) to mimic the behavior of the larger, more complex Gemini 2.0 Flash Thinking model (teacher) on the specific task of CDD. This is achieved by:

1. **Generating Reasoning Data:** Using the Gemini 2.0 Flash Thinking model, we generate responses to a dataset of C/C++ code snippets. These responses include both:
    *   **Step-by-step reasoning (thinking):** The model's internal thought process while analyzing the code for vulnerabilities.
    *   **Final vulnerability assessment (response):** The model's conclusion on whether the code has a vulnerability or not.

2. **Storing Results:** The generated data is carefully organized and stored in a JSON format, including:
    *   `idx`: A unique identifier for each code snippet.
    *   `thinking`: The model's reasoning process.
    *   `response`: The model's final answer.
    *   `label`: A regular expression-matched label indicating the presence or absence of a vulnerability ("the code has a vulnerability" or "the code does not have a vulnerability").

3. **Distillation (Future Work):** This generated data will serve as the training set for a student model. The student model will be trained to not only predict the correct vulnerability label but also to replicate the teacher model's reasoning process.

## Dataset

The project uses a dataset of C/C++ code snippets, loaded from the `test-00000-of-00001.parquet` file using the `datasets` library. Each entry in the dataset contains a `func` field representing the C/C++ function to be analyzed.

## Code Structure

The main script (`cdd_gemini_2_flash.py`) performs the following actions:

1. **Initialization:**
    *   Configures the Google Generative AI API key (ensure you have the `GEMINI_API_KEY` environment variable set).
    *   Loads the dataset.
    *   Opens an output file (`answer.json`) to store the results.

2. **Iteration:**
    *   Iterates through each code snippet in the dataset.
    *   Constructs a prompt for the Gemini 2.0 Flash Thinking model, instructing it to analyze the code and provide its reasoning and conclusion.
    *   Sends the prompt to the model and retrieves the response.

3. **Data Extraction and Storage:**
    *   Extracts the model's thinking process and final response.
    *   Uses regular expressions to identify the final vulnerability label ("the code has a vulnerability" or "the code does not have a vulnerability").
    *   Stores the extracted information (`idx`, `thinking`, `response`, `label`) in a JSON object and writes it to the `answer.json` file.

4. **Error Handling:**
    *   Includes error handling to gracefully manage potential exceptions during API calls or data processing.

## Requirements

*   Python 3.x
*   `google-generativeai` library
*   `datasets` library
*   `regex` library

Install the required packages using pip:

```bash
pip install google-generativeai datasets regex
Use code with caution.
Usage
Set up API Key:

Obtain a Gemini API key from Google AI Studio.

Set the GEMINI_API_KEY environment variable to your API key:

export GEMINI_API_KEY="your_api_key_here"
Use code with caution.
Bash
Or for Windows cmd:

setx GEMINI_API_KEY "your_api_key_here"
Use code with caution.
Bash
Run the Script:

Execute the cdd_gemini_2_flash.py script:

python cdd_gemini_2_flash.py
Use code with caution.
Bash
Output:

The script will generate an answer.json file containing the results in the specified JSON format.

Future Work
Student Model Training: Implement and train a student model using the generated data.

Distillation Techniques: Explore different knowledge distillation techniques (e.g., response-based, feature-based, relation-based) to optimize the transfer of knowledge from the teacher to the student model.

Evaluation: Evaluate the performance of the distilled student model on a held-out test set and compare it to the teacher model and other baselines.

Notes
The Gemini 2.0 Flash Thinking model is experimental, and its behavior might change in the future.

The code assumes a specific format for the model's response. Adjust the parsing logic if needed based on any updates to the model's output.

The effectiveness of knowledge distillation depends heavily on the quality and size of the generated dataset, as well as the architecture and training of the student model.

This project provides a starting point for exploring the potential of knowledge distillation with large language models for code vulnerability detection. By capturing the reasoning abilities of advanced models like Gemini 2.0 Flash Thinking, we aim to develop more efficient and accurate tools for securing software systems.

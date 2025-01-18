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

## Dataset Selection

This project focuses on exploring knowledge distillation across multiple datasets to ensure robustness and generalizability. The following datasets are considered:

*   **Devign:** A dataset of C functions extracted from two open-source projects, FFmpeg and Qemu. It contains various types of vulnerabilities, labeled by experienced security researchers.
*   **PrimVul:** This dataset is particularly useful as it contains real-world examples of code vulnerabilities, gathered and verified by an experienced penetration testing team. The diversity and practical relevance of vulnerabilities within PrimVul makes it valuable for developing robust and accurate vulnerability detection models.
*   **DiverseVul:** This dataset is designed to include a broad spectrum of vulnerability types and programming patterns, making it an excellent choice for training comprehensive models. DiverseVul stands out for its variety, covering numerous CWEs (Common Weakness Enumerations) and code complexities, ensuring the model's ability to generalize across different types of C/C++ vulnerabilities.
*   **Other Datasets:** The project remains open to incorporating other relevant CDD datasets to further expand the scope and diversity of the training data.

The specific dataset used for each run can be specified through configuration (details in the "Usage" section). Currently, the code is set up to load a dataset from the `test-00000-of-00001.parquet` file, representing a placeholder for any of the mentioned datasets.

## Code Structure

The main script (`cdd_gemini_2_flash.py`) performs the following actions:

1. **Initialization:**
    *   Configures the Google Generative AI API key (ensure you have the `GEMINI_API_KEY` environment variable set).
    *   Loads the dataset (Devign, PrimVul, DiverseVul, or others based on configuration).
    *   Opens an output file (`answer.json`) to store the results.

2. **Iteration:**
    *   Iterates through each code snippet in the selected dataset.
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
*   `google-genai` library
*   `datasets` library
*   `json` library

Install the required packages using pip:

```bash
pip install google-genai datasets json
```

## Usage

1. **Set up API Key:**
    *   Obtain a Gemini API key from Google AI Studio.
    *   Set the `GEMINI_API_KEY` environment variable to your API key:

    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```
    Or for Windows cmd:
    ```bash
    setx GEMINI_API_KEY "your_api_key_here"
    ```

2. **Dataset Configuration:**
    *   Modify the `cdd_gemini_2_flash.py` script to load the desired dataset. This might involve changing the file path in the `load_dataset` function or adding logic to select the dataset based on a command-line argument or configuration file.
    *   Ensure the dataset is in a compatible format (e.g., `.parquet` or a format supported by the `datasets` library).

3. **Run the Script:**
    *   Execute the `cdd_gemini_2_flash.py` script:

    ```bash
    python cdd_gemini_2_flash.py
    ```

4. **Output:**
    *   The script will generate an `answer.json` file containing the results in the specified JSON format.

## Future Work

*   **Student Model Training:** Implement and train a student model using the generated data from various datasets.
*   **Distillation Techniques:** Explore different knowledge distillation techniques (e.g., response-based, feature-based, relation-based) to optimize the transfer of knowledge from the teacher to the student model.
*   **Evaluation:** Evaluate the performance of the distilled student model on a held-out test set from each dataset and compare it to the teacher model and other baselines.
*   **Cross-Dataset Evaluation:** Assess the generalization capabilities of the student model by training on one dataset and evaluating on another.

## Notes

*   The Gemini 2.0 Flash Thinking model is experimental, and its behavior might change in the future.
*   The code assumes a specific format for the model's response. Adjust the parsing logic if needed based on any updates to the model's output.
*   The effectiveness of knowledge distillation depends heavily on the quality and size of the generated dataset, as well as the architecture and training of the student model.

This project provides a starting point for exploring the potential of knowledge distillation with large language models for code vulnerability detection across different datasets. By capturing the reasoning abilities of advanced models like Gemini 2.0 Flash Thinking and applying them to diverse vulnerability datasets, we aim to develop more efficient, accurate, and generalizable tools for securing software systems.

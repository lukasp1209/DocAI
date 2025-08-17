# Streamlit DocAI Application

This project is a Streamlit application that provides functionalities for analyzing medical findings, images, and videos. It aims to simplify medical terminology and assist in the interpretation of medical images and videos.

## Project Structure

```
streamlit-docai
├── src
│   ├── __init__.py
│   ├── image_analysis.py
│   ├── text_processing.py
│   └── video_analysis.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-docai
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Features

- **Text Translation**: Input medical findings and receive a simplified translation.
- **Image Analysis**: Upload MRI/CT images for analysis and receive feedback on findings.
- **Video Analysis**: Upload video files for analysis with diagnostic feedback.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
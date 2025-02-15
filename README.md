# sql-query-generator
# SQL Query Generator Bot 🤖

A Streamlit-based web application that converts natural language to SQL queries using Google's Gemini-Pro AI model. This tool helps users generate SQL queries without needing to know SQL syntax.

## 🌟 Features

- Natural language to SQL query conversion
- Clean and intuitive user interface
- Real-time query generation
- Copy to clipboard functionality
- Error handling and user feedback
- Responsive design
- Professional dark blue theme

## 📋 Prerequisites

Before running this application, make sure you have Python installed on your system. The application requires the following dependencies:

```bash
Python 3.7+
Streamlit
Google GenerativeAI Python SDK
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd sql-query-generator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install streamlit
pip install google-generativeai
```

4. Set up your Google API key:
   - Get your API key from the Google AI Studio
   - Replace the API key in the code or set it as an environment variable

## 🎯 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the local URL provided by Streamlit (typically http://localhost:8501)

3. Enter your query in natural language in the text area

4. Click the "Generate SQL Query" button to get your SQL query

## 💡 Example Queries

Try these example queries:
- "Show all customers who made purchases in the last month"
- "Find the total sales for each product category"
- "List all employees who have been with the company for more than 5 years"

## ⚙️ Configuration

The application can be configured by modifying the following parameters:
- Page title and icon in `st.set_page_config()`
- Custom CSS styles in the style section
- System prompt for the AI model
- UI layout and components

## 🔒 Security

- Keep your Google API key secure and never commit it directly to version control
- Consider using environment variables for sensitive information
- The application should be deployed behind appropriate security measures

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini-Pro AI for natural language processing
- Streamlit for the web framework
- The open-source community for inspiration and resources

## ⚠️ Troubleshooting

Common issues and solutions:

1. API Key Issues:
   - Ensure your API key is valid
   - Check if you have proper access permissions
   - Verify the API key is correctly set in the code

2. Installation Problems:
   - Make sure all dependencies are correctly installed
   - Check Python version compatibility
   - Verify virtual environment activation

3. Runtime Errors:
   - Check console logs for error messages
   - Verify internet connection for API calls
   - Ensure proper formatting of input queries

## 📞 Support

For support, please:
1. Check the existing documentation
2. Look through the troubleshooting section
3. Create an issue in the repository
4. Contact the development team

---
Made with ❤️ by GCT

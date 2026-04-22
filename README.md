# Anime Recommendation System

This project implements an anime recommendation system using a vector store and a language model. The system allows users to input their anime preferences and receive personalized recommendations based on those preferences.

## Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:morizin/anime-recommender.git
   ```
2. Navigate to the project directory:
   ```bash
   cd anime-recommender
   ```
3. Install uv if you haven't already:
   ```bash
   pip install uv
   ```
4. Install the required dependencies using uv:
   ```bash
    uv sync
    ```
5. Create a vector store for the anime data:
   ```bash
   uv run -m src.pipeline.create_vector_store
   ```
6. Start the Streamlit application:
   ```bash
   uv run streamlit run app.py
   ```

## Usage
Once the Streamlit application is running, you can input your anime preferences in the provided interface. The system will process your input and generate personalized anime recommendations based on the vector store and the language model.

## Contributing
Contributions to this project are welcome! If you have any suggestions or improvements, please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
# Movie Recommendation System

A content-based movie recommendation system built with Python that provides personalized movie suggestions using cosine similarity and machine learning techniques. The system features an interactive Streamlit web application integrated with The Movie Database (TMDB) API for dynamic content delivery.

## 🎯 Project Overview

This recommendation system analyzes **4,800+ movies** and generates personalized top 5 movie suggestions based on cosine similarity of **5,000+ unique features** extracted from movie metadata. The system employs content-based filtering techniques to recommend movies similar to user preferences.

### Key Features

- **Content-Based Filtering**: Recommends movies based on similarity in genres, cast, keywords, and plot
- **Interactive Web Interface**: Built with Streamlit for seamless user experience
- **Dynamic Content Loading**: Real-time movie posters and metadata fetching via TMDB API
- **Tag-Based Matching**: Enhanced content matching system using movie tags
- **Scalable Architecture**: Efficient processing of large movie datasets

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NLTK**: Natural language processing for text features
- **Scikit-learn**: Machine learning algorithms and cosine similarity
- **Streamlit**: Web application framework
- **TMDB API**: Movie metadata and poster retrieval

## 📊 Dataset

The system processes a comprehensive movie dataset containing:
- 4,800+ movies
- Multiple features including genres, cast, crew, keywords, and overview
- 5,000+ unique features extracted for similarity computation

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- TMDB API key (free from [TMDB](https://www.themoviedb.org/settings/api))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/NihalMishra17/Movie_recommendation.git
cd Movie_recommendation
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Download NLTK data**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

4. **Set up TMDB API key**
   - Sign up at [TMDB](https://www.themoviedb.org/)
   - Get your API key from account settings
   - Add your API key to the application configuration

## 🚀 Usage

### Running the Application

1. **Start the Streamlit app**
```bash
streamlit run app.py
```

2. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The application will load automatically

### Using the Recommendation System

1. Select or search for a movie from the dropdown menu
2. Click the "Recommend" button
3. View the top 5 recommended movies with posters and details
4. Click on any movie poster to explore more information

## 📁 Project Structure

```
Movie_recommendation/
│
├── app.py                  # Main Streamlit application
├── model.py               # Recommendation algorithm implementation
├── preprocessing.py       # Data preprocessing and feature extraction
├── requirements.txt       # Project dependencies
├── data/
│   └── movies.csv        # Movie dataset
├── models/
│   ├── similarity.pkl    # Precomputed similarity matrix
│   └── movies_dict.pkl   # Processed movie dictionary
└── README.md
```

## 🧮 Algorithm

### Content-Based Filtering Process

1. **Feature Extraction**
   - Extract and combine relevant features (genres, cast, keywords, overview)
   - Apply text preprocessing (lowercasing, stemming, stop word removal)
   - Create feature vectors using TF-IDF or Count Vectorization

2. **Similarity Computation**
   - Calculate cosine similarity between movie feature vectors
   - Generate similarity matrix for all movie pairs
   - Formula: `similarity = (A · B) / (||A|| × ||B||)`

3. **Recommendation Generation**
   - For a given movie, find top N most similar movies
   - Rank by similarity score (0 to 1)
   - Return top 5 recommendations with metadata

### Key Metrics

- **Cosine Similarity Range**: 0 (completely dissimilar) to 1 (identical)
- **Feature Vector Dimensions**: 5,000+ unique features
- **Processing Time**: < 1 second for recommendation generation


## 🎓 Learning Outcomes

This project demonstrates:
- Content-based recommendation system implementation
- Natural language processing for feature extraction
- Cosine similarity for measuring movie similarity
- Web application development with Streamlit
- API integration for dynamic content delivery
- Efficient handling of large datasets

## 🔮 Future Enhancements

- [ ] Add collaborative filtering for hybrid recommendations
- [ ] Implement user rating system
- [ ] Add movie search with autocomplete
- [ ] Include TV shows and series
- [ ] Deploy to cloud platform (Heroku/Streamlit Cloud)
- [ ] Add user authentication and personalized watchlists
- [ ] Implement A/B testing for recommendation algorithms
- [ ] Add multilingual support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---

⭐ **Star this repository if you find it helpful!**

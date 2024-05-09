# Movies-And-Shows-RecommendationSystem
This project is a recommendation system for movies and TV shows, designed to suggest content based on user preferences.

## Features  
* Recommends movies and TV shows based on user ratings and viewing history.  
* Allows users to discover new content similar to their favorites.  
* Supports personalized recommendations for each user.  

## Requirements  
* Python 3.6+  
* Pandas  
* Scikit-learn  
* NLTK  
* Pickle  
* NumPy  

## Installation  
Clone the repository:  
```git clone https://github.com/mithz-z/Movies-And-Shows-RecommendationSystem.git```

## Install the required packages:  
```pip install -r requirements.txt```

## Run the application (must run inside an IDE):  
```streamlit run streamlit.py```  

## How it works:  
* The system analyzes the features of movies and TV shows to build a profile for each item.  
* User preferences are compared to item profiles to recommend content that matches their tastes.  
* Recommendations are updated regularly based on user interactions and new content.

## License  
This project is licensed under the MIT License - see the LICENSE file for details.

## Note:  
Unable to provide similarity.pkl as it is more than 600mb  
To create the similarity dataset run the ipynb file

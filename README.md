# Scrapy-and-recommned-news

In this project, I drew inspiration from the questions people pose or the messages shared on various social media platforms. The objective was to develop a system capable of classifying these inquiries and posts into specific categories. The primary focus was on collecting data through web scraping, employing Scrapy to extract relevant information from news articles on the web, specifically from https://www.lemonde.fr/en/.

The process began with the extraction of pertinent data, followed by a meticulous cleaning phase to prepare the data for training. Subsequently, a model was crafted to classify news articles into distinct categories. The evaluation results demonstrated an accuracy of approximately 80%, a level deemed sufficient for effective use and recommendations.

This project underscores the power of utilizing web scraping techniques, such as Scrapy, to autonomously collect data from online sources. The ability to categorize news content based on machine learning models further enhances the project's utility, enabling it to effectively process and recommend relevant information to users.

By combining web scraping technology with categorization models, this project not only showcases technical proficiency but also highlights the practical applications of automated data collection and classification in the realm of news analysis and recommendation systems.



![example](topnews1.png)


![example2](topnews2.png)

### **How to Use**
1. Open the command prompt (cmd) and navigate to the folder where you want to store the project. For example, use the following command: cd 'path/to/your/directory'
2. Clone the project repository by entering the command: git clone https://github.com/alexday11/Scrapy-and-recommned-news.git
3. Move into the project directory: cd 'Scrapy-and-recommned-news'
4. Install the required dependencies by running: pip install -r requirements.txt
5. Start the app with the following command: streamlit run app.py

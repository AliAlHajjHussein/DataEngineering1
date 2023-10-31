first the web_scraping.py file is the one that scraps data from the sitemap of "ALjazeera" and save them as a json file. where the data it scraps are those articles and news related to "Gaza war"
the output.json is the output of the first file.
the post.py is the file for recognising the data in the output.json file with the properties (title , date , author , source) and put them in the output2.json.
the post_class.py is the class oop for the post.py file.
the web_scraping_with_mongodb.py is the file that takes the data in the output2.json file and put them in the mongodb collection.
the API.py is the file that creates an api that takes the data from mongo db and put them on web.



from tutorial.assets import get_stories_from_feed
from tutorial.mongo import store_data, get_all_data
from tutorial.cleaning import clean_data, store_dataframe
from tutorial.statistics import dataframe_for_word_count


stories = get_stories_from_feed()
# print(stories)
store_data("bronze", "feed", stories)
df = clean_data("bronze", "feed", ["id"])
print(df.head(5))
store_dataframe("silver", "feed", df)
print(list(get_all_data("silver", "feed")))
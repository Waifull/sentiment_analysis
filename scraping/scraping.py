import pandas as pd
from google_play_scraper import Sort, reviews

def scrape_reviews(app_id, lang='id', country='id', max_reviews=10000):
    all_reviews = []
    num_reviews = 0
    

    while num_reviews < max_reviews:
       
        reviews_batch, _ = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.MOST_RELEVANT,
            count=100,
        )
        
       
        all_reviews.extend(reviews_batch)
        num_reviews += len(reviews_batch)
        
        
        if len(reviews_batch) < 100:
            break
    
   
    df = pd.DataFrame(all_reviews)
    
   
    df = df[['content', 'score']]
    
  
    df = df[df['score'] != 3]
    
 
    df['sentiment'] = df['score'].apply(lambda x: 'positif' if x > 3 else 'negatif')
    
    return df


app_id = 'com.whatsapp'  
df_reviews = scrape_reviews(app_id)


df_reviews.to_csv('data/dataset.csv', index=False)
print("Data telah disimpan ke data/dataset.csv")
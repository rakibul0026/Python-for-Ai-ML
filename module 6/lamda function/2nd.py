import pandas as pd
df=pd.DataFrame({'price':[1,2,3,4]})
df['category']=df['price'].apply(lambda x: 'cheap' if x<3 else 'expensive')
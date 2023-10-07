# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df['sex'].value_counts()

# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.

df.nunique()

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df['pclass'].unique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df['pclass'].nunique()
df['parch'].nunique()


# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df['embarked'].dtype
df['embarked'] = df['embarked'].astype('category')
df['embarked'].dtype

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df['embarked'] == 'C'].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df['embarked'] != 'S'].head()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df['age'] > 30) & (df['sex'] == 'male')].head()


# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df[(df['fare'] > 500 ) | (df['age'] > 70 )].head()

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

# Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop(columns="who", inplace=True)
df.head()

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

type(df['deck'].mode())
df['deck'].fillna(df['deck'].mode()[0], inplace=True)
df['deck'].isnull().sum()

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
median_age = int(df['age'].median())
df['age'].fillna(median_age, inplace=True)
df['age'].isnull().sum()

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})



# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)


def age_category(age):
    if age < 30:
        return 1
    else:
        return 0

df['age_flag'] = df['age'].apply(lambda x: age_category(x))

print(df[['age', 'age_flag']])



# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset('Tips')
df.head()

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby(['time']).agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(['day', 'time']).agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

df[(df['time'] == "Lunch") & (df['sex'] == 'Female')].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"]})



# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()


# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df['total_bill_tip_sum'] = df['total_bill'] + df['tip']
df.head()
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

first30 = df.sort_values(by='total_bill_tip_sum', ascending=False)[:30]
first30.shape

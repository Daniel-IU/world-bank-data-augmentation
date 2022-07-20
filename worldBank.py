import pandas as pd

#-------------------------------first data sourcing--------------------------------

wldBnkData=pd.read_html('https://wits.worldbank.org/countryprofile/metadata/en/country/all#apl_E')

df=pd.DataFrame(wldBnkData[1])

df.drop([0,1],inplace=True)

df.reset_index(drop=True,inplace=True)

df.rename({'Country Name':'Country_Name'}, axis=1,inplace=True)

df['check']=df.Country_Name.apply(lambda x:len(x)>1)

df=df[df.check]

df.drop('check',axis=1,inplace=True)

df2=df[['Country_Name','Country ISO3','Income Group','Region']]

df2.loc[55,'Country ISO3']= 'COD' # changed the ISO3 code for drc
df2.loc[212,'Country ISO3']= 'ROU' # changed the ISO3 code for romania
df2.loc[245,'Country ISO3']= 'SDN' # changed the ISO3 code for Sudan
df2.loc[73,'Country ISO3']= 'TLS' # changed the ISO3 code for east timor

#---------------------Second data sourcing for continent mapping------------------------------------------

continentData=pd.read_html('https://statisticstimes.com/geography/countries-by-continents.php')

continentData1 = continentData[2]

continentData2 = continentData1[['ISO-alpha3 Code','Continent']]

continentData2.drop(195,inplace=True) # dropped one NA value that had continent as europe, should have used dropna()

continentData2.rename({'ISO-alpha3-Code':'ISO_alpha3_Code'},axis=1,inplace=True)

df3=df2.join(continentData2.set_index('ISO_alpha3_Code'), on='Country ISO3')

df3[df3.Continent.isna()].shape

df3.head(5)

df3.dropna(subset=['Continent'],inplace=True)

df3.to_csv('C:\\Users\\Igbinedion Uyiosa\\Documents\\countryCode.csv',index=False)

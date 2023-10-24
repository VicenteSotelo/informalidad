
# ====================================
# Project : Desarrollo Productivo 
# Creators: VS
# Date     :06.10.23
# Goal     :new leader indicators: indicadores del futuro
# source: https://www.ilo.org/shinyapps/bulkexplorer13/?lang=en&id=SDG_0831_SEX_ECO_RT_A	
 # ====================================

# r1= https://colorhunt.co/palette/f7f1e5e7b10a8981214c4b16
# r2='source:https://github.com/VicenteSotelo/desarrollo_productivo'

# A) Informalidad

# setting path

# path="/Users/luisvicentesotelofarfan/My\Drive(vicente@thewhyhub.com)/second_brain🧠/python🐍/projects/ilo"

#I. setting dev

#setting tools
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#setting dir
# cwd=os.getcwd()
# print (cwd)

#II. import data

df_ilo= pd.read_csv('SDG_0831_SEX_ECO_RT_A-filtered-2023-06-11.csv', sep=',')

#rename column name
df_ilo=df_ilo.rename(columns={'ref_area.label':'País'})


#explore data
# print(df_ilo.types)

print(df_ilo['País'].value_counts())

# #setting condions
cond=df_ilo['País'].isin(['Argentina','Colombia','Peru','Chile','Mexico','Uruguay','Brasil'])

# #pull data
df_1=df_ilo[cond]
# print(df_1.head(20))


# drawing

#L1: Marco o lienzo setting bacgkround 

sns.set_style('white') #background
sns.set_context('talk') #


#L2 paleta de colores de los trazos
sns.set_palette('Greys') 

    # paltette_twh=['#B4E4FF',''.''] # update ⏭️
    # pal= {'Argentina':'#B4E4FF','Colombia':'#F5EFE7','Peru':'#dd1c1a','Chile':'#DDFFBB','Mexico':'#C4DFDF','Uruguay':'#FFF8DE'}

g=sns.relplot(data=df_1,x='time',y='obs_value',hue='País',kind='line',legend=False)

plt.gca().lines[4].set_color('blue')
plt.gca().lines[5].set_color('gray')

#L3 titles and axez labels

#title
plt.title('Porcentaje del Empleo Informal en el Empleo Total')

#y-axis
y_label=plt.ylabel('%')
y_label.set_rotation(180)
plt.ylim(0, None)

#x-axis
plt.gca().set_xlabel('')


#text
plt.gca().annotate('Perú',(2022,69),color='blue', fontsize=18)
plt.gca().annotate('Uruguay',(2021,37),color='gray', fontsize=12)
plt.gca().annotate('Chile',(2022,28),color='gray', fontsize=12)
plt.gca().annotate('Colombia',(2022,63),color='gray', fontsize=12)
plt.gca().annotate('México',(2022,56),color='gray', fontsize=12)
plt.gca().annotate('Argentina',(2021,49),color='gray', fontsize=12)



# set up caption. 

# caption_text = "Source: https://github.com/VicenteSotelo/desarrollo_productivo"
# caption_x =-0.2
# caption_y =-0.2
# plt.annotate(caption_text, (caption_x, caption_y), xycoords='axes fraction', fontsize=14, color='gray')


# # title, label




# y_label.set_y(1)
# plt.ylim(0, None)

# plt.legend(False) #rm legend

# deliver plot
plt.show()




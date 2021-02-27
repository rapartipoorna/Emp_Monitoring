import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pandas.plotting import table
data = pd.read_excel('Email_Analytics.xlsx')
df=pd.DataFrame(data)

new_df=  df[['Date', 'Month', 'Year','Time','From (Email ID)','Sent/Received','Attachment']].copy()

# new_df.style.set_properties(subset=['From (Email ID)'], **{'width': '400px'})
fig, ax = plt.subplots(figsize=(19, 5)) 
# no axes
ax.xaxis.set_visible(False)  
ax.yaxis.set_visible(False)  
# no frame
ax.set_frame_on(False)  
# plot table
tab = table(ax, new_df, loc='upper left')  
# set font manually
tab.auto_set_font_size(False)
tab.set_fontsize(8) 
# save the result
plt.savefig('Email_images\\Mail_attachments.png')

#arrange the categories in the correct order
data['Day'] = pd.Categorical(data['Day'], categories= ['Mon','Tue','Wed','Thu','Fri','Sat', 'Sun'],ordered=True)

# sort by day of the week
count_sorted_by_day = data['Day'].value_counts().sort_index()

# plt.figure()
# count_sorted_by_day.plot(marker = 'o', color = 'blueviolet', linewidth = 2, ylim = [0,750])
# plt.title('Weekly Email Traffic', fontweight = 'bold' ,fontsize = 14)
# plt.ylabel("Received Email Count", fontweight = 'bold', labelpad = 15)
# plt.grid()
# plt.show()
plt.figure()
received = data[data['Sent/Received'] == 'Received']
# plt.show()

# splitting only the hour portion in the time column
hour = received['Time'].str.split(':').str[0] + ':00'

# sort by hour of the day - using sort_index for numeric sort
count_sorted_by_hour = hour.value_counts().sort_index()

count_sorted_by_hour.plot(marker = 'o', color = 'green')
plt.title('Hourly Email Traffic', fontsize = 14, fontweight = 'bold')
plt.ylabel("Received Email Count", fontweight = 'bold', labelpad = 15)
plt.xlabel("Hour of the Day", fontweight = 'bold', labelpad = 15)
plt.xticks(range(len(count_sorted_by_hour.index)), count_sorted_by_hour.index)
plt.xticks(rotation=90)
plt.grid()
plt.savefig('Email_images\\Email_trafic_time.png')

# extract the sender names and their frequencies of occurence
sender_top_20 =  received['From (Sender)'].value_counts().nlargest(20)
sender_top_20_count = sender_top_20.values
sender_top_20_names = sender_top_20.index.tolist()

plt.figure()
plt.barh(sender_top_20_names, sender_top_20_count, color = 'forestgreen', ec = 'black', linewidth = 1.0)
plt.gca().invert_yaxis()
plt.title('Top 20 Senders', fontsize = 14 ,fontweight = 'bold')
plt.xlabel('Received Email Count', fontweight = 'bold')
plt.tight_layout()
plt.savefig('Email_images\\Email_top_senders.png')

# count the number of words in the subject
# data['Subject Word Count'] = data['Subject'].str.split(' ').str.len()

# plt.figure()
# plt.hist(data['Subject Word Count'], bins=15, color = 'slategray', ec = 'black')
# plt.axis([0, 30, 0, 1200])
# plt.xlabel('Word Count', fontweight = 'bold')
# plt.ylabel('No. of Emails', fontweight = 'bold')
# plt.title('Subject Word Count Histogram', fontsize = 14, fontweight = 'bold')

# split the subject line into words and store them as a list
word_list_2d = data['Subject'].str.split(' ').fillna('none').tolist()
word_list_1d = [word for list in word_list_2d for word in list]

# treat all words as lower case
word_list_1d = [word.lower() for word in word_list_1d]

# exclude common words and words with three or lesser letters
exclude_list = ['this', 'that', 'your', 'with', 'from']
word_list_1d = [word for word in word_list_1d if word not in exclude_list and len(word)>3]

# extract common words in subject lines and their frequencies of occurrence
common_words_map = Counter(word_list_1d).most_common(10)
common_words = [pair[0] for pair in common_words_map]
frequency = [pair[1] for pair in common_words_map]

plt.figure()
plt.barh(common_words, frequency, color = 'lightcoral', ec = 'black', linewidth = 1.25)
plt.gca().invert_yaxis()
plt.title('Most Common Words in Subjects', fontsize = 14 ,fontweight = 'bold')
y = 0.15
for i in range(len(frequency)):
    if len(str(frequency[i])) == 3:
        x = frequency[i] - 14
    else:
        x = frequency[i] - 10
    plt.text(x,y,frequency[i], fontsize = 10,fontweight = 'bold')
    y = y + 1
plt.xticks([0,200])
plt.xlabel('Occurrences', fontweight = 'bold', labelpad=-5)
plt.savefig('Email_images\\Email_words.png')
# plt.show()
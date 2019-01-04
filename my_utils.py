import pandas as pd
import numpy as np
import re


def name_filter(raw_df,fields,file_path='./for_filter/useless_words.txt',isinplace=True):
	old_shape=raw_df.shape
	raw_df.dropna(inplace=isinplace)
	
	del_word_list=[]
	fff=open(file_path,'r')
	for word in fff.readlines():
		del_word_list.append(word.strip())
	del_word_list.append('')
	for field in fields:
		useless_index=raw_df[raw_df[field].isin(del_word_list)].index
		raw_df.drop(useless_index,inplace=True)
	
	new_shape=raw_df.shape
	print('Old Dataframe shape:',old_shape,' New Dataframe shape:',new_shape)
	print('Delete ',old_shape[0]-new_shape[0],'rows')
	return raw_df

def name_normalize(raw_df,fields):
	pattern = re.compile('[\u4e00-\u9fa5]+')
	pattern2 = re.compile('[(][\S]+[)]')
	
	for field in fields:
		temp_list=raw_df[field]
		temp_list=[aa.replace('（','(') for aa in temp_list]
		temp_list=[aa.replace('）',')') for aa in temp_list]
		
		temp_list=[''.join(pattern2.split(aa)) for aa in temp_list]
		temp_list=[''.join(pattern.findall(aa)) for aa in temp_list]
		
		raw_df[field]=temp_list
	return raw_df
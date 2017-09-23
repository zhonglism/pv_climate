
# coding: utf-8

# In[2]:

# url='http://api.data.cma.cn/api?key=2039E060E95DBE99F8D721B4A5A742BE&data=SURF_CHN_HOR&staIDs=54511&times=20170306020000'
import calendar 
import numpy as np
import json
import pandas as pd
from urllib.request import Request, urlopen, URLError
from urllib.parse import urlencode



# In[117]:

# pd.set_option('display.max_colwidth', -1)
pd.options.display.max_rows=5000


# In[4]:

def is_small_month(month):
    if month in (4,6,9,11):
        return True
    return False

def is_feb(month):
    if month==2:
        return True
    return False

def num2ymd(year,month,day):
    if day<10:
        daystr='0'+str(day)
    elif day>=10:
        daystr=str(day)
    if month<10:
        monstr='0'+str(month)
    elif month>=10:
        monstr=str(month)
    return str(year)+'-'+monstr+'-'+daystr


# In[5]:

def datelist(strd,stpd,strm=1,stpm=1,stry=2017,stpy=2017):
    if stry==stpy:
        if strm==stpm:
            if strd==stpd:
                return [num2ymd(stry,strm,strd)]
            else:
                datestrls1=[]
                for day in range(strd,stpd+1):
                    datestr1=num2ymd(stry,strm,day)
                    datestrls1.append(datestr1)
                return datestrls1
        else:
            datestrls2=[]
            for month in range(strm,stpm+1):
                if month==strm:
                    if is_feb(month):
                        if calendar.isleap(stry):
                            for day in range(strd,30):
                                datestr2=num2ymd(stry,month,day)
                                datestrls2.append(datestr2)
                        else:
                            for day in range(strd,29):
                                datestr2=num2ymd(stry,month,day)
                                datestrls2.append(datestr2)
                    elif is_small_month(month):
                        for day in range(strd,31):
                            datestr2=num2ymd(stry,month,day)
                            datestrls2.append(datestr2)
                    else:
                        for day in range(strd,32):
                            datestr2=num2ymd(stry,month,day)
                            datestrls2.append(datestr2)
                elif month>strm and month<stpm:
                    if is_feb(month):
                        if calendar.isleap(stry):
                            for day in range(1,30):
                                datestr3=num2ymd(stry,month,day)
                                datestrls2.append(datestr3)
                        else:
                            for day in range(1,29):
                                datestr3=num2ymd(stry,month,day)
                                datestrls2.append(datestr3)
                    elif is_small_month(month):
                        for day in range(1,31):
                            datestr3=num2ymd(stry,month,day)
                            datestrls2.append(datestr3)
                    else:
                        for day in range(1,32):
                            datestr3=num2ymd(stry,month,day)
                            datestrls2.append(datestr3)
                elif month==stpm:
                    for day in range(1,stpd+1):
                        datestr4=num2ymd(stry,month,day)
                        datestrls2.append(datestr4)
            return datestrls2            
#     not the same year
    else:
        datestrls3=[]
        for year in range(stry,stpy+1):
            if year==stry:
                for month in range(strm,13):
                    if month==strm:
                        if is_feb(month):
                            if calendar.isleap(year):
                                for day in range(strd,30):
                                    datestr5=num2ymd(year,month,day)
                                    datestrls3.append(datestr5)
                            else:
                                for day in range(strd,29):
                                    datestr5=num2ymd(year,month,day)
                                    datestrls3.append(datestr5)
                        elif is_small_month(month):
                            for day in range(strd,31):
                                datestr5=num2ymd(year,month,day)
                                datestrls3.append(datestr5)
                        else:
                            for day in range(strd,32):
                                datestr5=num2ymd(year,month,day)
                                datestrls3.append(datestr5)
                    else:
                        if is_feb(month):
                            if calendar.isleap(year):
                                for day in range(1,30):
                                    datestr6=num2ymd(year,month,day)
                                    datestrls3.append(datestr6)
                            else:
                                for day in range(1,29):
                                    datestr6=num2ymd(year,month,day)
                                    datestrls3.append(datestr6)
                        elif is_small_month(month):
                            for day in range(1,31):
                                datestr6=num2ymd(year,month,day)
                                datestrls3.append(datestr6)
                        else:
                            for day in range(1,32):
                                datestr6=num2ymd(year,month,day)
                                datestrls3.append(datestr6)
            elif year>stry and year<stpy:
                for month in range(1,13):
                    if is_feb(month):
                        if calendar.isleap(year):
                            for day in range(1,30):
                                datestr7=num2ymd(year,month,day)
                                datestrls3.append(datestr7)
                        else:
                            for day in range(1,29):
                                datestr7=num2ymd(year,month,day)
                                datestrls3.append(datestr7)
                    elif is_small_month(month):
                        for day in range(1,31):
                            datestr7=num2ymd(year,month,day)
                            datestrls3.append(datestr7)
                    else:
                        for day in range(1,32):
                            datestr7=num2ymd(year,month,day)
                            datestrls3.append(datestr7)
            elif year==stpy:
                for month in range(1,stpm+1):
                    if month==1:
                        if month==stpm:
                            for day in range(1,stpd+1):
                                datestr8=num2ymd(year,month,day)
                                datestrls3.append(datestr8)
                        else:
                            for day in range(1,32):
                                datestr8=num2ymd(year,month,day)
                                datestrls3.append(datestr8)
                    elif month>1 and month<stpm:
                        if is_feb(month):
                            if calendar.isleap(year):
                                for day in range(1,30):
                                    datestr9=num2ymd(year,month,day)
                                    datestrls3.append(datestr9)
                            else:
                                for day in range(1,29):
                                    datestr9=num2ymd(year,month,day)
                                    datestrls3.append(datestr9)
                        elif is_small_month(month):
                            for day in range(1,31):
                                datestr9=num2ymd(year,month,day)
                                datestrls3.append(datestr9)
                        else:
                            for day in range(1,32):
                                datestr9=num2ymd(year,month,day)
                                datestrls3.append(datestr9)
                    elif month==stpm:
                        for day in range(1,stpd+1):
                            datestr10=num2ymd(year,month,day)
                            datestrls3.append(datestr10)
        return datestrls3        
        


# In[6]:

def nowapi(url = 'http://api.k780.com', app='weather.history', weaid= '759',
            date='2017-06-12',  appkey = '26597', sign='c770a34825a86f510937115da20c6e03',
#                sign ='1020db0d15023fdb7606bc0ea72dda9c',
            format1='json'):
    url=url
    params={
        'app':app,
        'weaid':weaid,
        'date':date,
        'appkey':appkey,
        'sign' : sign,
        'format' : format1,
    }

    params = urlencode(params)
    f = urlopen('%s?%s' % (url, params))
    nowapi_call = f.read().decode('utf-8')
    a_result = json.loads(nowapi_call)
    data=a_result['result']
    return data


# In[28]:

# date1=datelist(1,30,1,6,2017,2017)


# In[135]:

# result_list=[]
# for d in cl:
#     try:
#         a=nowapi(date=d)
#         result_list+=a
#     except KeyError:
#         continue
# result_climate_data=pd.DataFrame(result_list)


# In[32]:

result_climate_data.to_csv('1-1_to_2-28_history_data.csv',encoding='utf-8')


# In[121]:

pvd=pd.read_excel('solardata.xlsx')


# In[132]:

# l=pvd.time.str.split(' ').tolist()
# cl=[item[0] for item in l]


# In[180]:

tmp=pd.read_csv('1-1_to_2-28_history_data.csv')

tmp=tmp.drop(['cityno','Unnamed: 0','weaid','citynm','weather_icon','cityid','temperature'],axis=1)

tmp.humidity=tmp.humidity.str.extract('^(\d+)',expand=False)

tmp.uptime=pd.to_datetime(tmp.uptime)
pvd.time=pd.to_datetime(pvd.time)

tmp['time']=1
tmp['pap']=0


# In[38]:

# tmp


# In[181]:

tmptest=tmp
# tmptest.uptime


# In[183]:

# tmptest.iloc[377:597,3]
tmptest=tmptest.drop(tmptest.index[377:597])


# In[198]:

def foo():
    t=0
    for it in range(tmptest.shape[0]):
        try:
            cote=[]
            lpkt={}
            lpkd={}
            for ip in range(t,pvd.shape[0]):
                dif=tmptest.iloc[it,3]-pvd.iloc[ip,0]
                sub=abs(dif / np.timedelta64(1,'m'))
    #             print(it,ip,sub)
    #             if sub<0:
    #                 continue
                if sub<30:
                    print(it,ip,sub)
                    cote.append(sub)
                    lpkt[sub]=pvd.iloc[ip,0]
                    lpkd[pvd.iloc[ip,0]]=pvd.iloc[ip,1]
                elif sub>=30:
                    if cote:
                        break
            if cote:
                t=ip
                tmptest.iloc[it,11]=lpkt[min(cote)]
                tmptest.iloc[it,12]=lpkd[lpkt[min(cote)]]
        except AttributeError:
            continue


# In[201]:

# foo()


# In[203]:

# tmptest


# In[204]:

tmptest.to_csv('merged_data.csv',encoding='utf-8')
Mostly used in [[preprocessing]], cleaning and analysis in machine learning 
## **Reading Files**
```python 
pd.read_csv('file.csv')
#Fields separatred with white-space
pd.read_csv('file.data',sep=r'\s+')
```
- `sep=r'\s+'` is a regular expression --> more flexible when fields are separated with other characters 
- 
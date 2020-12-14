import pandasql

df1 = pandasql.load_births()
df2 = pandasql.load_meat()


sql = """
        select 
            date,count(*) as n
        from df1 
        group by date
        order by n desc;
      """
result = pandasql.sqldf(sql)
result[result['n']==3]
print(result)
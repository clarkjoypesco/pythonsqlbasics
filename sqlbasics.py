create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);

       
QUERY = '''
select name, birthdate from animals where (not species = 'gorilla')
and (not name= 'Max');
'''


QUERY = '''
select name, birthdate from animals where !(not species = 'gorilla'
 or name= 'Max');
'''


#
# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.


QUERY = '''
select name from animals where species ='llamas' and birthdate >= '1995-01-01' 
and birthdate <= '1998-12-31'
 
'''







#
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!
#

# QUERY = "select max(name) from animals;"

# QUERY = "select * from animals limit 10;"

# QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

# QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

# QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

# QUERY = "select species, min(birthdate) from animals group by species;"

# QUERY = '''
# select name, count(*) as num from animals
# group by name
# order by num desc
# limit 5;
# '''
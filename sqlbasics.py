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

#
# Write a query that returns all the species in the zoo, and how many animals of
# each species there are, sorted with the most populous species at the top.
# 
# The result should have two columns:  species and number.
#
# The animals table has columns (name, species, birthdate) for each individual.
# 
QUERY = "select count(*) as num, species 
        from animals
        group by species
        order by num desc"

#
# Insert a newborn baby opossum into the animals table and verify that it's
# been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
# 
# SELECT_QUERY should find the names and birthdates of all opossums.
# 
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY = '''
select ... where ...;
'''

INSERT_QUERY = '''
insert into animals values('Wibble','opussom','2019-4-17');
'''

INSERT_QUERY = '''
insert into animals(name,species,birthdate) values('Wibble','opussom','2019-4-17');
'''
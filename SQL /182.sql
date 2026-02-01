SELECT email as Email   #alias
FROM Person
GROUP BY email
HAVING count(*) != 1

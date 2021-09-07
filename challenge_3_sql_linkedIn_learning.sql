INSERT INTO people
(first_name, last_name, city, state_code, shirt_or_hat,quiz_points,team)
VALUES
('Walter','St. John','Buffalo','NY','hat','93','Baffled Badgers'),
('Emerald','Chou','Topeka','KS','shirt','92','Angry Ants');

select id_number
from people
where first_name = 'Bonnie' AND last_name = 'Brooks' AND shirt_or_hat = 'hat';

UPDATE people
SET shirt_or_hat = 'shirt'
WHERE first_name = 'Bonnie' AND last_name = 'Brooks' AND shirt_or_hat = 'hat';

select id_number
from people
where first_name = 'Lois' AND last_name = 'Hart';

DELETE FROM people
WHERE first_name = 'Lois' AND last_name = 'Hart' AND id_number = '590';


# Heroes & Villains Bonus:

## Bonus 1:

- Create a Power model in the supers app that contains a 'name' property .
- Register Power model with admin site and seed several powers, 'Super Strength', 'Flight', 'Energy Beam' etc.
- Alter the Super model to replace primary & secondary ability with a 'powers' ManyToManyField.
- Create a PATCH endpoint for the supers app that allows you to add a new Power to a Super by submitting the PK of the hero and the new power as path variables.

## Bonus 2:

- Create an endpoint that allows you to pass in a hero name and villain name as Query params.
- Query for each of the submitted Supers and compare their number of powers. Whoever has more powers listed is the winner
- Send back a custom object response that contains a 'winner' key containing the winner's info and a 'loser' key containing the loser's info, or a different message if it is a tie.



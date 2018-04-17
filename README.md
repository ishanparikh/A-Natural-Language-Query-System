# A-Natural-Language-Query-System-NLTK
Using NLTK to construct a system that reads simple facts and then answers questions about them. A simple form of both machine reading and question answering. In the real world, such systems read large amounts of text (e.g. Wikipedia or news sites), populate database with facts learned from that text, and use the database to answer general knowledge questions about the world.

System will enable dialogues such as the following:
$$ John is a duck.
OK

$$ Mary is a duck.
OK

$$ John is purple.
OK
$$ Mary flies.
OK
$$ John likes Mary.
OK
$$ Who is a duck?
John Mary
$$ Who likes a duck who flies?
John
$$ Which purple ducks fly?
None

Sentences submitted are either statements or questions. Statements have
a very simple form, but the system uses them to learn what words are in the language
and what parts of speech they have. (For example, from the statements above, the
system learns that duck is a noun, fly is an intransitive verb and so on.) Questions can
have a much more complex form, but can only use words and names that the system
has already learned from the statements it has seen.

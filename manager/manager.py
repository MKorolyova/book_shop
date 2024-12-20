import mysql.connector
import uuid
import random
import json
from datetime import datetime
from input_validation import InputValidator

data =''' {
  "books" : [

    {
      "author_name": "George Orwell",
      "book_name": "1984",
      "price": 9.99,
      "publication_year": 1949,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "Set in a totalitarian dystopia, '1984' by George Orwell is a powerful exploration of surveillance, censorship, and state control. The novel takes place in Oceania, a superstate ruled by the Party and its leader, Big Brother, who maintains constant surveillance over its citizens. Winston Smith, the protagonist, works for the Party rewriting history to fit the regime's narrative. Disillusioned, he begins to secretly rebel, questioning the oppressive system that controls every aspect of life. Orwell’s chilling vision serves as a profound commentary on the dangers of totalitarianism, the loss of individuality, and the manipulative power of language. The novel remains a powerful warning about the consequences of unchecked political power and the erosion of personal freedoms.",
      "author_info": "George Orwell was an English novelist, essayist, journalist, and critic. His works, particularly '1984' and 'Animal Farm,' have become synonymous with critiques of totalitarianism, social injustice, and the abuse of power. Orwell’s writing reflects his deep concern for political freedom and human dignity.",
      "review": "A haunting and thought-provoking novel that resonates deeply with modern concerns about surveillance, censorship, and authoritarianism. Orwell’s vivid portrayal of a dystopian world offers a stark reminder of the fragility of freedom."
    },
    {
      "author_name": "J.K. Rowling",
      "book_name": "Harry Potter and the Sorcerer's Stone",
      "price": 10.99,
      "publication_year": 1997,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "The first book in the globally acclaimed Harry Potter series, 'Harry Potter and the Sorcerer's Stone' introduces readers to the magical world of Hogwarts and the adventures of a young boy named Harry. Orphaned and raised by cruel relatives, Harry discovers on his eleventh birthday that he is a wizard and is invited to attend Hogwarts School of Witchcraft and Wizardry. There, he learns about his true heritage, makes lifelong friends, and uncovers a sinister plot surrounding the powerful Sorcerer's Stone. J.K. Rowling’s brilliant world-building and her characters’ emotional depth have captivated millions, making this an unforgettable tale of friendship, bravery, and the fight between good and evil. The book explores themes of identity, belonging, and the power of love, while also offering a thrilling and imaginative adventure.",
      "author_info": "J.K. Rowling is a British author, best known for creating the 'Harry Potter' series, which has become one of the most successful and influential franchises in literary history. Rowling has also written novels for adults, including 'The Casual Vacancy' and the Cormoran Strike detective series.",
      "review": "A captivating and magical start to one of the most beloved literary series of all time. Rowling’s masterful storytelling immerses readers in a rich, imaginative world that continues to enchant readers of all ages."
    },
    {
      "author_name": "F. Scott Fitzgerald",
      "book_name": "The Great Gatsby",
      "price": 8.99,
      "publication_year": 1925,
      "publication_city": "New York",
      "genre": "Fiction",
      "description": "'The Great Gatsby' is a classic American novel that explores the decadence and excesses of the Roaring Twenties. Set in Long Island, the story follows the enigmatic Jay Gatsby, a wealthy man whose life is defined by his obsessive desire to reunite with Daisy Buchanan, a woman he loved years earlier. Through the eyes of narrator Nick Carraway, readers are drawn into a world of opulence, parties, and unrequited love, as Gatsby's pursuit of the American Dream ultimately leads to his tragic downfall. Fitzgerald's exploration of themes such as love, wealth, and social class remains relevant today, offering a critical view of the American ideal and its inherent flaws. The novel’s beautiful prose and emotional depth make it one of the most enduring works of American literature.",
      "author_info": "F. Scott Fitzgerald was an American novelist and short story writer, widely regarded as one of the greatest American writers of the 20th century. His works are often associated with the Jazz Age and the exploration of themes such as wealth, class, and the pursuit of happiness.",
      "review": "A masterpiece that beautifully captures the illusions of wealth and love, while exploring the moral decay of society. Fitzgerald's lyrical writing and poignant commentary on the American Dream make this a timeless and essential read."
    },
    {
      "author_name": "Jane Austen",
      "book_name": "Pride and Prejudice",
      "price": 6.99,
      "publication_year": 1813,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Pride and Prejudice' is a brilliant social commentary on the intricacies of relationships, class, and marriage in early 19th-century England. The novel follows the witty and independent Elizabeth Bennet as she navigates the complex world of love and social expectations. Elizabeth’s initial disdain for the aloof and wealthy Mr. Darcy turns to admiration and love as she uncovers his true character and the sacrifices he has made for others. Austen’s sharp humor, clever dialogue, and exploration of personal growth make this a timeless and highly influential novel. At its heart, 'Pride and Prejudice' is about the importance of understanding, mutual respect, and personal integrity, offering a sophisticated critique of the class system and the limitations placed on women in that era.",
      "author_info": "Jane Austen was an English novelist known for her keen observations on social life, class, and relationships. Her works, including 'Pride and Prejudice,' 'Emma,' and 'Sense and Sensibility,' are regarded as some of the most important in English literature.",
      "review": "A witty and insightful examination of love, social expectations, and personal growth. Austen’s sparkling dialogue and memorable characters make this a timeless classic that continues to captivate readers."
    },
    {
      "author_name": "Harper Lee",
      "book_name": "To Kill a Mockingbird",
      "price": 7.99,
      "publication_year": 1960,
      "publication_city": "Philadelphia",
      "genre": "Fiction",
      "description": "'To Kill a Mockingbird' is a poignant exploration of racial injustice, morality, and the loss of innocence in the Deep South during the 1930s. The novel follows young Scout Finch, who lives in the fictional town of Maycomb, Alabama, where her father, Atticus Finch, is a principled lawyer defending a black man, Tom Robinson, who is accused of raping a white woman. Through Scout’s eyes, readers experience the harsh realities of prejudice and the moral dilemmas that arise when individuals confront injustice. Harper Lee’s masterful storytelling, rich character development, and timeless themes make this an essential work of American literature, offering valuable lessons about empathy, courage, and the importance of standing up for what is right.",
      "author_info": "Harper Lee was an American novelist, best known for her Pulitzer Prize-winning novel, 'To Kill a Mockingbird.' Her works explore themes of racism, morality, and human dignity, and she remains one of the most important authors in American literature.",
      "review": "A powerful and moving novel that tackles difficult themes of race, morality, and justice. Lee’s eloquent prose and memorable characters make this book a timeless classic."
    },
    {
      "author_name": "Mark Twain",
      "book_name": "The Adventures of Huckleberry Finn",
      "price": 5.99,
      "publication_year": 1884,
      "publication_city": "Chicago",
      "genre": "Fiction",
      "description": "'The Adventures of Huckleberry Finn' is one of the most celebrated works in American literature. The novel follows Huck Finn, a young boy who runs away from home to escape his abusive father. He embarks on a journey down the Mississippi River with Jim, a runaway slave, and together they face numerous challenges and adventures. Twain’s sharp wit and exploration of themes such as race, freedom, and the moral dilemmas of society make this a timeless classic. Huck’s moral growth, as he comes to understand the complexities of right and wrong, is at the heart of the novel, offering readers a deep commentary on human nature and society.",
      "author_info": "Mark Twain, born Samuel Clemens, was an American author and humorist, best known for 'The Adventures of Huckleberry Finn' and 'The Adventures of Tom Sawyer.' His works explore social issues, morality, and the human condition, often through satire and humor.",
      "review": "A rich, adventurous tale with profound insights into the complexities of morality, race, and freedom in America."
    },
    {
      "author_name": "Leo Tolstoy",
      "book_name": "War and Peace",
      "price": 13.99,
      "publication_year": 1869,
      "publication_city": "Moscow",
      "genre": "Fiction",
      "description": "'War and Peace' is a monumental work by Leo Tolstoy, considered one of the greatest novels ever written. Set during the Napoleonic Wars, the novel follows the lives of several aristocratic families as they navigate love, loss, and the shifting tides of history. Tolstoy masterfully weaves together personal struggles with sweeping historical events, offering deep insights into human nature, morality, and the impact of war on individuals and society. The novel explores themes of duty, honor, and the meaning of life, all while capturing the grandeur and turmoil of 19th-century Russia. With its richly drawn characters and philosophical depth, 'War and Peace' is a profound meditation on the human condition.",
      "author_info": "Leo Tolstoy was a Russian novelist, philosopher, and social reformer, widely regarded as one of the greatest writers of all time. His works, including 'Anna Karenina' and 'War and Peace,' have had a lasting influence on literature and world thought.",
      "review": "A masterpiece of historical fiction that offers an unparalleled exploration of love, war, and the nature of human existence."
    },
    {
      "author_name": "Charles Dickens",
      "book_name": "A Tale of Two Cities",
      "price": 7.49,
      "publication_year": 1859,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'A Tale of Two Cities' is a historical novel by Charles Dickens, set during the turbulent period of the French Revolution. The story follows several characters, most notably Charles Darnay, a French aristocrat, and Sydney Carton, an English lawyer, whose lives are intertwined by the revolutionary events. Dickens uses these characters to explore themes of sacrifice, resurrection, and the effects of social injustice. The novel contrasts the cities of Paris and London, symbolizing the upheaval and hope of the time. With its unforgettable opening line, 'It was the best of times, it was the worst of times,' the novel remains a powerful commentary on social and political change.",
      "author_info": "Charles Dickens was an English novelist and social critic, renowned for his vivid characters and depictions of Victorian society. His works, including 'Oliver Twist,' 'Great Expectations,' and 'David Copperfield,' are considered classics of English literature.",
      "review": "A gripping and timeless tale of love, sacrifice, and social change during one of history's most tumultuous periods."
    },
    {
      "author_name": "William Shakespeare",
      "book_name": "Romeo and Juliet",
      "price": 5.49,
      "publication_year": 1597,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Romeo and Juliet' is one of William Shakespeare’s most famous tragedies, telling the timeless story of forbidden love. Set in Verona, Italy, the play centers around the passionate and ill-fated love between Romeo Montague and Juliet Capulet, whose families are engaged in a bitter feud. Their love leads to secret marriages, deception, and ultimately tragic consequences. The play explores themes of fate, family loyalty, love, and the destructive effects of enmity. Shakespeare’s poetic dialogue and the intensity of the couple’s emotions have made 'Romeo and Juliet' a staple of both the literary canon and popular culture.",
      "author_info": "William Shakespeare was an English playwright, poet, and actor, widely regarded as one of the greatest writers in the English language. His works, including 'Hamlet,' 'Macbeth,' and 'Othello,' have had a profound influence on literature and drama.",
      "review": "A timeless tragedy that explores the complexities of love, fate, and family. Shakespeare’s enduring themes and unforgettable characters continue to resonate with readers and audiences worldwide."
    },
    {
      "author_name": "Herman Melville",
      "book_name": "Moby-Dick",
      "price": 11.99,
      "publication_year": 1851,
      "publication_city": "New York",
      "genre": "Fiction",
      "description": "'Moby-Dick' is a novel by Herman Melville that delves into the obsessive quest of Captain Ahab, who pursues the white whale, Moby Dick, across the seas. The novel is both a thrilling adventure and a philosophical exploration of obsession, fate, and the limits of human knowledge. Through the eyes of Ishmael, the story examines the nature of the sea, the human struggle against the unknown, and the complexities of life and death. Melville’s rich symbolism and masterful prose have made 'Moby-Dick' a quintessential American novel, often interpreted as a metaphor for the human condition and our pursuit of meaning in the face of vast, indifferent forces.",
      "author_info": "Herman Melville was an American novelist, short story writer, and poet, best known for his masterpiece 'Moby-Dick.' His works explore complex themes such as the nature of existence, the conflict between man and nature, and the limitations of knowledge.",
      "review": "A dense, yet profoundly rewarding exploration of obsession, nature, and humanity’s struggle with the unknown. A true literary classic."
    },
    {
      "author_name": "Jane Austen",
      "book_name": "Pride and Prejudice",
      "price": 9.99,
      "publication_year": 1813,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Pride and Prejudice' by Jane Austen is a timeless classic that delves into the complexities of social class, marriage, and morality in early 19th-century England. The story revolves around Elizabeth Bennet, a strong-willed young woman, and her evolving relationship with the wealthy, aloof Mr. Darcy. As the narrative unfolds, Elizabeth grapples with her own biases and assumptions, and the novel explores themes of love, self-awareness, and the role of societal expectations. Austen's wit, irony, and insightful commentary on human nature make this one of the most beloved novels in English literature.",
      "author_info": "Jane Austen was an English novelist best known for her keen social observations and vibrant characterizations. Her works, including 'Sense and Sensibility,' 'Emma,' and 'Persuasion,' remain widely read and cherished.",
      "review": "A sharp, witty exploration of love, social expectations, and personal growth. Austen's characters and insights into human nature continue to resonate with readers today."
    },
    {
      "author_name": "Charlotte Brontë",
      "book_name": "Jane Eyre",
      "price": 10.99,
      "publication_year": 1847,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Jane Eyre' by Charlotte Brontë is a Gothic novel that explores themes of love, morality, and independence. The story follows the life of the orphaned Jane, who rises from a harsh childhood to become a governess at Thornfield Hall, where she meets the enigmatic Mr. Rochester. As their relationship deepens, Jane uncovers dark secrets that challenge her sense of self and morality. Brontë’s writing is rich with emotion and insight, capturing the struggle for personal freedom in a rigidly controlled society. 'Jane Eyre' is a tale of resilience, love, and empowerment.",
      "author_info": "Charlotte Brontë was an English novelist and poet, famous for her passionate and gothic stories. Her works, including 'Shirley' and 'Villette,' have a lasting impact on Victorian literature.",
      "review": "A richly atmospheric novel that combines romance, mystery, and social critique. Brontë’s unforgettable heroine remains a symbol of strength and self-reliance."
    },
    {
      "author_name": "George Orwell",
      "book_name": "1984",
      "price": 8.99,
      "publication_year": 1949,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'1984' by George Orwell is a dystopian novel set in a totalitarian society controlled by the Party and its leader, Big Brother. The story follows Winston Smith, a low-ranking member of the Party, as he navigates life under constant surveillance and manipulation. Winston begins to question the Party’s oppressive control and starts an illicit relationship with Julia, which ultimately leads him to confront the reality of rebellion and the consequences of truth in a world of lies. Orwell’s novel serves as a chilling warning about the dangers of totalitarianism, censorship, and the loss of personal freedoms.",
      "author_info": "George Orwell was an English writer, journalist, and social critic, known for his works on totalitarianism and political oppression. His novels, including 'Animal Farm' and '1984,' are among the most influential in modern literature.",
      "review": "A powerful, haunting exploration of government control and personal freedom. Orwell’s prescient vision of a surveillance state remains relevant today."
    },
    {
      "author_name": "Virginia Woolf",
      "book_name": "Mrs. Dalloway",
      "price": 10.49,
      "publication_year": 1925,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Mrs. Dalloway' by Virginia Woolf follows Clarissa Dalloway, a woman preparing for a party she will host that evening, as she reflects on her life, her past choices, and her relationships. The novel takes place in a single day in post-World War I London and is a profound exploration of mental health, memory, and societal expectations. Woolf’s stream-of-consciousness technique allows readers to dive deeply into the inner lives of her characters, offering insight into the complexities of human experience. The book is an eloquent examination of time, identity, and connection.",
      "author_info": "Virginia Woolf was an English writer and modernist, known for her exploration of the inner lives of her characters and her contributions to feminist literature. Her works include 'To the Lighthouse' and 'Orlando.'",
      "review": "A beautifully written novel that captures the nuances of life, memory, and time. Woolf’s lyrical prose and psychological depth make this a landmark work in modern literature."
    },
    {
      "author_name": "F. Scott Fitzgerald",
      "book_name": "The Great Gatsby",
      "price": 9.49,
      "publication_year": 1925,
      "publication_city": "New York",
      "genre": "Fiction",
      "description": "'The Great Gatsby' by F. Scott Fitzgerald is a critical exploration of the American Dream in the Jazz Age. The novel follows Nick Carraway, who narrates the story of the mysterious and wealthy Jay Gatsby, who is obsessed with reuniting with his lost love, Daisy Buchanan. The book explores themes of wealth, class, obsession, and the illusion of the American Dream. Fitzgerald’s portrayal of the excesses and disillusionment of the 1920s remains a poignant commentary on the fragility of success and the emptiness of materialism.",
      "author_info": "F. Scott Fitzgerald was an American novelist, widely regarded for his portrayal of the American Jazz Age. His works, including 'Tender Is the Night' and 'This Side of Paradise,' are celebrated for their lyrical prose and critical social insights.",
      "review": "A haunting exploration of love, loss, and the corruption of dreams. Fitzgerald’s elegant prose and sharp social commentary make this a timeless classic."
    },
    {
      "author_name": "Mark Twain",
      "book_name": "The Adventures of Huckleberry Finn",
      "price": 7.49,
      "publication_year": 1884,
      "publication_city": "New York",
      "genre": "Fiction",
      "description": "'The Adventures of Huckleberry Finn' by Mark Twain follows the journey of Huck, a young boy, as he escapes his abusive father and embarks on a river adventure with Jim, a runaway slave. The novel explores themes of racism, freedom, and moral growth as Huck grapples with his own conscience and the injustices of society. Through Huck’s wit and humor, Twain critiques the social norms and hypocrisy of his time. This groundbreaking work is one of the most important American novels, offering a powerful narrative about friendship, loyalty, and the struggle for freedom.",
      "author_info": "Mark Twain was an American author and humorist, best known for his works 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn.' His novels, often filled with social criticism and biting humor, have had a lasting impact on American literature.",
      "review": "A vivid, adventurous exploration of friendship, freedom, and moral dilemmas. Twain’s humor and social criticism make this a groundbreaking work in American literature."
    },
    {
      "author_name": "Toni Morrison",
      "book_name": "Beloved",
      "price": 12.99,
      "publication_year": 1987,
      "publication_city": "New York",
      "genre": "Fiction",
      "description": "'Beloved' by Toni Morrison is a haunting novel that explores the legacy of slavery in post-Civil War America. The story follows Sethe, a former enslaved woman, who is haunted by the ghost of her deceased daughter, Beloved. As Sethe’s past and present collide, Morrison examines themes of memory, trauma, and the impact of slavery on identity and family. 'Beloved' is a powerful narrative about the struggle for selfhood and the haunting consequences of history. Morrison’s prose is rich and lyrical, offering an unforgettable portrait of pain, survival, and redemption.",
      "author_info": "Toni Morrison was an American novelist and essayist, best known for her works addressing the African American experience, such as 'Song of Solomon' and 'The Bluest Eye.' She won the Nobel Prize in Literature in 1993.",
      "review": "A powerful, emotionally charged exploration of slavery’s lasting impact. Morrison’s lyrical prose and deep psychological insights make this a modern classic."
    },
    {
      "author_name": "Gabriel García Márquez",
      "book_name": "One Hundred Years of Solitude",
      "price": 13.49,
      "publication_year": 1967,
      "publication_city": "Bogotá",
      "genre": "Fiction",
      "description": "'One Hundred Years of Solitude' by Gabriel García Márquez is a landmark work of magical realism. The novel chronicles the rise and fall of the Buendía family in the fictional town of Macondo, blending reality with fantastical elements. Through the lives of the Buendía family, García Márquez explores themes of love, fate, isolation, and the passage of time. His narrative style, which weaves together the surreal and the real, creates a world where the boundaries between the two blur, offering a unique and deeply symbolic exploration of human history.",
      "author_info": "Gabriel García Márquez was a Colombian novelist and Nobel laureate, best known for his works that blend magic and reality, such as 'Love in the Time of Cholera' and 'Chronicle of a Death Foretold.'",
      "review": "A magnificent, sweeping tale of love, family, and the intertwining of history and myth. García Márquez’s prose is rich with symbolism and beauty."
    },
    {
      "author_name": "Leo Tolstoy",
      "book_name": "War and Peace",
      "price": 15.99,
      "publication_year": 1869,
      "publication_city": "Moscow",
      "genre": "Fiction",
      "description": "'War and Peace' by Leo Tolstoy is an epic novel set against the backdrop of the Napoleonic Wars. The story follows the lives of several aristocratic families, most notably Pierre Bezukhov, Andrei Bolkonsky, and Natasha Rostova, as they navigate the complexities of love, war, and personal growth. The novel explores themes of fate, free will, and the interplay between history and individual lives. Tolstoy’s exploration of the nature of war and peace, and his profound psychological insights into his characters, make 'War and Peace' one of the greatest works of literature.",
      "author_info": "Leo Tolstoy was a Russian novelist, philosopher, and social reformer, widely regarded as one of the greatest writers in world literature. His works, including 'Anna Karenina' and 'The Death of Ivan Ilyich,' continue to influence literature and philosophy.",
      "review": "An unparalleled epic that delves into the complexities of history, war, and human emotion. Tolstoy’s philosophical reflections and deeply human insights make this a masterpiece of literature."
    },
    {
      "author_name": "Emily Brontë",
      "book_name": "Wuthering Heights",
      "price": 9.99,
      "publication_year": 1847,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Wuthering Heights' by Emily Brontë is a dark and passionate novel set on the Yorkshire moors. The story centers around the intense, destructive love between Heathcliff, a brooding orphan, and Catherine Earnshaw, whose love for him causes a rift between them and their families. The novel explores themes of obsession, revenge, and the impact of love on one’s identity and soul. Brontë’s gothic style, along with her portrayal of complex, flawed characters, makes 'Wuthering Heights' one of the most compelling and enigmatic works in English literature.",
      "author_info": "Emily Brontë was an English novelist and poet, best known for her only novel, 'Wuthering Heights.' Her haunting, passionate style and exploration of complex emotions have made her a central figure in English literary history.",
      "review": "A haunting, gothic tale of obsessive love and revenge. Brontë’s unique voice and psychological depth make this an unforgettable classic."
    },
    {
      "author_name": "Charles Dickens",
      "book_name": "Great Expectations",
      "price": 8.49,
      "publication_year": 1861,
      "publication_city": "London",
      "genre": "Fiction",
      "description": "'Great Expectations' by Charles Dickens follows the life of Pip, an orphan who dreams of becoming a gentleman and winning the love of the beautiful Estella. As Pip grows up, he learns that his ambitions and desires come with unexpected consequences. The novel explores themes of social class, guilt, and personal development, all set against the backdrop of Victorian England. Through memorable characters like the convict Magwitch and the eccentric Miss Havisham, Dickens examines the complexities of morality, ambition, and the idea of self-improvement. 'Great Expectations' remains one of Dickens’ most beloved works, combining humor, tragedy, and a deep understanding of human nature.",
      "author_info": "Charles Dickens was an English novelist and social critic, known for his vivid characters and his commentary on the social and economic issues of Victorian England. His works, including 'A Tale of Two Cities,' 'David Copperfield,' and 'Oliver Twist,' are widely read and adapted.",
      "review": "A compelling coming-of-age story that critiques social norms and examines the cost of ambition. Dickens’ rich storytelling and memorable characters make this an enduring classic."
    },

    {
      "author_name": "Homer",
      "book_name": "The Odyssey",
      "price": 12.99,
      "publication_year": -800,
      "publication_city": "Ancient Greece",
      "genre": "Classic",
      "description": "'The Odyssey' is an epic poem attributed to Homer, recounting the adventures of Odysseus as he journeys home after the Trojan War. Along the way, he encounters gods, monsters, and temptations that test his wits and endurance. The work explores themes of perseverance, loyalty, and the hero’s journey, and it is one of the foundational texts of Western literature. Through Odysseus' long and arduous journey, Homer delves into the nature of human desire, fate, and the pursuit of home and identity.",
      "author_info": "Homer was an ancient Greek poet traditionally said to be the author of the two epic poems, 'The Iliad' and 'The Odyssey,' which are cornerstones of ancient Greek literature.",
      "review": "A masterful tale of heroism and adventure that has inspired countless generations. 'The Odyssey' offers deep insights into the human spirit and the trials of life."
    },
    {
      "author_name": "Leo Tolstoy",
      "book_name": "Anna Karenina",
      "price": 14.99,
      "publication_year": 1877,
      "publication_city": "Saint Petersburg",
      "genre": "Classic",
      "description": "'Anna Karenina' by Leo Tolstoy explores the complexities of love, marriage, and infidelity within the Russian aristocracy. The novel follows Anna, a beautiful and passionate woman, as she embarks on a doomed affair with the dashing Count Vronsky. The story also follows the contrasting life of Konstantin Levin, whose struggle to find happiness in family life serves as a counterpoint to Anna's tragic journey. Tolstoy’s exploration of morality, social pressures, and the search for meaning in life makes 'Anna Karenina' one of the greatest works of world literature.",
      "author_info": "Leo Tolstoy was a Russian writer best known for his epic novels 'War and Peace' and 'Anna Karenina.' His works, which explore themes of morality, faith, and human nature, are regarded as some of the finest in world literature.",
      "review": "A profound exploration of love, passion, and society’s constraints. Tolstoy’s writing is deeply insightful, and his characters resonate long after the last page."
    },
    {
      "author_name": "Charles Dickens",
      "book_name": "A Tale of Two Cities",
      "price": 10.49,
      "publication_year": 1859,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'A Tale of Two Cities' is a historical novel set during the turbulent time of the French Revolution. The novel follows the intertwined lives of Charles Darnay, a French aristocrat, and Sydney Carton, a disillusioned English lawyer, as they grapple with the events of the revolution. Dickens explores themes of resurrection, sacrifice, and the clash between social classes. Through memorable characters and dramatic twists, Dickens crafts a tale of redemption and the enduring power of love and loyalty amidst revolution and chaos.",
      "author_info": "Charles Dickens was an English novelist and social critic, best known for his vivid characters and his commentary on the social and economic issues of Victorian England. His works include 'Oliver Twist,' 'David Copperfield,' and 'Great Expectations.'",
      "review": "A timeless tale of sacrifice and redemption, with Dickens’ trademark vivid characters and sharp social commentary."
    },
    {
      "author_name": "Fyodor Dostoevsky",
      "book_name": "Crime and Punishment",
      "price": 11.99,
      "publication_year": 1866,
      "publication_city": "Saint Petersburg",
      "genre": "Classic",
      "description": "'Crime and Punishment' by Fyodor Dostoevsky is a psychological novel that explores the mind of Rodion Raskolnikov, a young law student who commits a brutal murder in an attempt to justify his theory of extraordinary men who are above moral law. The novel delves into themes of guilt, redemption, and the consequences of one's actions. Through Raskolnikov’s internal struggle, Dostoevsky explores deep questions of morality, faith, and the human psyche, making it a seminal work in the exploration of existential and philosophical themes.",
      "author_info": "Fyodor Dostoevsky was a Russian novelist and philosopher, whose works explore human psychology and moral dilemmas. His notable works include 'The Brothers Karamazov' and 'The Idiot.'",
      "review": "A deeply introspective and thought-provoking novel, 'Crime and Punishment' confronts the complexity of human nature and the consequences of actions with profound insight."
    },
    {
      "author_name": "Herman Melville",
      "book_name": "Moby-Dick",
      "price": 12.49,
      "publication_year": 1851,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'Moby-Dick' is Herman Melville’s masterpiece about Captain Ahab’s obsessive pursuit of the great white whale, Moby Dick. The novel is a study of obsession, human frailty, and the natural world. Through Ishmael, the narrator, Melville reflects on themes of fate, free will, and humanity’s place in the universe. 'Moby-Dick' is a dense, symbolic, and philosophical work that examines the darker sides of human nature, and its influence on American literature is immeasurable.",
      "author_info": "Herman Melville was an American novelist and poet, best known for his work 'Moby-Dick.' His writing is known for its philosophical and symbolic depth, exploring themes of obsession, fate, and the human condition.",
      "review": "A complex and multi-layered novel that probes deeply into themes of obsession, fate, and human nature, 'Moby-Dick' is a timeless classic."
    },
    {
      "author_name": "Mark Twain",
      "book_name": "The Adventures of Tom Sawyer",
      "price": 7.99,
      "publication_year": 1876,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'The Adventures of Tom Sawyer' is a novel by Mark Twain that follows the mischievous Tom as he grows up in the town of St. Petersburg, Missouri. Alongside his friends, including Huckleberry Finn, Tom embarks on a series of adventures, ranging from treasure hunts to run-ins with villains. The novel is both humorous and insightful, exploring themes of childhood, morality, and the differences between society’s expectations and individual desires. Twain’s vivid descriptions and sharp wit make it one of the most beloved works in American literature.",
      "author_info": "Mark Twain was an American author and humorist, famous for his novels 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn.' His sharp wit and social commentary made him one of the most influential American writers.",
      "review": "A charming and adventurous tale that captures the essence of childhood. Twain’s wit and humor shine through in every page."
    },
    {
      "author_name": "Jane Austen",
      "book_name": "Pride and Prejudice",
      "price": 9.99,
      "publication_year": 1813,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Pride and Prejudice' is a novel by Jane Austen that explores the complexities of social class, marriage, and individual desires. The story centers on Elizabeth Bennet and her developing relationship with the proud, wealthy Mr. Darcy. The novel critiques societal expectations and the limitations they place on women’s roles and marriages. Austen’s sharp wit and insight into human nature make 'Pride and Prejudice' a timeless examination of love, class, and individual growth.",
      "author_info": "Jane Austen was an English novelist whose works, including 'Pride and Prejudice,' 'Sense and Sensibility,' and 'Emma,' are known for their keen social observations and witty depictions of domestic life.",
      "review": "A witty, engaging exploration of love, society, and personal growth. Austen’s sharp critique of social norms remains relevant to this day."
    },
    {
      "author_name": "Charlotte Brontë",
      "book_name": "Jane Eyre",
      "price": 10.99,
      "publication_year": 1847,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Jane Eyre' by Charlotte Brontë is a gothic novel that tells the story of Jane, an orphan who becomes a governess at Thornfield Hall, where she meets the enigmatic Mr. Rochester. As their relationship develops, dark secrets emerge that challenge Jane’s sense of morality and independence. Brontë’s novel is a powerful exploration of love, self-respect, and the desire for freedom, particularly within the constraints of Victorian society. The novel has become a classic of English literature for its strong heroine and gothic atmosphere.",
      "author_info": "Charlotte Brontë was an English novelist, best known for her novel 'Jane Eyre.' Her works often explore themes of love, independence, and the emotional struggles of women in Victorian society.",
      "review": "A dark and compelling novel about love, independence, and morality. Brontë’s writing remains a powerful statement about the strength of the human spirit."
    },
    {
      "author_name": "George Orwell",
      "book_name": "1984",
      "price": 9.99,
      "publication_year": 1949,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'1984' by George Orwell is a dystopian novel that critiques totalitarianism, surveillance, and the loss of individual freedom. The story follows Winston Smith, a member of the Party, as he begins to question the oppressive regime under the leadership of Big Brother. Orwell’s novel explores themes of truth, mind control, and the dangers of unchecked power. It remains one of the most influential works of political literature, warning of the dangers of authoritarianism and the erosion of personal freedoms.",
      "author_info": "George Orwell was an English novelist and journalist, known for his works '1984' and 'Animal Farm,' which critique totalitarian regimes and social injustice.",
      "review": "A chilling and thought-provoking critique of totalitarianism and the power of propaganda. Orwell’s vision of a dystopian future remains remarkably relevant today."
    },
    {
      "author_name": "Virginia Woolf",
      "book_name": "Mrs Dalloway",
      "price": 10.99,
      "publication_year": 1925,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Mrs Dalloway' by Virginia Woolf follows Clarissa Dalloway, a middle-aged woman, as she prepares for a party while reflecting on her past, including lost love and the choices she has made. The novel’s stream-of-consciousness style explores themes of time, memory, and the fragmented nature of human experience. Woolf’s innovative narrative techniques and exploration of the inner lives of her characters make 'Mrs Dalloway' a landmark work of modernist literature, examining the intersections of mental illness, identity, and societal norms.",
      "author_info": "Virginia Woolf was an English writer and modernist, best known for her novels 'Mrs Dalloway,' 'To the Lighthouse,' and 'Orlando.' She is regarded as one of the most important writers of the 20th century.",
      "review": "A beautifully written exploration of memory, time, and consciousness. Woolf’s modernist style offers a deep dive into the human psyche."
    },
    {
      "author_name": "Franz Kafka",
      "book_name": "The Metamorphosis",
      "price": 7.49,
      "publication_year": 1915,
      "publication_city": "Berlin",
      "genre": "Classic",
      "description": "'The Metamorphosis' by Franz Kafka is a novella about Gregor Samsa, a traveling salesman who wakes up one morning to find himself transformed into a giant insect. The story explores themes of alienation, identity, and the absurdity of human existence. Kafka’s surreal narrative delves into the psychological impact of Gregor’s transformation, as he struggles to communicate and relate to his family. The novella has been interpreted as a critique of societal expectations and the dehumanizing aspects of modern life.",
      "author_info": "Franz Kafka was a German-speaking Bohemian writer, best known for his works 'The Trial' and 'The Metamorphosis.' His works explore themes of existential dread and the absurdity of human life.",
      "review": "A strange, haunting novella that explores the alienation and isolation of the human condition in a modern, absurd world."
    },
    {
      "author_name": "Herman Melville",
      "book_name": "Bartleby, the Scrivener",
      "price": 6.99,
      "publication_year": 1853,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'Bartleby, the Scrivener' by Herman Melville is a short story about an employee in a law office, Bartleby, who refuses to comply with his employer’s requests with the famous phrase, ‘I would prefer not to.’ The story explores themes of isolation, alienation, and the dehumanizing aspects of modern work. Through Bartleby’s passive resistance, Melville critiques the mechanized, impersonal nature of society and work. The story is a poignant meditation on individuality, free will, and the search for meaning in a bureaucratic world.",
      "author_info": "Herman Melville was an American writer best known for his novel 'Moby-Dick,' as well as his short stories, including 'Bartleby, the Scrivener,' which reflect his interest in the complexities of human nature.",
      "review": "A thought-provoking story about isolation, individualism, and the power of passive resistance in a dehumanizing society."
    },
    {
      "author_name": "Oscar Wilde",
      "book_name": "The Picture of Dorian Gray",
      "price": 8.99,
      "publication_year": 1890,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'The Picture of Dorian Gray' by Oscar Wilde is a novel about a young man named Dorian Gray, whose portrait ages and reflects the moral degradation of his soul while his outward appearance remains youthful and beautiful. The novel explores themes of vanity, moral corruption, and the consequences of a hedonistic lifestyle. Wilde’s sharp wit and masterful use of symbolism create a chilling commentary on the dangers of excessive pursuit of pleasure and the denial of moral responsibility.",
      "author_info": "Oscar Wilde was an Irish playwright, poet, and author, known for his wit, flamboyant style, and works such as 'The Importance of Being Earnest' and 'The Picture of Dorian Gray.'",
      "review": "A brilliantly dark and thought-provoking novel that critiques vanity, corruption, and the consequences of living a life driven by self-indulgence."
    },
    {
      "author_name": "William Shakespeare",
      "book_name": "Macbeth",
      "price": 7.99,
      "publication_year": 1606,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Macbeth' is a tragedy by William Shakespeare that tells the story of Macbeth, a Scottish general whose ambition leads him to murder the king and seize the throne. However, his guilt and paranoia quickly unravel him, leading to his downfall. The play explores themes of ambition, fate, guilt, and the corrupting power of unchecked ambition. Shakespeare’s use of supernatural elements, including the three witches, enhances the atmosphere of inevitable doom that permeates the tragedy.",
      "author_info": "William Shakespeare was an English playwright, poet, and actor, widely regarded as one of the greatest writers in the English language. His works, including 'Hamlet,' 'Macbeth,' and 'Romeo and Juliet,' have had a profound influence on literature and theater.",
      "review": "A gripping and tragic exploration of ambition and guilt. Shakespeare’s mastery of language and complex characters makes 'Macbeth' a timeless classic."
    },
    {
      "author_name": "Emily Brontë",
      "book_name": "Wuthering Heights",
      "price": 9.49,
      "publication_year": 1847,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Wuthering Heights' by Emily Brontë is a dark and passionate novel about the tumultuous love between Heathcliff and Catherine Earnshaw, two characters whose obsessive emotions lead to betrayal, revenge, and tragedy. Set on the bleak Yorkshire moors, the novel explores themes of love, vengeance, and the destructive power of obsession. The novel's gothic atmosphere and complex narrative structure, told through the perspectives of multiple narrators, create a haunting portrayal of the consequences of passion unchecked by morality.",
      "author_info": "Emily Brontë was an English novelist and poet, best known for her only novel, 'Wuthering Heights,' which is considered one of the greatest works of English literature.",
      "review": "A dark, passionate, and ultimately tragic tale of love and obsession, with an atmosphere that has made it one of the most powerful works of gothic literature."
    },
    {
      "author_name": "John Steinbeck",
      "book_name": "Of Mice and Men",
      "price": 8.99,
      "publication_year": 1937,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'Of Mice and Men' by John Steinbeck follows two displaced migrant workers, George and Lennie, during the Great Depression. As they search for work and dream of owning a piece of land, the novel explores themes of friendship, loneliness, and the American Dream. The tragic ending of the story highlights the harsh realities faced by the disenfranchised and the power dynamics between the strong and weak in society. Steinbeck’s novel is known for its deep compassion for the human condition and its portrayal of the struggle for dignity in a world filled with hardship.",
      "author_info": "John Steinbeck was an American author, best known for his novels 'The Grapes of Wrath,' 'Of Mice and Men,' and 'East of Eden.' His works explore social issues and the struggles of the working class.",
      "review": "A poignant and tragic exploration of friendship, dreams, and social injustice. Steinbeck’s novel is a powerful portrayal of human vulnerability."
    },
    {
      "author_name": "Jack London",
      "book_name": "The Call of the Wild",
      "price": 6.99,
      "publication_year": 1903,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'The Call of the Wild' by Jack London is the story of Buck, a domesticated dog who is torn from his comfortable home and thrust into the brutal wilderness of the Klondike Gold Rush. As Buck transforms into a wild animal, the novel explores themes of survival, instinct, and the relationship between man and nature. London’s vivid descriptions and his portrayal of Buck’s journey make this novel an unforgettable adventure that examines the primal instincts within us all.",
      "author_info": "Jack London was an American novelist and journalist, best known for his adventure stories, including 'The Call of the Wild' and 'White Fang.' His works often explore the struggle for survival and the harshness of nature.",
      "review": "A powerful adventure story about survival and the primal instincts that define both animals and humans. London’s writing immerses readers in the wilderness."
    },
    {
      "author_name": "George Eliot",
      "book_name": "Middlemarch",
      "price": 11.99,
      "publication_year": 1871,
      "publication_city": "London",
      "genre": "Classic",
      "description": "'Middlemarch' by George Eliot is a novel that examines the lives of several characters in the fictional town of Middlemarch, focusing on their relationships, personal ambitions, and social challenges. The novel explores themes of idealism, marriage, political reform, and the consequences of personal choices. Eliot’s richly drawn characters and her keen social insights make 'Middlemarch' one of the greatest novels of the 19th century, offering a detailed portrait of provincial life in Victorian England.",
      "author_info": "George Eliot was the pen name of Mary Ann Evans, an English novelist known for her works 'Middlemarch,' 'Silas Marner,' and 'The Mill on the Floss.' Her works often explore social issues and the complexities of human nature.",
      "review": "A deeply insightful and richly detailed exploration of human nature, ambition, and societal expectations. Eliot’s novel is a timeless classic."
    },
    {
      "author_name": "Dante Alighieri",
      "book_name": "The Divine Comedy",
      "price": 13.99,
      "publication_year": 1320,
      "publication_city": "Florence",
      "genre": "Classic",
      "description": "'The Divine Comedy' by Dante Alighieri is an epic poem that describes the journey of the poet through the realms of Hell, Purgatory, and Paradise. Through his encounters with historical, mythical, and literary figures, Dante explores themes of sin, redemption, and divine justice. The work is not only a spiritual journey but also a reflection on the human condition and the moral consequences of actions. Its influence on Western literature and thought has been immense, and it remains one of the greatest works in the Italian language.",
      "author_info": "Dante Alighieri was an Italian poet, best known for his epic work 'The Divine Comedy,' which is considered one of the most important literary works of the Middle Ages.",
      "review": "A profound and visionary journey through the afterlife, exploring themes of sin, redemption, and divine justice in one of the most influential literary works ever written."
    },
    {
      "author_name": "Mark Twain",
      "book_name": "Adventures of Huckleberry Finn",
      "price": 10.49,
      "publication_year": 1884,
      "publication_city": "New York",
      "genre": "Classic",
      "description": "'Adventures of Huckleberry Finn' by Mark Twain follows the adventures of a young boy, Huck, as he travels down the Mississippi River with Jim, a runaway slave. The novel critiques the social norms and injustices of the time, particularly with regard to race and freedom. Huck’s journey is a moral one, as he grapples with his own sense of right and wrong in the face of societal expectations. Twain’s humor, vivid characters, and keen social commentary have made this novel one of the most important works of American literature.",
      "author_info": "Mark Twain was an American author and humorist, famous for his novels 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn.' His sharp wit and social commentary made him one of the most influential American writers.",
      "review": "A timeless American classic that explores the themes of freedom, race, and morality with humor and depth. Twain’s writing remains a powerful critique of society."
    },
    {
    "author_name": "Leo Tolstoy",
    "book_name": "Anna Karenina",
    "price": 12.99,
    "publication_year": 1878,
    "publication_city": "Moscow",
    "genre": "Classic",
    "description": "'Anna Karenina' by Leo Tolstoy is a monumental novel that examines the lives of several interconnected characters in 19th-century Russian society. The central plot revolves around Anna, a beautiful and passionate woman who embarks on a tragic affair with Count Vronsky, ultimately leading to her social downfall and personal despair. The novel explores themes of love, infidelity, societal expectations, and the search for meaning in life. Tolstoy’s rich psychological insight into his characters and his depiction of Russian aristocracy make 'Anna Karenina' one of the most important novels in world literature, with a timeless exploration of the human condition.",
    "author_info": "Leo Tolstoy was a Russian author, best known for his novels 'War and Peace' and 'Anna Karenina.' His works explore themes of morality, spirituality, and the complexities of human nature.",
    "review": "A sweeping and emotional narrative that delves deeply into the complexities of love, betrayal, and social pressures. Tolstoy’s brilliance in portraying human nature and the intricacies of Russian society makes this novel a masterpiece."
  },

  {
      "author_name": "Jane Austen",
      "book_name": "Pride and Prejudice",
      "price": 9.99,
      "publication_year": 1813,
      "publication_city": "London",
      "genre": "Romance",
      "description": "'Pride and Prejudice' by Jane Austen is a classic novel that explores the romantic entanglements of Elizabeth Bennet and Mr. Darcy. Set in 19th-century England, the story delves into themes of love, marriage, and social class. Elizabeth, a sharp-witted young woman, initially rejects the proud and wealthy Mr. Darcy, but over time, they both realize their misunderstandings and grow to love each other. Austen's sharp commentary on social norms and her unforgettable characters have made 'Pride and Prejudice' one of the most beloved works in the Romance genre.",
      "author_info": "Jane Austen was an English novelist known for her works exploring themes of love, marriage, and society. Her novels, including 'Pride and Prejudice,' 'Sense and Sensibility,' and 'Emma,' are considered some of the most significant in English literature.",
      "review": "A timeless classic that explores the complexities of love, social expectations, and personal growth. Austen's writing is as sharp and witty as ever."
    },
    {
      "author_name": "Nicholas Sparks",
      "book_name": "The Notebook",
      "price": 8.99,
      "publication_year": 1996,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Notebook' by Nicholas Sparks is a heart-wrenching love story that spans decades. The novel follows Noah and Allie, who fall in love as teenagers but are separated by circumstances. Years later, their paths cross again, and they rekindle their romance. The story explores themes of memory, love, and fate, with an emotional depth that resonates deeply with readers. Sparks’ portrayal of unconditional love and commitment has made 'The Notebook' a modern-day Romance classic.",
      "author_info": "Nicholas Sparks is an American novelist, known for his heartwarming and often tragic love stories, including 'The Notebook,' 'A Walk to Remember,' and 'Dear John.' His novels have been adapted into several successful films.",
      "review": "A beautifully tragic love story that tugs at the heartstrings, exploring themes of memory, loss, and the enduring power of love."
    },
    {
      "author_name": "E.L. James",
      "book_name": "Fifty Shades of Grey",
      "price": 10.99,
      "publication_year": 2011,
      "publication_city": "London",
      "genre": "Romance",
      "description": "'Fifty Shades of Grey' by E.L. James is a contemporary romance that follows the intense and complicated relationship between Anastasia Steele and the wealthy businessman Christian Grey. The novel explores themes of power, control, and desire as the couple navigates their emotionally charged and often controversial bond. James' portrayal of a complex relationship, along with its provocative content, has made 'Fifty Shades of Grey' a global bestseller and a defining work in modern Romance literature.",
      "author_info": "E.L. James is a British author, best known for her 'Fifty Shades' trilogy. Her works have sparked debate due to their explicit content, but they have also attracted a large and dedicated following.",
      "review": "A provocative and controversial love story that dives into the complexities of desire and power dynamics, creating an intense reading experience."
    },
    {
      "author_name": "Julia Quinn",
      "book_name": "The Duke and I",
      "price": 7.49,
      "publication_year": 2000,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Duke and I' by Julia Quinn is a Regency romance that centers around Daphne Bridgerton and Simon Basset, the Duke of Hastings. Their relationship begins as a fake courtship, but soon develops into a passionate love affair. The novel explores themes of love, family, and the societal pressures of 19th-century England. Quinn's witty and charming characters, along with her engaging storytelling, have made 'The Duke and I' a fan-favorite in the Romance genre, particularly among fans of historical fiction.",
      "author_info": "Julia Quinn is an American author known for her historical romance novels, particularly her 'Bridgerton' series, which became widely popular after being adapted into a Netflix series.",
      "review": "A delightful and witty romance full of charm and emotional depth, perfect for fans of historical fiction and love stories."
    },
    {
      "author_name": "Diana Gabaldon",
      "book_name": "Outlander",
      "price": 12.99,
      "publication_year": 1991,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'Outlander' by Diana Gabaldon is a historical romance that blends time travel, adventure, and passion. The novel follows Claire Randall, a 20th-century nurse who is mysteriously transported to 18th-century Scotland, where she becomes entangled in the Jacobite rebellion and falls in love with a dashing Highland warrior named Jamie Fraser. The book explores themes of love, fate, and historical events, with Gabaldon’s intricate world-building and rich characters creating a captivating and immersive experience for readers.",
      "author_info": "Diana Gabaldon is an American author, best known for her 'Outlander' series, which combines historical fiction, romance, and fantasy. The series has been adapted into a successful television show.",
      "review": "An epic and thrilling romance that combines history, adventure, and time travel into a captivating story that will keep readers hooked."
    },
    {
      "author_name": "Nora Roberts",
      "book_name": "Vision in White",
      "price": 9.49,
      "publication_year": 2009,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'Vision in White' by Nora Roberts is the first book in the 'Bride Quartet' series, which revolves around four childhood friends who run a wedding planning business. The novel focuses on Mackensie 'Mac' Elliot, a wedding photographer who falls in love with a man named Carter Maguire. The story explores themes of love, friendship, and commitment, with Roberts’ signature blend of heartwarming romance and humor. 'Vision in White' is perfect for readers who enjoy a mix of romantic tension and lighthearted moments.",
      "author_info": "Nora Roberts is an American author, widely regarded as one of the best-selling romance novelists of all time. Her works often blend romance with suspense, mystery, and elements of family drama.",
      "review": "A sweet and charming romance that also delves into friendship and personal growth, making it a perfect start to a beloved series."
    },
    {
      "author_name": "Stephanie Meyer",
      "book_name": "Twilight",
      "price": 7.99,
      "publication_year": 2005,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'Twilight' by Stephanie Meyer is a supernatural romance that follows Bella Swan, a teenage girl who falls in love with Edward Cullen, a vampire. The novel explores themes of forbidden love, danger, and the complexities of relationships, set against the backdrop of a mysterious small town in Washington. The book became a global sensation, sparking the 'Twilight Saga' and influencing a new generation of paranormal romance fans.",
      "author_info": "Stephanie Meyer is an American author, best known for her 'Twilight Saga,' a series of supernatural romance novels that became a worldwide phenomenon.",
      "review": "A captivating and addictive story of forbidden love, danger, and mystery. 'Twilight' remains one of the most popular paranormal romance novels of the 21st century."
    },
    {
      "author_name": "Jojo Moyes",
      "book_name": "Me Before You",
      "price": 8.49,
      "publication_year": 2012,
      "publication_city": "London",
      "genre": "Romance",
      "description": "'Me Before You' by Jojo Moyes tells the poignant and heart-wrenching story of Louisa Clark, a quirky young woman who becomes a caregiver to Will Traynor, a man who is paralyzed after a tragic accident. The novel explores themes of love, disability, and the power of personal choice, as Louisa and Will’s relationship evolves in unexpected ways. Moyes’ deeply emotional storytelling makes 'Me Before You' a tear-jerker that resonates with readers long after they finish the book.",
      "author_info": "Jojo Moyes is a British novelist, best known for her best-selling novel 'Me Before You,' which explores themes of love, loss, and personal growth.",
      "review": "A beautiful and heart-wrenching story about love, sacrifice, and the choices that define our lives. 'Me Before You' is a modern classic in romantic fiction."
    },
    {
      "author_name": "Kiera Cass",
      "book_name": "The Selection",
      "price": 7.99,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Selection' by Kiera Cass is a dystopian romance set in a future society where the royal family holds a competition to find a wife for the prince. The story follows America Singer, a girl who is selected to compete for Prince Maxon’s affections, despite her feelings for someone else. The novel explores themes of love, class, and societal expectations, as America navigates the challenges of the competition while discovering her true feelings. 'The Selection' has captivated readers with its romantic tension and compelling world-building.",
      "author_info": "Kiera Cass is an American author, best known for her 'Selection' series, which combines romance, dystopian themes, and intrigue.",
      "review": "A thrilling and romantic tale of love, choice, and destiny. Cass creates an intriguing world filled with passion, competition, and emotional growth."
  },
  {
      "author_name": "Sarah J. Maas",
      "book_name": "A Court of Thorns and Roses",
      "price": 9.99,
      "publication_year": 2015,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'A Court of Thorns and Roses' by Sarah J. Maas is a fantasy romance novel that combines elements of classic fairy tales with a dark, gripping narrative. The story follows Feyre Archeron, a young huntress who is taken to the magical land of the Fae after killing a wolf that was actually a faerie in disguise. As Feyre navigates this dangerous world, she finds herself falling in love with Tamlin, a powerful faerie lord. The novel weaves together themes of love, sacrifice, and redemption, set against a backdrop of political intrigue and dangerous magic.",
      "author_info": "Sarah J. Maas is an American author, best known for her 'Throne of Glass' and 'A Court of Thorns and Roses' series. Her works blend fantasy and romance with elements of adventure and personal growth.",
      "review": "A captivating and intense fantasy romance with lush world-building and a passionate love story that will keep readers hooked from beginning to end."
    },
    {
      "author_name": "Rachel Gibson",
      "book_name": "True Confessions",
      "price": 8.99,
      "publication_year": 2008,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'True Confessions' by Rachel Gibson is a contemporary romance that follows the story of True, a former beauty queen who returns to her small hometown to help with a family crisis. There, she reconnects with an old flame, professional baseball player and former bad boy, Derek. The story blends humor, heartache, and passion as True and Derek navigate their rekindled romance while dealing with their own personal demons. Gibson’s engaging writing and the chemistry between the main characters make 'True Confessions' a fun and emotional read.",
      "author_info": "Rachel Gibson is an American author known for her contemporary romance novels. Her books often feature witty dialogue, compelling characters, and heartfelt emotional depth.",
      "review": "A light-hearted and heartwarming romance with a dash of humor and plenty of emotional moments. A perfect choice for readers who enjoy witty banter and second-chance love stories."
    },
    {
      "author_name": "Tessa Dare",
      "book_name": "The Duchess Deal",
      "price": 8.49,
      "publication_year": 2017,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Duchess Deal' by Tessa Dare is a historical romance that follows the story of Emma, a seamstress who agrees to an arranged marriage with the reclusive Duke of Ashbury. The Duke, who was scarred in battle, needs a wife to fulfill his family's legacy, and Emma is the perfect candidate. What begins as a practical arrangement soon turns into a passionate and heartfelt romance as Emma and the Duke discover more about each other. Dare’s witty writing and memorable characters make this a delightful and engaging read.",
      "author_info": "Tessa Dare is an American author of historical romance novels, known for her charming writing and strong, independent heroines. Her books often feature humor, heart, and a great deal of emotional depth.",
      "review": "A fun and steamy historical romance with an endearing couple and a story full of humor, warmth, and surprising depth."
    },
    {
      "author_name": "Katy Regnery",
      "book_name": "The Devil's Spring",
      "price": 9.99,
      "publication_year": 2018,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Devil's Spring' by Katy Regnery is a contemporary romance novel with a suspenseful twist. The story follows Camille, a woman who has been hiding from an abusive past, and Luke, a former bad boy turned successful businessman. When the two are forced to work together, their undeniable chemistry leads to a complicated and passionate romance. Regnery’s writing creates an intense, emotional journey filled with tension and a deep connection between the characters.",
      "author_info": "Katy Regnery is an American author known for her contemporary romance novels. Her works often feature strong characters overcoming personal challenges and finding love in unexpected places.",
      "review": "An intense and emotional romance filled with chemistry, suspense, and unforgettable characters that keep you hooked until the last page."
    },
    {
      "author_name": "Penny Reid",
      "book_name": "Truth or Beard",
      "price": 7.99,
      "publication_year": 2015,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'Truth or Beard' by Penny Reid is a romantic comedy that follows the story of Jessica, who returns to her hometown and gets caught up in an unexpected romance with the bearded and mysterious Beau. The story combines humor, quirky characters, and a heartfelt romance. As Jessica and Beau navigate their feelings for each other, they must also deal with family dynamics, small-town gossip, and the challenges of love in an unexpected place.",
      "author_info": "Penny Reid is an American author who specializes in writing romantic comedies and contemporary romance. Her books are known for their witty dialogue, humor, and well-developed characters.",
      "review": "A hilarious and charming romance full of wit, heart, and the kind of characters you can’t help but root for."
    },
    {
      "author_name": "Samantha Young",
      "book_name": "The Impossible Vastness of Us",
      "price": 8.99,
      "publication_year": 2017,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Impossible Vastness of Us' by Samantha Young is a contemporary romance that tells the story of India, a young woman struggling to adjust to a new life after her mother's remarriage. She meets the charming and enigmatic Finn, and the two embark on an emotional and intense romance. The novel explores themes of family, personal growth, and love as India and Finn navigate their complex emotions and histories. Young’s writing is both poignant and heartwarming, making this a deeply emotional read.",
      "author_info": "Samantha Young is a Scottish author known for her contemporary romance novels. Her books often feature complex characters and emotional journeys, blending romance with personal discovery.",
      "review": "A heartfelt and intense romance that explores love, family, and personal growth with depth and authenticity."
    },
    {
      "author_name": "Christina Lauren",
      "book_name": "The Unhoneymooners",
      "price": 9.49,
      "publication_year": 2019,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Unhoneymooners' by Christina Lauren is a romantic comedy that follows Olive, who is forced to take her twin sister’s honeymoon trip with Ethan, the groom’s brother, after a food poisoning disaster. The two are opposites, but the trip leads to unexpected romance. The book is full of humor, chemistry, and heart, and it explores the dynamics of relationships, both romantic and familial. Christina Lauren’s witty writing and charming characters make this an enjoyable and heartwarming read.",
      "author_info": "Christina Lauren is a writing duo known for their contemporary romance novels. Their books are full of humor, emotional depth, and unforgettable characters.",
      "review": "A hilarious and heartwarming romance with a great mix of humor, chemistry, and emotional moments that keep you turning the pages."
    },
    {
      "author_name": "Lauren Blakely",
      "book_name": "The Sexy One",
      "price": 7.49,
      "publication_year": 2016,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'The Sexy One' by Lauren Blakely is a contemporary romance that follows the story of Charlotte, who finds herself falling for her best friend’s brother, Jake. Their chemistry is undeniable, but they are both hesitant to act on their feelings. The book explores the complications of love, family, and friendship with a perfect blend of humor, heat, and heartfelt moments. Blakely’s ability to craft characters with real emotional depth makes this a fun and engaging read.",
      "author_info": "Lauren Blakely is an American author known for her steamy contemporary romance novels. Her books are full of humor, passion, and emotional connections.",
      "review": "A sizzling and emotional romance with a great balance of humor, heat, and heart that will keep you invested from start to finish."
    },
    {
      "author_name": "Anna Todd",
      "book_name": "After",
      "price": 8.99,
      "publication_year": 2014,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'After' by Anna Todd is a contemporary romance that follows the tumultuous relationship between Tessa Young, an ambitious college student, and Hardin Scott, a rebellious and mysterious bad boy. The story explores themes of love, trust, and emotional vulnerability as Tessa and Hardin navigate their intense and complicated connection. 'After' is filled with drama, passion, and twists, making it a compelling read for fans of romantic fiction.",
      "author_info": "Anna Todd is an American author known for her 'After' series, which began as a fanfiction and became a best-selling book series. Her novels explore themes of love, conflict, and personal growth.",
      "review": "A passionate and dramatic romance that will captivate readers with its emotional intensity and compelling characters."
    },
    {
      "author_name": "Beth O'Leary",
      "book_name": "The Flatshare",
      "price": 7.99,
      "publication_year": 2019,
      "publication_city": "London",
      "genre": "Romance",
      "description": "'The Flatshare' by Beth O'Leary is a contemporary romance that tells the story of Tiffy and Leon, who share a flat but have never met. Due to their unusual living arrangement, their relationship begins through notes and messages left for each other. As they navigate their lives and grow closer, the book explores themes of love, friendship, and the importance of human connection. O'Leary’s charming writing and unique premise make this a heartwarming and delightful romance.",
      "author_info": "Beth O'Leary is a British author known for her contemporary romance novels, which often feature quirky characters and emotional, heartfelt stories.",
      "review": "A charming and heartwarming romance with a unique premise, perfect for readers who enjoy stories about love, connection, and personal growth."
    },
    {
      "author_name": "Colleen Hoover",
      "book_name": "It Ends with Us",
      "price": 9.49,
      "publication_year": 2016,
      "publication_city": "New York",
      "genre": "Romance",
      "description": "'It Ends with Us' by Colleen Hoover is a contemporary romance that follows Lily Bloom, a young woman who falls in love with Ryle Kincaid, a successful neurosurgeon with emotional baggage. As their relationship evolves, Lily must confront the complexities of love, abuse, and self-worth. The novel is both heart-wrenching and empowering, exploring difficult themes with honesty and emotional depth. Hoover’s writing style and her sensitive handling of difficult topics make this an unforgettable and impactful read.",
      "author_info": "Colleen Hoover is an American author known for her emotional and thought-provoking romance novels, including 'It Ends with Us,' 'Verity,' and 'November 9.'",
      "review": "A raw, emotional, and powerful romance that tackles heavy topics with care, making it a must-read for fans of contemporary fiction."
    },
    {
    "author_name": "Jojo Moyes",
    "book_name": "Me Before You",
    "price": 8.99,
    "publication_year": 2012,
    "publication_city": "London",
    "genre": "Romance",
    "description": "'Me Before You' by Jojo Moyes is a poignant and emotional romance that tells the story of Louisa Clark, a young woman who becomes the caregiver for Will Traynor, a man who is paralyzed after a motorcycle accident. As they form an unlikely bond, their lives are transformed in unexpected ways. The novel explores themes of love, loss, and the difficult decisions we must make in life. Moyes’ writing is tender and heartfelt, making this book a deeply moving and unforgettable read.",
    "author_info": "Jojo Moyes is a British author known for her contemporary fiction and romance novels, with 'Me Before You' being one of her most popular works. Her books often explore themes of love, loss, and human connection.",
    "review": "A heart-wrenching and emotionally powerful romance that will stay with you long after you turn the last page."
  },

  {
      "author_name": "Agatha Christie",
      "book_name": "Murder on the Orient Express",
      "price": 9.99,
      "publication_year": 1934,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'Murder on the Orient Express' by Agatha Christie is one of her most famous works, featuring the iconic detective Hercule Poirot. The story takes place on the luxurious train, the Orient Express, where a wealthy passenger is found murdered. Poirot must solve the crime before the train reaches its destination, interviewing a colorful cast of characters. Christie’s signature plot twists and intricate character development make this a classic in the mystery genre.",
      "author_info": "Agatha Christie is an English writer known for her detective novels, particularly those featuring Hercule Poirot and Miss Marple. Her books have sold billions of copies worldwide.",
      "review": "A masterful and captivating mystery with a thrilling plot and an unforgettable conclusion."
    },
    {
      "author_name": "Arthur Conan Doyle",
      "book_name": "The Hound of the Baskervilles",
      "price": 7.99,
      "publication_year": 1902,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'The Hound of the Baskervilles' by Arthur Conan Doyle is one of the most famous Sherlock Holmes mysteries. Set in the eerie moors of Devon, the story centers around the legend of a supernatural hound and the mysterious death of Sir Charles Baskerville. Holmes and Watson investigate the case, uncovering dark secrets and criminal schemes. The novel blends suspense, intrigue, and the sharp intellect of Holmes, making it a landmark in the mystery genre.",
      "author_info": "Arthur Conan Doyle was a British author, best known for creating the detective Sherlock Holmes. His stories have become iconic in both literature and popular culture.",
      "review": "A thrilling, atmospheric mystery with a chilling sense of dread and a brilliant detective at its heart."
    },
    {
      "author_name": "Raymond Chandler",
      "book_name": "The Big Sleep",
      "price": 8.49,
      "publication_year": 1939,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Big Sleep' by Raymond Chandler introduces the hard-boiled detective Philip Marlowe, who is hired by a wealthy man to investigate the blackmail of his two daughters. What follows is a web of corruption, deceit, and murder. Chandler’s sharp prose, complex characters, and intricate plotting make this a definitive work of noir fiction and a must-read in the mystery genre.",
      "author_info": "Raymond Chandler was an American-British novelist and screenwriter, best known for his Philip Marlowe detective stories, which helped define the hard-boiled crime fiction genre.",
      "review": "A fast-paced, gritty detective novel with a complex plot and a protagonist whose cynical, yet principled nature shines through."
    },
    {
      "author_name": "Gillian Flynn",
      "book_name": "Gone Girl",
      "price": 9.49,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'Gone Girl' by Gillian Flynn is a psychological thriller that follows the disappearance of Amy Dunne, and the subsequent investigation that turns her husband Nick into a prime suspect. The novel alternates between Nick’s perspective and Amy’s journal entries, slowly unraveling dark secrets about their marriage. Flynn’s sharp writing and unpredictable twists keep the reader on edge, making 'Gone Girl' a gripping and intense mystery that explores themes of deception and media manipulation.",
      "author_info": "Gillian Flynn is an American author known for her dark psychological thrillers, including 'Gone Girl' and 'Sharp Objects.' Her works often explore the complexities of human relationships and the darker sides of human nature.",
      "review": "A chilling, twist-filled thriller that keeps you guessing until the final page."
    },
    {
      "author_name": "Agatha Christie",
      "book_name": "The Murder of Roger Ackroyd",
      "price": 8.99,
      "publication_year": 1926,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'The Murder of Roger Ackroyd' is one of Agatha Christie’s most groundbreaking works, featuring Hercule Poirot. When Roger Ackroyd is found dead in his study, Poirot investigates, uncovering a complex web of relationships and secrets. The novel’s shocking twist is one of the most famous in detective fiction, making it a seminal work in the genre.",
      "author_info": "Agatha Christie is known as the 'Queen of Crime.' She authored 66 detective novels and 14 short story collections, and her works remain popular worldwide.",
      "review": "A groundbreaking mystery with an unforgettable twist that changed the detective genre forever."
    },
    {
      "author_name": "Tana French",
      "book_name": "In the Woods",
      "price": 9.99,
      "publication_year": 2007,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'In the Woods' by Tana French is a psychological mystery that centers on Detective Rob Ryan, who investigates the murder of a young girl in a small Irish village. As the investigation unfolds, Ryan discovers unsettling connections to his own childhood. French’s atmospheric writing and complex characters elevate the novel, making it a captivating and haunting mystery.",
      "author_info": "Tana French is an Irish author known for her psychological thrillers and literary mysteries, with her debut novel 'In the Woods' receiving widespread acclaim.",
      "review": "A dark and atmospheric mystery with richly developed characters and an eerie sense of foreboding."
    },
    {
      "author_name": "Stieg Larsson",
      "book_name": "The Girl with the Dragon Tattoo",
      "price": 10.49,
      "publication_year": 2005,
      "publication_city": "Stockholm",
      "genre": "Mystery",
      "description": "'The Girl with the Dragon Tattoo' by Stieg Larsson is a gripping mystery that follows journalist Mikael Blomkvist and hacker Lisbeth Salander as they investigate the disappearance of a young woman from a wealthy family decades earlier. The novel combines murder mystery, corporate corruption, and social commentary, making it a complex and thrilling read.",
      "author_info": "Stieg Larsson was a Swedish author and journalist, best known for his 'Millennium' series, which includes 'The Girl with the Dragon Tattoo.' His books have been widely successful worldwide.",
      "review": "A fast-paced, intelligent thriller with unforgettable characters and an intricate, twist-filled plot."
    },
    {
      "author_name": "Michael Connelly",
      "book_name": "The Lincoln Lawyer",
      "price": 8.49,
      "publication_year": 2005,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Lincoln Lawyer' by Michael Connelly introduces Mickey Haller, a defense attorney who operates out of the back of his Lincoln Town Car. When Haller is hired to represent a wealthy client accused of assault, he uncovers a dangerous conspiracy that could put his life at risk. The novel is a fast-paced legal thriller with sharp dialogue and a morally complex protagonist.",
      "author_info": "Michael Connelly is an American author, best known for his legal thrillers and detective novels featuring characters like Harry Bosch and Mickey Haller.",
      "review": "A fast-paced, twisty thriller with a likable, morally complex protagonist and a tightly woven plot."
    },
    {
      "author_name": "James Patterson",
      "book_name": "Along Came a Spider",
      "price": 8.99,
      "publication_year": 1993,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'Along Came a Spider' by James Patterson is the first novel in the Alex Cross series. Cross, a psychologist and detective, is called to investigate the kidnapping of two children from an elite school. As the case unravels, Cross uncovers a much deeper conspiracy. Patterson’s engaging writing and fast-paced plot make this a thrilling mystery.",
      "author_info": "James Patterson is an American author, best known for his crime thrillers and detective novels, particularly the Alex Cross and Women's Murder Club series.",
      "review": "A gripping and fast-paced thriller that introduces a memorable and resourceful protagonist."
    },
    {
      "author_name": "John Grisham",
      "book_name": "The Firm",
      "price": 9.49,
      "publication_year": 1991,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Firm' by John Grisham is a legal thriller that follows Mitch McDeere, a recent law school graduate who accepts a lucrative job at a small but secretive firm in Memphis. Soon, Mitch discovers that the firm is involved in illegal activities, and he must find a way to expose the truth without endangering his life. Grisham’s suspenseful writing and taut plotting make this a classic mystery novel.",
      "author_info": "John Grisham is an American author known for his legal thrillers, many of which have been adapted into films. His books often tackle themes of justice, corruption, and morality.",
      "review": "A fast-paced and suspenseful legal thriller that keeps you on the edge of your seat from beginning to end."
    },
    {
      "author_name": "Dennis Lehane",
      "book_name": "Mystic River",
      "price": 10.99,
      "publication_year": 2001,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'Mystic River' by Dennis Lehane is a powerful mystery that delves into the lives of three childhood friends who are brought back together after one of them is found murdered. The novel explores themes of guilt, justice, and the impact of the past on the present. Lehane’s complex characters and emotionally charged narrative make this a compelling read.",
      "author_info": "Dennis Lehane is an American author known for his mystery and crime novels, including 'Mystic River' and 'Shutter Island.' His books often explore the darker side of human nature.",
      "review": "A haunting and emotionally rich mystery with deep, complex characters and a powerful, tragic narrative."
    },
    {
      "author_name": "Karin Slaughter",
      "book_name": "Pretty Girls",
      "price": 9.99,
      "publication_year": 2015,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'Pretty Girls' by Karin Slaughter is a dark and suspenseful mystery that follows sisters Claire and Lydia, who are forced to confront a tragedy from their past when a series of horrifying events unfold. The book examines deep themes of loss, survival, and betrayal, with shocking twists and an emotional depth that keeps readers on edge.",
      "author_info": "Karin Slaughter is an American author known for her crime thrillers and mysteries. She has been praised for her gritty and emotional storytelling, often exploring dark, complex characters.",
      "review": "A gripping and intense psychological thriller with an unexpected, heart-pounding conclusion."
    },
    {
      "author_name": "Patricia Highsmith",
      "book_name": "Strangers on a Train",
      "price": 8.49,
      "publication_year": 1950,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'Strangers on a Train' by Patricia Highsmith is a classic psychological thriller that revolves around two men, Guy and Bruno, who meet on a train and jokingly discuss swapping murders to get rid of inconvenient people in their lives. When one of them turns the joke into reality, the other becomes entangled in a deadly game. Highsmith’s tension-filled prose and exploration of guilt and obsession make this a standout in the mystery genre.",
      "author_info": "Patricia Highsmith was an American author of psychological thrillers and suspense novels, best known for creating the Tom Ripley series. Her works often explore themes of morality and human nature.",
      "review": "A suspenseful, tautly written thriller that explores the dark psychology of obsession and guilt."
    },
    {
      "author_name": "John le Carré",
      "book_name": "The Spy Who Came in from the Cold",
      "price": 9.49,
      "publication_year": 1963,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'The Spy Who Came in from the Cold' by John le Carré is a Cold War-era espionage thriller that follows Alec Leamas, a disillusioned British intelligence officer tasked with a dangerous mission in East Germany. As the plot unfolds, Leamas is forced to question his loyalties and the true nature of espionage. Le Carré’s intricate plotting and exploration of moral ambiguity make this a masterpiece of spy fiction.",
      "author_info": "John le Carré was a British author best known for his espionage novels, particularly 'The Spy Who Came in from the Cold.' His works often focus on the complexity of intelligence operations and the ethical dilemmas faced by spies.",
      "review": "A chilling and complex Cold War thriller that blurs the lines between loyalty and betrayal."
    },
    {
      "author_name": "Louise Penny",
      "book_name": "Still Life",
      "price": 8.99,
      "publication_year": 2005,
      "publication_city": "Toronto",
      "genre": "Mystery",
      "description": "'Still Life' by Louise Penny is the first book in the Chief Inspector Armand Gamache series. Set in the idyllic village of Three Pines, the story begins with the murder of a beloved local artist. As Gamache investigates, he uncovers dark secrets hidden beneath the surface of this seemingly peaceful community. Penny’s writing is rich with detail, creating a compelling atmosphere of mystery and intrigue.",
      "author_info": "Louise Penny is a Canadian author known for her Chief Inspector Gamache series, which is set in the fictional village of Three Pines. Her books combine engaging mysteries with a deep exploration of human nature.",
      "review": "A beautifully written, atmospheric mystery with a charming protagonist and an intriguing plot."
    },
    {
      "author_name": "James Ellroy",
      "book_name": "The Black Dahlia",
      "price": 9.99,
      "publication_year": 1987,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Black Dahlia' by James Ellroy is a gripping and noir-inspired mystery based on the real-life unsolved murder of Elizabeth Short in Los Angeles in 1947. Two detectives, Bucky Bleichert and Lee Blanchard, investigate the case, uncovering a world of corruption and secrets. Ellroy’s fast-paced prose and exploration of the dark side of post-war America make this a compelling and chilling read.",
      "author_info": "James Ellroy is an American crime writer known for his noir-inspired novels, which often explore dark themes of corruption, crime, and violence in Los Angeles. 'The Black Dahlia' is one of his most famous works.",
      "review": "A gritty, intense, and atmospheric thriller that captures the dark heart of post-war Los Angeles."
    },
    {
      "author_name": "Daphne du Maurier",
      "book_name": "Rebecca",
      "price": 8.99,
      "publication_year": 1938,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'Rebecca' by Daphne du Maurier is a gothic mystery novel that follows an unnamed young woman who marries a wealthy widower, Maxim de Winter. Upon moving to his estate, Manderley, she is haunted by the memory of Rebecca, his first wife. As the narrator unravels the mystery of Rebecca’s life and death, du Maurier weaves a tale of love, jealousy, and suspense with a memorable twist.",
      "author_info": "Daphne du Maurier was an English author known for her gothic and psychological thrillers, particularly 'Rebecca.' Her works often explore themes of memory, identity, and obsession.",
      "review": "A haunting and atmospheric novel that expertly builds tension and intrigue until its dramatic conclusion."
    },
    {
      "author_name": "David Baldacci",
      "book_name": "The Camel Club",
      "price": 8.49,
      "publication_year": 2005,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Camel Club' by David Baldacci follows a group of eccentric individuals who call themselves the Camel Club. The group uncovers a conspiracy involving the U.S. government, which leads them into dangerous situations. Baldacci’s fast-paced narrative and intricate plotting create a suspenseful, action-packed mystery with a touch of humor.",
      "author_info": "David Baldacci is an American author known for his political thrillers and mystery novels. His works often feature protagonists who uncover complex conspiracies.",
      "review": "A thrilling, action-packed mystery with a cast of quirky, memorable characters and a twisting plot."
    },
    {
      "author_name": "Dan Brown",
      "book_name": "The Da Vinci Code",
      "price": 9.99,
      "publication_year": 2003,
      "publication_city": "New York",
      "genre": "Mystery",
      "description": "'The Da Vinci Code' by Dan Brown is a fast-paced mystery that follows symbologist Robert Langdon as he uncovers a secret society and ancient codes hidden within famous works of art. The novel blends historical conspiracy with modern-day thrills, making it one of the best-selling books of all time. Brown’s writing is filled with twists and turns that keep readers hooked.",
      "author_info": "Dan Brown is an American author known for his thriller novels, particularly 'The Da Vinci Code,' which has been adapted into a successful film. His books often explore themes of history, religion, and secret societies.",
      "review": "A gripping, fast-paced thriller with an intricate, twist-filled plot and an explosive conclusion."
    },
    {
      "author_name": "Ruth Ware",
      "book_name": "The Woman in Cabin 10",
      "price": 9.49,
      "publication_year": 2016,
      "publication_city": "London",
      "genre": "Mystery",
      "description": "'The Woman in Cabin 10' by Ruth Ware is a psychological mystery that takes place on a luxury cruise ship. Journalist Lo Blacklock witnesses a woman being thrown overboard from her cabin but finds no trace of the woman or any evidence of the crime. As Lo’s investigation spirals, Ware creates an atmosphere of claustrophobia and tension with a shocking ending.",
      "author_info": "Ruth Ware is a British author known for her psychological thrillers and mysteries, often set in isolated or claustrophobic environments. 'The Woman in Cabin 10' is one of her most popular works.",
      "review": "A tense, atmospheric thriller that builds suspense to a gripping and surprising climax."
    },

    {
      "author_name": "Stephen King",
      "book_name": "The Shining",
      "price": 12.99,
      "publication_year": 1977,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Shining' by Stephen King is a chilling psychological horror novel set in the isolated Overlook Hotel, where Jack Torrance, his wife Wendy, and their son Danny are trapped during the winter. As the hotel’s dark history begins to take hold, Jack descends into madness, and Danny's psychic abilities reveal the horrifying events that occurred in the hotel’s past. King masterfully weaves themes of isolation, madness, and supernatural terror.",
      "author_info": "Stephen King is an American author known for his extensive works in horror, supernatural fiction, and suspense. His works often explore the fragility of the human psyche and the influence of evil forces.",
      "review": "A terrifying psychological horror that masterfully builds tension, with a haunting and unforgettable ending."
    },
    {
      "author_name": "H.P. Lovecraft",
      "book_name": "The Call of Cthulhu",
      "price": 7.99,
      "publication_year": 1928,
      "publication_city": "Providence",
      "genre": "Horror",
      "description": "'The Call of Cthulhu' by H.P. Lovecraft introduces readers to the cosmic horror of Cthulhu, an ancient, malevolent entity that lies dormant beneath the sea. Through the fragmented accounts of several individuals, Lovecraft explores the terror of encountering an incomprehensible, otherworldly force. The story exemplifies Lovecraft’s mastery of creating a sense of existential dread and the insignificance of humanity in the face of the cosmos.",
      "author_info": "H.P. Lovecraft was an American writer known for his creation of the Cthulhu Mythos and his influence on the genre of cosmic horror. His works explore themes of the unknown, forbidden knowledge, and human insignificance.",
      "review": "A seminal work of horror that captures the terror of the unknown and the fragile nature of reality."
    },
    {
      "author_name": "Shirley Jackson",
      "book_name": "The Haunting of Hill House",
      "price": 10.99,
      "publication_year": 1959,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Haunting of Hill House' by Shirley Jackson is a gothic horror novel that tells the story of four people who visit Hill House, a mansion with a dark history, for a study on the supernatural. As strange occurrences mount, the house’s sinister influence takes hold of the group. Jackson’s psychological approach to horror delves deeply into themes of isolation, madness, and the supernatural.",
      "author_info": "Shirley Jackson was an American author known for her works of horror and psychological suspense. Her most famous works include 'The Haunting of Hill House' and 'We Have Always Lived in the Castle.'",
      "review": "A masterful, eerie psychological horror novel that explores the fragility of the human mind and the terror of the unknown."
    },
    {
      "author_name": "Bram Stoker",
      "book_name": "Dracula",
      "price": 9.99,
      "publication_year": 1897,
      "publication_city": "London",
      "genre": "Horror",
      "description": "'Dracula' by Bram Stoker is a classic gothic horror novel that introduced the world to Count Dracula, the vampire who seeks to move from Transylvania to England in order to spread the undead curse. The story is told through letters, diary entries, and newspaper clippings, building a chilling atmosphere of dread and suspense. Stoker’s exploration of immortality, seduction, and terror has made 'Dracula' a foundational work of horror literature.",
      "author_info": "Bram Stoker was an Irish author best known for his classic novel 'Dracula,' which has had a profound impact on vampire lore and the horror genre.",
      "review": "A timeless, atmospheric horror novel that set the standard for vampire fiction and continues to haunt readers."
    },
    {
      "author_name": "Mary Shelley",
      "book_name": "Frankenstein",
      "price": 8.49,
      "publication_year": 1818,
      "publication_city": "London",
      "genre": "Horror",
      "description": "'Frankenstein' by Mary Shelley is a gothic horror novel that tells the tragic tale of Victor Frankenstein, a scientist who creates a monster from body parts. As the creature is abandoned and shunned by society, he becomes increasingly vengeful. Shelley's exploration of unchecked scientific ambition, the nature of humanity, and the consequences of creation make 'Frankenstein' a profound and chilling work of horror.",
      "author_info": "Mary Shelley was an English author, best known for writing 'Frankenstein,' one of the earliest examples of science fiction and gothic horror. Her work explores themes of ambition, ethics, and the supernatural.",
      "review": "A thought-provoking and horrifying exploration of creation, humanity, and the consequences of playing god."
    },
    {
      "author_name": "Stephen King",
      "book_name": "It",
      "price": 14.99,
      "publication_year": 1986,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'It' by Stephen King is a sprawling horror novel set in the small town of Derry, Maine, where a group of children confronts an ancient evil that takes the form of a clown named Pennywise. As the children grow into adults, they must return to face the terror they once escaped. The novel explores themes of fear, friendship, and the power of memory, with King’s characteristic depth and detail.",
      "author_info": "Stephen King is a prolific American author, known for his works in the horror, supernatural fiction, and suspense genres. His books often explore the intersection of ordinary life and extraordinary terror.",
      "review": "An epic and terrifying story that delves deep into childhood fears and the horrors that linger in memory."
    },
    {
      "author_name": "Richard Matheson",
      "book_name": "I Am Legend",
      "price": 7.49,
      "publication_year": 1954,
      "publication_city": "Philadelphia",
      "genre": "Horror",
      "description": "'I Am Legend' by Richard Matheson is a post-apocalyptic horror novel about Robert Neville, the last human survivor of a world overtaken by a vampiric plague. As Neville struggles to stay alive, he realizes that his enemies may no longer be the monsters he thought, but something much more human. Matheson’s novel has had a profound influence on the zombie and vampire genres, exploring themes of survival, isolation, and the nature of humanity.",
      "author_info": "Richard Matheson was an American author, primarily of horror, science fiction, and fantasy. His works often explore themes of the supernatural and psychological horror.",
      "review": "A chilling and thought-provoking tale of isolation, survival, and the definition of humanity in a post-apocalyptic world."
    },
    {
      "author_name": "Clive Barker",
      "book_name": "The Hellbound Heart",
      "price": 9.99,
      "publication_year": 1986,
      "publication_city": "London",
      "genre": "Horror",
      "description": "'The Hellbound Heart' by Clive Barker is the novel that inspired the iconic horror film series 'Hellraiser.' The story follows Frank, a man who opens a mysterious puzzle box and is torn apart by demonic beings called the Cenobites. As he seeks to escape their torment, the story delves into themes of desire, pain, and the boundaries between pleasure and suffering.",
      "author_info": "Clive Barker is an English author and filmmaker known for his works of horror, dark fantasy, and the creation of the 'Hellraiser' series. His writing often explores the intersection of pain, pleasure, and the supernatural.",
      "review": "A dark and visceral horror novel that explores the darker sides of desire and torment, with unforgettable imagery."
    },
    {
      "author_name": "Joe Hill",
      "book_name": "Heart-Shaped Box",
      "price": 8.99,
      "publication_year": 2007,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'Heart-Shaped Box' by Joe Hill follows Judas Coyne, a former rock star who buys a haunted suit from an auction site. The suit comes with a ghostly presence, and soon, Coyne’s life is turned into a nightmare as he is pursued by the vengeful spirit. Hill’s debut novel is a chilling, modern horror story with emotional depth and psychological horror elements.",
      "author_info": "Joe Hill is an American author known for his works of horror, fantasy, and suspense. He is the son of Stephen King and has carved out his own niche in the genre with works like 'Heart-Shaped Box.'",
      "review": "A suspenseful, eerie debut novel that blends traditional horror with deep emotional and psychological tension."
    },
    {
      "author_name": "Dean Koontz",
      "book_name": "Phantoms",
      "price": 8.49,
      "publication_year": 1983,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'Phantoms' by Dean Koontz is a supernatural horror novel set in the small town of Snowfield, California, where a mysterious and deadly force begins killing off the residents. As survivors band together to investigate the cause, they uncover terrifying truths about the force’s origins. Koontz’s atmospheric and fast-paced storytelling creates an unforgettable sense of fear and dread.",
      "author_info": "Dean Koontz is an American author known for his horror, thriller, and suspense novels. His works often feature characters confronting both supernatural and psychological terror.",
      "review": "A thrilling and eerie novel that blends supernatural horror with fast-paced suspense, keeping readers on edge until the very end."
    },
    {
      "author_name": "Richard Laymon",
      "book_name": "The Cellar",
      "price": 9.49,
      "publication_year": 1980,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Cellar' by Richard Laymon is a brutal and terrifying horror novel about a group of teenagers who encounter an enigmatic man and his sinister secrets hidden in the cellar of his home. The novel explores themes of fear, evil, and the human capacity for violence. Laymon's fast-paced and shocking storytelling will keep readers on the edge of their seats.",
      "author_info": "Richard Laymon was an American author known for his visceral and disturbing horror novels. His works often feature graphic violence, dark humor, and psychological terror.",
      "review": "A fast-paced and disturbing horror story that will leave readers questioning the nature of evil."
    },
    {
      "author_name": "Joe Hill",
      "book_name": "Horns",
      "price": 9.99,
      "publication_year": 2010,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'Horns' by Joe Hill is a supernatural horror novel that follows Ignatius “Ig” Perrish, who, after the mysterious death of his girlfriend Merrin, wakes up one morning to find horns growing from his head. As he tries to uncover the truth about her death, he discovers that the horns give him strange powers that compel others to confess their darkest secrets. Hill blends horror with dark humor and emotional depth.",
      "author_info": "Joe Hill is an American author known for his horror, fantasy, and suspense works. He is the son of Stephen King and has earned critical acclaim for his writing.",
      "review": "A unique blend of horror and dark humor, with a gripping and original storyline that will captivate readers."
    },
    {
      "author_name": "Stephen King",
      "book_name": "Carrie",
      "price": 8.49,
      "publication_year": 1974,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'Carrie' by Stephen King is the story of a shy, bullied high school girl who discovers she has telekinetic powers. As Carrie’s powers grow, so does her anger, leading to a tragic and violent climax at her high school prom. King’s exploration of social isolation, bullying, and the consequences of cruelty makes 'Carrie' a powerful and disturbing horror novel.",
      "author_info": "Stephen King is a renowned American author whose works in horror, supernatural fiction, and suspense have made him a household name. His books often explore the darker sides of human nature.",
      "review": "A gripping and tragic tale of supernatural power and revenge that has become a horror classic."
    },
    {
      "author_name": "David Wong",
      "book_name": "John Dies at the End",
      "price": 7.99,
      "publication_year": 2004,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'John Dies at the End' by David Wong is a bizarre and darkly comic horror novel that follows two friends, John and Dave, as they encounter strange events after using a mysterious drug. The drug allows them to experience a world of supernatural horrors and alternate realities. Wong’s unique blend of absurdity, humor, and terror creates a wildly entertaining and unsettling read.",
      "author_info": "David Wong is the pseudonym of Jason Pargin, an American author best known for his horror-comedy novels. His works blend dark humor with supernatural horror and often tackle themes of reality and identity.",
      "review": "A hilarious and unnerving blend of horror, dark comedy, and mind-bending twists that keeps you guessing until the very end."
    },
    {
      "author_name": "John Ajvide Lindqvist",
      "book_name": "Let the Right One In",
      "price": 10.99,
      "publication_year": 2004,
      "publication_city": "Stockholm",
      "genre": "Horror",
      "description": "'Let the Right One In' by John Ajvide Lindqvist is a haunting and tragic vampire horror novel about a young boy named Oskar, who befriends a mysterious girl named Eli, who turns out to be a centuries-old vampire. The novel explores themes of loneliness, childhood, and the brutal nature of the supernatural. Lindqvist’s atmospheric storytelling creates a chilling and deeply emotional narrative.",
      "author_info": "John Ajvide Lindqvist is a Swedish author known for his dark and atmospheric horror novels. His works often explore themes of loneliness, violence, and the supernatural.",
      "review": "A deeply moving and terrifying tale of friendship, love, and the monstrous nature of the supernatural."
    },
    {
      "author_name": "Bentley Little",
      "book_name": "The Store",
      "price": 8.49,
      "publication_year": 1998,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Store' by Bentley Little is a psychological horror novel set in a small town where a new mega-store opens, bringing with it an oppressive atmosphere and strange, sinister occurrences. As the store’s influence spreads, it begins to consume the town and its residents. Little’s novel delves into the fear of commercialism and the power of societal conformity, blending horror with social commentary.",
      "author_info": "Bentley Little is an American author known for his horror novels, often involving everyday settings with an unsettling and supernatural twist.",
      "review": "A chilling critique of consumerism, with an eerie, suspense-filled narrative that builds to a terrifying conclusion."
    },
    {
      "author_name": "Ramsey Campbell",
      "book_name": "The Influence",
      "price": 9.49,
      "publication_year": 1988,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Influence' by Ramsey Campbell is a psychological horror novel about a man named Lewis who moves into a new home, only to discover that his neighbors are involved in dark and sinister rituals. The novel explores themes of power, manipulation, and fear, with Campbell’s skillful narrative building a sense of unease and tension throughout.",
      "author_info": "Ramsey Campbell is a British author known for his psychological horror novels. His works often deal with themes of isolation, fear, and the human mind’s fragility.",
      "review": "A slow-burning and disturbing psychological horror novel that keeps readers on edge, filled with dread and tension."
    },
    {
      "author_name": "Caitlín R. Kiernan",
      "book_name": "The Drowning Girl",
      "price": 11.99,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Drowning Girl' by Caitlín R. Kiernan is a gothic horror novel about a young woman named Imp, who is haunted by memories of a girl who drowned. As Imp’s reality begins to unravel, the line between memory and madness blurs, and she must confront the ghosts of her past. Kiernan’s atmospheric writing and exploration of grief, loss, and the supernatural creates a haunting and immersive story.",
      "author_info": "Caitlín R. Kiernan is an American author known for her dark fantasy and horror works. Her stories often focus on psychological horror, with themes of grief, loss, and obsession.",
      "review": "A beautifully written and deeply unsettling novel that explores themes of loss, madness, and the supernatural in a haunting and poetic way."
    },
    {
      "author_name": "Paul Tremblay",
      "book_name": "The Cabin at the End of the World",
      "price": 13.49,
      "publication_year": 2018,
      "publication_city": "New York",
      "genre": "Horror",
      "description": "'The Cabin at the End of the World' by Paul Tremblay is a psychological horror novel about a family vacationing at a remote cabin, who are taken hostage by four strangers with a terrifying ultimatum. The novel explores themes of love, trust, and sacrifice, with Tremblay’s masterful tension building creating an atmosphere of dread and uncertainty.",
      "author_info": "Paul Tremblay is an American author known for his works of horror and psychological suspense. His books often explore the fragility of the human mind and the consequences of fear and isolation.",
      "review": "A tense, nerve-wracking thriller that blends psychological horror with deep emotional resonance, keeping readers on the edge of their seats."
    },

    {
      "author_name": "Ken Follett",
      "book_name": "The Pillars of the Earth",
      "price": 12.99,
      "publication_year": 1989,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Pillars of the Earth' by Ken Follett is a sweeping historical epic set in 12th-century England. The novel focuses on the construction of a cathedral in the fictional town of Kingsbridge, amid political intrigue, war, and religious conflict. Through its rich tapestry of characters, it explores the lives of commoners and nobles alike, with themes of power, ambition, and love.",
      "author_info": "Ken Follett is a Welsh author best known for his historical fiction novels. His works often explore complex political and historical events, blending detailed settings with gripping stories.",
      "review": "An enthralling historical saga that will immerse readers in its intricate characters and dramatic events."
    },
    {
      "author_name": "Hilary Mantel",
      "book_name": "Wolf Hall",
      "price": 14.99,
      "publication_year": 2009,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'Wolf Hall' by Hilary Mantel is a gripping historical novel set during the reign of King Henry VIII. The story follows Thomas Cromwell, the king’s advisor, as he navigates the treacherous world of Tudor politics. Mantel’s masterful prose and deep character exploration make this an unforgettable portrayal of power, ambition, and betrayal.",
      "author_info": "Hilary Mantel is an English author known for her historical fiction works, particularly those set in Tudor England. Her books often explore the lives of historical figures in a detailed and insightful manner.",
      "review": "A powerful and atmospheric portrayal of Tudor England, with a nuanced and complex protagonist in Thomas Cromwell."
    },
    {
      "author_name": "Allan Massie",
      "book_name": "The Roman Quintet",
      "price": 10.99,
      "publication_year": 1990,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Roman Quintet' by Allan Massie is a collection of five novels set in the time of Ancient Rome, focusing on different aspects of Roman life and history. Each book offers a unique perspective, from the political intrigues of the Republic to the personal struggles of individuals during the Empire. Massie’s series provides a compelling and immersive journey into the heart of Roman civilization.",
      "author_info": "Allan Massie is a Scottish author known for his historical fiction novels. His works often explore ancient history and delve into the lives of significant historical figures.",
      "review": "An excellent series that brings Ancient Rome to life with richly developed characters and historically accurate details."
    },
    {
      "author_name": "Margaret George",
      "book_name": "The Autobiography of Henry VIII",
      "price": 13.49,
      "publication_year": 1991,
      "publication_city": "New York",
      "genre": "Historical Fiction",
      "description": "'The Autobiography of Henry VIII' by Margaret George presents the life story of the notorious English king through his own voice. Set against the backdrop of 16th-century England, the novel offers a deeply personal perspective on Henry’s marriages, political machinations, and his complicated character. George’s portrayal of Henry is both humanizing and richly detailed.",
      "author_info": "Margaret George is an American author known for her historical fiction novels. Her books often focus on famous historical figures and provide a fictionalized account of their lives.",
      "review": "A captivating and detailed historical novel that brings the infamous Henry VIII to life through an intimate and compelling narrative."
    },
    {
      "author_name": "Philippa Gregory",
      "book_name": "The Other Boleyn Girl",
      "price": 12.99,
      "publication_year": 2001,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Other Boleyn Girl' by Philippa Gregory tells the story of Mary Boleyn, the sister of Anne Boleyn, who was the mistress of King Henry VIII before Anne’s rise to power. The novel focuses on Mary’s emotional and political struggles within the tumultuous court of Henry VIII and her relationship with her ambitious sister. Gregory’s portrayal of the Boleyn sisters is both dramatic and vivid.",
      "author_info": "Philippa Gregory is an English author known for her historical fiction novels. She often writes about the lives of women in history, particularly those in royal circles.",
      "review": "A compelling and richly told story of ambition, love, and rivalry set against the backdrop of Tudor England."
    },
    {
      "author_name": "Bernard Cornwell",
      "book_name": "The Last Kingdom",
      "price": 11.49,
      "publication_year": 2004,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Last Kingdom' by Bernard Cornwell is the first book in the Saxon Stories series. It follows Uhtred, a young Saxon nobleman who is captured and raised by Vikings. As he navigates the tumultuous political landscape of 9th-century England, Uhtred must choose between loyalty to his Saxon heritage and his Viking upbringing. Cornwell’s action-packed writing and historical detail create a gripping tale of warfare and betrayal.",
      "author_info": "Bernard Cornwell is an English author known for his historical fiction novels, particularly those set in the medieval and Viking eras. His works are known for their detailed historical accuracy and fast-paced storytelling.",
      "review": "A thrilling and action-packed story that immerses readers in the world of Saxon England and Viking invasions."
    },
    {
      "author_name": "Tatiana de Rosnay",
      "book_name": "Sarah’s Key",
      "price": 9.99,
      "publication_year": 2006,
      "publication_city": "Paris",
      "genre": "Historical Fiction",
      "description": "'Sarah’s Key' by Tatiana de Rosnay is a heartbreaking novel that intertwines the stories of a young Jewish girl, Sarah, who is taken away during the Vel' d'Hiv Roundup in Nazi-occupied France, and a modern-day journalist, Julia Jarmond, who is investigating the historical event. The novel explores themes of memory, guilt, and the long-lasting effects of history on the present.",
      "author_info": "Tatiana de Rosnay is a French author whose works often explore themes of history, memory, and identity. Her books have been translated into several languages and are widely read around the world.",
      "review": "A moving and thought-provoking story that examines the impact of historical events on individuals and their families."
    },
    {
      "author_name": "Ken Follett",
      "book_name": "World Without End",
      "price": 13.99,
      "publication_year": 2007,
      "publication_city": "New York",
      "genre": "Historical Fiction",
      "description": "'World Without End' by Ken Follett is the sequel to 'The Pillars of the Earth,' set two centuries later in the same fictional town of Kingsbridge. The novel follows a new generation of characters as they navigate war, plague, and political strife in 14th-century England. Follett once again crafts a compelling story of love, ambition, and survival in a turbulent period of history.",
      "author_info": "Ken Follett is a Welsh author who has written many bestselling historical fiction novels. His books are known for their richly detailed historical settings and intricate plots.",
      "review": "A captivating historical epic that continues the story of Kingsbridge with compelling characters and thrilling events."
    },
    {
      "author_name": "Kate Morton",
      "book_name": "The Forgotten Garden",
      "price": 10.49,
      "publication_year": 2008,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Forgotten Garden' by Kate Morton is a multi-layered historical fiction novel that spans several generations. The story follows Nell, a woman who discovers a mysterious garden and a hidden family secret, and her granddaughter, Cassandra, who unravels the truth about their past. Morton’s novel is filled with intrigue, family drama, and the exploration of loss and identity.",
      "author_info": "Kate Morton is an Australian author known for her historical fiction novels. Her works often revolve around family secrets, mysteries, and the passage of time.",
      "review": "A beautifully written and atmospheric story that keeps readers guessing with its intricate plot and compelling characters."
    },
    {
      "author_name": "Edward Rutherfurd",
      "book_name": "London",
      "price": 15.99,
      "publication_year": 1997,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'London' by Edward Rutherfurd is an epic historical novel that traces the history of the city of London from its Roman beginnings to the present day. The novel follows the lives of several families whose fates intertwine over the centuries, giving readers a vivid portrayal of the city’s evolution and the key historical events that shaped it.",
      "author_info": "Edward Rutherfurd is an English author known for his historical fiction novels that span centuries of history. His books often focus on the history of cities or regions and the people who lived there.",
      "review": "An ambitious and richly detailed historical saga that brings the history of London to life through its memorable characters and sweeping narrative."
    },
    {
      "author_name": "Isabel Allende",
      "book_name": "The House of the Spirits",
      "price": 12.49,
      "publication_year": 1982,
      "publication_city": "Santiago",
      "genre": "Historical Fiction",
      "description": "'The House of the Spirits' by Isabel Allende is a family saga set in Chile, spanning several generations. The novel blends historical events with magical realism, following the Trueba family as they navigate political unrest, love, and betrayal. Allende’s storytelling creates a vivid portrait of Chile’s tumultuous history and the personal lives of those caught in its wake.",
      "author_info": "Isabel Allende is a Chilean-American author known for her works of historical fiction and magical realism. Her novels often explore themes of family, memory, and political change.",
      "review": "A captivating and beautifully written tale of love, politics, and the intertwining of personal and national histories."
    },
    {
      "author_name": "Louis de Bernières",
      "book_name": "Birds Without Wings",
      "price": 11.49,
      "publication_year": 2004,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'Birds Without Wings' by Louis de Bernières is a historical novel set in the final years of the Ottoman Empire. The story follows the lives of the people in a small Turkish village as they are swept up in the events of war, nationalism, and social change. De Bernières combines humor, tragedy, and richly drawn characters to create a powerful and poignant narrative.",
      "author_info": "Louis de Bernières is an English author known for his historical fiction novels. His works often explore themes of war, love, and the complexities of human relationships.",
      "review": "A richly layered and emotionally powerful novel that explores the impact of history on ordinary lives."
    },
    {
      "author_name": "Aminatta Forna",
      "book_name": "The Memory of Love",
      "price": 11.99,
      "publication_year": 2010,
      "publication_city": "London",
      "genre": "Historical Fiction",
      "description": "'The Memory of Love' by Aminatta Forna is set against the backdrop of Sierra Leone’s civil war. The novel explores the lives of two men, a psychiatrist and a former soldier, whose fates become intertwined as they grapple with their own traumatic pasts. Forna’s writing is intimate and thought-provoking, providing a deeply human exploration of love, loss, and the scars of war.",
      "author_info": "Aminatta Forna is a Sierra Leonean-British author known for her works that explore themes of war, memory, and identity. Her books often focus on the intersection of personal lives and historical events.",
      "review": "A beautifully crafted and poignant exploration of the lasting impact of war on individuals and societies."
    },
    {
      "author_name": "Colleen McCullough",
      "book_name": "The Thorn Birds",
      "price": 10.99,
      "publication_year": 1977,
      "publication_city": "Sydney",
      "genre": "Historical Fiction",
      "description": "'The Thorn Birds' by Colleen McCullough is an epic family saga set in the Australian Outback, spanning several decades. The novel follows the Cleary family, particularly the forbidden love between Meggie Cleary and a Catholic priest. McCullough’s vivid portrayal of life in Australia, combined with the dramatic themes of love, faith, and tragedy, has made 'The Thorn Birds' a beloved classic.",
      "author_info": "Colleen McCullough was an Australian author best known for her historical fiction novels. She explored themes of family, love, and the complexities of human nature in her works.",
      "review": "A timeless and emotionally powerful story of forbidden love, family, and sacrifice set in the Australian wilderness."
    },

    {
      "author_name": "George Orwell",
      "book_name": "1984",
      "price": 12.99,
      "publication_year": 1949,
      "publication_city": "London",
      "genre": "Dystopian",
      "description": "'1984' by George Orwell is a chilling dystopian novel set in a totalitarian society where the government, led by Big Brother, exerts complete control over every aspect of citizens' lives. The protagonist, Winston Smith, rebels against the oppressive regime but finds himself caught in a web of surveillance, propaganda, and ideological manipulation. Orwell’s novel remains a powerful critique of authoritarianism and the loss of individual freedom.",
      "author_info": "George Orwell was an English author and journalist, known for his works critiquing totalitarian regimes and social injustice. His most famous works include '1984' and 'Animal Farm.'",
      "review": "A masterful and terrifying portrayal of totalitarianism and its dehumanizing effects on society."
    },
    {
      "author_name": "Aldous Huxley",
      "book_name": "Brave New World",
      "price": 13.49,
      "publication_year": 1932,
      "publication_city": "London",
      "genre": "Dystopian",
      "description": "'Brave New World' by Aldous Huxley is set in a future society where humanity has achieved apparent peace and happiness through scientific control, genetic engineering, and mind-altering drugs. However, beneath this utopian facade, the novel explores the cost of individual freedom and emotional depth. Huxley’s dark vision warns of a world where technology erodes human connection and autonomy.",
      "author_info": "Aldous Huxley was an English writer and philosopher, renowned for his dystopian novel 'Brave New World.' His works often explore themes of social control, human nature, and the consequences of scientific advancement.",
      "review": "A haunting vision of a future where individuality is sacrificed for superficial happiness and conformity."
    },
    {
      "author_name": "Ray Bradbury",
      "book_name": "Fahrenheit 451",
      "price": 11.99,
      "publication_year": 1953,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'Fahrenheit 451' by Ray Bradbury depicts a future society where books are banned and 'firemen' burn any that are found. The protagonist, Guy Montag, is a fireman who begins to question his role in this oppressive world and seeks knowledge and personal freedom. Bradbury’s novel is a powerful commentary on censorship, conformity, and the importance of literature and independent thought.",
      "author_info": "Ray Bradbury was an American author known for his works of science fiction and dystopian fiction, particularly 'Fahrenheit 451.' His writing often addresses themes of censorship, technology, and the human condition.",
      "review": "A thought-provoking and timely exploration of censorship, individuality, and the dangers of mass conformity."
    },
    {
      "author_name": "Margaret Atwood",
      "book_name": "The Handmaid’s Tale",
      "price": 14.99,
      "publication_year": 1985,
      "publication_city": "Toronto",
      "genre": "Dystopian",
      "description": "'The Handmaid’s Tale' by Margaret Atwood is set in the near future in the totalitarian society of Gilead, where women have been stripped of their rights and forced into rigid roles. The protagonist, Offred, is a Handmaid whose sole purpose is to bear children for the ruling class. Atwood’s novel explores themes of patriarchy, power, and the subjugation of women.",
      "author_info": "Margaret Atwood is a Canadian author renowned for her works of fiction, particularly dystopian novels. Her works often examine themes of gender, power, and social justice.",
      "review": "A chilling and thought-provoking exploration of oppression, patriarchy, and the resilience of the human spirit."
    },
    {
      "author_name": "Suzanne Collins",
      "book_name": "The Hunger Games",
      "price": 11.49,
      "publication_year": 2008,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'The Hunger Games' by Suzanne Collins is set in a future society called Panem, where a brutal annual event forces children from each district to fight to the death in a televised spectacle. The protagonist, Katniss Everdeen, volunteers to take her sister’s place in the Games and becomes a symbol of resistance against the oppressive government. Collins’ novel explores themes of survival, sacrifice, and social inequality.",
      "author_info": "Suzanne Collins is an American author best known for her dystopian series 'The Hunger Games.' Her works often deal with themes of survival, power, and rebellion in oppressive societies.",
      "review": "A gripping and intense tale of survival, resistance, and the cost of rebellion in a dystopian world."
    },
    {
      "author_name": "Veronica Roth",
      "book_name": "Divergent",
      "price": 12.49,
      "publication_year": 2011,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'Divergent' by Veronica Roth is set in a future society divided into factions based on personality traits. The protagonist, Beatrice (Tris), discovers she is 'Divergent,' meaning she does not fit neatly into any one faction. As she uncovers dark secrets about the government and its control over the population, Tris must decide where her true loyalty lies. Roth’s novel explores themes of identity, power, and the dangers of rigid societal structures.",
      "author_info": "Veronica Roth is an American author best known for her dystopian 'Divergent' series. Her works often focus on themes of identity, rebellion, and social structures.",
      "review": "A thrilling and thought-provoking story that explores the struggle for individuality in a highly controlled society."
    },
    {
      "author_name": "Philip K. Dick",
      "book_name": "Do Androids Dream of Electric Sheep?",
      "price": 13.49,
      "publication_year": 1968,
      "publication_city": "Philadelphia",
      "genre": "Dystopian",
      "description": "'Do Androids Dream of Electric Sheep?' by Philip K. Dick is set in a post-apocalyptic future where Earth is in decline and androids are indistinguishable from humans. The protagonist, Rick Deckard, is tasked with hunting down and 'retiring' rogue androids. Dick’s novel explores questions of humanity, consciousness, and the ethics of artificial intelligence, making it a thought-provoking dystopian classic.",
      "author_info": "Philip K. Dick was an American writer known for his science fiction works, particularly those exploring themes of identity, reality, and technology.",
      "review": "A mind-bending and philosophical exploration of what it means to be human in a world increasingly dominated by artificial intelligence."
    },
    {
      "author_name": "Octavia Butler",
      "book_name": "Parable of the Sower",
      "price": 14.49,
      "publication_year": 1993,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'Parable of the Sower' by Octavia Butler is set in a near-future America ravaged by climate change, economic collapse, and societal breakdown. The protagonist, Lauren Olamina, has a rare ability to feel the pain of others and creates a new belief system called Earthseed. Butler’s novel is a powerful exploration of survival, hope, and the potential for change in the face of collapse.",
      "author_info": "Octavia Butler was an American science fiction writer known for her exploration of race, gender, and social issues. Her works often delve into dystopian futures and the complexities of human nature.",
      "review": "A profound and thought-provoking dystopian novel that blends social critique with a gripping narrative of survival and hope."
    },
    {
      "author_name": "Koushun Takami",
      "book_name": "Battle Royale",
      "price": 15.99,
      "publication_year": 1999,
      "publication_city": "Tokyo",
      "genre": "Dystopian",
      "description": "'Battle Royale' by Koushun Takami is set in a dystopian future where the Japanese government forces a class of students to participate in a deadly televised game of survival. The novel explores themes of violence, fear, and the human instinct for survival, while also delving into the psychological toll of the brutal event on the participants.",
      "author_info": "Koushun Takami is a Japanese author best known for his dystopian novel 'Battle Royale.' His works often explore themes of survival, society, and human nature in extreme circumstances.",
      "review": "A gripping, violent, and thought-provoking novel that examines the lengths people will go to in order to survive in a dystopian world."
    },
    {
      "author_name": "Ruth Ozeki",
      "book_name": "A Tale for the Time Being",
      "price": 13.99,
      "publication_year": 2013,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'A Tale for the Time Being' by Ruth Ozeki is a novel that blends elements of dystopian fiction with literary exploration. It tells the story of Nao, a Japanese teenager who writes in a journal, and Ruth, a writer in Canada who finds the journal. The novel explores themes of time, identity, and the effects of global crises on personal lives.",
      "author_info": "Ruth Ozeki is a Japanese-American author known for her unique blend of fiction that often explores themes of time, memory, and identity.",
      "review": "A deeply layered novel that intertwines personal and societal struggles, examining the impact of dystopian themes on individuals."
    },
    {
      "author_name": "John Wyndham",
      "book_name": "The Day of the Triffids",
      "price": 10.99,
      "publication_year": 1951,
      "publication_city": "London",
      "genre": "Dystopian",
      "description": "'The Day of the Triffids' by John Wyndham is a classic post-apocalyptic novel set in a world where a strange meteor shower blinds most of humanity. Amid the chaos, a deadly species of plant, the Triffids, begins to attack the survivors. Wyndham’s novel explores themes of survival, human nature, and societal collapse.",
      "author_info": "John Wyndham was an English science fiction writer known for his works that explore themes of disaster, survival, and the end of civilization.",
      "review": "A chilling and suspenseful post-apocalyptic tale that explores human vulnerability and the threat of a changing world."
    },
    {
      "author_name": "Louis-Sébastien Mercier",
      "book_name": "Memoirs of the Year 2500",
      "price": 13.49,
      "publication_year": 1771,
      "publication_city": "Paris",
      "genre": "Dystopian",
      "description": "'Memoirs of the Year 2500' by Louis-Sébastien Mercier is an early example of dystopian literature. Set in the future, it imagines a world where technology and social systems have drastically changed. The novel offers a critique of contemporary society, predicting both the benefits and dangers of progress.",
      "author_info": "Louis-Sébastien Mercier was a French author known for his early dystopian works, which often critiqued social and political structures.",
      "review": "A visionary work that offers an early glimpse of the potential pitfalls of progress and technological change."
    },
    {
      "author_name": "M.T. Anderson",
      "book_name": "Feed",
      "price": 12.99,
      "publication_year": 2002,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'Feed' by M.T. Anderson is set in a future where people are constantly connected to the internet through brain implants known as 'feeds.' The novel follows Titus and his friends as they navigate a world where consumerism and corporate control dominate every aspect of life. Anderson’s novel is a sharp critique of technology, consumer culture, and the loss of individual thought.",
      "author_info": "M.T. Anderson is an American author known for his works in young adult literature, particularly dystopian fiction. His novels often address themes of technology, society, and individual autonomy.",
      "review": "A chilling and thought-provoking examination of a future where technology erodes personal freedom and critical thought."
    },
    {
      "author_name": "Lauren Oliver",
      "book_name": "Delirium",
      "price": 13.49,
      "publication_year": 2011,
      "publication_city": "New York",
      "genre": "Dystopian",
      "description": "'Delirium' by Lauren Oliver is set in a world where love is considered a disease, and citizens undergo a procedure to have their emotions 'cured.' The protagonist, Lena, is set to undergo the procedure but begins to question the society’s beliefs when she falls in love. The novel explores themes of love, control, and the impact of emotion on humanity.",
      "author_info": "Lauren Oliver is an American author known for her dystopian novels, particularly 'Delirium,' which explore themes of love, government control, and the human experience.",
      "review": "A captivating and emotional exploration of love, freedom, and the consequences of living in a society that seeks to eliminate both."
    },
    {
      "author_name": "Kazuo Ishiguro",
      "book_name": "Never Let Me Go",
      "price": 14.99,
      "publication_year": 2005,
      "publication_city": "London",
      "genre": "Dystopian",
      "description": "'Never Let Me Go' by Kazuo Ishiguro is set in a dystopian world where clones are bred for the sole purpose of donating their organs. The novel follows Kathy, Tommy, and Ruth as they confront the truth of their existence and the meaning of their lives. Ishiguro’s novel is a poignant exploration of identity, loss, and the ethical implications of cloning.",
      "author_info": "Kazuo Ishiguro is a British author known for his works that often explore themes of memory, identity, and the human condition. His novel 'Never Let Me Go' was adapted into a critically acclaimed film.",
      "review": "A hauntingly beautiful exploration of love, humanity, and the ethical questions surrounding cloning and organ donation."
    },

    {
      "author_name": "Malcolm Gladwell",
      "book_name": "Outliers: The Story of Success",
      "price": 16.99,
      "publication_year": 2008,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Outliers: The Story of Success' by Malcolm Gladwell explores the factors that contribute to high levels of success. Gladwell challenges the traditional notion of the self-made individual, showing that success is often a product of cultural background, timing, and opportunity. Using case studies ranging from sports to business, he argues that success is shaped by a combination of innate ability, hard work, and external factors.",
      "author_info": "Malcolm Gladwell is a Canadian journalist and author known for his best-selling books on social science, including 'The Tipping Point' and 'Outliers.' His work focuses on psychology, sociology, and behavioral economics.",
      "review": "An insightful exploration of the unseen factors that contribute to extraordinary success, challenging common assumptions."
    },
    {
      "author_name": "Yuval Noah Harari",
      "book_name": "Sapiens: A Brief History of Humankind",
      "price": 18.99,
      "publication_year": 2014,
      "publication_city": "Tel Aviv",
      "genre": "Non-fiction",
      "description": "'Sapiens: A Brief History of Humankind' by Yuval Noah Harari takes readers on a journey through the history of humankind, from the emergence of Homo sapiens in prehistoric times to the present day. Harari examines the ways in which humans have shaped the world, discussing agriculture, empire-building, capitalism, and the scientific revolution. The book explores the evolution of human society and culture, providing deep insights into our past and future.",
      "author_info": "Yuval Noah Harari is an Israeli historian and author, best known for his works 'Sapiens' and 'Homo Deus.' He is renowned for his interdisciplinary approach to history, combining insights from biology, anthropology, and philosophy.",
      "review": "A fascinating and thought-provoking look at the history of humanity, raising profound questions about our future."
    },
    {
      "author_name": "Michelle Obama",
      "book_name": "Becoming",
      "price": 14.99,
      "publication_year": 2018,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Becoming' by Michelle Obama is a memoir that chronicles the former First Lady's life from her childhood in Chicago to her years in the White House. Obama discusses her struggles with balancing family life, her professional ambitions, and her role as a public figure. The book explores themes of identity, belonging, and personal growth, providing an intimate and powerful reflection on her journey to becoming who she is today.",
      "author_info": "Michelle Obama is an American lawyer, author, and former First Lady of the United States. Her memoir 'Becoming' became a global best-seller, and she is also known for her advocacy on issues like education and health.",
      "review": "An inspiring and deeply personal memoir that offers a candid look at the challenges and triumphs of a remarkable woman."
    },
    {
      "author_name": "Stephen Hawking",
      "book_name": "A Brief History of Time",
      "price": 17.99,
      "publication_year": 1988,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'A Brief History of Time' by Stephen Hawking is a groundbreaking work that explains complex concepts in theoretical physics in a way that is accessible to the general public. Hawking discusses subjects like the nature of time, black holes, and the origin of the universe, offering insights into the nature of the cosmos. The book is known for making highly technical scientific ideas understandable without requiring a background in physics.",
      "author_info": "Stephen Hawking was a British theoretical physicist and cosmologist, renowned for his work on black holes and the nature of the universe. His books, including 'A Brief History of Time,' have made science accessible to millions.",
      "review": "A landmark book that brings complex scientific concepts to life for the general reader, offering profound insights into the universe."
    },
    {
      "author_name": "Viktor Frankl",
      "book_name": "Man's Search for Meaning",
      "price": 9.99,
      "publication_year": 1946,
      "publication_city": "Vienna",
      "genre": "Non-fiction",
      "description": "'Man's Search for Meaning' by Viktor Frankl is a powerful account of Frankl's experiences as a Holocaust survivor and his psychological insights into the human condition. Frankl introduces his theory of logotherapy, which emphasizes the search for meaning in life, even in the most difficult circumstances. The book is a profound meditation on suffering, resilience, and the importance of finding purpose in life.",
      "author_info": "Viktor Frankl was an Austrian neurologist, psychiatrist, and Holocaust survivor. He is best known for his work in existential psychology and for founding logotherapy, a therapeutic approach centered around meaning.",
      "review": "An inspiring and life-changing book that offers a profound perspective on overcoming adversity and finding meaning in life."
    },
    {
      "author_name": "David McRaney",
      "book_name": "You Are Not So Smart",
      "price": 13.49,
      "publication_year": 2011,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'You Are Not So Smart' by David McRaney is a witty and engaging exploration of human psychology. The book delves into the many cognitive biases and logical fallacies that shape our thinking and behavior, offering a fun and insightful look at why we often make irrational decisions. McRaney uses humor and real-world examples to highlight the ways in which our minds trick us into believing falsehoods and misconceptions.",
      "author_info": "David McRaney is an American journalist and author who specializes in psychology and cognitive science. His blog and books, including 'You Are Not So Smart,' have explored the quirks of human thinking.",
      "review": "A fun and enlightening book that reveals the surprising ways our brains deceive us, making psychology accessible and entertaining."
    },
    {
      "author_name": "Brené Brown",
      "book_name": "Daring Greatly",
      "price": 14.49,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Daring Greatly' by Brené Brown explores the power of vulnerability and how embracing our imperfections can lead to greater courage, creativity, and connection. Drawing on her research in social work and psychology, Brown challenges the stigma around vulnerability and demonstrates how it can be a source of strength. The book provides practical strategies for cultivating authenticity and resilience in everyday life.",
      "author_info": "Brené Brown is an American research professor and author, known for her work on vulnerability, courage, and empathy. Her TED Talk on vulnerability is one of the most viewed of all time.",
      "review": "An inspiring and transformative book that challenges conventional ideas of strength and shows the power of vulnerability."
    },
    {
      "author_name": "Mark Manson",
      "book_name": "The Subtle Art of Not Giving a F*ck",
      "price": 13.99,
      "publication_year": 2016,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'The Subtle Art of Not Giving a F*ck' by Mark Manson offers a no-nonsense approach to living a fulfilling life. Manson argues that the key to happiness is not in relentlessly pursuing success or avoiding problems but in accepting the inevitable struggles of life and focusing on what truly matters. With humor and blunt wisdom, he challenges conventional self-help advice and offers a refreshing perspective on how to prioritize the things that bring true meaning.",
      "author_info": "Mark Manson is an American author, blogger, and personal development expert. He is known for his straightforward and often irreverent approach to self-help.",
      "review": "A refreshing and brutally honest book that encourages readers to focus on what really matters and let go of the need for constant positivity."
    },
    {
      "author_name": "Tim Ferriss",
      "book_name": "The 4-Hour Workweek",
      "price": 15.49,
      "publication_year": 2007,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'The 4-Hour Workweek' by Tim Ferriss challenges conventional ideas about work and success. Ferriss offers strategies for automating your income, outsourcing tasks, and achieving a work-life balance that allows for more freedom and travel. The book is a blueprint for those seeking to escape the 9-to-5 grind and build a lifestyle that prioritizes adventure and personal fulfillment.",
      "author_info": "Tim Ferriss is an American entrepreneur, author, and podcaster, best known for his books on productivity, entrepreneurship, and lifestyle design.",
      "review": "A practical and unconventional guide to escaping the traditional workweek and creating a life of freedom and adventure."
    },
    {
      "author_name": "Jon Krakauer",
      "book_name": "Into the Wild",
      "price": 14.99,
      "publication_year": 1996,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Into the Wild' by Jon Krakauer tells the true story of Christopher McCandless, a young man who abandoned his privileged life to venture into the Alaskan wilderness, where he ultimately perished. The book examines McCandless’s motivations, the challenges he faced, and the philosophical questions surrounding his search for meaning and freedom in nature.",
      "author_info": "Jon Krakauer is an American author and journalist known for his non-fiction books on adventure and survival, particularly 'Into the Wild' and 'Into Thin Air.'",
      "review": "A gripping and tragic tale that explores the quest for freedom, the dangers of idealism, and the complex nature of human decision-making."
    },
    {
      "author_name": "Susan Cain",
      "book_name": "Quiet: The Power of Introverts in a World That Can’t Stop Talking",
      "price": 16.49,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Quiet: The Power of Introverts in a World That Can’t Stop Talking' by Susan Cain explores the power and potential of introverts in a society that often favors extroverted traits. Cain examines the science behind introversion and offers compelling arguments for why introverts can thrive in both personal and professional environments. The book encourages introverts to embrace their nature and challenges society to rethink its approach to leadership, creativity, and communication.",
      "author_info": "Susan Cain is an American author and speaker, best known for her work on introversion and personality psychology. She is the author of 'Quiet' and advocates for the rights and recognition of introverts in society.",
      "review": "An enlightening and empowering book that gives a voice to introverts and challenges the extrovert ideal."
    },
    {
      "author_name": "Ruth Bader Ginsburg",
      "book_name": "My Own Words",
      "price": 17.99,
      "publication_year": 2016,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'My Own Words' by Ruth Bader Ginsburg is a collection of the late Supreme Court Justice’s speeches, writings, and opinions. The book offers readers insight into her life, career, and the legal principles that guided her work. Ginsburg reflects on issues such as gender equality, civil rights, and the role of the judiciary in American democracy.",
      "author_info": "Ruth Bader Ginsburg was a U.S. Supreme Court Justice known for her advocacy for gender equality, civil rights, and social justice. She became an iconic figure for her trailblazing career and legacy.",
      "review": "A deeply inspiring and intellectual collection that highlights the profound impact of Ruth Bader Ginsburg on law and justice."
    },
    {
      "author_name": "Walter Isaacson",
      "book_name": "Steve Jobs",
      "price": 19.99,
      "publication_year": 2011,
      "publication_city": "New York",
      "genre": "Non-fiction",
      "description": "'Steve Jobs' by Walter Isaacson is a biography of the iconic Apple founder, based on extensive interviews with Jobs, his family, and colleagues. The book offers a candid look at Jobs’s innovative genius, his management style, and the personal challenges he faced. Isaacson reveals the complex, sometimes contradictory nature of Jobs, highlighting his drive, vision, and pursuit of perfection.",
      "author_info": "Walter Isaacson is an American author and journalist, best known for his biographies of historical figures such as Steve Jobs, Leonardo da Vinci, and Benjamin Franklin.",
      "review": "A detailed and fascinating portrait of one of the most influential and controversial figures in the tech industry."
    },

    {
      "author_name": "J.K. Rowling",
      "book_name": "Harry Potter and the Sorcerer's Stone",
      "price": 12.99,
      "publication_year": 1997,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'Harry Potter and the Sorcerer\'s Stone' is the first book in J.K. Rowling\'s magical series about a young wizard named Harry Potter. The story follows Harry as he discovers his true heritage, attends Hogwarts School of Witchcraft and Wizardry, and begins to uncover the secrets surrounding the mysterious Sorcerer\'s Stone. The book is a blend of adventure, magic, and friendship.",
      "author_info": "J.K. Rowling is a British author best known for writing the 'Harry Potter' series, which has become one of the best-selling book series in history.",
      "review": "A thrilling and magical start to one of the most beloved book series of all time, full of wonder and adventure."
    },
    {
      "author_name": "Roald Dahl",
      "book_name": "Matilda",
      "price": 9.99,
      "publication_year": 1988,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'Matilda' by Roald Dahl tells the story of a young girl named Matilda who is extremely gifted but often mistreated by her family. She discovers she has telekinetic powers and befriends her kind teacher, Miss Honey. Together, they face off against the cruel headmistress, Miss Trunchbull. The novel explores themes of intelligence, courage, and standing up against injustice.",
      "author_info": "Roald Dahl was a British novelist, short story writer, and poet, known for his beloved children\'s books, including 'Charlie and the Chocolate Factory' and 'The BFG.'",
      "review": "A wonderfully imaginative and empowering story for children, filled with humor, heart, and a message of resilience."
    },
    {
      "author_name": "E.B. White",
      "book_name": "Charlotte's Web",
      "price": 7.99,
      "publication_year": 1952,
      "publication_city": "New York",
      "genre": "Children's Literature",
      "description": "'Charlotte\'s Web' by E.B. White is the classic tale of a young pig named Wilbur and his friendship with Charlotte, a kind and clever spider. When Wilbur is at risk of being slaughtered, Charlotte spins a series of messages in her web to save him. The book explores themes of friendship, loyalty, and the cycle of life.",
      "author_info": "E.B. White was an American author and essayist, best known for his works such as 'Charlotte\'s Web' and 'Stuart Little.'",
      "review": "A timeless and heartwarming story that teaches the values of friendship, sacrifice, and the beauty of life."
    },
    {
      "author_name": "Beatrix Potter",
      "book_name": "The Tale of Peter Rabbit",
      "price": 5.99,
      "publication_year": 1902,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'The Tale of Peter Rabbit' by Beatrix Potter follows the mischievous Peter Rabbit as he sneaks into Mr. McGregor\'s garden, despite his mother\'s warnings. The story is a classic tale of adventure and consequence, with beautiful illustrations that have captivated children for over a century.",
      "author_info": "Beatrix Potter was an English author, illustrator, and natural scientist, best known for her children\'s books featuring animals, such as 'Peter Rabbit' and 'Jemima Puddle-Duck.'",
      "review": "A delightful and charming story that has enchanted generations with its whimsical characters and gentle lessons."
    },
    {
      "author_name": "C.S. Lewis",
      "book_name": "The Lion, the Witch, and the Wardrobe",
      "price": 10.99,
      "publication_year": 1950,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'The Lion, the Witch, and the Wardrobe' by C.S. Lewis is the first book in 'The Chronicles of Narnia' series. It follows four siblings who discover a magical land called Narnia through a wardrobe. There, they join forces with Aslan, a great lion, to defeat the White Witch and restore peace to the land. The novel is an allegorical tale of good versus evil, courage, and redemption.",
      "author_info": "C.S. Lewis was a British author, academic, and theologian, best known for his fantasy series 'The Chronicles of Narnia' and his Christian apologetics.",
      "review": "A captivating and adventurous story filled with magic, bravery, and unforgettable characters."
    },
    {
      "author_name": "J.R.R. Tolkien",
      "book_name": "The Hobbit",
      "price": 11.99,
      "publication_year": 1937,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'The Hobbit' by J.R.R. Tolkien follows the journey of Bilbo Baggins, a hobbit who is thrust into an adventure with a group of dwarves to reclaim their homeland from the dragon Smaug. Along the way, Bilbo faces numerous challenges and discovers the hero within himself. The book is a classic fantasy tale filled with bravery, friendship, and self-discovery.",
      "author_info": "J.R.R. Tolkien was an English author, philologist, and academic, best known for writing 'The Hobbit' and 'The Lord of the Rings' series.",
      "review": "An enchanting and timeless tale of adventure and personal growth that continues to captivate readers of all ages."
    },
    {
      "author_name": "Louise Fitzhugh",
      "book_name": "Harriet the Spy",
      "price": 6.99,
      "publication_year": 1964,
      "publication_city": "New York",
      "genre": "Children's Literature",
      "description": "'Harriet the Spy' by Louise Fitzhugh follows the story of Harriet M. Welsch, an 11-year-old girl who dreams of becoming a writer and spends her time spying on the people in her neighborhood. When her private notebook of observations is accidentally discovered, Harriet faces the consequences of her actions, learning valuable lessons about honesty, friendship, and trust.",
      "author_info": "Louise Fitzhugh was an American author and illustrator, best known for her children's book 'Harriet the Spy,' which became a classic of children's literature.",
      "review": "A brilliant and thought-provoking book that captures the challenges of growing up and understanding the complexities of relationships."
    },
    {
      "author_name": "L. Frank Baum",
      "book_name": "The Wonderful Wizard of Oz",
      "price": 8.99,
      "publication_year": 1900,
      "publication_city": "Chicago",
      "genre": "Children's Literature",
      "description": "'The Wonderful Wizard of Oz' by L. Frank Baum tells the story of Dorothy, a young girl who is swept away by a tornado to the magical land of Oz. She teams up with the Scarecrow, the Tin Man, and the Cowardly Lion to defeat the Wicked Witch of the West and find her way home. The novel is a timeless fantasy adventure about courage, friendship, and self-discovery.",
      "author_info": "L. Frank Baum was an American author, best known for writing 'The Wonderful Wizard of Oz' and its sequels, which have become some of the most beloved books in American literature.",
      "review": "A magical and heartwarming adventure that continues to inspire and captivate readers of all ages."
    },
    {
      "author_name": "Katherine Paterson",
      "book_name": "Bridge to Terabithia",
      "price": 7.99,
      "publication_year": 1977,
      "publication_city": "New York",
      "genre": "Children's Literature",
      "description": "'Bridge to Terabithia' by Katherine Paterson tells the story of Jess Aarons, a young boy who befriends a girl named Leslie Burke. Together, they create an imaginary kingdom called Terabithia in the woods, where they reign as king and queen. The book deals with themes of friendship, loss, and the power of imagination.",
      "author_info": "Katherine Paterson is an American author of children's books, best known for her novels 'Bridge to Terabithia' and 'Jacob Have I Loved,' both of which have won prestigious awards.",
      "review": "A touching and emotional story that explores the deep impact of friendship and the painful realities of life."
    },
    {
      "author_name": "A.A. Milne",
      "book_name": "Winnie-the-Pooh",
      "price": 6.99,
      "publication_year": 1926,
      "publication_city": "London",
      "genre": "Children's Literature",
      "description": "'Winnie-the-Pooh' by A.A. Milne is a heartwarming collection of stories about the adventures of Winnie the Pooh and his friends in the Hundred Acre Wood. The book follows Pooh, Piglet, Tigger, Eeyore, and others as they navigate friendship, problem-solving, and everyday adventures. It is a classic tale that celebrates the simple joys of life and the value of friendship.",
      "author_info": "A.A. Milne was an English author and playwright, best known for creating the beloved 'Winnie-the-Pooh' stories, which have been cherished by generations of readers.",
      "review": "A timeless classic that captures the innocence and charm of childhood with its endearing characters and heartwarming stories."
    },

    {
      "author_name": "Agatha Christie",
      "book_name": "Murder on the Orient Express",
      "price": 12.99,
      "publication_year": 1934,
      "publication_city": "London",
      "genre": "Detective",
      "description": "'Murder on the Orient Express' by Agatha Christie is one of the most famous Hercule Poirot mysteries. When a wealthy American is murdered aboard the luxurious train, Poirot is asked to investigate. With a train full of suspects, each with their own secrets, Poirot uses his sharp intellect and keen observation to unravel the mystery. The novel is a classic example of Christie’s mastery of suspense and intricate plotting.",
      "author_info": "Agatha Christie was an English writer known for her detective novels, particularly those featuring Hercule Poirot and Miss Marple. She is one of the best-selling authors of all time.",
      "review": "A brilliant and intricately woven mystery, with a surprise ending that will leave readers astounded."
    },
    {
      "author_name": "Arthur Conan Doyle",
      "book_name": "The Hound of the Baskervilles",
      "price": 10.99,
      "publication_year": 1902,
      "publication_city": "London",
      "genre": "Detective",
      "description": "'The Hound of the Baskervilles' is one of the most famous Sherlock Holmes stories by Arthur Conan Doyle. When Sir Charles Baskerville is found dead on his estate, seemingly the victim of a supernatural hound, Holmes and Watson investigate the mysterious circumstances. The novel blends elements of gothic horror with classic detective fiction, keeping readers on the edge of their seats.",
      "author_info": "Arthur Conan Doyle was a British author, best known for creating the legendary detective Sherlock Holmes. His works have become some of the most famous detective stories in literature.",
      "review": "A masterful blend of mystery, suspense, and gothic elements that showcases Holmes at his best."
    },
    {
      "author_name": "Dashiell Hammett",
      "book_name": "The Maltese Falcon",
      "price": 9.99,
      "publication_year": 1930,
      "publication_city": "New York",
      "genre": "Detective",
      "description": "'The Maltese Falcon' is a hard-boiled detective novel by Dashiell Hammett. The story follows private detective Sam Spade as he investigates the mysterious case of a priceless statue, the Maltese Falcon. The novel features crime, deception, and complex characters, making it one of the definitive works of the noir genre.",
      "author_info": "Dashiell Hammett was an American author and screenwriter, widely regarded as one of the founders of the hard-boiled detective genre.",
      "review": "A gritty, fast-paced detective novel that captures the essence of the noir genre and features a compelling protagonist."
    },
    {
      "author_name": "Raymond Chandler",
      "book_name": "The Big Sleep",
      "price": 11.99,
      "publication_year": 1939,
      "publication_city": "New York",
      "genre": "Detective",
      "description": "'The Big Sleep' by Raymond Chandler introduces Philip Marlowe, a private detective hired to investigate the blackmail of a wealthy family. As Marlowe dives deeper into the case, he uncovers a web of crime, corruption, and intrigue that leads him into a dangerous world. The novel is a classic of the hard-boiled detective genre, with its dark, cynical tone and complex characters.",
      "author_info": "Raymond Chandler was an American author known for his detective fiction, particularly those featuring Philip Marlowe, a cynical and morally ambiguous private detective.",
      "review": "A gritty, atmospheric novel that set the standard for hard-boiled detective stories with its sharp dialogue and complex narrative."
    },
    {
      "author_name": "Gillian Flynn",
      "book_name": "Gone Girl",
      "price": 14.99,
      "publication_year": 2012,
      "publication_city": "New York",
      "genre": "Detective",
      "description": "'Gone Girl' by Gillian Flynn is a psychological thriller and detective novel that follows the disappearance of Amy Dunne and the investigation that ensues. As her husband, Nick, becomes the prime suspect, secrets and lies about their marriage are revealed. The novel explores themes of deception, media manipulation, and the complexities of relationships.",
      "author_info": "Gillian Flynn is an American author and screenwriter, best known for her psychological thrillers, including 'Gone Girl,' which became a best-seller and was adapted into a major film.",
      "review": "A twisted, gripping thriller that keeps readers guessing until the very end, with complex characters and a shocking conclusion."
    },
    {
      "author_name": "John Grisham",
      "book_name": "The Firm",
      "price": 13.99,
      "publication_year": 1991,
      "publication_city": "New York",
      "genre": "Detective",
      "description": "'The Firm' by John Grisham follows Mitch McDeere, a young law graduate who takes a job at a small but prestigious law firm in Memphis. However, he soon discovers that the firm has dangerous ties to the mob. As Mitch tries to navigate the world of crime and corruption, he is forced to make difficult choices to survive.",
      "author_info": "John Grisham is an American author best known for his legal thrillers, including 'The Firm,' 'A Time to Kill,' and 'The Pelican Brief.' His works often explore the legal system and moral dilemmas.",
      "review": "A fast-paced, suspenseful legal thriller that keeps readers on the edge of their seats with its twists and turns."
    },
    {
      "author_name": "Henning Mankell",
      "book_name": "Faceless Killers",
      "price": 12.99,
      "publication_year": 1991,
      "publication_city": "Stockholm",
      "genre": "Detective",
      "description": "'Faceless Killers' by Henning Mankell introduces Swedish detective Kurt Wallander, who investigates the brutal murder of an elderly couple. As Wallander delves deeper into the case, he uncovers a series of complexities and challenges that reflect broader issues within Swedish society. The novel is both a gripping detective story and a commentary on contemporary life.",
      "author_info": "Henning Mankell was a Swedish author, best known for his Kurt Wallander detective series, which has been translated into numerous languages and adapted into television series and films.",
      "review": "A chilling and thought-provoking mystery that introduces an iconic detective in a gripping and socially aware context."
    },
    {
      "author_name": "Agatha Christie",
      "book_name": "The Murder of Roger Ackroyd",
      "price": 10.99,
      "publication_year": 1926,
      "publication_city": "London",
      "genre": "Detective",
      "description": "'The Murder of Roger Ackroyd' by Agatha Christie is one of her most famous Hercule Poirot mysteries. When Roger Ackroyd is found murdered in his study, Poirot is called upon to investigate. The novel is renowned for its innovative twist, which challenges the conventions of detective fiction and remains one of the genre’s most shocking conclusions.",
      "author_info": "Agatha Christie was an English writer known for her detective novels, particularly those featuring Hercule Poirot and Miss Marple. She is one of the best-selling authors of all time.",
      "review": "A groundbreaking mystery that surprises and delights with its ingenious plot and unexpected ending."
    },
    {
      "author_name": "Louise Penny",
      "book_name": "Still Life",
      "price": 14.99,
      "publication_year": 2005,
      "publication_city": "Toronto",
      "genre": "Detective",
      "description": "'Still Life' by Louise Penny introduces Chief Inspector Armand Gamache of the Sûreté du Québec, who investigates the death of a beloved local artist in the village of Three Pines. As he uncovers secrets within the close-knit community, Gamache must navigate his own feelings of guilt and personal loss. The novel is the first in the Chief Inspector Gamache series.",
      "author_info": "Louise Penny is a Canadian author, best known for her Chief Inspector Gamache series of detective novels, which have won numerous literary awards.",
      "review": "A poignant and atmospheric mystery that combines a rich setting, compelling characters, and a gripping plot."
    }
  ],


  "genres" : [
    {
      "genre": "Fiction",
      "description": "Fiction is a literary genre that includes narratives which are created from the imagination, rather than being based entirely on real events. It allows authors to craft entirely new worlds, characters, and situations, often exploring themes and concepts that are not bound by the constraints of reality. Fiction encompasses a wide range of subgenres, including fantasy, science fiction, and drama, each of which offers unique storytelling possibilities."
    },
    {
      "genre": "Classic",
      "description": "Classic literature refers to works that have been recognized for their enduring quality and significant impact on culture and society. These works are often characterized by their deep exploration of universal themes such as love, loss, and identity. Classics are considered timeless and continue to be read and appreciated by readers across generations. They have influenced the development of literature and are often used as educational tools in the study of literature and history."
    },
    {
      "genre": "Romance",
      "description": "Romance is a literary genre that centers around romantic relationships, with a strong focus on the emotions and connections between characters. These stories often explore themes of love, passion, and the complexities of relationships. While many romance novels have a happy ending, the genre can also explore more complex aspects of love, such as heartbreak, personal growth, and the challenges of maintaining a relationship. Romance novels are popular for their emotional depth and ability to evoke strong feelings of empathy from readers."
    },
    {
      "genre": "Mystery",
      "description": "Mystery novels are a genre centered around the investigation of a crime or puzzle, often involving a protagonist such as a detective, amateur sleuth, or investigator who works to uncover the truth behind a mysterious event. The genre is known for its suspenseful plots, where the reader is challenged to piece together clues alongside the main character. Mysteries often involve intricate plots with red herrings, false leads, and unexpected twists, keeping readers on the edge of their seats as they try to solve the puzzle before the characters do."
    },
    {
      "genre": "Horror",
      "description": "Horror is a genre intended to evoke feelings of fear, dread, and terror in the reader. It often includes supernatural elements, such as ghosts, monsters, or dark forces, as well as psychological horror, where the fear stems from the characters' own minds or distorted perceptions of reality. Horror fiction taps into the human instinct to be frightened, using tension and surprise to keep the reader on edge. The genre often explores themes of mortality, the unknown, and the darkness within human nature, making it both thrilling and unsettling."
    },
    {
      "genre": "Historical Fiction",
      "description": "Historical fiction is a genre that blends fictional storytelling with real historical events and figures, bringing the past to life through imaginative narratives. Writers in this genre often immerse readers in specific historical periods, providing a detailed and immersive experience of what life was like during those times. Historical fiction can explore important events such as wars, political movements, and cultural changes, while also delving into personal stories of individuals who lived through these events. This genre offers both education and entertainment, providing insight into history through compelling stories."
    },
    {
      "genre": "Dystopian",
      "description": "Dystopian fiction presents a vision of the future that is often bleak, oppressive, and dehumanizing. In these narratives, society is typically characterized by a totalitarian government, environmental degradation, or extreme social inequality. The genre explores themes of control, surveillance, and the loss of individual freedoms, raising questions about the consequences of unchecked power and technological advancement. Dystopian stories often feature protagonists who rebel against the system, offering a critique of contemporary society and a warning about the possible outcomes of current trends."
    },
    {
      "genre": "Non-fiction",
      "description": "Non-fiction is a genre that deals with factual accounts of real events, people, and places. Unlike fiction, which is created from the imagination, non-fiction is grounded in reality and aims to inform, educate, or persuade the reader. This genre encompasses a wide range of formats, including biographies, history, essays, self-help, and journalism. Non-fiction works are valued for their factual accuracy, providing insight into real-world issues and experiences. They help readers expand their knowledge and understanding of the world, offering diverse perspectives on topics ranging from science to personal development."
    },
    {
      "genre": "Children's Literature",
      "description": "Children's literature is a genre specifically written for young readers, focusing on stories and themes that are appropriate for children at various developmental stages. These works often include colorful illustrations, simple language, and engaging plots designed to capture the imagination of young minds. Children's literature can encompass a wide range of themes, from fairy tales and adventures to stories about friendship, family, and personal growth. This genre plays a crucial role in childhood development, fostering literacy skills, creativity, and a love for reading from an early age."
    },
    {
      "genre": "Detective",
      "description": "Detective fiction is a genre that revolves around the investigation of a crime, typically involving a detective or investigator who uses logic, deduction, and observation to solve the case. These stories often feature complex puzzles, hidden clues, and red herrings that challenge both the detective and the reader to solve the mystery. Detective fiction can range from traditional whodunits to more modern, gritty investigations. The genre often explores themes of justice, morality, and the nature of truth, with the detective serving as a guide for the reader through the labyrinth of the case."
    }
  ]

}'''

class BookShopDatabase:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def list_all_books(self):
        sql = "SELECT book_id, book_name, author_name FROM Books"
        self.cursor.execute(sql)
        books = self.cursor.fetchall()
        
        if books:
            print("Existing books in the database:")
            for book in books:
                print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}")
        else:
            print("No books found in the database.")


    def add_genre(self, genre, description):
        genre_id = int(uuid.uuid4().int % 2147483647)
        sql = "INSERT INTO Genre (genre_id, genre, description) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (genre_id, genre, description))
        self.db.commit()
        print(f"Genre '{genre}' added with description '{description}'")

    def get_genre_id(self, genre_name):
        sql = "SELECT genre_id FROM Genre WHERE genre = %s"
        self.cursor.execute(sql, (genre_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]

        print("Genre not found. Genre '{genre}' added with description '{description}'.")
        self.add_genre(genre_name, "")
        return self.get_genre_id(genre_name)

    def add_book(self, author_name, book_name, price, publication_year, publication_city, genre, description, author_info, review):
        book_id = int(uuid.uuid4().int % 2147483647)
        genre_id = self.get_genre_id(genre)
        sql = """
            INSERT INTO Books 
            (book_id, author_name, book_name, price, publication_year, publication_city, genre_id, genre, description, author_info, review)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (book_id, author_name, book_name, price, publication_year, publication_city, genre_id, genre, description, author_info, review)
        self.cursor.execute(sql, values)
        self.db.commit()
        print(f"Book '{book_name}' by {author_name} added")
        self.add_storage_info(book_id)
        return book_id

    def add_storage_info_by_manager(self, book_id, floor_number, aisle, shelf):
        sql = "INSERT INTO Storage (book_id, floor_number, aisle, shelf) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (book_id, floor_number, aisle, shelf))
        self.db.commit()
        print(f"Storage info for book {book_id} added. Floor: {floor_number}, Aisle: {aisle}, Shelf: {shelf}")

    def add_storage_info(self, book_id):
        floor_number = random.randint(1, 2)
        aisle = random.randint(1, 4)
        shelf = random.randint(1, 3)
        sql = "INSERT INTO Storage (book_id, floor_number, aisle, shelf) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (book_id, floor_number, aisle, shelf))
        self.db.commit()
        print(f"Storage info for book {book_id} added. Floor: {floor_number}, Aisle: {aisle}, Shelf: {shelf}")

    def update_book(self, book_id, author_name=None, book_name=None, price=None, publication_year=None, 
        publication_city=None, genre=None, description=None, author_info=None, review=None):

        sql = "UPDATE Books SET "
        values = []

        if author_name:
            sql += "author_name = %s, "
            values.append(author_name)
        if book_name:
            sql += "book_name = %s, "
            values.append(book_name)
        if price:
            sql += "price = %s, "
            values.append(price)
        if publication_year:
            sql += "publication_year = %s, "
            values.append(publication_year)
        if publication_city:
            sql += "publication_city = %s, "
            values.append(publication_city)
        if genre:
            sql += "genre = %s, "
            values.append(genre)
        if description:
            sql += "description = %s, "
            values.append(description)
        if author_info:
            sql += "author_info = %s, "
            values.append(author_info)
        if review:
            sql += "review = %s, "
            values.append(review)

        sql = sql.rstrip(', ')

        sql += " WHERE book_id = %s"
        values.append(book_id)

        self.cursor.execute(sql, tuple(values))
        self.db.commit()
        print(f"Book with ID {book_id} has been updated.")

    def delete_book(self, book_id):
        sql_check = "SELECT * FROM Books WHERE book_id = %s"
        self.cursor.execute(sql_check, (book_id,))
        result = self.cursor.fetchone()

        if result:
            sql_delete = "DELETE FROM Books WHERE book_id = %s"
            self.cursor.execute(sql_delete, (book_id,))
            self.db.commit()

            sql_delete_storage = "DELETE FROM Storage WHERE book_id = %s"
            self.cursor.execute(sql_delete_storage, (book_id,))
            self.db.commit()

            print(f"Book with ID {book_id} has been deleted.")
        else:
            print(f"Book with ID {book_id} not found.")


    def load_from_json(self, json_data):

        data = json.loads(json_data)

        for genre in data.get("genres", []):
            self.add_genre(genre['genre'], genre['description'])

        for book in data.get("books", []):
            self.add_book(
                book['author_name'], book['book_name'], book['price'], book['publication_year'],
                book['publication_city'], book['genre'], book['description'], book['author_info'], book['review']
            )

        print("Data loaded from JSON.")


    def generate_sales_report(self, date):
        sql = "SELECT Books.book_name, Books.price, Orders.update_date FROM Orders LEFT JOIN Order_item ON Order_item.order_id = Orders.order_id LEFT JOIN Books ON Order_item.book_id = Books.book_id WHERE Orders.update_date = %s AND Orders.status='complete';"
        self.cursor.execute(sql, (date,))
        sales = self.cursor.fetchall()
        print(f"Sales report for {date}:")
        for sale in sales:
            print(f"Book: {sale[0]}, Price: {sale[1]}")

    def not_active_customers(self):
        sql = """
            SELECT Orders.address, Orders.update_date, Orders.create_date, Orders.first_name, Customers.email 
            FROM Orders 
            LEFT JOIN Customers ON Orders.customer_id = Customers.customer_id 
            WHERE update_date < (CURRENT_DATE - INTERVAL 3 MONTH)
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print("Outdated Orders Report:")
        for row in results:
            print(f"Address: {row[0]}, Update Date: {row[1]}, Create Date: {row[2]}, First Name: {row[3]}, Email: {row[4]}")


    def close(self):
        self.cursor.close()
        self.db.close()
        print("Database connection closed.")



def main():
    db = BookShopDatabase(host="localhost", user="root", password="pw", database="BookShope")
    validator = InputValidator()
    
    while True:
        print("\n--- Bookshop Database Menu ---")
        print("1. Add Genre")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Load Data from JSON")
        print("6. Generate Sales Report")
        print("7. Find customers who haven't placed an order in the last 3 months")
        print("8. List all books")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            genre = validator.get_string_input("Enter genre name: ")
            description = validator.get_string_input("Enter genre description: ")
            db.add_genre(genre, description)

        elif choice == "2":
            author_name = validator.get_string_input("Enter author name: ")
            book_name = validator.get_string_input("Enter book name: ")
            price = validator.get_float_input("Enter price: ", min_value=0)
            current_year = datetime.datetime.now().year
            publication_year = validator.get_int_input("Enter publication year: ", max_value=current_year)
            publication_city = validator.get_string_input("Enter publication city: ")
            genre = validator.get_string_input("Enter genre: ")
            description = validator.get_string_input("Enter book description: ")
            author_info = validator.get_string_input("Enter author info: ")
            review = validator.get_string_input("Enter review: ")
            book_id = db.add_book(author_name, book_name, price, publication_year, publication_city, genre, description, author_info, review)

            print("Now you need to add Storage Info")
            floor_number = validator.get_int_input("Enter floor number: ", min_value=1, max_value = 2)
            aisle = validator.get_int_input("Enter aisle: ", min_value=1, max_value = 4)
            shelf = validator.get_int_input("Enter shelf: ", min_value=1, max_value = 3)
            db.add_storage_info_by_manager(book_id, floor_number, aisle, shelf)

        elif choice == "3":
            book_id = validator.get_int_input("Enter the book ID to update: ")
            author_name = validator.get_string_input("Enter new author name (leave empty if no change): ")
            book_name = validator.get_string_input("Enter new book name (leave empty if no change): ")
            price = validator.get_float_input("Enter new price (leave empty if no change): ")
            publication_year = validator.get_int_input("Enter new publication year (leave empty if no change): ")
            publication_city = validator.get_string_input("Enter new publication city (leave empty if no change): ")
            genre = validator.get_string_input("Enter new genre (leave empty if no change): ")
            description = validator.get_string_input("Enter new description (leave empty if no change): ")
            author_info = validator.get_string_input("Enter new author info (leave empty if no change): ")
            review = validator.get_string_input("Enter new review (leave empty if no change): ")
            
            db.update_book(book_id, author_name, book_name, price, publication_year, publication_city, genre, description, author_info, review)
        
        elif choice == "4":
            book_id = validator.get_int_input("Enter the book ID to delete: ")
            db.delete_book(book_id)

        elif choice == "5":
            db.load_from_json(data) 

        elif choice == "6":
            date = validator.get_date_input("Enter the date (YYYY-MM-DD) for sales report: ")
            db.generate_sales_report(date)

        elif choice == "7":
            db.not_active_customers()

        elif choice == "8":
            db.list_all_books()
        
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

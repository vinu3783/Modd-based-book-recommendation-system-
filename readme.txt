const books = [
    
    // Fiction
    
    
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald", reviews: "4.3/5", genre: "Fiction", image: "./images/fiction1.jpg" },
    { title: "To Kill a Mockingbird", author: "Harper Lee", reviews: "4.8/5", genre: "Fiction", image: "./images/fiction 2.jpg" },
    { title: "The White Tiger", author: "Aravind Adiga", reviews: "4.2/5", genre: "Fiction", image: "./images/fiction 3.jpg" },
    { title: "A Fine Balance", author: "Rohinton Mistry", reviews: "4.4/5", genre: "Fiction", image: "./images/fiction 4.jpg" },
    { title: "Midnight's Children", author: "Salman Rushdie", reviews: "4.1/5", genre: "Fiction", image: "./images/fiction 5.jpg" },
    { title: "Beloved", author: "Toni Morrison", reviews: "4.5/5", genre: "Fiction", image: "./images/fiction 6.jpg" },
    { title: "The Namesake", author: "Jhumpa Lahiri", reviews: "4.3/5", genre: "Fiction", image: "./images/fiction 7.jpg" },
    { title: "The God of Small Things", author: "Arundhati Roy", reviews: "4.6/5", genre: "Fiction", image: "./images/fiction 8.jpg" },
    { title: "Half of a Yellow Sun", author: "Chimamanda Ngozi Adichie", reviews: "4.5/5", genre: "Fiction", image: "./images/fiction 9.jpg" },
    { title: "The Alchemist", author: "Paulo Coelho", reviews: "4.7/5", genre: "Fiction", image: "./images/fiction 10.jpg" },
  
    // Science Fiction
    { title: "1984", author: "George Orwell", reviews: "4.7/5", genre: "Science Fiction", image: "./images/scifi1.jpg" },
    { title: "Dune", author: "Frank Herbert", reviews: "4.8/5", genre: "Science Fiction", image: "./images/scifi2.jpg" },
    { title: "Brave New World", author: "Aldous Huxley", reviews: "4.6/5", genre: "Science Fiction", image: "./images/scifi3.jpg" },
    { title: "Foundation", author: "Isaac Asimov", reviews: "4.5/5", genre: "Science Fiction", image: "./images/scifi4.jpg" },
    { title: "Neuromancer", author: "William Gibson", reviews: "4.4/5", genre: "Science Fiction", image: "./images/scifi5.jpg" },
    { title: "The Three-Body Problem", author: "Cixin Liu", reviews: "4.6/5", genre: "Science Fiction", image: "./images/scifi6.jpg" },
    { title: "The Left Hand of Darkness", author: "Ursula K. Le Guin", reviews: "4.3/5", genre: "Science Fiction", image: "./images/scifi7.jpg" },
    { title: "Kindred", author: "Octavia E. Butler", reviews: "4.7/5", genre: "Science Fiction", image: "./images/scifi8.jpg" },
    { title: "Frankenstein", author: "Mary Shelley", reviews: "4.6/5", genre: "Science Fiction", image: "./images/scifi9.jpg" },
    { title: "Solaris", author: "Stanisław Lem", reviews: "4.5/5", genre: "Science Fiction", image: "./images/scifi10.jpg" },
  
    // Romance
    { title: "Pride and Prejudice", author: "Jane Austen", reviews: "4.6/5", genre: "Romance", image: "./images/Rom 1.jpg" },
    { title: "The Fault in Our Stars", author: "John Green", reviews: "4.4/5", genre: "Romance", image: "./images/Rom 2.jpg" },
    { title: "The Palace of Illusions", author: "Chitra Banerjee Divakaruni", reviews: "4.5/5", genre: "Romance", image: "./images/Rom 3.jpg" },
    { title: "Me Before You", author: "Jojo Moyes", reviews: "4.3/5", genre: "Romance", image: "./images/Rom 4.jpg" },
    { title: "Norwegian Wood", author: "Haruki Murakami", reviews: "4.2/5", genre: "Romance", image: "./images/Rom 5.jpg" },
    { title: "It Ends with Us", author: "Colleen Hoover", reviews: "4.5/5", genre: "Romance", image: "./images/Rom 6.jpg" },
    { title: "The Rosie Project", author: "Graeme Simsion", reviews: "4.2/5", genre: "Romance", image: "./images/Rom 7.jpg" },
    { title: "Love Story", author: "Erich Segal", reviews: "4.3/5", genre: "Romance", image: "./images/Rom 8.jpg" },
    { title: "Eleven Minutes", author: "Paulo Coelho", reviews: "4.1/5", genre: "Romance", image: "./images/Rom 9.jpg" },
    { title: "Message in a Bottle", author: "Nicholas Sparks", reviews: "4.4/5", genre: "Romance", image: "./images/Rom 10.jpg" },

      // Thriller
    { title: "The Da Vinci Code", author: "Dan Brown", reviews: "4.6/5", genre: "Thriller", image: "./images/thriller1.jpg" },
    { title: "The Girl on the Train", author: "Paula Hawkins", reviews: "4.3/5", genre: "Thriller", image: "./images/thriller2.jpg" },
    { title: "The Silent Corner", author: "Dean Koontz", reviews: "4.4/5", genre: "Thriller", image: "./images/thriller3.jpg" },
    { title: "Into the Water", author: "Paula Hawkins", reviews: "4.1/5", genre: "Thriller", image: "./images/thriller4.jpg" },
    { title: "Sacred Games", author: "Vikram Chandra", reviews: "4.5/5", genre: "Thriller", image: "./images/thriller5.jpg" },
    { title: "The Maze Runner", author: "James Dashner", reviews: "4.2/5", genre: "Thriller", image: "./images/thriller6.jpg" },
    { title: "The Bourne Identity", author: "Robert Ludlum", reviews: "4.6/5", genre: "Thriller", image: "./images/thriller7.jpg" },
    { title: "I Am Pilgrim", author: "Terry Hayes", reviews: "4.8/5", genre: "Thriller", image: "./images/thriller8.jpg" },
    { title: "Behind Closed Doors", author: "B.A. Paris", reviews: "4.4/5", genre: "Thriller", image: "./images/thriller9.jpg" },
    { title: "Shutter Island", author: "Dennis Lehane", reviews: "4.7/5", genre: "Thriller", image: "./images/thriller10.jpg" },

    // Mystery
  { title: "The Girl with the Dragon Tattoo", author: "Stieg Larsson", reviews: "4.4/5", genre: "Mystery", image: "./images/mystery1.jpg" },
  { title: "Gone Girl", author: "Gillian Flynn", reviews: "4.3/5", genre: "Mystery", image: "./images/mystery2.jpg" },
  { title: "Big Little Lies", author: "Liane Moriarty", reviews: "4.2/5", genre: "Mystery", image: "./images/mystery3.jpg" },
  { title: "The Silent Patient", author: "Alex Michaelides", reviews: "4.5/5", genre: "Mystery", image: "./images/mystery4.jpg" },
  { title: "Sacred Games", author: "Vikram Chandra", reviews: "4.2/5", genre: "Mystery", image: "./images/mystery5.jpg" },
  { title: "In the Woods", author: "Tana French", reviews: "4.0/5", genre: "Mystery", image: "./images/mystery6.jpg" },
  { title: "The Devotion of Suspect X", author: "Keigo Higashino", reviews: "4.6/5", genre: "Mystery", image: "./images/mystery7.jpg" },
  { title: "The Murder of Roger Ackroyd", author: "Agatha Christie", reviews: "4.8/5", genre: "Mystery", image: "./images/mystery8.jpg" },
  { title: "The No. 1 Ladies' Detective Agency", author: "Alexander McCall Smith", reviews: "4.1/5", genre: "Mystery", image: "./images/mystery9.jpg" },
  { title: "Sherlock Holmes: A Study in Scarlet", author: "Arthur Conan Doyle", reviews: "4.7/5", genre: "Mystery", image: "./images/mystery10.jpg" },

  // Fantasy
  { title: "The Hobbit", author: "J.R.R. Tolkien", reviews: "4.5/5", genre: "Fantasy", image: "./images/fantasy1.jpg" },
  { title: "Harry Potter and the Philosopher's Stone", author: "J.K. Rowling", reviews: "4.9/5", genre: "Fantasy", image: "./images/fantasy2.jpg" },
  { title: "The Name of the Wind", author: "Patrick Rothfuss", reviews: "4.7/5", genre: "Fantasy", image: "./images/fantasy3.jpg" },
  { title: "A Song of Ice and Fire", author: "George R.R. Martin", reviews: "4.8/5", genre: "Fantasy", image: "./images/fantasy4.jpg" },
  { title: "Percy Jackson and the Olympians", author: "Rick Riordan", reviews: "4.6/5", genre: "Fantasy", image: "./images/fantasy5.jpg" },
  { title: "The Palace of Illusions", author: "Chitra Banerjee Divakaruni", reviews: "4.5/5", genre: "Fantasy", image: "./images/fantasy6.jpg" },
  { title: "The Immortals of Meluha", author: "Amish Tripathi", reviews: "4.4/5", genre: "Fantasy", image: "./images/fantasy7.jpg" },
  { title: "Children of Blood and Bone", author: "Tomi Adeyemi", reviews: "4.5/5", genre: "Fantasy", image: "./images/fantasy8.jpg" },
  { title: "The Golem and the Jinni", author: "Helene Wecker", reviews: "4.3/5", genre: "Fantasy", image: "./images/fantasy9.jpg" },
  { title: "Eragon", author: "Christopher Paolini", reviews: "4.2/5", genre: "Fantasy", image: "./images/fantasy10.jpg" },
 
  ];
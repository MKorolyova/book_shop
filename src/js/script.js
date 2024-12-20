const customer = {};

async function fetchDataLogIn() {
    try {
        const response = await fetch(`http://localhost:8000/data/customer/log-in/email/${customer.email}/password/${customer.password}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json(); 
        return data;

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}

async function fetchDataRandBooks(limit) {
        try {
            const response = await fetch(`http://localhost:8000/data/book/get-book-by-random-page/customer_id/${customer.customer_id}/limit/${limit}`);
            if (!response.ok) {
                throw new Error(`Server returned ${response.status}`);
            }
            const data = await response.json(); 
            return data;
    
        } catch (error) {
            console.error("Error fetching data:", error);
            return null; 
        }
}

async function fetchDataBookPage(book_id) {
    try {
        const response = await fetch(`http://localhost:8000/data/book/get-book-page/customer_id/${customer.customer_id}/book_id/${book_id}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json(); 
        return data;

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}

async function fetchDataGenreBooksPage(genre_id) {
    try {
        const response = await fetch(`http://localhost:8000/data/book/get-book-by-genre-page/customer_id/${customer.customer_id}/genre_id/${genre_id}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json(); 
        return data;

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}


async function fetchDataCartPage() {
    try {
        const response = await fetch(`http://localhost:8000/data/cart/get-cart-page/customer_id/${customer.customer_id}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json(); 
        return data;

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}


async function fetchDataAddBook(book_id) {
    try {
        const response = await fetch(`http://localhost:8000/data/order-item/add-item-to-order/customer_id/${customer.customer_id}/book_id/${book_id}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }else{
            console.log("done")
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}


async function fetchDataDeleteBook(order_item_id) {
    try {
        const response = await fetch(`http://localhost:8000/data/order-item/del-item-from-order/customer_id/${customer.customer_id}/order_item_id/${order_item_id}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }else{
            console.log("done")
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}

async function fetchDataCompleteOrder(first_name, last_name, postal_zip, address, city, country) {
    try {
        const response = await fetch(`http://localhost:8000/data/order/complete-order/customer_id/${customer.customer_id}/first_name/${first_name}/last_name/${last_name}/postal_zip/${postal_zip}/address/${address}/city/${city}/counry/${country}`);
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }else{
            console.log("done")
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        return null; 
    }
}
    
function loadDataHomePage(){
        fetchDataRandBooks(16)        
        
        .then(data => {
            const midIndex = Math.ceil(data.book.length / 2);
            const booksForSwiper1 = data.book.slice(0, midIndex); 
            const booksForSwiper2 = data.book.slice(midIndex); 
            const imgLink = "./public/img/home.jpg"
    
            document.getElementById("body").innerHTML = `

                ${customerRegistrationForm()}

                <div class="section">
                    ${menu()}

                    <header>
                        <div class="background">
                            <img src="${imgLink}" alt="background" class="background_img">

                            <nav id="genre_menu" class="genre_menu">
                                ${ menuGenre(data.genre)} 
                                <p id="find_out_more" class="link_button">find out more</p>
                            </nav>
                            ${ sticker()}
                        </div>
                    </header>
                </div>

                <h2 class="title">Newies in store</h2>
    
                <div class="swiper">
                    <div class="swiper-wrapper">
                        ${loadBooksInSwiper(booksForSwiper1, 4)}
                    </div>
                    <div class="swiper-button-prev"></div>
                    <div class="swiper-button-next"></div>
                </div>
    
                <h2 class="title">Easy Delivery</h2>
    
                <div class="section">
                    <div class="delivery_items">
                        <div class="delivery_item">
                            <span class="delivery_number">01</span>
                            <p class="subtitle">
                                Return 14 days.<br>
                                The argument "did not like" we have enough.
                            </p>
                        </div>
                        <div class="delivery_item">
                            <span class="delivery_number">02</span>
                            <p class="subtitle">
                                Everyone gets a present.<br>
                                Fast delivery.
                            </p>
                        </div>
                        <div class="delivery_item">
                            <span class="delivery_number">03</span>
                            <p class="subtitle">
                                Regular customers and<br>
                                Members get discounts.
                            </p>
                        </div>
                    </div>
                </div>
    
                <h2 class="title">Bestsellers</h2>
    
                <div class="swiper">
                    <div class="swiper-wrapper">
                        ${loadBooksInSwiper(booksForSwiper2, 4)}
                    </div>
                    <div class="swiper-button-prev"></div>
                    <div class="swiper-button-next"></div>
                </div>
                ${footer(data.genre)}
            `;
            
            const swiper = new Swiper('.swiper', {
                loop: true,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
        
                });
        })
        .catch(error => {
            console.error("Error:", error);
        });
    
}


function loadDataBookPage(event){

    const clickedElement = event.target; 

    if (clickedElement.classList.contains("see_details_button")) {
        const book_id = clickedElement.closest(".book").id; 
        fetchDataBookPage(book_id)     
        
        .then(data => {
            const imgLink = "./public/img/book.jpg"
            document.getElementById("body").innerHTML = `
            
                <div class="section">
                    ${menu()}

                    <header>
                        <div class="background">
                            <img src="${imgLink}" alt="background" class="background_img">

                            <nav id="genre_menu" class="genre_menu">
                                ${ menuGenre(data.genre)} 
                                <p id="find_out_more" class="link_button">find out more</p>
                            </nav>
                            ${ sticker()}
                        </div>
                    </header>
                </div>

                <div class="section">
                    <div id = "${data.book.book_id}" class="book_section book">

                        <div class="book_general_info ">
                            <div class="book_photo">
                                <a class="book_img" href="" target="_blank" rel="noreferrer noopener" >
                                    <div class="book_cover">
                                        <div class="book_cover_info">
                                            <p id = "book_name" class="title">${data.book.book_name}</p>
                                            <p id="author_name" class="subtitle"> ${data.book.author_name}</p>
                                        </div>
                                        
                                    </div>
                                </a>
                            </div>
            
                            <div class="book_info">
                                <p id = "book_name" class="title">${data.book.book_name}</p>
                                <p id="author_name" class="subtitle">${data.book.author_name}</p>
                                <p id="${data.book.genre_id}" class="subtitle"> ${data.book.genre}</p>
                                <div class="price">
                                    <p id="price" class="subtitle"> ${data.book.price}$</p>
                                </div>
            
                                <button class=" buy_button green_button" > Buy </button>
                            </div>
                        </div>
                        
                        <div class="book_aditional_info">
                            <p class="title">Description</p>
                            <p id = "book_description"  class="subtitle">${data.book.description}</p>
                            <p class="title">About the Author</p>
                            <p id="author_info" class="subtitle">${data.book.author_info}</p>
                            <p class="title">Reviews</p>
                            <p id="book_review" class="subtitle">${data.book.review}</p>
                            
                        </div>

                    </div>
                </div>
                ${footer(data.genre)}

            `
        });
    } 
}

function loadDataGenreBooksPage(event){

    const clickedElement = event.target; 

    if (clickedElement.classList.contains("ganre_menu_item")) {

        const genre_id = clickedElement.id;

        if (genre_id == "home"){
            loadDataHomePage();
            return;
        }

        fetchDataGenreBooksPage(genre_id)

        .then(data => {
            const imgLink = "./public/img/genres.jpg"
            const genre_item = data.genre.find(g => g.genre_id == genre_id);
            const genre = genre_item ? genre_item.genre : 'None';
            const genre_description = genre_item ? genre_item.description : 'None';
            document.getElementById("body").innerHTML = `
            
                <div class="section">
                    ${menu()}

                    <header>
                        <div class="background">
                            <img src="${imgLink}" alt="background" class="background_img">

                            <nav id="genre_menu" class="genre_menu">
                                ${ menuGenre(data.genre)} 
                                <p id="find_out_more" class="link_button">find out more</p>
                            </nav>
                            ${ stickerGenre(genre, genre_description)}
                        </div>
                    </header>
                </div>

                <h2 class="title choosen_section"> ${clickedElement.textContent} </h2>

        
                <div class="books_section section ">
                    ${loadBooks(data.book)}
                </div>

                ${footer(data.genre)}
            `

            document.querySelectorAll(".ganre_menu_item").forEach(element => {
                if (element.id === genre_id) {
                    element.classList.add("white_text");
                    element.classList.add("green_background");
                } else {
                    element.classList.remove("white_text");
                    element.classList.remove("green_background");
                }
            });

        });

    } 
}

function loadDataRandBooksPage(event){

    const clickedElement = event.target; 

    if (clickedElement.id === "top" || clickedElement.id === "newiest") {

        fetchDataRandBooks(30)
        .then(data => {
            const imgLink = "./public/img/genres.jpg"

            document.getElementById("body").innerHTML = `
            
                <div class="section">
                    ${menu()}

                    <header>
                        <div class="background">
                            <img src="${imgLink}" alt="background" class="background_img">
                            <nav id="genre_menu" class="genre_menu">
                                ${ menuGenre(data.genre)} 
                                <p id="find_out_more" class="link_button">find out more</p>
                            </nav>
                            ${ sticker()}
                        </div>
                    </header>
                </div>

                <h2 class="title choosen_section"> ${clickedElement.textContent} </h2>

        
                <div class="books_section section ">
                    ${loadBooks(data.book)}
                </div>

                ${footer(data.genre)}
            `
        
            document.querySelectorAll(".menu_item,  .ganre_menu_item").forEach(element => {
                if (element.id === clickedElement.id) {
                    element.classList.add("white_text");
                    element.classList.add("green_background");
                } else {
                    element.classList.remove("white_text");
                    element.classList.remove("green_background");
                }
            });
        });


    }

}

function loadDataCartPage(event){
    const clickedElement = event.target; 

    if (clickedElement.id === "cart") {

        fetchDataCartPage()

        .then(data => {
            const imgLink = "./public/img/cart.jpg"
            const total = data.order_items.reduce((sum, item) => { return sum + (item.book.price || 0); }, 0); 
            document.getElementById("body").innerHTML = `
            
                <div class="section">
                    ${menu()}

                    <header>
                        <div class="background">
                            <img src="${imgLink}" alt="background" class="background_img">

                            <nav id="genre_menu" class="genre_menu">
                                ${ menuGenre(data.genre)} 
                                <p id="find_out_more" class="link_button">find out more</p>
                            </nav>
                            ${ sticker()}
                        </div>
                    </header>
                </div>

                <div class="cart_section section">
                    <div class="order_items">
                        ${loadOrderItems(data.order_items)}
                    </div>
                    
                    <div class="order_info">
                        <div class="order_summary">
                            <h2 class="title">Order summary</h2>
                            <div class="total">
                                <p class="title">Total excluding tax</p> 
                                <p class="price">$${total}</p>
                            </div>
                        </div>
            
                        <div class="form">
                            <input id="first_name" class="input" type="text" placeholder="Enter first name" required>
                            <input id="last_name" class="input" type="text" placeholder="Enter last name" required>
                            <input id="postal_zip" class="input" type="text" placeholder="Enter postal_zip" required>
                            <input id="address" class="input" type="text" placeholder="Enter address" required>
                            <input id="city" class="input" type="text" placeholder="Enter city" required>
                            <input id="country" class="input" type="text" placeholder="Enter country" required>
                        </div>
            
                        <button id="finish_order" class="green_button" > Buy </button>
                    </div>
                            
                </div>

                ${footer(data.genre)}
            `
  
            document.querySelectorAll(".menu_item,  .ganre_menu_item").forEach(element => {
                if (element.id === clickedElement.id) {
                    element.classList.add("white_text");
                    element.classList.add("green_background");
                } else {
                    element.classList.remove("white_text");
                    element.classList.remove("green_background");
                }
            });

        });
    }
}

function loadAddBook(event){
    const clickedElement = event.target; 

    if (clickedElement.classList.contains("buy_button")) {
        const book_id = clickedElement.closest(".book").id; 
        fetchDataAddBook(book_id);
    }
}

function loadDeleteBook(event){
    const clickedElement = event.target; 

    if (clickedElement.classList.contains("delete_button")) {
        const order_item_id = clickedElement.closest(".order_item").id; 
        fetchDataDeleteBook(order_item_id)
        const fakeEvent = { target: document.getElementById("cart") }; 
        loadDataCartPage(fakeEvent);

    }
}

function findOutMore(event){

    const clickedElement = event.target; 

    if (clickedElement.id === "find_out_more") {
        fetchDataRandBooks(1)
        .then(data => {
            document.getElementById("genre_menu").innerHTML =  menuGenre(data.genre, 100)
        });

    }
}

function logIn(event){
    const clickedElement = event.target; 

    if (clickedElement.id === "submit_button") {
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const repeatPassword = document.getElementById("repeatPassword").value;
        const customerRegistration =  document.getElementById("customer_registration");

        if (!email || !password || !repeatPassword) {
            alert("Please fill out all fields.");
            return;
        }

        if (password !== repeatPassword) {
            alert("Passwords do not match");
            return;
        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            alert("Please enter a valid email.");
            return;
        }

        customer.email = email
        customer.password = password

        fetchDataLogIn()

        .then(data => {

            if(data.status == "error"){
                alert("Wrong password.");
                return;
            }

            customer.customer_id = data.customer.customer_id
            customerRegistration.classList.add("none");
        
        });
    }
}

function completeOrder(event){
    const clickedElement = event.target; 

    if (clickedElement.id === "finish_order") {
        const orderItemsContainer = document.querySelector(".order_items");
        if (!orderItemsContainer || orderItemsContainer.innerHTML.trim() === "") {
            alert("The cart is empty. Please add items before purchasing.");
            return;
        }
    
        const firstName = document.getElementById("first_name").value.replace(/\s+/g, "-");
        const lastName = document.getElementById("last_name").value.replace(/\s+/g, "-");
        const postalZip = document.getElementById("postal_zip").value.replace(/\s+/g, "-");
        const address = document.getElementById("address").value.replace(/\s+/g, "-");
        const city = document.getElementById("city").value.replace(/\s+/g, "-");
        const country = document.getElementById("country").value.replace(/\s+/g, "-");
        
        if (!firstName || !lastName || !postalZip || !address || !city || !country) {
            alert("Please fill out all fields of the form.");
            return;
        }

        fetchDataCompleteOrder(firstName, lastName, postalZip, address, city, country)
        alert("Data sent successfully");
        const fakeEvent = { target: document.getElementById("cart") }; 
        loadDataCartPage(fakeEvent);
    
    }
}

function footer(genres){

    section= `
        <footer id="footer_frame" class="footer_frame">
            <nav id="genre_menu" class="genre_menu">
                ${ menuGenre(genres)} 
            </nav>   
            <div class="language green_background white_texts"> 
                <p> eng </p>
            </div>
        </footer>
    `  
    return section
}

function menuGenre(genres, amount= 5){

    const limitedGenres = genres.slice(0, amount);
    section = ``
    genresMarkup = ``
    limitedGenres.forEach(genre => {
        genresMarkup += `
            <li id = "${genre.genre_id}"  class="ganre_menu_item">
                ${genre.genre}
            </li>
        `
    })

    section += `
        <ul id="genre_menu_frame" class="genre_menu_frame">
            <li id = "home" class="ganre_menu_item green_background white_text">
                Home
            </li>
            ${genresMarkup}
        </ul>
    `
    return section
}

function sticker(){
    section=`
        <div id = "sticker" class="sticker">
            <p class="title">Discover the World in Every Page</p>
            <p class="subtitle">Step into a world of adventure, knowledge, and creativity. Our carefully curated selection of books is your gateway to new journeys—whether you're seeking excitement, inspiration, or a peaceful escape. Find your next favorite book today!</p>
            <a href="https://en.wikipedia.org/wiki/Book" class="link_button">find out more</a>
        </div>
    `
    return section
}

function stickerGenre(genre_name, genre_discription){
    section=`
    <div id = "sticker" class="sticker">
        <p class="title">${genre_name}</p>
        <p class="subtitle">${genre_discription}</p>
        <a href="https://en.wikipedia.org/wiki/Book" class="link_button">find out more</a>
    </div>
`
return section
}


function menu(){
    section = `
        <nav id="menu" class="menu">
            <ul id="menu_frame" class="menu_frame">
                <li class="menu_item green_background white_text" style = "font-size:20px;"">
                    🕮
                </li>
                <li id="newiest" class="menu_item ">
                   NEWIEST
                </li>
                <li id="top" class="menu_item">
                    TOP
                </li>
                <li id="cart" class="menu_item">
                    CART
                </li>
            </ul>
        </nav>            
    `
    return section
}

function loadOrderItems(orderItems){
    section=``

    if(!orderItems){
        return section;
    }

    orderItems.forEach(orderItem => {
        section += `
        <div id="${orderItem.order_item_id}" class="order_item">
            <div id = "${orderItem.book.book_id}" class="book">

                <div class="book_photo">
                    <a class="book_img" href="" target="_blank" rel="noreferrer noopener" >
                        <div class="book_cover">
                            <div class="book_cover_info">
                                <p id = "book_name" class="title">${orderItem.book.book_name}</p>
                                <p id="author_name" class="subtitle">${orderItem.book.author_name}</p>
                            </div>
                            
                        </div>
                    </a>
                </div>
    
                <div class="book_info">
                    <p id = "book_name" class="title">${orderItem.book.book_name}</p>
                    <p id="author_name" class="subtitle">${orderItem.book.author_name}</p>
                    <p id="genre" class="subtitle">${orderItem.book.genre}</p>
                    <div class="price">
                        <p id="price" class="subtitle">${orderItem.book.price}$</p>
                    </div>

                    <div class="book_buttons">
                        <button  class="green_button delete_button" > Delete </button>
                        <button  class="gray_button see_details_button" > See Details </button>
                    </div>
                </div>

            </div>
        </div>

        `;
    });
    return section;
}

function loadBooks(books){
    section=``

    books.forEach(book => {
        section += `
            <div id="${book.book_id}" class="book">
                <div class="book_photo">
                    <a class="book_img" href="#" target="_blank" rel="noreferrer noopener">
                        <div class="book_cover">
                            <div class="book_cover_info">
                                <p class="title">${book.book_name}</p>
                                <p class="subtitle">${book.author_name}</p>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="book_info">
                    <p class="title">${book.book_name}</p>
                    <p class="subtitle">${book.author_name}</p>
                    <p class="subtitle">${book.genre}</p>
                    <div class="price">
                        <p class="subtitle">${book.price}$</p>
                    </div>
                </div>
                <div class="book_buttons">
                    <button class="green_button buy_button">Buy</button>
                    <button class="gray_button see_details_button">See Details</button>
                </div>
            </div>`;
    });
    return section;
}

function loadBooksInSwiper(books, itemsPerSlide = 4) {
    let section = ``;

    for (let i = 0; i < books.length; i += itemsPerSlide) {
        const slideBooks = books.slice(i, i + itemsPerSlide); 
        section += `
            <div class="swiper-slide">
                <div class="book_swiper">
                    ${loadBooks(slideBooks)}
                </div>
            </div>`;
    }

    return section;
}

function customerRegistrationForm(){
    section=``
    if (!customer.customer_id) {
        section=`
        <div id="customer_registration" class="customer_registration_background">

            <div id="" class="customer_registration">

                    <h2 class="title">Login</h2>
                <div id="loginForm" class="loginForm">
                    
                    <input  id="email" class="input" type="text" placeholder="Enter email" required>
                    <input  id="password" class="input" type="text" placeholder="Enter password" required>
                    <input  id="repeatPassword" class="input" type="text" placeholder="Repeat password" required>
                    

                </div>

                    <button id="submit_button" class = "green_button" >Log in / Sign in</button>

            </div>
        </div>
    `
    }

    return section
}

document.addEventListener("DOMContentLoaded", () => {
    loadDataHomePage();
    document.body.addEventListener("click", (event) => {loadDataBookPage(event);});
    document.body.addEventListener("click", (event) => {loadDataGenreBooksPage(event);});
    document.body.addEventListener("click", (event) => {loadDataCartPage(event);});
    document.body.addEventListener("click", (event) => {loadDataRandBooksPage(event);});
    document.body.addEventListener("click", (event) => {loadAddBook(event);});
    document.body.addEventListener("click", (event) => {loadDeleteBook(event);});
    document.body.addEventListener("click", (event) => {findOutMore(event);});
    document.body.addEventListener("click", (event) => {logIn(event);});
    document.body.addEventListener("click", (event) => {completeOrder(event);});
    

});
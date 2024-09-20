// const menuBar  = document.getElementsByClassName("menu-bar")[0];
// const navLinks = document.getElementById("navLinks");


// console.log(navLinks)
// menuBar.addEventListener("click", (event) => {
//     // event.preventDefault()
//     console.log(event);
//     console.log(navLinks)
//     // navLinks?.classList.remove("hidden");
//     // navLinks?.classList.add("flex");
// });

type Tags = {
    id : number
}

type BlogPost = {
    author : number,
    user_that_last_updated : number,
    title : string,
    body : string,
    category : number,
    tags : Tags[],
    comment : number,
    is_archive : Boolean,
    is_draft : Boolean,
    views : number,
    cover_image : string,
    tableOfContent : number,
    slug : string,
    totalLikes : number,
    totalDislikes : number,
    dateCreated : Date
    lastUpdated : Date

}




const outerContainer = document.getElementById("blog-post-container");


function createBlogPost(data:BlogPost) {
  console.log(data);
  const coverImage = data.cover_image;
  // const content = data.body;
  // Create the container div
  const container = document.createElement('div');
  container.className = 'md:w-1/3 border-4 flex flex-col text-center shadow-xl';

  // Create the image
  const img = document.createElement('img');
  img.src = coverImage;
  img.alt = '';
  img.className = 'max-h-60 border-b-4 w-full';

  // Create the div that wraps content
  const contentDiv = document.createElement('div');

  // Create the flex div for calendar and heart icons
  const flexDiv = document.createElement('div');
  flexDiv.className = 'flex justify-evenly mb-8';

  // Create the calendar icon and text
  const calendarDiv = document.createElement('div');
  calendarDiv.className = 'flex items-center justify-center gap-2';
  const calendarIcon = document.createElement('i');
  calendarIcon.className = 'fas fa-calendar-week';
  const calendarText = document.createElement('p');
  calendarText.textContent = 'AUG 4';

  // Append calendar icon and text to the calendar block
  calendarDiv.appendChild(calendarIcon);
  calendarDiv.appendChild(calendarText);

  // Create the heart icon and text
  const heartDiv = document.createElement('div');
  heartDiv.className = 'flex items-center justify-center gap-2';
  const heartIcon = document.createElement('i');
  heartIcon.className = 'fas fa-heart';
  const heartText = document.createElement('p');
  heartText.textContent = '102';

  // Append heart icon and text to the heart block
  heartDiv.appendChild(heartIcon);
  heartDiv.appendChild(heartText);

  // Append calendar and heart blocks to the flex div
  flexDiv.appendChild(calendarDiv);
  flexDiv.appendChild(heartDiv);

  // Create the paragraph
  const paragraph = document.createElement('p');
  paragraph.className = 'mb-8';
  paragraph.textContent = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem molestias praesentium quae recusandae maxime, sunt amet maiores rerum nostrum dolor delectus saepe quo nobis placeat ab nisi perspiciatis. Atque, ad.';

  // Create the button
  const button = document.createElement('button');
  button.className = 'p-2 bg-black text-white font-bold rounded-lg text-lg mb-8';
  button.textContent = 'Read More';

  // Append everything to the content div
  contentDiv.appendChild(flexDiv);
  contentDiv.appendChild(paragraph);
  contentDiv.appendChild(button);

  // Append the image and content div to the main container
  container.appendChild(img);
  container.appendChild(contentDiv);

  return container

}


async function renderData() {
  const response = await fetch("http://127.0.0.1:8000/api/v1/blog/post/list/recent/");
  const response_body = await response.json();
  
    for (let data of response_body){
      const container = createBlogPost(data); 
    // Append the container to the body or any other desired element
    outerContainer?.appendChild(container);
    }
    
  }
  
// Call the function to render the data
renderData();
  


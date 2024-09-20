"use strict";
const outerContainer = document.getElementById("blog-post-container");
function createBlogPost(data) {
    console.log(data);
    const coverImage = data.cover_image;
    const container = document.createElement('div');
    container.className = 'md:w-1/3 border-4 flex flex-col text-center shadow-xl';
    const img = document.createElement('img');
    img.src = coverImage;
    img.alt = '';
    img.className = 'max-h-60 border-b-4 w-full';
    const contentDiv = document.createElement('div');
    const flexDiv = document.createElement('div');
    flexDiv.className = 'flex justify-evenly mb-8';
    const calendarDiv = document.createElement('div');
    calendarDiv.className = 'flex items-center justify-center gap-2';
    const calendarIcon = document.createElement('i');
    calendarIcon.className = 'fas fa-calendar-week';
    const calendarText = document.createElement('p');
    calendarText.textContent = 'AUG 4';
    calendarDiv.appendChild(calendarIcon);
    calendarDiv.appendChild(calendarText);
    const heartDiv = document.createElement('div');
    heartDiv.className = 'flex items-center justify-center gap-2';
    const heartIcon = document.createElement('i');
    heartIcon.className = 'fas fa-heart';
    const heartText = document.createElement('p');
    heartText.textContent = '102';
    heartDiv.appendChild(heartIcon);
    heartDiv.appendChild(heartText);
    flexDiv.appendChild(calendarDiv);
    flexDiv.appendChild(heartDiv);
    const paragraph = document.createElement('p');
    paragraph.className = 'mb-8';
    paragraph.textContent = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem molestias praesentium quae recusandae maxime, sunt amet maiores rerum nostrum dolor delectus saepe quo nobis placeat ab nisi perspiciatis. Atque, ad.';
    const button = document.createElement('button');
    button.className = 'p-2 bg-black text-white font-bold rounded-lg text-lg mb-8';
    button.textContent = 'Read More';
    contentDiv.appendChild(flexDiv);
    contentDiv.appendChild(paragraph);
    contentDiv.appendChild(button);
    container.appendChild(img);
    container.appendChild(contentDiv);
    return container;
}
async function renderData() {
    const response = await fetch("http://127.0.0.1:8000/api/v1/blog/post/list/recent/");
    const response_body = await response.json();
    for (let data of response_body) {
        const container = createBlogPost(data);
        outerContainer === null || outerContainer === void 0 ? void 0 : outerContainer.appendChild(container);
    }
}
renderData();

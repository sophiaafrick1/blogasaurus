const homePage = document.querySelector(".button");

homePage.addEventListener('mouseover', (e) => {
  homePage.style.backgroundColor = "#042779"
})

homePage.addEventListener('mouseout', (e) => {
  homePage.style.backgroundColor = "#3782BA"
})

const blogPage = document.querySelector("#blog");

blogPage.addEventListener('mouseover', (e) => {
  blogPage.style.backgroundColor = "#042779"
})

blogPage.addEventListener('mouseout', (e) => {
  blogPage.style.backgroundColor = "#3782BA"
})

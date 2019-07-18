console.log("I'm working!!");

const myFamily = document.querySelector(".button");

myFamily.addEventListener('mouseover', (e) => {
  myFamily.style.backgroundColor = "#042779"
})

myFamily.addEventListener('mouseout', (e) => {
  myFamily.style.backgroundColor = "#3782BA"
})

const newYorkCity = document.querySelector("img");

newYorkCity.addEventListener('mouseover', (e) => {
  newYorkCity.style.border = "50px groove #042779"
})

newYorkCity.addEventListener('mouseout', (e) => {
  newYorkCity.style.border = "50px groove #3782BA"
})

const sophiaBlog = document.querySelector("h1")

sophiaBlog.addEventListener('mouseover', (e) => {
  sophiaBlog.style.fontSize = "100px"
})

//randomColor.addEventListener('click', (e) => {
  //randomColor.style.color = "blue"
//})

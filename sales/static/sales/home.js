console.log('hello world!')

const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBdy = document.getElementById('modal-body')

console.log(reportBtn)
console.log(img)


if (img){
    reportBtn.classList.remove('not-visible')
}

reportBtn.addEventListener('click', ()=>{
    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modalBdy.prepend(img)
})